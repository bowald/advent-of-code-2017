maze = [int(line) for line in open('input.txt').readlines()]
p = 0
jumps = 0

while p < len(maze) and p > -1:
	l = p
	p += maze[p]
	d = -1 if p - l > 2 else 1
	maze[l] += d
	jumps += 1

print jumps