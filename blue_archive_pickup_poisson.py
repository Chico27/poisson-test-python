from scipy.stats import poisson
l = 200*0.007
for i in range(11):
    print('ピックアップが' + str(i) + '回出る確率は' + str(poisson.pmf(i, l) * 100) + '%')

sum = 0
for i in range(10):
    sum += poisson.pmf(i, l) * 100
    print('ピックアップが' + str(i+1) + '回以上出る確率は' + str(100 - sum) + '%')
