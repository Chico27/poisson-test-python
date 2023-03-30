from scipy.stats import poisson
l = 200*0.007
for i in range(11):
    print('ピックアップが' + str(i) + '回出る確率は' + str(poisson.pmf(i, l) * 100) + '%')