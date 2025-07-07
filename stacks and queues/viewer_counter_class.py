from collections import deque


class ViewerCounterOptimized:
    def __init__(self, window_size):
        self.window_size = window_size
        self.viewers = {"subscriber": deque(), "guest": deque(), "follower": deque()}

    def join(self, timestamp, viewer_type):
        queue = self.viewers[viewer_type]
        if queue and queue[-1][0] == timestamp:
            queue[-1][1] += 1
        else:
            queue.append([timestamp, 1])

    def get_viewers(self, timestamp, viewer_type):
        queue = self.viewers[viewer_type]
        count = 0

        while queue and queue[0][0] < timestamp - self.window_size:
            queue.popleft()

        for ts, num in queue:
            count += num

        return count


def run_tests_optimized():
    counter = ViewerCounterOptimized(10)
    actions = [
        (1, "subscriber"),
        (1, "guest"),
        (2, "follower"),
        (2, "follower"),
        (2, "follower"),
        (3, "follower"),
    ]
    for timestamp, viewer_type in actions:
        counter.join(timestamp, viewer_type)

    tests = [
        (10, "subscriber", 1),
        (10, "guest", 1),
        (10, "follower", 4),
        (13, "follower", 1),
    ]

    passed = 0
    failed = 0

    print("🔍 Running ViewerCounterOptimized Tests...\n")

    for i, (timestamp, viewer_type, expected) in enumerate(tests, 1):
        result = counter.get_viewers(timestamp, viewer_type)
        if result == expected:
            status = "✅ PASSED"
            passed += 1
        else:
            status = "❌ FAILED"
            failed += 1

        print(f"Test {i}: {status}")
        print(f"  Input:     timestamp = {timestamp}, type = '{viewer_type}'")
        print(f"  Expected:  {expected}")
        print(f"  Got:       {result}")
        print()

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests_optimized()
