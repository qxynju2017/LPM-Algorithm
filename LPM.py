class LPM(object):
    def __init__(self):
        self.L1 = []
        self.m = 0

    def input_m(self):
        self.m = int(input())
        for _ in range(self.m):
            self.L1.append(list(map(int, input().rstrip().split())))

    def LPM_atom(self, Lm):
        Lmp1 = []
        for l in range(self.m):
            Lmp1.append([])
        for i in range(self.m):
            for j in range(self.m):
                temp = []
                for k in range(self.m):
                    if self.L1[i][k] == -1 or Lm[k][j] == -1:
                        temp.append(-1)
                    else:
                        temp.append(self.L1[i][k] + Lm[k][j])
                Lmp1[i].append(max(temp))
                temp = []
        return Lmp1

    def LPM(self):
        temp = []
        T = []
        for i in range(self.m):
            if i == 0:
                temp = self.L1
            else:
                temp = self.LPM_atom(temp)
            for k in range(self.m):
                if temp[k][k] == -1:
                    continue
                else:
                    T.append(temp[k][k] / (i + 1))
            print("L" + str(i + 1) + ": ", temp)
        print("iter bound: ", max(T))


if __name__ == '__main__':
    inst = LPM()
    inst.input_m()
    inst.LPM()


