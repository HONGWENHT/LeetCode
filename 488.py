import functools


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:

        self.ret = float('inf')

        @functools.lru_cache(None)
        def remove(board):
            ans = []
            i = 0
            N = len(board)
            oneMoreTime = False
            while i < N:
                j = i
                while j < N and board[j] == board[i]:
                    j += 1

                if j - i <= 2:
                    ans.extend(board[i:j])
                else:
                    oneMoreTime = True

                i = j
            ans = tuple(ans)
            if oneMoreTime:
                remove(ans)

            return ans

        @functools.lru_cache(None)
        def dfs(hand, board, moves):

            check = ''.join(board)


            print('board : ' + ''.join(board))
            print('hand : ' + ''.join(hand))

            hand = [b for b in hand if b in board and (hand.count(b) + board.count(b)) >= 3]

            board = remove(board)

            if len(board) == 0:
                self.ret = min(self.ret, moves)
            elif len(hand) <= 0:
                pass
            else:

                n = 0
                while n < len(hand):
                    h_l = list(hand)
                    ball = h_l.pop(n)

                    steps = set()

                    count = 0
                    i = 0
                    for j in range(len(board)):
                        if board[i] == board[j]:
                            count += 1
                        else:
                            i = j
                            count = 1
                        if count == 1 and ball == board[i]:
                            steps.add((i, ball))

                    for j in range(1, len(board)):
                        if j < len(board) - 1:
                            if board[j + 1] != ball and board[j - 1] != ball:
                                steps.add((j, ball))

                    for i, b in steps:
                        b_l = list(board)
                        b_l.insert(i, b)
                        dfs(tuple(h_l), tuple(b_l), moves + 1)

                    n += 1

        dfs(tuple(sorted(list(hand))), tuple(board), 0)

        return self.ret if self.ret != float('inf') else -1

Solution().findMinStep("WWRRBBWW",
"WRBRW")