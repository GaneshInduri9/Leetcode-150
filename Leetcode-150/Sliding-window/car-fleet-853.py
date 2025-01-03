from typing import List

class Solution:
    """
    Explanation:
        To better understand this problem draw postion vs time graph 
        for this problem we see that at some point two positions are going 
        to intersect and if they so that means they are involved in a car feet.
        To solve this we would sort the pair array we just created in desecnding 
        order calculate the time for each position to reach the target.
        Then for B car if the time is less then the A car's target time 
        that means we have found fleet and we remove the one with higher speed 
        cause it's going to move with speed of one which has slower sped after fleet 
        and in the end we can return the len of the stack to find the fleets.
    """

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        # Sort positions in descending order
        pair.sort(key=lambda x: x[0], reverse=True)
        
        stack = []
        for p, s in pair:
            # Calculate time to reach the target
            time = (target - p) / s
            stack.append(time)
            # If the car behind reaches the target sooner or simultaneously, they form a fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # Remove the faster car since it merges with the slower car
        return len(stack)

# Helper function for testing
def testCarFleet():
    solution = Solution()

    # Test cases
    tests = [
        {
            "target": 12,
            "position": [10, 8, 0, 5, 3],
            "speed": [2, 4, 1, 1, 3],
            "expected": 3
        },
        {
            "target": 10,
            "position": [6, 8],
            "speed": [3, 2],
            "expected": 2
        },
    ]

    # Run each test
    for i, test in enumerate(tests):
        result = solution.carFleet(test["target"], test["position"], test["speed"])
        assert result == test["expected"], f"Test {i+1} failed: got {result}, expected {test['expected']}"
        print(f"Test {i+1} passed!")

# Run tests
if __name__ == "__main__":
    testCarFleet()
