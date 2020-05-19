import sys
answer = ''

def isValidPosition(current_column, current_row, queen_columns, n):
    is_valid = True
    for j in range(current_row):
        # check for column conflict
        if(queen_columns[j] == current_column):
            is_valid = False
            break
        #check for diagonal conflict
        if(abs(queen_columns[j] - current_column) == abs(current_row - j)):
            is_valid = False
            break
    return is_valid

def appendToAnswerString(queen_columns, n):
    global answer
    for i in range(n):
        for j in range(n):
            if(queen_columns[j] == i):
                answer += '1'
            else:
                answer += '0'
        answer += '\n'
    answer += '\n'
        
def getQueenPositions(current_row, queen_columns, n):
    if(current_row == n):  #solution has been found
        appendToAnswerString(queen_columns, n)
        return
    #try out each column as possible position for current_row
    for column in range(n):
        if(isValidPosition(column, current_row, queen_columns, n)):
            queen_columns[current_row] = column
            #good so far, check if next queen can find a position
            getQueenPositions(current_row + 1, queen_columns, n)

def nQueens(n):
    global answer
    queen_columns = [0] * n
    getQueenPositions(0, queen_columns, n) #main Method
    is_answer = False 
    for i in range(len(answer)):
        if(answer[i] == '1'):
            is_answer = True 
            break 
    if(is_answer):
        return answer 
    return 'No Solution Exists'
    
def main():
    n = int(input())
    result = nQueens(n)
    print(result)

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    main()

