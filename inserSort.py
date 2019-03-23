def inserSort(data):
	for i in range(1, len(data), 1):
		j = 1
		while(data[j-1] > data[j] and j > 0):
			temp = data[j-1]
			data[j-1] = data[j]
			data[j] = temp
	return data
