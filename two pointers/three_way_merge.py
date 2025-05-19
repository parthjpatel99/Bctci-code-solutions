def three_way_merge(arr1, arr2, arr3):
    p1 = p2 = p3 = 0
    res = []

    while p1 < len(arr1) or p2 < len(arr2) or p3 < len(arr3):
        min_val = float('inf')
        
        if p1 < len(arr1) and min_val > arr1[p1]:
            min_val = arr1[p1]
        if p2 < len(arr2) and min_val > arr2[p2]:
            min_val = arr2[p2]
        if p3 < len(arr3) and min_val > arr3[p3]:
            min_val = arr3[p3]

        if p1 < len(arr1) and arr1[p1] == min_val:
            p1 += 1
        if p2 < len(arr2) and arr2[p2] == min_val:
            p2 += 1
        if p3 < len(arr3) and arr3[p3] == min_val:
            p3 += 1
        
        if not res or res[-1] != min_val:
            res.append(min_val)

    return res
        
def run_tests():
    tests = [
        # Example from the book
        ([2, 3, 3, 4, 5, 7], [3, 3, 9], [3, 3, 9], [2, 3, 4, 5, 7, 9]),
        # Additional test cases
        ([], [], [], []),
        ([1], [], [], [1]),
        ([1], [1], [1], [1]),
        ([1, 2, 3], [2, 3, 4], [3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 1, 1], [1, 1], [1], [1]),
        ([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ]
    
    passed = 0
    failed = 0
    
    print("Running tests:")
    print("-" * 50)
    
    for i, (arr1, arr2, arr3, want) in enumerate(tests, 1):
        got = three_way_merge(arr1, arr2, arr3)
        test_name = f"Test #{i}"
        
        try:
            assert got == want, f"got: {got}, want: {want}"
            print(f"✅ {test_name} PASSED")
            print(f"   Input: arr1={arr1}, arr2={arr2}, arr3={arr3}")
            print(f"   Expected: {want}")
            print(f"   Got: {got}")
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_name} FAILED: {e}")
            print(f"   Input: arr1={arr1}, arr2={arr2}, arr3={arr3}")
            print(f"   Expected: {want}")
            print(f"   Got: {got}")
            failed += 1
        
        print("-" * 50)
    
    print(f"Summary: {passed} passed, {failed} failed")

run_tests()