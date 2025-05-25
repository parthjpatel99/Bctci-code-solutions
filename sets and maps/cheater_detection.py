from collections import defaultdict
import math

def suspect_students(answers, m, students):
    def same_row(desk1, desk2):
        return math.ceil(desk1 / m) == math.ceil(desk2 / m)

    desk_to_idx = {}
    res = []
    for i, [id, desk, answer] in enumerate(students):
        if answer != answers:
            desk_to_idx[desk] = i

    for id, desk, answer in students:
        next_desk = desk + 1
        if same_row(desk, next_desk) and next_desk in desk_to_idx:
            next_std = students[desk_to_idx[next_desk]]
            if answer == next_std[2]:
                res.append([id, next_std[0]])
    return res


def run_tests():
    tests = [
        # Example from the book
        (
            ["a", "b", "c", "c"],
            5,
            [
                (4, 10, ["a", "b", "c", "d"]),
                (1, 6, ["a", "b", "c", "d"]),
                (3, 8, ["a", "b", "d", "d"]),
                (5, 11, ["a", "b", "c", "d"]),
                (9, 7, ["a", "b", "c", "d"]),
                (6, 16, ["a", "b", "d", "d"]),
            ],
            [[1, 9]],
        ),
        # Additional test cases
        (
            ["a", "b"],
            2,
            [
                (1, 1, ["a", "b"]),
                (2, 2, ["a", "b"]),
            ],
            [],
        ),
        (
            ["a", "b"],
            2,
            [
                (1, 1, ["b", "b"]),
                (2, 2, ["b", "b"]),
            ],
            [[1, 2]],
        ),
        (
            ["a", "b"],
            2,
            [
                (1, 1, ["b", "b"]),
                (2, 3, ["b", "b"]),
            ],
            [],
        ),
    ]

    passed = 0
    failed = 0
    test_num = 1

    for answers, m, students, want in tests:
        got = suspect_students(answers, m, students)
        got.sort()
        want.sort()
        status = "✅" if got == want else "❌"
        print(f"Test {test_num}: {status}")
        print(f"  Answers:  {answers}")
        print(f"  m:        {m}")
        print(f"  Students: {students}")
        print(f"  Expected Output: {want}")
        print(f"  Actual Output:   {got}")
        print("-" * 40)

        if got == want:
            passed += 1
        else:
            failed += 1
        test_num += 1

    total = passed + failed
    print("\nSUMMARY")
    print("=" * 40)
    print(f"Total tests: {total}")
    print(f"Passed:      {passed}")
    print(f"Failed:      {failed}")
    print("=" * 40)


run_tests()
