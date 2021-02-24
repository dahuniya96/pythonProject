def solution(board, moves):
    answer = 0
    board2 = []

    for i in moves:
        for j in range(len(board)):
            if (board[j][i - 1] != 0):
                board2.append(board[j][i - 1])
                board[j][i - 1] = 0
                break

    k = 1
    for i in range(len(board2)):
        for j in range(len(board2)):
            if (len(board2) <= 1):
                k = 0
                break
            if (board2[j] == board2[j + 1]):
                board2.pop(j + 1)
                board2.pop(j)
                answer += 2
                break
            if (len(board2) - 2 == j):
                k = 0
                break
        if (k == 0):
            break
    return answer


board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 5, 1, 4, 3]
# 43
# 4

solution(board, moves)
