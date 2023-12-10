import queue

# Step 1 & 2: Create a Priority Queue object
pq = queue.PriorityQueue()

# Step 3: Add elements to the priority queue
# The first element of the tuple is the priority, and the second element is the data
pq.put((2, "Second task"))
pq.put((1, "First task"))
pq.put((3, "Third task"))

# Step 4: Pop an element from the priority queue
# The item with the highest priority (lowest number) will be popped first
item = pq.get()

# Step 5: Show the output
print("Popped item:", item)

# Optional: Show remaining items in the priority queue
print("Remaining items in priority queue:")
while not pq.empty():
    print(pq.get())
