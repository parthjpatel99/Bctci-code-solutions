# Q1

input1 = ["apple", "Banana", "3", "Cherry", "42", "GRAPE", "10"]
expected1 = ["GRAPE", "Cherry", "Banana", "apple", "42", "3", "10"]


def sort_q1(input1):
    return sorted(input1, key=lambda s: s.lower(), reverse=True)


try:
    print("Running Q1 Test...")
    print("-" * 50)
    result1 = sort_q1(input1)
    print(f"Input: {input1}")
    print(f"Expected Output: {expected1}")
    print(f"Actual Output:   {result1}")
    assert result1 == expected1, f"Test failed: {result1} != {expected1}"
    print("Test passed!")
except AssertionError as e:
    print(e)

# Q2
input2 = [[3, 9], [1, 4], [4, 7], [2, 3]]
expected2 = [[2, 3], [1, 4], [4, 7], [3, 9]]


def sort_q2(input2):
    return sorted(input2, key=lambda x: x[1])


try:
    print("Running Q2 Test...")
    print("-" * 50)
    result2 = sort_q2(input2)
    print(f"Input: {input2}")
    print(f"Expected Output: {expected2}")
    print(f"Actual Output:   {result2}")
    assert result2 == expected2, f"Test failed: {result2} != {expected2}"
    print("Test passed!")
except AssertionError as e:
    print(e)

# Q3


class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value


input3 = [
    Card(8, "hearts"),
    Card(8, "clubs"),
    Card(3, "clubs"),
    Card(3, "hearts"),
]

expected3 = [
    Card(3, "clubs"),
    Card(3, "hearts"),
    Card(8, "clubs"),
    Card(8, "hearts"),
]


def sort_q3(input3):
    suit_map = {
        "clubs": 0,
        "diamonds": 3,
        "hearts": 1,
        "spades": 2,
    }
    return sorted(input3, key=lambda card: (card.value, suit_map[card.suit]))


try:
    print("Running Q3 Test...")
    print("-" * 50)
    result3 = sort_q3(input3)
    result3_str = [(card.value, card.suit) for card in result3]
    expected3_str = [(card.value, card.suit) for card in expected3]
    print(f"Input: {[(card.value, card.suit) for card in input3]}")
    print(f"Expected Output: {expected3_str}")
    print(f"Actual Output:   {result3_str}")
    assert (
        result3_str == expected3_str
    ), f"Test failed: {result3_str} != {expected3_str}"
    print("Test passed!")
except AssertionError as e:
    print(e)

# Q4

input4 = [Card(8, "hearts"), Card(8, "clubs"), Card(3, "clubs"), Card(3, "hearts")]
expected4 = [Card(3, "hearts"), Card(8, "hearts"), Card(3, "clubs"), Card(8, "clubs")]


def sort_q4(input4):
    suit_map = {"hearts": 0, "clubs": 1, "diamonds": 2, "spades": 3}

    return sorted(input4, key=lambda card: (suit_map[card.suit], card.value))

try:
    print("Running Q4 Test...")
    print("-" * 50)
    result4 = sort_q4(input4)
    result4_str = [(card.value, card.suit) for card in result4]
    expected4_str = [(card.value, card.suit) for card in expected4]
    print(f"Input: {[(card.value, card.suit) for card in input4]}")
    print(f"Expected Output: {expected4_str}")
    print(f"Actual Output:   {result4_str}")
    assert (
        result4_str == expected4_str
    ), f"Test failed: {result4_str} != {expected4_str}"
    print("Test passed!")
except AssertionError as e:
    print(e)
# Q5

input5 = [
    Card(9, "clubs"),
    Card(4, "spades"),
    Card(9, "spades"),
    Card(4, "clubs"),
]

expected5 = [
    Card(4, "spades"),
    Card(4, "clubs"),
    Card(9, "clubs"),
    Card(9, "spades"),
]

def sort_q5(input5):
    return sorted(input5, key = lambda card: card.value)

try:
    print("Running Q5 Test...")
    print("-" * 50)
    result5 = sort_q5(input5)
    result5_str = [(card.value, card.suit) for card in result5]
    expected5_str = [(card.value, card.suit) for card in expected5]
    print(f"Input: {[(card.value, card.suit) for card in input5]}")
    print(f"Expected Output: {expected5_str}")
    print(f"Actual Output:   {result5_str}")
    assert (
        result5_str == expected5_str
    ), f"Test failed: {result5_str} != {expected5_str}"
    print("Test passed!")
except AssertionError as e:
    print(e)
# Q6