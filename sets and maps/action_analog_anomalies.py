def find_anomalies(log):
    opened = {}  # ticket -> agent who opened it
    working_on = {}  # agent -> ticket they are working on
    seen = set()  # tickets that were opened or closed
    anomalies = set()

    for agent, action, ticket in log:
        if action == "open":
            if ticket in seen:
                anomalies.add(ticket)
                continue

            if agent in working_on:
                # If agent is working on another ticket, that ticket is anomalous
                anomalies.add(working_on[agent])

            opened[ticket] = agent
            working_on[agent] = ticket
            seen.add(ticket)
        else:  # close
            if ticket not in opened or opened[ticket] != agent:
                anomalies.add(ticket)
                continue
            if agent not in working_on or working_on[agent] != ticket:
                anomalies.add(ticket)
                continue
            del working_on[agent]
            del opened[ticket]

    # Any tickets still open are anomalous
    anomalies.update(opened.keys())
    return list(anomalies)


def run_tests():
    tests = [
        (
            [
                ["Dwight", "close", 2],
                ["Dwight", "open", 2],
                ["Drew", "open", 32],
                ["Drew", "close", 32],
                ["Drew", "open", 32],
                ["Drew", "close", 32],
                ["Susa", "open", 7],
                ["Jo", "close", 7],
                ["Susa", "open", 33],
                ["Jo", "open", 8],
                ["Jo", "open", 36],
                ["Jo", "close", 8],
                ["Susa", "close", 33],
            ],
            [2, 32, 7, 8, 36],
        ),
        ([], []),
        ([["Alice", "open", 1], ["Alice", "close", 1]], []),
        ([["Alice", "open", 1], ["Alice", "open", 1]], [1]),
        (
            [["Alice", "open", 1], ["Alice", "close", 1], ["Alice", "open", 1]],
            [1],
        ),
        ([["Alice", "open", 1]], [1]),
        ([["Alice", "open", 1], ["Susa", "open", 1]], [1]),
        ([["Alice", "close", 1]], [1]),
    ]

    all_passed = True

    for i, (log, want) in enumerate(tests, 1):
        got = find_anomalies(log)
        got.sort()
        want.sort()
        passed = got == want

        print(f"Test Case {i}: {'PASSED' if passed else 'FAILED'}")
        print(f"  Input Log: {log}")
        print(f"  Expected Output: {want}")
        print(f"  Actual Output:   {got}")
        print()

        if not passed:
            all_passed = False

    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed.")


run_tests()
