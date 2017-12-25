def main():
	fileName = "input.txt"
	divisionArray = []
	with open(fileName) as f:
		for line in f:
			digitList = [ int(x) for x in line.split()]
			for digit in digitList:
				for elm in digitList:
					if elm % digit == 0 and elm / digit != 1:
						print elm
						divisionArray.append(elm / digit)
						break

	print(sum(divisionArray))

if __name__ == "__main__":
	main()
