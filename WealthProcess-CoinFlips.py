#simulation of wealth process for a b:1 payoff sequence of bets with constant proportional (f) betting
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
	geom_Avg = [(1/k)*math.log(Wealth[k]) for k in range(1,trials)] #sequence of running geometric averages
	print('geometric average is ', geom_Avg[trials-2])

matplotlib.pyplot.show()
print('theoretical long run growth rate is ', 0.6*math.log(1+fraction) + 0.4*math.log(1-fraction))



