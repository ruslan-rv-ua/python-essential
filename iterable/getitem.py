class Pow2:
    def __init__(self, max_len):
        self.max_len = max_len
    def __getitem__(self, index):
        if 0 <= index <= self.max_len:
            return 2 ** index
        else:
            raise IndexError
		
p = Pow2(3)
it = iter(p)

for n in Pow2(4):
	print(n)
	

	
	
