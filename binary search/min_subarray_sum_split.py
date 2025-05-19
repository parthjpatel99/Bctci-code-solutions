def min_subarray_sum_split(arr, k):

    def get_no_of_splits(max_sum):
        splits = 1
        currSum = 0

        for num in arr:
            if currSum + num > max_sum:
                splits+=1
                currSum = num
            else:
                currSum+=num
        return splits
    
    def isBefore(max_sum):
        splits = get_no_of_splits(max_sum)
        return splits > k
    
    l = max(arr)
    r = sum(arr)

    if not isBefore(l):
        return l
    while r - l > 1:
        mid = (l+r) //2 
        if isBefore(mid):
            l = mid
        else:
            r = mid
        
    return r

def run_tests():
    tests = [
        # Example 1 from the book
        ([10, 5, 8, 9, 11], 3, 17),
        # Example 2 from the book
        ([10, 10, 10, 10, 10], 2, 30),
        # Example 3 from the book
        ([9, 12, 13], 3, 13),
        # Edge case - k=1
        ([1, 2, 3], 1, 6),
        # Edge case - k=length
        ([1, 2, 3], 3, 3),
        # Edge case - single element
        ([5], 1, 5)
    ]

    total_tests = len(tests)
    passed_tests = 0
    failed_tests = 0
    
    print("==== Running Subarray Split Tests ====\n")
    
    for i, (arr, k, want) in enumerate(tests, 1):
        try:
            got = min_subarray_sum_split(arr, k)
            
            if got == want:
                result = "✅ PASS"
                passed_tests += 1
            else:
                result = "❌ FAIL"
                failed_tests += 1
                
            print(f"Test #{i}: {result}")
            print(f"  Array: {arr}")
            print(f"  Number of subarrays (k): {k}")
            print(f"  Expected Min Sum: {want}")
            print(f"  Actual Min Sum: {got}")
            print("")
            
        except Exception as e:
            failed_tests += 1
            print(f"Test #{i}: ❌ ERROR")
            print(f"  Array: {arr}")
            print(f"  Number of subarrays (k): {k}")
            print(f"  Expected Min Sum: {want}")
            print(f"  Error: {str(e)}")
            print("")
    
    # Print summary
    print("==== Test Summary ====")
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_tests} ({passed_tests/total_tests*100:.1f}%)")
    print(f"Failed: {failed_tests} ({failed_tests/total_tests*100:.1f}%)")
    
    if failed_tests == 0:
        print("\n✅ All tests passed!")
    else:
        print(f"\n❌ {failed_tests} test(s) failed!")

run_tests()