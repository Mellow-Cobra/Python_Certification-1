import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


os.chdir("C:\\Users\\MMR3\\Documents\\UW\\")

if os.path.isfile("Titanic.csv") is True:
    print("exists")

else:

    print("does not exist")

csv_data = pd.read_csv("Titanic.csv")

df_pclass = csv_data['Pclass']
df_age = csv_data['Age']

