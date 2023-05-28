import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import os
import pickle
import pydotplus
import matplotlib.image as pltimg
import matplotlib.pyplot as plt

def make_decision(Wzrost, wilgotnosc, dni_od_nawiezienia, aktualna_pogoda, czy_roslina_robaczywa, paliwo, pojemnosc_ekwipunku,cena_sprzedarzy, tree):
    decision = tree.predict([[Wzrost,wilgotnosc, dni_od_nawiezienia, aktualna_pogoda, czy_roslina_robaczywa, paliwo, pojemnosc_ekwipunku,cena_sprzedarzy]])
    return decision

def learnTree():
    # Read the CSV file
    train = pd.read_csv("src/train_3.csv", delimiter=";")

    # print(f'Shape: {train.shape}')
    # print(f'Head:\n{train.head()}')

    x_train = train.drop('czy_zebrac',axis=1)
    y_train = train['czy_zebrac']

    d_tree = DecisionTreeClassifier()
    d_tree = d_tree.fit(x_train,y_train)

    pickle.dump(d_tree, open(os.path.join('.','tree.plk'),'wb'))
    data = tree.export_graphviz(d_tree, out_file=None, feature_names=['Wzrost','wilgotnosc','dni_od_nawiezienia','aktualna_pogoda','czy_roslina_robaczywa','paliwo','pojemnosc_ekwipunku','cena_sprzedarzy'])
    graph = pydotplus.graph_from_dot_data(data)

    # Save the graph as a PNG image in the script's folder
    graph.write_png(os.path.join('.', 'mytree.png'))

    # Read the PNG image
    # img = pltimg.imread(os.path.join('.', 'mytree.png'))
    # Display the image
    # imgplot = plt.imshow(img)
    # plt.show()

    return d_tree

# dtree = learnTree()    #w, w, d, p,R,P,P,S
                            #przy robaczywej == 1 daje ok czyli jak 1 to git jest mozna zbierac, ale planowalem inaczej
# decision=make_decision(70,85,12,3,1,65,54,1000,dtree)
# print(decision)
