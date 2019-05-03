#1. simulation of wealth process for a b:1 payoff sequence of bets with constant proportional (f) betting
import numpy
import matplotlib.pyplot
import math

paths = 100 #number of different omegas
trials = 1000 #number of times we gamble, frequency of betting
winning_payoff = 1 #this is b in the b:1 odds
probability_of_winning = 0.6 #this is p
fraction = .2 #this is f, exposure of wealth/bankroll/reserves to gamble payoffs


for j in range(1, paths):
	Wealth = numpy.arange(0,trials,dtype=numpy.float) #initial wealth process sequence/array to be filled in
	Wealth[0] = 1 #initial wealthj
	
	for i in range(1,trials):
		if numpy.random.random() > 1.0 - probability_of_winning:
			payoff = winning_payoff
		else:
			payoff = -1
		Wealth[i] = Wealth[i-1]*(1+(fraction*payoff)) #recursive wealth process
		
	#print(Wealth)
	print('final wealth is ', Wealth[trials-1])
	matplotlib.pyplot.plot(Wealth) #plotting wealth process on arbitrary scale
	geom_Avg = [(1/n)*math.log(Wealth[n]) for n in range(1,trials)] #sequence of running geometric averages
	print('geometric average is ', geom_Avg[trials-2])

matplotlib.pyplot.show()
print('theoretical long run growth rate is ', 0.6*math.log(1+fraction) + 0.4*math.log(1-fraction))


#2.approximation of growth function, theoretical growth function, Kelly-criterion is to maximize theoretical growth rate
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
matplotlib.pyplot.show()

#3.we should add some plots of drawdowns and statistics on the drawdowns with fractional Kelly
#try to visualize the tradeoff between drawdowns and growth-rate with fractional Kelly
import numpy
import math
import matplotlib


trials = 1000
probability_of_winning = .6
winning_payoff = 1

f = numpy.arange(0, 1, .05, dtype = numpy.float)


for j in range(0, len(f[0:5])):
    #drawdown = numpy.arange(0, trials, dtype = numpy.float)
    rel_drawdown_f = numpy.arange(0, trials, dtype = numpy.float)
    rel_drawdown_f[0] = 0


    Wealth_f = numpy.arange(0, trials, dtype = numpy.float)
    Wealth_f[0] = 1

    for i in range(1,trials):
        if numpy.random.random() > 1.0 - probability_of_winning:
            payoff = winning_payoff
        else:
        	payoff = -1
        Wealth_f[i] = Wealth_f[i-1]*(1+(f[j]*payoff)) #recursive wealth process
        rel_drawdown_f[i] = (max(Wealth_f[0:i]) - Wealth_f[i]) / max(Wealth_f[0:i])
    
    #wealth process
    #print(Wealth_f)
    matplotlib.pyplot.figure()
    matplotlib.pyplot.plot(Wealth_f)
    
    #relative drawdown process
    #print(rel_drawdown_f)
    matplotlib.pyplot.figure()
    matplotlib.pyplot.ylim((-1.0,1.0))
    matplotlib.pyplot.plot(rel_drawdown_f)
#still need to add some statistics