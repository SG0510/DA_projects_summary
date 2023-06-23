import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
import numpy as np
df = pd.read_csv('/Users/amberguan/Desktop/BA:DA course/_/data/page_traffic.csv')
print(df)
print(df.shape)
print(df.columns)
# count sample for each page
sns.countplot(x=df["Page"])
# get boxpot to find the mean for each page
sns.boxplot(data=df, x="Page", y="Time")
plt.show()
## from the chart we know the B has longer session time
# then we want to know if b is significantly different than a, we can not do the parametirtc test, because the sample size is too small
mean_a = df[df.Page == 'Page A'].Time.mean()
mean_b = df[df.Page == 'Page B'].Time.mean()
mean_diff = mean_b - mean_a

num_A = df[df.Page=='Page A'].shape[0]
num_B = df[df.Page=='Page B'].shape[0]


def permutation_fun(x, nA, nB):
    num_records = nA + nB
    idx_B = set(random.sample(range(num_records), nA))
    idx_A = set(range(num_records)) - idx_B
    return x.loc[list(idx_B)].mean() - x.loc[list(idx_A)].mean()

perm_diff = [permutation_fun(df.Time,num_A,num_B) for x in range(1000)]
fig, ax = plt.subplots(figsize=(5,5))
ax.hist(perm_diff, bins=11, rwidth=0.9)

# plot the mean_diff to see if it is sig
ax.axvline(mean_diff, color='red', lw =2)
plt.show()

perm_diff = np.array(perm_diff)
print(np.mean(perm_diff > mean_diff))

lower_limit_bs = np.percentile(perm_diff, 5)
upper_limit_bs = np.percentile(perm_diff,95)
print(lower_limit_bs,upper_limit_bs)

# p < critial value, so there is no sig difference between a and b