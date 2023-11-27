[7:31 pm, 27/11/2023] Chandrika: class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for i in range(n):
            res += mat[i][i] + (0 if n - i - 1 == i else mat[i][n - i - 1])
        return res
[7:45 pm, 27/11/2023] Poornima Aditya (H): Ok
