#Import libraries
import numpy as np                                             # linear algebra
import pandas as pd                                            # data processing, CSV file Input/Output (e.g. pd.read_csv)
pd.set_option('display.max_columns', None)

import plotly.express as px #for visualization
import matplotlib.pyplot as plt #for visualization 

#Read the dataset
data_df = pd.read_csv(".\Data\BankChurners.csv")
