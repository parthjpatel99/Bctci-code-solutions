def num_refills(a, b):
    def isBefore(quo):
        return quo * b <= a
    
    k = 1 
    while isBefore(k*2):
        k*=2
    
    l = k
    r = k*2
    
    while r - l > 1:
        mid = l+ ((r-l) >> 1)
        if isBefore(mid):
            l = mid
        else:
            r = mid
    
    return l

def run_tests():
    tests = [
        # Basic cases
        (10, 2, 5),
        (10, 3, 3),
        (10, 4, 2),
        (10, 5, 2),
        # Large numbers
        (1_000_000, 1, 1_000_000),
        # Large numbers with multiple refills
        (1_000_000, 500_000, 2),
        # Random cases
        (18, 5, 3),
        (182_983, 90, 2033),
    ]

    total_tests = len(tests)
    passed_tests = 0
    failed_tests = 0
    
    print("==== Running Refill Tests ====\n")
    
    for i, (a, b, expected) in enumerate(tests, 1):
        try:
            result = num_refills(a, b)
            
            if result == expected:
                result_status = "✅ PASS"
                passed_tests += 1
            else:
                result_status = "❌ FAIL"
                failed_tests += 1
                
            print(f"Test #{i}: {result_status}")
            print(f"  Initial Amount (a): {a}")
            print(f"  Refill Amount (b): {b}")
            print(f"  Expected Refills: {expected}")
            print(f"  Actual Refills: {result}")
            print("")
            
        except Exception as e:
            failed_tests += 1
            print(f"Test #{i}: ❌ ERROR")
            print(f"  Initial Amount (a): {a}")
            print(f"  Refill Amount (b): {b}")
            print(f"  Expected Refills: {expected}")
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