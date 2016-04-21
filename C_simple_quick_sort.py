import xml.etree.ElementTree as X

def partition(input, low, high):
	pivot = input[high]
#	print "low = %d"%low
#	print "high = %d"%high
	i = low
	for j in range (low, high):
#		print "j = %d"%j
		if input[j] < pivot:
			input[i], input[j] = input[j], input[i]
			i = i + 1
	input[i], input[high] = input[high], input[i]
	return i

def quick_sort(input, low, high):
	if low < high:
		p = partition(input, low, high)
		quick_sort(input, p+1, high)
		quick_sort(input, low, p-1)


r = X.parse('C_sample.xml').getroot()
print r
arr = map(int, r.text.split())
print arr
quick_sort(arr, 0, (len(arr) - 1))

for i in arr:
	print i
