import numpy as np
import matplotlib.pyplot as plt
# boostraping
pre_compaign = [30, 55, 92, 5, 79, 63, 80, 17, 2, 83, 88, 61, 7, 46, 39, 29, 77, 76, 71, 22, 27, 84, 53, 96, 26, 45, 99, 15, 41, 75, 91, 24, 11, 13, 10, 51, 60, 54, 18, 3, 38, 64, 49, 0, 42, 37, 21, 35, 57, 12]
post_compaign= [65, 34, 51, 23, 56, 88, 84, 57, 87, 58, 24, 62, 21, 63, 45, 93, 59, 0, 6, 95, 2, 71, 61, 17, 46, 44, 91, 28, 72, 12, 85, 32, 96, 69, 67, 75, 4, 41, 92, 40, 54, 25, 99, 74, 52, 50, 89, 53, 78, 94, 29,47,46,57,50,87, 58, 24, 62, 21, 63, 45, 93, 59]

# eda
print(len(pre_compaign),len(post_compaign))
print(round(np.mean(pre_compaign),2),round(np.mean(post_compaign),2))

## test if normal distribution: his/qq plot
# plt.hist(pre_compaign,bins=50, )
# plt.show()
# plt.hist(post_compaign,bins=50, )
# plt.show()

# if the post and pre are normal distribution
# test the difference of the mean are signifacant or not
diff_mean = np.mean(pre_compaign) - np.mean(post_compaign)
print('sample mean is', diff_mean)

# given the CI is deigned to be 90% and two tails
import scipy.stats as stats
lcv = stats.norm.ppf(0.05)
ucv = stats.norm.ppf(0.95)
print(lcv,ucv)

# standard error
se = np.sqrt((np.std(pre_compaign)**2/len(pre_compaign)) + (np.std(post_compaign)**2/len(post_compaign)))
print(se)
lower_limit = diff_mean + lcv*se
up_limit = diff_mean + se*ucv

print(lower_limit,up_limit)

bs_diff = []
for i in range(5000):
    re_pre_campaign = np.random.choice(pre_compaign,len(pre_compaign))
    re_post_campaign = np.random.choice(post_compaign, len(pre_compaign))
    bs_diff.append(np.mean(re_pre_campaign)-np.mean(re_post_campaign))

print('bootrapping mean -', np.mean(bs_diff))

plt.hist(bs_diff,bins=50, )
plt.grid()
plt.show()

lower_limit_bs = np.percentile(bs_diff, 5)
upper_limit_bs = np.percentile(bs_diff,95)
print(lower_limit_bs,upper_limit_bs)
