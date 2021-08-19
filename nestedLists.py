if __name__ == '__main__':
    arr = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        arr.append([name,score])
    
    arr.sort()
    first = 100000
    second = 100000
    
    for i in range(len(arr)):
        if (arr[i][1] < first):
            second = first
            first = arr[i][1]
        elif (arr[i][1] < second and arr[i][1] != first):
            second = arr[i][1]
    
    for x in range(len(arr)):
        if(arr[x][1] == second):
            print(arr[x][0])
