#plot of long term growth function for coin flips and Kelly Criterion is to maximize this growth function
import numpy
import matplotlib
import math


trials = 1000
probability_of_winning = .6
winning_payoff = 1
f = numpy.arange(0, 1, .1, dtype = numpy.float) #admissable fractions, fraction axis
geomAvgfor_f = numpy.arange(0, len(f), dtype = numpy.float)

#we're creating a wealth process(array) for every fraction in f
for j in range(0, len(f)): 
    Wealth_f = numpy.arange(0,trials,dtype=numpy.float)#initial wealth process sequence/array to be filled in
    Wealth_f[0] = 1 #initial wealth
   
    for i in range(1,trials):
    	if numpy.random.random() > 1.0 - probability_of_winning:
    		payoff = winning_payoff
    	else:
    		payoff = -1
    	Wealth_f[i] = Wealth_f[i-1]*(1+(f[j]*payoff)) #recursive wealth process
    
    geomAvg_f = [(1/k)*math.log(Wealth_f[k]) for k in range(1,trials)] #sequence of running geometric averages
    geomAvgfor_f[j] = geomAvg_f[trials-2]
    print('f is ', f[j], ' geometric average is ', geomAvg_f[trials-2])

#matplotlib.pyplot.ylim((-.5,.5))
matplotlib.pyplot.plot(f, geomAvgfor_f)   
matplotlib.pyplot.title('LongTerm Growth Rate') 
matplotlib.pyplot.xlabel('Exposure/Fraction f')
matplotlib.pyplot.show()