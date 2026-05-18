#!/usr/bin/env python3
"""
Time Complexity Visualizer for LeetCode Solutions

This script generates visualizations comparing time complexity of different algorithms.
It plots the growth rates of various complexity classes (O(1), O(log n), O(n), O(n log n), O(n²), etc.)
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Tuple


def plot_complexity_comparison(max_n: int = 100) -> None:
    """
    Plot various time complexity functions to visualize their growth rates.
    
    Args:
        max_n: Maximum input size to plot
    """
    n = np.arange(1, max_n + 1)
    
    plt.figure(figsize=(12, 8))
    
    # Plot different complexity classes
    plt.plot(n, np.ones_like(n), label='O(1)', linewidth=2)
    plt.plot(n, np.log2(n), label='O(log n)', linewidth=2)
    plt.plot(n, n, label='O(n)', linewidth=2)
    plt.plot(n, n * np.log2(n), label='O(n log n)', linewidth=2)
    plt.plot(n, n**2, label='O(n²)', linewidth=2)
    plt.plot(n, n**3, label='O(n³)', linewidth=2)
    plt.plot(n, 2**n, label='O(2ⁿ)', linewidth=2, linestyle='--')
    
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Operations', fontsize=12)
    plt.title('Time Complexity Growth Rates', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    plt.xlim(0, max_n)
    
    # Save the plot
    plt.savefig('/home/logan/Projects/LeetCode/docs/complexity_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Complexity comparison plot saved to docs/complexity_comparison.png")


def plot_specific_complexities(complexities: Dict[str, callable], max_n: int = 100) -> None:
    """
    Plot specific complexity functions for comparison.
    
    Args:
        complexities: Dictionary mapping complexity names to functions
        max_n: Maximum input size to plot
    """
    n = np.arange(1, max_n + 1)
    
    plt.figure(figsize=(12, 8))
    
    for name, func in complexities.items():
        plt.plot(n, func(n), label=name, linewidth=2)
    
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Operations', fontsize=12)
    plt.title('Custom Complexity Comparison', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.xlim(0, max_n)
    
    plt.savefig('/home/logan/Projects/LeetCode/docs/custom_complexity.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Custom complexity plot saved to docs/custom_complexity.png")


def plot_leetcode_problem_complexities() -> None:
    """
    Plot complexity classes for common LeetCode problem patterns.
    """
    n = np.arange(1, 51)  # Plot up to n=50 for better visibility
    
    plt.figure(figsize=(14, 10))
    
    # Hash Map problems (Two Sum, Contains Duplicate, etc.)
    plt.subplot(2, 3, 1)
    plt.plot(n, n, label='O(n)', linewidth=2)
    plt.title('Hash Map Pattern', fontweight='bold')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Operations')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Two Pointers problems (Valid Palindrome, Merge Sorted Array, etc.)
    plt.subplot(2, 3, 2)
    plt.plot(n, n, label='O(n)', linewidth=2)
    plt.title('Two Pointers Pattern', fontweight='bold')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Operations')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Binary Search problems
    plt.subplot(2, 3, 3)
    plt.plot(n, np.log2(n), label='O(log n)', linewidth=2)
    plt.title('Binary Search Pattern', fontweight='bold')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Operations')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Dynamic Programming problems
    plt.subplot(2, 3, 4)
    plt.plot(n, n**2, label='O(n²)', linewidth=2)
    plt.title('Dynamic Programming Pattern', fontweight='bold')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Operations')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Backtracking problems
    plt.subplot(2, 3, 5)
    plt.plot(n[:20], 2**n[:20], label='O(2ⁿ)', linewidth=2)
    plt.title('Backtracking Pattern', fontweight='bold')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Operations')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Sorting-based problems
    plt.subplot(2, 3, 6)
    plt.plot(n, n * np.log2(n), label='O(n log n)', linewidth=2)
    plt.title('Sorting-Based Pattern', fontweight='bold')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Operations')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/logan/Projects/LeetCode/docs/leetcode_patterns_complexity.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("LeetCode patterns complexity plot saved to docs/leetcode_patterns_complexity.png")


def main() -> None:
    """
    Main function to generate all complexity visualizations.
    """
    print("Generating time complexity visualizations...")
    
    # Generate standard complexity comparison
    plot_complexity_comparison(max_n=100)
    
    # Generate LeetCode pattern-specific visualizations
    plot_leetcode_problem_complexities()
    
    # Example custom comparison: Brute Force vs Optimized approaches
    custom_complexities = {
        'Brute Force O(n²)': lambda n: n**2,
        'Hash Map O(n)': lambda n: n,
        'Binary Search O(log n)': lambda n: np.log2(n),
    }
    plot_specific_complexities(custom_complexities, max_n=50)
    
    print("All visualizations generated successfully!")


if __name__ == "__main__":
    main()
