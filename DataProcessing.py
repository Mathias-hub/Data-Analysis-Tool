from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

### DEFINE DATA ###
planets = sns.load_dataset('planets')


print(planets.describe())

sns.lineplot(x = 'year', y = 'number', data = planets)



plt.show()
