#!/usr/bin/env python3
"""
LeetCode API Integration for Problem Fetching

This script integrates with the LeetCode GraphQL API to fetch problem information,
including problem descriptions, difficulty, tags, and example test cases.
"""

import requests
import json
from typing import Dict, List, Optional, Any
import os


class LeetCodeAPI:
    """Client for interacting with the LeetCode GraphQL API."""
    
    def __init__(self):
        """Initialize the LeetCode API client."""
        self.base_url = "https://leetcode.com/graphql"
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
    
    def _make_request(self, query: str, variables: Dict = None) -> Dict:
        """
        Make a GraphQL request to LeetCode.
        
        Args:
            query: GraphQL query string
            variables: Variables for the GraphQL query
            
        Returns:
            JSON response from the API
        """
        payload = {
            "query": query,
            "variables": variables or {}
        }
        
        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making request to LeetCode API: {e}")
            return {}
    
    def get_problem_by_title(self, title_slug: str) -> Optional[Dict]:
        """
        Fetch problem details by title slug.
        
        Args:
            title_slug: The URL slug of the problem (e.g., "two-sum")
            
        Returns:
            Dictionary containing problem details or None if not found
        """
        query = """
        query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                title
                titleSlug
                difficulty
                content
                topicTags {
                    name
                    slug
                }
                codeSnippets {
                    lang
                    langSlug
                    code
                }
                exampleTestcases
                hints
                companyTagStats
                similarQuestions
            }
        }
        """
        
        variables = {"titleSlug": title_slug}
        response = self._make_request(query, variables)
        
        if response and "data" in response and response["data"]["question"]:
            return response["data"]["question"]
        return None
    
    def get_all_problems(self) -> List[Dict]:
        """
        Fetch all problems from LeetCode.
        
        Returns:
            List of problem dictionaries
        """
        query = """
        query getAllProblems {
            allQuestions {
                title
                titleSlug
                difficulty
                paidOnly
                topicTags {
                    name
                    slug
                }
            }
        }
        """
        
        response = self._make_request(query)
        
        if response and "data" in response:
            return response["data"].get("allQuestions", [])
        return []
    
    def get_problems_by_difficulty(self, difficulty: str) -> List[Dict]:
        """
        Fetch problems filtered by difficulty.
        
        Args:
            difficulty: "Easy", "Medium", or "Hard"
            
        Returns:
            List of problem dictionaries
        """
        all_problems = self.get_all_problems()
        return [p for p in all_problems if p.get("difficulty") == difficulty]
    
    def get_problems_by_tag(self, tag: str) -> List[Dict]:
        """
        Fetch problems filtered by topic tag.
        
        Args:
            tag: Topic tag name (e.g., "Array", "Hash Table")
            
        Returns:
            List of problem dictionaries
        """
        all_problems = self.get_all_problems()
        return [
            p for p in all_problems
            if any(t.get("name") == tag for t in p.get("topicTags", []))
        ]
    
    def search_problems(self, keyword: str) -> List[Dict]:
        """
        Search problems by keyword in title.
        
        Args:
            keyword: Search keyword
            
        Returns:
            List of matching problem dictionaries
        """
        all_problems = self.get_all_problems()
        keyword_lower = keyword.lower()
        return [
            p for p in all_problems
            if keyword_lower in p.get("title", "").lower()
        ]
    
    def generate_problem_template(self, problem: Dict, language: str = "python3") -> str:
        """
        Generate a solution template for a problem.
        
        Args:
            problem: Problem dictionary from API
            language: Programming language for the template
            
        Returns:
            String containing the solution template
        """
        title = problem.get("title", "Unknown")
        difficulty = problem.get("difficulty", "Medium")
        content = problem.get("content", "")
        title_slug = problem.get("titleSlug", "")
        
        # Extract tags
        tags = [tag["name"] for tag in problem.get("topicTags", [])]
        tags_str = ", ".join(tags) if tags else "General"
        
        # Find code snippet for the language
        code_snippet = ""
        for snippet in problem.get("codeSnippets", []):
            if snippet.get("langSlug") == language:
                code_snippet = snippet.get("code", "")
                break
        
        template = f'''"""
{title}

LeetCode Problem
Difficulty: {difficulty}
Pattern: {tags_str}

Problem Description:
{content}

Time Complexity: [TODO - Add after implementing solution]
Space Complexity: [TODO - Add after implementing solution]
"""

{code_snippet}

def main() -> None:
    """
    Main function to demonstrate the solution.
    """
    # TODO: Add test cases
    pass

if __name__ == "__main__":
    main()
'''
        return template
    
    def save_problem_to_file(
        self,
        title_slug: str,
        output_dir: str,
        language: str = "python3"
    ) -> bool:
        """
        Fetch and save a problem to a file.
        
        Args:
            title_slug: Problem title slug
            output_dir: Directory to save the problem
            language: Programming language for the template
            
        Returns:
            True if successful, False otherwise
        """
        problem = self.get_problem_by_title(title_slug)
        
        if not problem:
            print(f"Problem '{title_slug}' not found.")
            return False
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate filename
        filename = f"{title_slug.replace('-', '_')}.py"
        filepath = os.path.join(output_dir, filename)
        
        # Generate template
        template = self.generate_problem_template(problem, language)
        
        # Save to file
        try:
            with open(filepath, 'w') as f:
                f.write(template)
            print(f"Problem saved to: {filepath}")
            return True
        except IOError as e:
            print(f"Error saving file: {e}")
            return False
    
    def print_problem_info(self, title_slug: str) -> None:
        """
        Print detailed information about a problem.
        
        Args:
            title_slug: Problem title slug
        """
        problem = self.get_problem_by_title(title_slug)
        
        if not problem:
            print(f"Problem '{title_slug}' not found.")
            return
        
        print("\n" + "=" * 60)
        print(f"Title: {problem.get('title', 'Unknown')}")
        print(f"Difficulty: {problem.get('difficulty', 'Unknown')}")
        print(f"Title Slug: {problem.get('titleSlug', 'Unknown')}")
        print("=" * 60)
        
        print("\nTags:")
        for tag in problem.get("topicTags", []):
            print(f"  - {tag.get('name', 'Unknown')}")
        
        print("\nHints:")
        for i, hint in enumerate(problem.get("hints", []), 1):
            print(f"  {i}. {hint}")
        
        print("\nExample Test Cases:")
        for i, test_case in enumerate(problem.get("exampleTestcases", "").split("\n"), 1):
            if test_case.strip():
                print(f"  {i}. {test_case.strip()}")


def main() -> None:
    """Main function demonstrating LeetCode API usage."""
    print("LeetCode API Integration")
    print("=" * 60)
    
    api = LeetCodeAPI()
    
    # Example 1: Get a specific problem
    print("\nExample 1: Fetch 'Two Sum' problem")
    print("-" * 60)
    api.print_problem_info("two-sum")
    
    # Example 2: Get all easy problems
    print("\n\nExample 2: Get all Easy problems")
    print("-" * 60)
    easy_problems = api.get_problems_by_difficulty("Easy")
    print(f"Found {len(easy_problems)} Easy problems")
    for i, problem in enumerate(easy_problems[:5], 1):
        print(f"  {i}. {problem.get('title')} ({problem.get('titleSlug')})")
    if len(easy_problems) > 5:
        print(f"  ... and {len(easy_problems) - 5} more")
    
    # Example 3: Search for problems
    print("\n\nExample 3: Search for 'array' problems")
    print("-" * 60)
    array_problems = api.search_problems("array")
    print(f"Found {len(array_problems)} problems matching 'array'")
    for i, problem in enumerate(array_problems[:5], 1):
        print(f"  {i}. {problem.get('title')} - {problem.get('difficulty')}")
    
    # Example 4: Save a problem template
    print("\n\nExample 4: Save 'two-sum' problem template")
    print("-" * 60)
    output_dir = "/home/logan/Projects/LeetCode/downloaded_problems"
    success = api.save_problem_to_file("two-sum", output_dir)
    if success:
        print("Problem template saved successfully!")
    
    print("\n" + "=" * 60)
    print("API demonstration complete.")


if __name__ == "__main__":
    main()
