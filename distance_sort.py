def merge_distances(a,b,dist):
    i,j,k = 0,0,0

    while i < len(a) and j < len(b):
        if a[i][1] < b[j][1]:
            dist[k] = a[i]
            i += 1
        else:
            dist[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        dist[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        dist[k] = b[j]
        j += 1
        k += 1

def merge_sort_distance(arr):
    if len(arr) <= 1:
        return arr

    mid  = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort_distance(left)
    merge_sort_distance(right)

    res = merge_distances(right, left, arr)

def return_dist(res):
    for restaurant in res:
        print(restaurant[0] + ' is about ' + restaurant[1] + ' away')

