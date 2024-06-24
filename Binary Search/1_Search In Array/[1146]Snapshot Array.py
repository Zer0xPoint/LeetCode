# Implement a SnapshotArray that supports the following interface: 
# 
#  
#  SnapshotArray(int length) initializes an array-like data structure with the 
# given length. Initially, each element equals 0. 
#  void set(index, val) sets the element at the given index to be equal to val. 
# 
#  int snap() takes a snapshot of the array and returns the snap_id: the total 
# number of times we called snap() minus 1. 
#  int get(index, snap_id) returns the value at the given index, at the time we 
# took the snapshot with the given snap_id 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation: 
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= length <= 5 * 10⁴ 
#  0 <= index < length 
#  0 <= val <= 10⁹ 
#  0 <= snap_id < (the total number of times we call snap()) 
#  At most 5 * 10⁴ calls will be made to set, snap, and get. 
#  
# 
#  Related Topics Array Hash Table Binary Search Design 👍 3689 👎 497


# leetcode submit region begin(Prohibit modification and deletion)
class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = 0
        self.arr = []
        for i in range(length):
            self.arr.append([])

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([val, self.snaps])

    def snap(self) -> int:
        self.snaps += 1
        return self.snaps - 1

    def get(self, index: int, snap_id: int) -> int:
        values = self.arr[index]
        res = 0
        start, end = 0, len(values) - 1
        while start <= end:
            mid = (start + end) >> 1
            if values[mid][1] <= snap_id:
                res = values[mid][0]
                start = mid + 1
            else:
                end = mid - 1
        return res


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# leetcode submit region end(Prohibit modification and deletion)


"""Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5"""

# test from here
snapshotArr = SnapshotArray(3)
print(snapshotArr.set(0, 5))
print(snapshotArr.snap())
print(snapshotArr.set(0, 6))
print(snapshotArr.get(0, 0))
