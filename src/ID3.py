import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Read the CSV file
data = pd.read_csv("train_2.csv", delimiter=";")

y = data[['czy_zebrac']].copy()
y.head()