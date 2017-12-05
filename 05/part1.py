maze = [int(line) for line in open('input.txt').readlines()]
jumps = []
p = 0
jumps = 0

while p < len(maze):
	l = p
	p += maze[p]
	maze[l] += 1
	jumps += 1

print jumps