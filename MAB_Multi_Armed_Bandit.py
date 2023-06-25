import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# model simulation
epsilon = 0.1
num_of_trail = 10000


ctr_list = [0.01, 0.05, 0.1, 0.15, 0.25]
num_ad = len(ctr_list)
ad_ids = range(num_ad)
clicks = np.zeros(num_ad)
trails = np.zeros(num_ad)
empirical_ctr = np.zeros(num_ad)

weights = np.full(num_ad,1/num_ad)
print('clicks are',clicks,'trails are',trails,'empirical are',empirical_ctr,'weights are',weights)

df = pd.DataFrame(columns=['ad_1','ad_2','ad_3','ad_4','ad_5'])

for trail in range(num_of_trail):
    ad_selected = np.random.choice(ad_ids,size=1,p=weights)[0]
    click_selected = np.random.binomial(size=1, n=1, p=ctr_list[ad_selected])

    clicks[ad_selected] += click_selected
    trails[ad_selected] += 1
    empirical_ctr[ad_selected] = clicks[ad_selected]/trails[ad_selected]
    print(ad_selected)

    if clicks.any():
        print(weights)
        weights[:] = epsilon / (num_ad - 1)
        print('we use only',weights, 'of them to do exploration')
        best_ad = np.argmax(empirical_ctr)
        # we used 1 - epsilon to do exploitation, epsilon to do exploration
        weights[best_ad] = 1 - epsilon

    if trail in [100,500,1000,2000,5000,9999]:
        df.loc[len(df)] = empirical_ctr

df.plot()
plt.show()




