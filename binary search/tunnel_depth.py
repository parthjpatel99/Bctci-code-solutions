"""
# Tunnel Depth

We are given an `n x n` binary matrix, `tunnel_network`, representing a tunnel network that archeologists have excavated. The ground level is above the first row. The first row is at depth `0`, and each subsequent row is deeper underground.

- 1's represent excavated tunnel pathways in the network.
- 0's represent earth that has not been excavated yet.

The tunnel starts at the top-left and top-right corners (the cells `(0, 0)` and `(0, n - 1)` are always 1's) and consists of a single connected network. That is, this is not a valid input because there is a `1` that is not reachable:

tunnel_network = [
    [1, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
]

Write a function that returns the maximum tunnel depth.

Example 1:
Input: tunnel_network = [
  [1,0,0,0,1],  # depth 0
  [1,1,1,0,1],  # depth 1
  [1,0,1,0,1],  # depth 2
  [1,1,1,1,1],  # depth 3
  [0,0,0,0,0]   # depth 4
]
Output: 3
Explanation: The deepest row containing a 1 is row 3 (0-indexed).

Example 2:
Input: tunnel_network = [
  [1,1,0,0,0,1],
  [0,1,0,0,0,1],
  [1,1,0,0,0,1],
  [1,0,0,0,0,1],
  [1,1,0,0,0,1],
  [0,1,1,1,1,1]
]
Output: 5
Explanation: The deepest row containing a 1 is row 5.

Example 3:
Input: tunnel_network = [[1]]
Output: 0
Explanation: The only row containing a 1 is row 0.

Constraints:

- `1 <= n <= 10^4`
- `tunnel_network[i][j]` is either `0` or `1`
- `tunnel_network[0][0]` and `tunnel_network[0][n-1]` are both `1`
- All `1`s in the grid form a single connected component

Inefficient DFS

def tunnel_depth(tunnel_network):
    R = len(tunnel_network)
    C = len(tunnel_network[0]) if R > 0 else 0

    def isValid(r, c, visited):
        return (
            0 <= r < R
            and 0 <= c < C
            and (r, c) not in visited
            and tunnel_network[r][c] == 1
        )

    def dfs(visited, r, c):
        visited.add((r, c))
        max_depth = r
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if isValid(nr, nc, visited):
                max_depth = max(max_depth, dfs(visited, nr, nc))

        return max_depth

    # Since all 1's are connected, starting from (0,0) suffices
    visited = set()
    max_depth = dfs(visited, 0, 0)

    return max_depth
"""


# Binary Search
def tunnel_depth(tunnel_network):
    R = len(tunnel_network)
    C = len(tunnel_network[0]) if R > 0 else 0

    l = 0
    r = R - 1

    def hasOne(row):
        for c in range(C):
            if tunnel_network[row][c] == 1:
                return True
        return False

    while r - l > 1:
        mid = (l + r) // 2
        if hasOne(mid):
            l = mid
        else:
            r = mid

    return r if hasOne(r) else l


# Test cases
tunnel_network1 = [
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]
print("Example 1:", tunnel_depth(tunnel_network1))  # 3

tunnel_network2 = [
    [1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1],
]
print("Example 2:", tunnel_depth(tunnel_network2))  # 5

tunnel_network3 = [[1]]
print("Example 3:", tunnel_depth(tunnel_network3))  # 0

# T: O(n^2) since grid is n x n
# S: O(n^2) for visited set
