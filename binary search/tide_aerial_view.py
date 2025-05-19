def run_tests():
    tests = [
        # Example from the book
        ([[[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],
          [[1, 0, 0],
           [0, 0, 0],
           [1, 0, 0]],
          [[1, 1, 0],
           [0, 0, 0],
           [1, 0, 0]],
          [[1, 1, 0],
           [1, 1, 1],
           [1, 0, 0]],
          [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 0]]], 2),
        # 3 pictures with increasing water
        ([[[1, 0, 0],
           [1, 0, 0],
           [1, 0, 0]],
          [[1, 1, 0],
           [1, 1, 0],
           [1, 0, 0]],
          [[1, 1, 1],
           [1, 1, 1],
           [1, 0, 0]]], 1),
        # 2 pictures
        ([[[1, 0],
           [0, 0]],
          [[1, 1],
           [1, 0]]], 0),
        # Incremental progression
        ([[[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],
          [[1, 0, 0],
           [0, 0, 0],
           [0, 0, 0]],
          [[1, 0, 0],
           [1, 0, 0],
           [0, 0, 0]],
          [[1, 1, 0],
           [1, 0, 0],
           [0, 0, 0]],
          [[1, 1, 1],
           [1, 0, 0],
           [0, 0, 0]],
          [[1, 1, 1],
           [1, 1, 0],
           [0, 0, 0]],
          [[1, 1, 1],
           [1, 1, 1],
           [0, 0, 0]],
          [[1, 1, 1],
           [1, 1, 1],
           [1, 0, 0]],
          [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 0]],
          [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]],
          ], 4),
        # Edge case - single picture
        ([[[1, 1], [0, 0]]], 0),
        # Edge case - all water
        ([[[1, 1], [1, 1]]], 0),
        # Edge case - all land
        ([[[0, 0], [0, 0]]], 0)
    ]

    total_tests = len(tests)
    passed_tests = 0
    failed_tests = 0
    
    print("==== Running Tide Aerial View Tests ====\n")
    
    for i, (pictures, want) in enumerate(tests, 1):
        try:
            got = TideAerialView().solve(pictures)
            
            if got == want:
                result = "✅ PASS"
                passed_tests += 1
            else:
                result = "❌ FAIL"
                failed_tests += 1
            
            # Format the pictures for better visualization
            formatted_pictures = []
            for pic in pictures:
                pic_str = "[\n"
                for row in pic:
                    pic_str += f"    {row}\n"
                pic_str += "  ]"
                formatted_pictures.append(pic_str)
            
            pictures_str = "[\n  " + ",\n  ".join(formatted_pictures) + "\n]"
                
            print(f"Test #{i}: {result}")
            print(f"  Pictures:")
            print(f"{pictures_str}")
            print(f"  Expected Answer: {want}")
            print(f"  Actual Answer: {got}")
            print("")
            
        except Exception as e:
            failed_tests += 1
            print(f"Test #{i}: ❌ ERROR")
            print(f"  Pictures: {pictures}")
            print(f"  Expected Answer: {want}")
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