import math
def min_pages_per_day(page_counts, days):
    if not page_counts:
        return 0
    def days_to_finsh(daily_pages):
        req_days = 0

        for chap_pages in page_counts:
            req_days += math.ceil(chap_pages / daily_pages)
        
        return req_days
    
    def isBefore(min_pages):
        return days_to_finsh(min_pages) <= days

    l = 1
    r = max(page_counts)

    while r-l>1:
        mid = (l+r) //2
        if isBefore(mid):
            r = mid
        else:
            l = mid
    return r

def run_tests():
    tests = [
        # Example 1 from book
        ([20, 15, 17, 10], 14, 5),
        # Example 2 from book
        ([20, 15, 17, 10], 5, 17),
        # Example 3 from book
        ([20, 15, 17, 10], 17, 4),
        # Edge case - empty array
        ([], 1, 0),
        # Edge case - single chapter
        ([10], 5, 2),
        # Edge case - days = chapters
        ([1, 2, 3], 3, 3)
    ]

    total_tests = len(tests)
    passed_tests = 0
    failed_tests = 0
    
    print("==== Running Minimum Pages Tests ====\n")
    
    for i, (page_counts, days, want) in enumerate(tests, 1):
        try:
            got = min_pages_per_day(page_counts, days)
            
            if got == want:
                result = "✅ PASS"
                passed_tests += 1
            else:
                result = "❌ FAIL"
                failed_tests += 1
                
            print(f"Test #{i}: {result}")
            print(f"  Chapter Page Counts: {page_counts}")
            print(f"  Available Days: {days}")
            print(f"  Expected Min Pages: {want}")
            print(f"  Actual Min Pages: {got}")
            print("")
            
        except Exception as e:
            failed_tests += 1
            print(f"Test #{i}: ❌ ERROR")
            print(f"  Chapter Page Counts: {page_counts}")
            print(f"  Available Days: {days}")
            print(f"  Expected Min Pages: {want}")
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