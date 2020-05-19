def balancedBraces(N):
    ans = []
    def backtrack(S = '', left = 0, right = 0):
        if len(S) == 2 * N:
            ans.append(S)
            return
        if left < N:
            backtrack(S+'(', left+1, right)
        if right < left:
            backtrack(S+')', left, right+1)

    backtrack()
    return ans

def main():
    n = int(input())
    result = balancedBraces(n)
    for line in result:
        print(line)

if __name__ == '__main__':
    main()
