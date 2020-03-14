import numpy as np
import pandas as pd

data_train=pd.read_csv("Data.csv")
data_train.shape

data_train.info()

data_train = data_train.drop(['state', 'phone number','area code','number vmail messages','total day minutes'], axis = 1)
data_train.head()
type("Loan")
