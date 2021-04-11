# 实验的理论基础作业
# 网络诈骗数据相关性分析

# 一、导入模块
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 二、构建数据
# 输入数据向量
rj= [5106,9471,14413,24476,24549]
wm= [68826,73125,77198,85449,90359]
wlzf= [35886,47450,53110,60040,76798]
sjgm= [8.852,9.26,10.07,10.37,10.62]
ydjjgm= [4503,7907,10487,13288,16071]
nf= [2015,2016,2017,2018,2019]
rjzpsr= [21966,23821,25974,28228,30733]
# 利用pandas建立数据框
# 'rjzpje':人均诈骗金额，'wmgm'：网民规模，'wlzfgm'：网络支付规模，'sjyhgm'：社交APP用户规模，
# 'ydjjgm'：移动经济规模,'ydjjgm',人均可支配收入(元)'
df=pd.DataFrame({'人均诈骗金额（元）':rj,'网民规模（万人）':wm,'网络支付规模(万)':wlzf,\
    '社交APP用户规模（万人）':sjgm,'移动经济规模（亿元）':ydjjgm,'人均可支配收入(元)':rjzpsr},index=[2015,2016,2017,2018,2019])
df
df=pd.DataFrame({'rjzpje':rj,'wmgm':wm,'wlzfgm':wlzf,\
    'sjyhgm':sjgm,'ydjjgm':ydjjgm,'rjzpsr':rjzpsr},index=[2015,2016,2017,2018,2019])
df

# 三、相关性分析
# 个各属性相关性
df.corr()
# 相关性图
sns.pairplot(df)
# 相关性图和诈骗金额的关系
sns.pairplot(df, hue= 'rjzpje', markers=["o", "s"])
# 相关热力图
sns.heatmap(df.corr())
# 两两属性相关性图 
# joint plot图
sns.jointplot(x = 'rjzpje', y= 'wmgm', data = df)                   # 人均诈骗金额对网民规模
sns.jointplot(x = 'rjzpje', y= 'wmgm', data = df, kind = 'hex')     
sns.jointplot(x = 'rjzpje', y= 'wmgm', data = df, kind = 'reg')
sns.jointplot(x = 'rjzpje', y= 'wlzfgm', data = df)                 # 人均诈骗金额对网络支付规模
sns.jointplot(x = 'rjzpje', y= 'wlzfgm', data = df, kind = 'hex')
sns.jointplot(x = 'rjzpje', y= 'wlzfgm', data = df, kind = 'reg')
sns.jointplot(x = 'rjzpje', y= 'sjyhgm', data = df)                 # 人均诈骗金额对社交APP规模
sns.jointplot(x = 'rjzpje', y= 'sjyhgm', data = df, kind = 'hex')
sns.jointplot(x = 'rjzpje', y= 'sjyhgm', data = df, kind = 'reg')
sns.jointplot(x = 'rjzpje', y= 'ydjjgm', data = df)                 # 人均诈骗金额对移动支付规模
sns.jointplot(x = 'rjzpje', y= 'ydjjgm', data = df, kind = 'hex')
sns.jointplot(x = 'rjzpje', y= 'ydjjgm', data = df, kind = 'reg')
sns.jointplot(x = 'rjzpje', y= 'rjzpsr', data = df, kind = 'reg')   # 人均诈骗金额对人均可支配收入
# boxplot图
sns.boxplot(x = 'rjzpje', y= 'wmgm', data = df)
sns.boxplot(x = 'rjzpje', y= 'wlzfgm', data = df)
sns.boxplot(x = 'rjzpje', y= 'sjyhgm', data = df)
sns.boxplot(x = 'rjzpje', y= 'ydjjgm', data = df)
sns.boxplot(x = 'rjzpje', y= 'rjzpsr', data = df)
