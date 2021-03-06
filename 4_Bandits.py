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
#for visualizing the Beta distributions
from scipy.stats import beta
import matplotlib.pyplot as plt


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

#Does the testing for a number of samples
def runexperiment(Banditslist):
    for i in range(0,1000):
    #chooses bandit
        testbandit = ChooseBandit(Banditslist)
    #triggers bandit and updates its Beta distribution
        testbandit.updateBeta(testbandit.pullTrigger())
        if i%200 == 0:
            plotbandits(Banditslist)


def plotbandits(Banditslist):
    for i in Banditslist:
    #bring a set of samples
        samples = np.linspace(0,1,200)
    #bring the pdf
    #plot the pdf and label it
        plt.plot(samples,beta.pdf(samples,i.a,i.b),label="Bandit with p = %s"%i.p)
#plot the lengend
    plt.legend()
#show all the pdfs
    plt.show()





#Visualize probability density functions of the Beta distribution

if __name__ == '__main__':
    runexperiment(Banditslist)
    for i in Banditslist:
        print("Bandit p: %s \t has Beta distribution with a = %s and b = %s"%(i.p,i.a,i.b))







