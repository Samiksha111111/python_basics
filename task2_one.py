from collections import deque

tasks = deque()

tasks.append('Task 1')
tasks.append('Task 2')
tasks.append('Task 3')

tasks.popleft()  # Removes 'Task 1'
tasks.rotate(-1)  # Moves 'Task 2' to the end
print(tasks)
