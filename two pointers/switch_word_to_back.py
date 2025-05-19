def move_word(arr, word):
    i = s = w = 0 

    while s < len(arr):
        if i < len(word) and arr[s] == word[i]:
            i+=1
            s+=1
        else:
            arr[w] = arr[s]
            w+=1
            s+=1
    
    for c in word:
        arr[w] = c
        w+=1
    

def run_tests():
    tests = [
        # Example 1 from the book
        (list("seekerandwriter"), "edit", list("sekeranwreredit")),
        # Example 2 from the book
        (list("bacb"), "ab", list("bcab")),
        # Example 3 from the book
        (list("babc"), "b", list("abcb")),
        # Additional test cases
        ([], "", []),
        (list("a"), "a", list("a")),
        (list("abc"), "", list("abc")),
        (list("hello"), "ho", list("ellho")),
        (list("abcabc"), "abc", list("abcabc")),
    ]
    
    passed = 0
    failed = 0
    
    print("Running tests:")
    print("-" * 50)
    
    for i, (arr, word, want) in enumerate(tests, 1):
        arr_copy = arr.copy()  # Make a copy since move_word modifies in place
        move_word(arr_copy, word)
        test_name = f"Test #{i}"
        
        try:
            assert arr_copy == want, f"got: {arr_copy}, want: {want}"
            print(f"✅ {test_name} PASSED")
            print(f"   Input: arr={''.join(arr) if arr else '[]'}, word='{word}'")
            print(f"   Expected: {''.join(want) if want else '[]'}")
            print(f"   Got: {''.join(arr_copy) if arr_copy else '[]'}")
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_name} FAILED: {e}")
            print(f"   Input: arr={''.join(arr) if arr else '[]'}, word='{word}'")
            print(f"   Expected: {''.join(want) if want else '[]'}")
            print(f"   Got: {''.join(arr_copy) if arr_copy else '[]'}")
            failed += 1
        
        print("-" * 50)
    
    print(f"Summary: {passed} passed, {failed} failed")

run_tests()