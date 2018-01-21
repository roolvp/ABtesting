#Matplotlib tutorial
#https://matplotlib.org/users/pyplot_tutorial.html
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta

#The first list is the x axis the y axis is the second
#The third argument is a solid blue line by default
#'ro' represents red circles
#plt.plot([1,2,3,12],[2,4,5,2],'ro')
#arguments are xmin xmax ymin y max
#plt.axis([0,15,0,6])
plt.ylabel('random number')
plt.xlabel('more numbers')
#plt.show()
#it internally works with numpy arraws
#samples = np.arange(0.,5.,0.2)
#print(samples)
#plt.plot(samples,samples*samples,'r')
#plt.show()
#evenly distributed set of numbers
x = np.linspace(0, 1, 200)

pdfvalues = beta.pdf(x,140,20)
pdfvalues2 = beta.pdf(x,50,20)

plt.plot(x,pdfvalues,label="Disbribution")
plt.plot(x,pdfvalues2,label="Disbribution 2")
plt.legend()
plt.show()






