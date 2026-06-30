# each row has to not have duplicate numbers 1 - 9
# each column has to not have duplicate numbers 1 - 9
# each 3 x 3 cannot have duplicates 1 - 9


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for line in board:
            print(line)
        
        for line in board:
            c = Counter(line)
            for value, freq in c.items():
                if value != ".":
                    if freq > 1:
                        return False
        
        for col_ind in range(len(board[0])):
            for row in board:
                column = [row[col_ind]]
            c = Counter(column)
            for value, freq in c.items():
                if value != ".":
                    if freq > 1:
                        return False

        for box_row in range(3):
            for box_col in range(3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[box_row * 3 + i][box_col * 3 + j])
                # now check your 3x3 box
                c = Counter(box)
                for value, freq in c.items():
                    if value != ".":
                        if freq > 1:
                            return False

        return True




