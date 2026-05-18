#!/usr/bin/env python3
"""
Performance Benchmarking Tool for LeetCode Solutions

This tool benchmarks different algorithmic approaches to compare their performance.
It measures execution time, memory usage, and provides detailed statistics.
"""

import time
import tracemalloc
import statistics
from typing import Callable, List, Dict, Any, Tuple
import matplotlib.pyplot as plt
import numpy as np


class BenchmarkResult:
    """Stores benchmark results for a single function."""
    
    def __init__(self, name: str):
        """
        Initialize a benchmark result.
        
        Args:
            name: Name of the function being benchmarked
        """
        self.name = name
        self.execution_times: List[float] = []
        self.memory_usages: List[float] = []
        self.input_sizes: List[int] = []
    
    def add_run(self, execution_time: float, memory_usage: float, input_size: int) -> None:
        """
        Add a benchmark run result.
        
        Args:
            execution_time: Time taken in seconds
            memory_usage: Memory used in bytes
            input_size: Size of the input
        """
        self.execution_times.append(execution_time)
        self.memory_usages.append(memory_usage)
        self.input_sizes.append(input_size)
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get statistical summary of benchmark results.
        
        Returns:
            Dictionary containing mean, median, min, max, std dev
        """
        if not self.execution_times:
            return {}
        
        return {
            "name": self.name,
            "mean_time": statistics.mean(self.execution_times),
            "median_time": statistics.median(self.execution_times),
            "min_time": min(self.execution_times),
            "max_time": max(self.execution_times),
            "std_time": statistics.stdev(self.execution_times) if len(self.execution_times) > 1 else 0,
            "mean_memory": statistics.mean(self.memory_usages),
            "median_memory": statistics.median(self.memory_usages),
        }


class Benchmark:
    """Main benchmarking class for comparing algorithmic approaches."""
    
    def __init__(self):
        """Initialize the benchmark tool."""
        self.results: Dict[str, BenchmarkResult] = {}
    
    def benchmark_function(
        self,
        func: Callable,
        *args,
        name: str = None,
        iterations: int = 10,
        **kwargs
    ) -> BenchmarkResult:
        """
        Benchmark a function with multiple iterations.
        
        Args:
            func: Function to benchmark
            *args: Arguments to pass to the function
            name: Name for the benchmark (defaults to function name)
            iterations: Number of iterations to run
            **kwargs: Keyword arguments to pass to the function
            
        Returns:
            BenchmarkResult containing all measurements
        """
        if name is None:
            name = func.__name__
        
        result = BenchmarkResult(name)
        
        # Estimate input size
        input_size = self._estimate_input_size(args, kwargs)
        
        for _ in range(iterations):
            # Measure memory
            tracemalloc.start()
            
            # Measure time
            start_time = time.perf_counter()
            try:
                func(*args, **kwargs)
            except Exception as e:
                print(f"Error benchmarking {name}: {e}")
                tracemalloc.stop()
                continue
            end_time = time.perf_counter()
            
            # Get memory usage
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            execution_time = end_time - start_time
            memory_usage = peak
            
            result.add_run(execution_time, memory_usage, input_size)
        
        self.results[name] = result
        return result
    
    def _estimate_input_size(self, args: tuple, kwargs: dict) -> int:
        """
        Estimate the size of the input for benchmarking.
        
        Args:
            args: Positional arguments
            kwargs: Keyword arguments
            
        Returns:
            Estimated input size
        """
        size = 0
        for arg in args:
            if hasattr(arg, '__len__'):
                size += len(arg)
            else:
                size += 1
        for value in kwargs.values():
            if hasattr(value, '__len__'):
                size += len(value)
            else:
                size += 1
        return size
    
    def compare_functions(
        self,
        functions: List[Tuple[Callable, str]],
        test_cases: List[Tuple[tuple, dict]],
        iterations: int = 5
    ) -> Dict[str, BenchmarkResult]:
        """
        Compare multiple functions across multiple test cases.
        
        Args:
            functions: List of (function, name) tuples
            test_cases: List of (args, kwargs) tuples for test cases
            iterations: Number of iterations per test case
            
        Returns:
            Dictionary mapping function names to aggregated results
        """
        aggregated_results = {}
        
        for func, name in functions:
            all_times = []
            all_memory = []
            
            for args, kwargs in test_cases:
                result = self.benchmark_function(
                    func, *args, name=name, iterations=iterations, **kwargs
                )
                all_times.extend(result.execution_times)
                all_memory.extend(result.memory_usages)
            
            # Create aggregated result
            aggregated = BenchmarkResult(name)
            for t, m in zip(all_times, all_memory):
                aggregated.add_run(t, m, 0)
            aggregated_results[name] = aggregated
        
        return aggregated_results
    
    def print_results(self, result: BenchmarkResult = None) -> None:
        """
        Print benchmark results.
        
        Args:
            result: Specific result to print, or None to print all
        """
        if result:
            self._print_single_result(result)
        else:
            for result in self.results.values():
                self._print_single_result(result)
                print()
    
    def _print_single_result(self, result: BenchmarkResult) -> None:
        """Print results for a single benchmark."""
        stats = result.get_statistics()
        if not stats:
            print(f"No results for {result.name}")
            return
        
        print(f"Benchmark Results: {stats['name']}")
        print("-" * 50)
        print(f"Execution Time (seconds):")
        print(f"  Mean:   {stats['mean_time']:.6f}")
        print(f"  Median: {stats['median_time']:.6f}")
        print(f"  Min:    {stats['min_time']:.6f}")
        print(f"  Max:    {stats['max_time']:.6f}")
        print(f"  Std:    {stats['std_time']:.6f}")
        print(f"\nMemory Usage (bytes):")
        print(f"  Mean:   {stats['mean_memory']:.2f}")
        print(f"  Median: {stats['median_memory']:.2f}")
        print(f"  Min:    {min(result.memory_usages):.2f}")
        print(f"  Max:    {max(result.memory_usages):.2f}")
    
    def plot_comparison(self, results: Dict[str, BenchmarkResult] = None) -> None:
        """
        Plot comparison of benchmark results.
        
        Args:
            results: Dictionary of results to plot, or None to plot all
        """
        if results is None:
            results = self.results
        
        if not results:
            print("No results to plot.")
            return
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        names = list(results.keys())
        times = [results[name].execution_times for name in names]
        memories = [results[name].memory_usages for name in names]
        
        # Plot execution times
        ax1.boxplot(times, labels=names)
        ax1.set_ylabel('Execution Time (seconds)')
        ax1.set_title('Execution Time Comparison')
        ax1.tick_params(axis='x', rotation=45)
        ax1.grid(True, alpha=0.3)
        
        # Plot memory usage
        ax2.boxplot(memories, labels=names)
        ax2.set_ylabel('Memory Usage (bytes)')
        ax2.set_title('Memory Usage Comparison')
        ax2.tick_params(axis='x', rotation=45)
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('/home/logan/Projects/LeetCode/docs/benchmark_comparison.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("Benchmark comparison plot saved to docs/benchmark_comparison.png")
    
    def plot_scalability(
        self,
        func: Callable,
        input_sizes: List[int],
        iterations: int = 3
    ) -> None:
        """
        Plot how a function scales with input size.
        
        Args:
            func: Function to benchmark
            input_sizes: List of input sizes to test
            iterations: Number of iterations per size
        """
        mean_times = []
        mean_memories = []
        
        for size in input_sizes:
            # Generate test input of given size
            test_input = list(range(size))
            
            result = self.benchmark_function(
                func, test_input, iterations=iterations
            )
            
            mean_times.append(statistics.mean(result.execution_times))
            mean_memories.append(statistics.mean(result.memory_usages))
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Plot time vs input size
        ax1.plot(input_sizes, mean_times, 'o-', linewidth=2)
        ax1.set_xlabel('Input Size (n)')
        ax1.set_ylabel('Mean Execution Time (seconds)')
        ax1.set_title(f'Scalability: {func.__name__}')
        ax1.grid(True, alpha=0.3)
        
        # Plot memory vs input size
        ax2.plot(input_sizes, mean_memories, 'o-', linewidth=2, color='orange')
        ax2.set_xlabel('Input Size (n)')
        ax2.set_ylabel('Mean Memory Usage (bytes)')
        ax2.set_title(f'Memory Scalability: {func.__name__}')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('/home/logan/Projects/LeetCode/docs/scalability_plot.png', dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Scalability plot saved to docs/scalability_plot.png")


# Example usage and test functions
def linear_search(arr: list, target: int) -> bool:
    """Linear search implementation."""
    for item in arr:
        if item == target:
            return True
    return False


def binary_search(arr: list, target: int) -> bool:
    """Binary search implementation."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    """Brute force two sum."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_hash_map(nums: list[int], target: int) -> list[int]:
    """Hash map two sum."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def main() -> None:
    """Main function demonstrating benchmark usage."""
    print("LeetCode Performance Benchmarking Tool")
    print("=" * 60)
    
    benchmark = Benchmark()
    
    # Example 1: Compare search algorithms
    print("\nExample 1: Linear Search vs Binary Search")
    print("-" * 60)
    
    sorted_array = list(range(10000))
    target = 9999
    
    benchmark.benchmark_function(linear_search, sorted_array, target, name="Linear Search", iterations=10)
    benchmark.benchmark_function(binary_search, sorted_array, target, name="Binary Search", iterations=10)
    
    benchmark.print_results()
    benchmark.plot_comparison()
    
    # Example 2: Compare two sum approaches
    print("\nExample 2: Two Sum - Brute Force vs Hash Map")
    print("-" * 60)
    
    benchmark.results.clear()  # Clear previous results
    
    test_array = list(range(1000))
    test_target = 1999
    
    benchmark.benchmark_function(two_sum_brute_force, test_array, test_target, name="Two Sum Brute Force", iterations=5)
    benchmark.benchmark_function(two_sum_hash_map, test_array, test_target, name="Two Sum Hash Map", iterations=5)
    
    benchmark.print_results()
    benchmark.plot_comparison()
    
    # Example 3: Scalability test
    print("\nExample 3: Scalability Test - Binary Search")
    print("-" * 60)
    
    benchmark.results.clear()
    input_sizes = [100, 1000, 10000, 50000, 100000]
    benchmark.plot_scalability(binary_search, input_sizes, iterations=3)
    
    print("\nAll benchmarks completed. Plots saved to docs/ directory.")


if __name__ == "__main__":
    main()
