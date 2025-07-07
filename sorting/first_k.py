import random

def first_k(arr, k):
  if arr == []:
    return []
  kth_val = quickselect(arr, k)
  return [x for x in arr if x <= kth_val]

def quickselect(arr, k):
  if len(arr) == 1:
    return arr[0]
  pivot = random.choice(arr)
  smaller, larger = [], []
  for x in arr:
    if x < pivot:
      smaller.append(x)
    elif x > pivot:
      larger.append(x)

  if k <= len(smaller):
    return quickselect(smaller, k)
  elif k == len(smaller) + 1:
    return pivot
  else:
    return quickselect(larger, k - len(smaller) - 1)
    

def run_tests():
  tests = [
      # Example from the book
      ([15, 4, 13, 8, 10, 5, 2, 20, 3, 9, 11, 27], 5, [2, 3, 4, 5, 8]),
      # Edge case - k = 1
      ([5, 2, 1, 3, 4], 1, [1]),
      # # Edge case - k = length of array
      ([3, 1, 2], 3, [1, 2, 3]),
      # # Edge case - array of length 1
      ([42], 1, [42]),
      # # Reverse sorted array
      ([5, 4, 3, 2, 1], 4, [1, 2, 3, 4]),
      # # Already sorted array
      ([1, 2, 3, 4, 5], 3, [1, 2, 3]),
      # # Edge case - empty array
      ([], 0, []),
      # # Edge case - k = 0
      # ([1, 2, 3], 0, []),
      # # Array with negative numbers
      # ([-3, -1, -4, -2], 3, [-4, -3, -2]),
      # # Mix of positive and negative
      # ([-5, 3, -2, 8, -1], 4, [-5, -2, -1, 3]),
      # # Large numbers
      # ([10**9, -(10**9), 0], 2, [-(10**9), 0])
  ]

  for arr, k, want in tests:
    got = first_k(arr.copy(), k)
    assert set(got) == set(want), f"\nfirst_k({
        arr}, {k}): got: {got}, want: {want}\n"
    assert len(got) == len(want), f"\nfirst_k({arr}, {k}): got length {
        len(got)}, want length {len(want)}\n"

  # Test with large shuffled array
  large_arr = list(range(1, 1_000_001))
  random.shuffle(large_arr)
  got = first_k(large_arr, 2)
  assert set(got) == {1, 2}, f"\nfirst_k(large_shuffled_array, 2): got: {
      got}, want: [1, 2]\n"

run_tests()