import queue

# Step 1 & 2: Create a Queue object
q = queue.Queue()

# Step 3: Add an element to the queue
q.put("Hello")

# Step 4: Pop an element from the queue
item = q.get()

# Step 5: Show the output
print("Popped item:", item)

# Optional: Check if the queue is empty now
print("Is the queue empty?", q.empty())
