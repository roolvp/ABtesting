#How does Beta work? What is the a and b?
#great video explaining it https://www.youtube.com/watch?v=v1uUgTcInQk

#How to define a class in Python?
#https://www.youtube.com/watch?v=v1uUgTcInQk

#What's important about it? Do do you define methods within a class?
#How does matplotlib pyplot work?
#Why if __name__ main is used?


#The code must plot the Beta distribution of every bandit after a certain number of trials
#With every trial we sample the Beta distribution and choose the bandit with the highest value
#After we choose that bandit, we update the distribution with a value (0 or 1).
#The intuition is that a brings the probability to the right
#a is updated by summing 0 or 1, b is updated with 1 - x. B brings the probability to the left


import numpy as np
from scipy.stats import beta


class Bandit():
    def __init__(self,p):
        self.p = p
        self.a = 1
        self.b = 1
    def pullTrigger(self):
        x = np.random.random()
        print(x < self.p)
        return (x < self.p)
    def updateBeta(self,x):
        self.a += x
        self.b += 1 - x

def ChooseBandit(Bandits):
    winner = []
    hihgest_value = 0
    for bandit in Bandits:
        print(bandit.p)
        sample = np.random.beta(bandit.a, bandit.b)
        if sample > hihgest_value:
            hihgest_value = sample
            winner = bandit
    print("The winner is %s"%winner.p)
    return winner

Banditsp = [0.1,0.4,0.6,0.5]

Banditslist = [Bandit(p) for p in Banditsp]


for i in range(0,1000):
    testbandit = ChooseBandit(Banditslist)
    testbandit.updateBeta(testbandit.pullTrigger())
    print(testbandit.p)
    print(testbandit.a)
    print(testbandit.b)



for i in Banditslist:
    print("Bandit p: %s \t has Beta distribution with a = %s and b = %s"%(i.p,i.a,i.b))

#To do: visualize distributions
