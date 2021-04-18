"""
Simulate a queue of integers using list methods:
append (to simulate enqueue) and pop with the argument 0 (to simulate dequeue).
Enqueue the values 3, 2 and 1, then dequeue them to show that they’re removed in FIFO order.
"""

nums = list()

nums.append(3)
nums.append(2)
nums.append(1)

print(nums)

print(nums.pop(0))
print(nums.pop(0))
print(nums.pop(0))

print(nums)
