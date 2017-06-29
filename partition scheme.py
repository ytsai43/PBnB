class Subregion:
    def __init__(self,x1,x2):
        self.vertx1 = x1
        self.vertx2 = x2
    def cut(self):
        self.subPoints1 = []
        self.subPoints2 = []
        for a in range(2):
            self.subPoints1.append((self.vertx1[0][a]+self.vertx1[1][a])/2)   # middle point we need in an interval    
            self.subPoints2.append((self.vertx2[0][a]+self.vertx2[1][a])/2)   # middle point we need in an interval
        self.vertx1.append(self.subPoints1)
        self.vertx2.append(self.subPoints2)
        self.vertx1.sort(key = lambda x: (x[-1]))
        self.vertx2.sort(key = lambda x: (x[-1]))
    def pickPoint(self,M):
        self.seg = []
        j = 0
        for m in range(M):
            self.calSubx1 = []
            self.calSubx2 = []
            self.subregion = []
            for i in range(2):
                self.calSubx1.append(self.vertx1[i+m])
                self.calSubx2.append(self.vertx2[i+m])
            self.subregion.append(self.calSubx1)
            self.subregion.append(self.calSubx2)
            self.seg.append(self.subregion)
            #self.subregion.append(self.calSubx2)
            #self.subregion[m].sort(key = lambda x: (x[0]))
        return self.seg

            
feasible=[[[[0, 0], [0, 2]], [[2, 0], [2, 2]]]]
for j in range(3): 
    subset=[]
    for i in range(len(feasible)):
        first = Subregion(feasible[i][0],feasible[i][1])
        first.cut()
        first.pickPoint(2)  
        subset= subset + first.pickPoint(2)
    print(subset)
    feasible=subset[:]
