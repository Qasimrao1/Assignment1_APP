def swap(A,B):
    temp = A
    A = B
    B = temp
    return A,B


def factorial(n):

    result = 1
    for i in range(1,n+1):
        result *= i
    return result


def fibonacci(n):
    if n<=0:
        return [0]
    else:
        a=0
        b=1
        result=[a]

    for i in range(n - 1):
        c = a + b
        result.append(c)
        b = a
        a = c
    
    return result

def substr(S1,S2):
    if S2 in S1:
        return True
    else:
        return False

def concat(S1,S2):
    return (S1+S2)

def findpath(maze):
    start = False
    start_row = -1
    start_col = -1
    end = False

    rows=len(maze)
    cols=len(maze[0])

    for r in range(0, rows):
        for c in range(0, cols):
            print(maze[r][c], end=" ")
        print()

    path = []

    for r in range(0, rows):
        for c in range(0, cols):
            if maze[r][c] == 1:
                start= True
                start_row = r
                start_col = c
            if start:
                if start_row == 0:
                    if r == 0:
                        path.append([r, c])

                    if r == 1:
                        path.append([1, 2])
                        break
                    if r == 2:
                        path.append([2, 2])
                        break

                if start_row == 1:
                    if r == 1:
                        path.append([r, c])
                        break
            
                    if r == 2:
                        if start_col == 2:
                            path.append([r, start_col])
                            break
                        elif start_col == 0:
                            path.append([r, c])

    return path


if __name__ == "__main__":
    print("====SWAP FUNCTION=====")
    A,B=1,2
    print('Original Values : {},{}'.format(A,B))
    A,B = swap(A,B)
    print('Swapped Values : {},{}'.format(A,B))

    print('\n')
    print("====FACTORIAL=====")
    n=3
    print('Given Number : {}'.format(n))
    print('Factorial : {}'.format(factorial(n)))

    print('\n')
    print("====FIBONACCI=====")
    n=8
    print('Given Number : {}'.format(n))
    print('Fibonacci Series : {}'.format(fibonacci(n)))

    print('\n')
    print("====STRING LENGTH=====")
    String="Qasimrao"
    print('Given String : ' + String)
    print('String Length : {}'.format(len(String)))

    print('\n')
    print("====SUBSTRING CHECK=====")
    Substr='rao'
    print('Main String : ' + String)
    print('Substring : ' + Substr)
    print('Present? : {}'.format(substr(String,Substr)))
    
    print('\n')
    print("====STRING CONCATENATION=====")
    String2=' Assignment'
    print('First String : ' + String)
    print('Second String : ' + String2)
    print('Concatenated : ' + concat(String,String2))

    print('\n')
    print("====PATH FINDER=====")
    maze=[[0, 0, 0], [0, -1, 1], [0, 0, 2]]
    print(findpath(maze))


