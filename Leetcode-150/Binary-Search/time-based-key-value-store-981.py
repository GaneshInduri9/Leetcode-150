from collections import defaultdict

class TimeMap:
    """
    TimeMap class to store key-value pairs with timestamps and retrieve the closest value at a given timestamp.
    
    Operations:
    - set(key, value, timestamp): Stores the key-value pair with the given timestamp.
    - get(key, timestamp): Returns the value associated with the key at the given timestamp.
      If the exact timestamp does not exist, it returns the value associated with the largest timestamp <= given timestamp.
    """

    def __init__(self):
        # Dictionary to store key-value pairs with timestamps
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the key-value pair with the provided timestamp in the map.
        """
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Retrieves the value for the key at or before the given timestamp using binary search.
        If no such value exists, returns an empty string.
        """
        if key not in self.map:
            return ""
        
        values = self.map[key]
        bestIndex = -1
        
        # Binary search to find the largest timestamp <= the given timestamp
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            midTimestamp = values[mid][0]
            if midTimestamp <= timestamp:
                bestIndex = mid  # Found a valid timestamp, search further to the right
                l = mid + 1
            else:
                r = mid - 1
        
        if bestIndex == -1:
            return ""  # No valid timestamp found
        return values[bestIndex][1]  # Return the value at the closest timestamp

# Time Complexity:
# - `set` operation: O(1), since we just append to the list.
# - `get` operation: O(log n), where n is the number of timestamps stored for the given key, due to the binary search.

# Helper function to test the TimeMap implementation
def testTimeMap():
    # Test 1: Basic functionality
    tm = TimeMap()
    tm.set("foo", "bar", 1)  # Store key "foo" with value "bar" at timestamp 1
    assert tm.get("foo", 1) == "bar"  # Exact timestamp match
    assert tm.get("foo", 2) == "bar"  # Closest earlier timestamp is 1
    print("Test 1 passed!")

    # Test 2: Multiple values for the same key
    tm.set("foo", "bar2", 4)  # Store a new value for the same key at timestamp 4
    assert tm.get("foo", 3) == "bar"  # Closest earlier timestamp is 1
    assert tm.get("foo", 5) == "bar2"  # Closest earlier timestamp is 4
    print("Test 2 passed!")

    # Test 3: No valid timestamp (timestamp is before any set values)
    assert tm.get("foo", 0) == ""  # No timestamp before 1, so return ""
    print("Test 3 passed!")

    # Test 4: Multiple keys with separate timestamps
    tm.set("bar", "baz", 2)
    assert tm.get("bar", 2) == "baz"  # Exact match at timestamp 2
    assert tm.get("bar", 3) == "baz"  # Closest earlier timestamp is 2
    print("Test 4 passed!")

    # Test 5: Case where key is not present
    assert tm.get("nonexistent_key", 1) == ""  # No such key, should return ""
    print("Test 5 passed!")

# Main function to execute the tests
if __name__ == "__main__":
    testTimeMap()
