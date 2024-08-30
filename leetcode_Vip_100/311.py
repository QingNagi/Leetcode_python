class Solution(object):
    def multiply(self, A, B):
        m = len(A)
        n = len(B[0])
        posA = self.getSparseRepresentation(A)
        posB = self.getSparseRepresentation(B)
        res = [[0 for i in range(n)] for j in range(m)]
        for valA, xA, yA in posA:
            for valB, xB, yB in posB:
                if yA == xB:
                    res[xA][yB] += valA * valB
        return res
    def getSparseRepresentation(self, A):
        posList = []
        m = len(A)
        n = len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    posList.append([A[i][j],i,j])
        return posList