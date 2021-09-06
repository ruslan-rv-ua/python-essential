def hanoi1(n, s1, s2, s3):
	if n == 1:
		print(s1, '-', s3)
	else:
		hanoi(n-1, s1, s3, s2)
		print(s1, '-', s3)
		hanoi(n-1, s2, s1, s3)

def hanoi(n, s1, s2, s3):
	if n > 0:
		hanoi(n-1, s1, s3, s2)
		print(s1, '-', s3)
		hanoi(n-1, s2, s1, s3)

		
hanoi(3, '1', '2', '3')