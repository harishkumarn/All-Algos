import math
class Sudoku(object):
    def __init__(self, data):
        self.board=data
        self.size=len(data)
        self.max=(self.size*(self.size+1))/2
    def is_valid(self):
        print(self.board)
        return self.valid_filling()
    def valid_filling(self):
        length=self.size
        vertical_sum=[0 for i in range(length)]
        transpose=[ [] for i in range(length)]
        for i in self.board:
            for k in i:
                if not isinstance(k,int) or k is True:
                    return False
            if len(set(i)) != length:
                return False
            
            if sum(i) != self.max:
                return False
            for j in range(length):
                if i[j] in transpose[j]:
                    return False
                else:
                    transpose[j]+=[i[j]]
                vertical_sum[j]+=i[j]
        if sum(vertical_sum) != self.max*length:
            return False
        blockSize=int(math.sqrt(length))
        for i in range(0,length,blockSize):
            for j in range(0,length,blockSize):
                cellSet=[]
                for k in range(blockSize):
                    cellSet+=self.board[i+k][j:j+blockSize]
                cellSet=set(cellSet)
                if len(cellSet) != length or sum(cellSet) != self.max:
                    return False
        return True
        