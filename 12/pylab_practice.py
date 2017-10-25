import pylab

principal = 10000
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * interestRate

pylab.figure(1)
pylab.clf()
pylab.title('5% Growth, Compounded Annually')
pylab.xlabel('Years of compounding')
pylab.ylabel('Principal')
pylab.plot(values, 'ko')
pylab.show()