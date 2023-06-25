# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 12:55:34 2022

@author: dq000
"""

'''
Pre-test | design the test
- independent  test on the [landing page]
- dependent    reulst on the [converted]
- signafiicance alpha = 0.05 | confidence level is 95T
- sample size

- kpi metrics [ 13% ----> 15%, 2 percent increament for conversion rate]
- hypotheis 2 tailed test
- HO
- HA


Power analysis  to deterimne the sample size
- alpha = 0.05
- power[1-beta] = 0.8
- effiecitve size
'''

import statsmodels.api as sms
import scipy.stats as stats
eff_size = sms.stats.proportion_effectsize(0.13, 0.15)
#print(eff_size)

import statsmodels.stats.power as power
import math
power_ratio = 0.8
sample_size = power.NormalIndPower().solve_power(eff_size, power = power_ratio, alpha = 0.05)
sample_size = math.ceil(sample_size)
print(f'The test needs {sample_size} sampels for both control and treatment group')

#Test - collect the data


import pandas as pd
df = pd.read_csv('c:/data/ab_data.csv', parse_dates=['timestamp'])
#print(df.info())
# shapes
# columns
# statistics

#print(df.shape)
#print(df.columns)
#print(df.dtypes)
#print(df)

'''
print(df['group'].unique())
print(df['landing_page'].unique())
print(pd.crosstab(df['group'], df['landing_page']))
print(df['user_id'].value_counts())
'''

counts = df['user_id'].value_counts()
user_drop_list = counts[counts > 1].index

df = df[~df['user_id'].isin(user_drop_list)]

#print(df)

# data sampling

df_control = df[df['group'] == 'control'].sample(n=sample_size, random_state=22)
df_treatment = df[df['group'] == 'treatment'].sample(n=sample_size, random_state=22)


df_sample = pd.concat([df_control, df_treatment])
df_sample.reset_index(drop=True, inplace=True)
print(df_sample)

'''

Post-test

'''

import numpy as np

stderr = lambda x: stats.sem(x)

c_ = df_sample.groupby(['group'])['converted']
test_summary = c_.agg([np.mean, np.std, stderr])
test_summary.columns=['conv_rate', 'std', 'str']
print(test_summary)

import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x=df_sample['group'], y=df_sample['converted'])
plt.show()


from statsmodels.stats.proportion import proportions_ztest, proportion_confint
result_control = df_sample[df_sample['group']=='control']['converted']
result_treatment = df_sample[df_sample['group']=='treatment']['converted']

n_control = result_control.count()
n_treatment = result_treatment.count()



z_stat, p_value = proportions_ztest([result_control.sum(), result_treatment.sum()], [n_control, n_treatment])
(l_c, l_t), (u_c, u_t) = proportion_confint([result_control.sum(), result_treatment.sum()], [n_control, n_treatment], alpha = 0.05)

print(p_value)
print(f'for the control group:   [{l_c:.3f}, {u_c:.3f}]')
print(f'for the treatment group: [{l_t:.3f}, {u_t:.3f}]')






