class data:
    sum_of_papers=[]
    name_of_paper=[]
    TOI=[]
    Hindu=[]
    ET=[]
    BM=[]
    HT=[]
    
    def __init__(self):
        self.TOI=[3,3,3,3,3,5,6]
        self.Hindu=[2.5,2.5,2.5,2.5,2.5,4,4]
        self.ET=[4,4,4,4,4,4,10]
        self.BM=[1.5,1.5,1.5,1.5,1.5,1.5,1.5]
        self.HT=[2,2,2,2,2,4,4]
        
    def weeklyCharges(self):
        self.name_of_paper=['TOI','Hindu','ET','BM','HT']
        self.sum_of_papers=[sum(self.TOI),sum(self.Hindu),sum(self.ET),sum(self.BM),sum(self.HT)]

obj=data()

obj.weeklyCharges()

weekly_sum=obj.sum_of_papers

budget=int(input("Enter the weekly budget "))

res=set()

for i in range(len(weekly_sum)):
    for j in range(i+1,len(weekly_sum)):
        if((weekly_sum[i]+weekly_sum[j])<budget):
           res.add("{"+str(obj.name_of_paper[i])+","+str(obj.name_of_paper[j])+"}")
           
for i in res:
    print(i,end=' ')
