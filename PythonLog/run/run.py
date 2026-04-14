import sys

def solution():
    input = list(sys.stdin.readline().strip()) 
    bomb = list(sys.stdin.readline().strip())

    result = [] 

    for c in input: 
        result.append(c)

        if len(result) >= len(bomb): 
            start = len(result) - len(bomb)
            tail = result[start:]

            if tail == bomb: 
                del result[-len(bomb):]
    
    result = "".join(result) if len(result) > 0 else "FRULA"
    print(result)

solution()