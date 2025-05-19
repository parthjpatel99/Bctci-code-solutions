def find_squared(arr):
    res = []
    map = {}

    for i, num in enumerate(arr):
        if num not in map:
            map[num] = i
        
    for i, num in enumerate(arr):
        sq = num * num
        if sq in map:
            res.append([i, map[sq]])    
    return res

def run_tests():
    tests = [
        # Example from the book
        ([4, 10, 3, 100, 5, 2, 10000], [[5, 0], [1, 3], [3, 6]]),
        # Additional test cases
        ([], []),
        ([1], [[0, 0]]),
        ([2, 4], [[0, 1]]),
    ]

    for i, (arr, want) in enumerate(tests, 1):
        got = find_squared(arr)
        # Sort for comparison (shallow sort is fine here)
        got.sort()
        want.sort()
        status = "✅" if got == want else "❌"
        print(f"Test {i}: {status}")
        print(f"Input: {arr}")
        print(f"Expected Output: {want}")
        print(f"Actual Output:   {got}")
        print("-" * 40)

run_tests()