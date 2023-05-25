import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle
import os
from sklearn import tree
import pydotplus
import matplotlib.image as pltimg
import matplotlib.pyplot as plt

# Read the CSV file
train = pd.read_csv("train_2.csv", delimiter=";")

x_train = train.drop('czy_zebrac',axis=1)
y_train = train['czy_zebrac']

d_tree = DecisionTreeClassifier()
d_tree = d_tree.fit(x_train,y_train)

# Save the decision tree model as a pickle file in the script's folder
pickle.dump(d_tree, open('tree.plk', 'wb'))

# Export the decision tree as DOT data
data = tree.export_graphviz(d_tree, out_file=None)

# Create a graph from the DOT data
graph = pydotplus.graph_from_dot_data(data)

# Save the graph as a PNG image in the script's folder
graph.write_png(os.path.join('.', 'mytree.png'))

# Read the PNG image
img = pltimg.imread(os.path.join('.', 'mytree.png'))

# Display the image
imgplot = plt.imshow(img)
plt.show()