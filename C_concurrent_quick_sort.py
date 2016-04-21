import xml.etree.ElementTree as X
import threading

def partition(input, low, high):
	pivot = input[high]
	i = low
	for j in range(low, high):
		if input[j] <= pivot:
			input[i], input[j] = input[j], input[i]
			i = i+1;
	input[i], input[high] = input[high], input[i]
	return i

def quick_sort(input, low, high):
	if low < high:
		p = partition(input, low, high)
		t1 = threading.Thread(target = quick_sort, args = (input, low, p-1))
		t2 = threading.Thread(target = quick_sort, args = (input, p+1, high))
		t1.start()
		print "\nInvoking thread 1:\n Sorting array from %d to %d"%(low, p-1)
		t2.start()
		print "\nInvoking thread 2:\nSorting array from %d to %d"%(p, high)
		t1.join()
	#	print "Terminating thread 1"
		t2.join()
	#	print "terminating thread 2"


r = X.parse('C_sample.xml').getroot()
arr = map(int, r.text.split())
quick_sort(arr, 0, len(arr) - 1)
for i in arr:
	print i
