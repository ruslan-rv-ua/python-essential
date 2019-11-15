__all__ = ['main']

def log():
	print('name:', __name__)
	print('file:', __file__)

def main():
	log()

if __name__ == '__main__':
	main()