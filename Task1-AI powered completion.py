# ===== TASK 1: AI-POWERED CODE COMPLETION =====
# Tool: GitHub Copilot (AI-suggested) vs Manual Implementation

# --- 1. AI-Suggested Implementation (GitHub Copilot) ---
def sort_dicts_by_key_ai(data, key):
    """
    Sorts a list of dictionaries by a specific key (AI-generated)
    :param data: List of dictionaries
    :param key: Key to sort by
    :return: Sorted list of dictionaries
    """
    return sorted(data, key=lambda x: x[key])

# --- 2. Manual Implementation ---
from operator import itemgetter

def sort_dicts_by_key_manual(data, key):
    """
    Sorts a list of dictionaries by a specific key (Optimized manual version)
    :param data: List of dictionaries
    :param key: Key to sort by
    :return: Sorted list of dictionaries
    """
    return sorted(data, key=itemgetter(key))

# --- 3. Benchmarking and Verification ---
import timeit
import random

def generate_test_data(size=100000):
    """Generate test data for benchmarking"""
    return [
        {'id': i, 'value': random.randint(1, 10000), 'name': f'item_{i}'} 
        for i in range(size)
    ]

def main():
    """Main function to execute performance comparison"""
    # Generate test data
    print("Generating test data (100,000 dictionaries)...")
    test_data = generate_test_data()
    
    # Verify functions work
    sample = [{'a': 3}, {'a': 1}, {'a': 2}]
    print("\nFunctional test (AI version):", sort_dicts_by_key_ai(sample.copy(), 'a'))
    print("Functional test (Manual version):", sort_dicts_by_key_manual(sample.copy(), 'a'))
    
    # Create local context for timeit
    local_vars = {
        'sort_dicts_by_key_ai': sort_dicts_by_key_ai,
        'sort_dicts_by_key_manual': sort_dicts_by_key_manual,
        'test_data': test_data
    }
    
    # Performance comparison
    print("\nRunning performance benchmark (100 iterations)...")
    
    # Benchmark AI version
    ai_time = timeit.timeit(
        'sorted_ai = sort_dicts_by_key_ai(test_data, "value")',
        number=100,
        globals=local_vars
    )
    
    # Benchmark manual version
    manual_time = timeit.timeit(
        'sorted_manual = sort_dicts_by_key_manual(test_data, "value")',
        number=100,
        globals=local_vars
    )
    
    # Results analysis
    print("\n=== Benchmark Results ===")
    print(f"AI Version (lambda): {ai_time:.4f} seconds")
    print(f"Manual Version (itemgetter): {manual_time:.4f} seconds")
    
    if ai_time > manual_time:
        improvement = ((ai_time - manual_time) / ai_time) * 100
        print(f"Performance improvement: {improvement:.1f}%")
    else:
        regression = ((manual_time - ai_time) / manual_time) * 100
        print(f"Performance regression: {regression:.1f}%")
    
    # Verify functional equivalence
    ai_result = sort_dicts_by_key_ai(test_data, "value")
    manual_result = sort_dicts_by_key_manual(test_data, "value")
    print("\n=== Functional Verification ===")
    print(f"Results identical: {ai_result == manual_result}")
    
    # SAFE PRINT: Extract values first to avoid syntax issues
    ai_values = [item['value'] for item in ai_result[:3]]
    manual_values = [item['value'] for item in manual_result[:3]]
    print(f"First 3 values: {ai_values} (AI) vs {manual_values} (Manual)")

# --- 4. 200-Word Analysis ---
"""
Efficiency Analysis:

The manual implementation using itemgetter typically shows better performance (20-35% faster) for three key reasons:

1. Execution Mechanism: 
   - Lambda creates a Python function call per comparison
   - Itemgetter uses a single C-compiled callable (lower overhead)

2. Memory Handling:
   - Itemgetter creates one reusable callable
   - Lambda rebuilds function logic during sorting

3. Internal Optimization:
   - Itemgetter allows direct attribute access
   - Lambda requires Python's abstraction layer

While both have O(n log n) complexity, the constant factors differ. The performance gap is negligible for small datasets (<1,000 items) but significant at scale.

Functional equivalence was verified: both produce identical sorted outputs. The AI suggestion provides correct basic functionality but misses optimization opportunities. This demonstrates AI's strength for prototyping versus human expertise for optimization.

Recommendation: Use AI suggestions for initial implementation but prefer itemgetter in performance-critical systems processing large datasets.
"""

if __name__ == "__main__":
    main()