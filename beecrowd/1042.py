numeros = list(map(int, input("").split(" ")))

def simple_sort(arr1):
	arr = arr1.copy()
	for n in range(len(arr)):
		for i in range(len(arr)):
			current = arr[i]
			if i < len(arr)-1:
				next = arr[i+1]
				if current > next:
                    
					arr[i] = next
					arr[i+1] = current
	return arr

sorted = simple_sort(numeros)
for n in sorted:
	print(n)
	
print("")

for n in numeros:
	print(n)