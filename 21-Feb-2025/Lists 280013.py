# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())  
    lst = []  # Initialize an empty list
    
    for _ in range(N):
        operation = input().split() 
        
        if operation[0] == "insert":
            lst.insert(int(operation[1]), int(operation[2]))
        elif operation[0] == "print":
            print(lst)
        elif operation[0] == "remove":
            value = int(operation[1])
            if value in lst:  # Check if the value exists before removing
                lst.remove(value)
        elif operation[0] == "append":
            lst.append(int(operation[1]))
        elif operation[0] == "sort":
            lst.sort()
        elif operation[0] == "pop":
            if lst:  # Ensure the list is not empty before popping
                lst.pop()
        elif operation[0] == "reverse":
            lst.reverse()
