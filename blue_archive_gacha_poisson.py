from scipy.stats import poisson
l = 200*0.03
for i in range(21):
    print('星3以上が' + str(i) + '回出る確率は' + str(poisson.pmf(i, l) * 100) + '%')

sum = 0
for i in range(20):
    sum += poisson.pmf(i, l) * 100
    print('星3以上が' + str(i+1) + '回以上出る確率は' + str(100 - sum) + '%')
