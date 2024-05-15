from restaurants import restaurant_data

def merge_restaurants(a,b,arr,key):
    i,j,k = 0,0,0
    #sorted_restaurants = []

    while i < len(a) and j < len(b):
        if a[i][key] < b[j][key]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1

    #return sorted_restaurants

def merge_sort_restaurants(arr,key):
    if len(arr) <= 1:
        return restaurant_data

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort_restaurants(left,key)
    merge_sort_restaurants(right,key)
    
    res = merge_restaurants(right, left, arr, key)
    

def return_restaurants(res, key):
    if key == 'name':
        for i in res:
            print(f'{i}\n')
            # print(i[key])
    elif key == 'price':
        for i in res:
            print("Average price per person at " + i['name'] + " is $" + str(i[key]) + "\n")
    elif key == 'ratings':
        for i in res[::-1]:
            print(i['name'] + "'s rating is " + str(i['ratings']))
    elif key == 'test':
        print(res)


def main():

    merge_sort_restaurants(restaurant_data, 'price')
    return_restaurants(restaurant_data, 'test')

    
if __name__ == '__main__':
    main()

