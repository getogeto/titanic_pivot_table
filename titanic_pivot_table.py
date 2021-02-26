# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:00:57 2021

@author: GeTo
"""


import seaborn as sns
titanic = sns.load_dataset("titanic")
titanic.head()
titanic.groupby(["sex","class"])[["survived"]].aggregate("mean").unstack()
titanic.groupby(["sex","class"])["survived"].aggregate("mean")
titanic.pivot_table("survived",index="sex",columns="class")
