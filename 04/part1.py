print len([line for line in open('input.txt').readlines() if not any([word == other for i, word in enumerate(line.split()) for other in line.split()[:i] + line.split()[i+1:]])])