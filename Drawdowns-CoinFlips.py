#we should add some plots of drawdowns and statistics on the drawdowns with fractional Kelly
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
    #matplotlib.pyplot.subplot(2,1,1)
    matplotlib.pyplot.plot(Wealth_f)
    matplotlib.pyplot.title('Wealth/PortfolioValue for f = ' + str(f[j]))
    
    #relative drawdown process
    #print(rel_drawdown_f)
    matplotlib.pyplot.figure()
    #matplotlib.pyplot.subplot(2,1,2)
    matplotlib.pyplot.ylim((-1.0,1.0))
    matplotlib.pyplot.plot(rel_drawdown_f)
    matplotlib.pyplot.title('RelativeDrawdown of Portfolio for Exposure f = ' + str(f[j]))
