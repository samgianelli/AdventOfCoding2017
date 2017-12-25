def main():
	fileName = "input.txt"
	checksumArray = []
	with open(fileName) as f:
		for line in f:
			print(line)
			digitList = [ int(x) for x in line.split()]
			minDigit = min(digitList)
			maxDigit = max(digitList)
			checksumArray.append(maxDigit - minDigit)

	print(sum(checksumArray))

if __name__ == "__main__":
	main()
