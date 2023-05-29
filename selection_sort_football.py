def selection_sort_football(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j][2] > arr[min_index][2]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        

arr =[['Kylian Mbappe', 'Paris Saint Germain', 40],
    ['Victor Osimhen', 'Napoli',  28],
    ['Robert Lewandowski', 'Barcelona', 33],
    ['Erling Haaland', 'Mancherter City',  52],
    ['Christopher', 'RB Leipzig', 22]]

selection_sort_football(arr)
print("Hasil pengurutan : ",arr)