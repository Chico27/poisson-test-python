p = 0.007
lose = 1 - p
for i in range(1, 1001):
    if i % 10:
        continue
    print(str(i) + '連目でピックアップが出ない確率は' + str((lose ** i) * 100))
