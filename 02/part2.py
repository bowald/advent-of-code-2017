print sum([c for row in [[int(nr) for nr in line.split()] for line in open('input.txt').readlines()] for a in row for c in [a/b for b in row if a is not b and a % b == 0]])