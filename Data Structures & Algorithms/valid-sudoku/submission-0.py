class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # recorrer filas 
        for i in range(len(board)):
            numbers = []
            for cell in board[i]:
                if cell == ".":
                    continue
                if cell in numbers:
                    return False
                numbers.append(cell)

        #  recorrer columnas
        for i in range(len(board)):
            numbers = []
            for k in range(len(board)):
                if board[k][i] == ".":
                    continue
                if board[k][i] in numbers:
                    return False
                numbers.append(board[k][i])

        # recorrer cuadros de 3x3
        n = 0
        z = 0
        for i in range(3):
            for i in range(3):
                ## bloque inicia
                numbers = []
                for i in range(n,n+3):
                    for k in range(z,z+3):
                        if board[i][k] == ".":
                            continue
                        if board[i][k] in numbers:
                            return False
                        numbers.append(board[i][k])
                n += 3
                ## bloque termina
            n = 0
            z += 3

        return True