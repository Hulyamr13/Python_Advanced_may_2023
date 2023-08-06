def generate_array(arr, index):
    if index == len(arr):
        print(' '.join(map(str, arr)))
        return


    for i in range(len(arr)):
        arr[index] = i + 1
        generate_array(arr, index + 1)
        

n = int(input())
arr = [0] * n
generate_array(arr, 0)
