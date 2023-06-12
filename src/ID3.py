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
    train = pd.read_csv("./train_3.csv")

    print(f'Shape: {train.shape}')
    print(f'Head:\n{train.head()}')

    x_train = train.drop('czy_zebrac',axis=1)
    y_train = train['czy_zebrac']

    d_tree = DecisionTreeClassifier()
    d_tree = d_tree.fit(x_train,y_train)

    pickle.dump(d_tree, open(os.path.join('.','tree.plk'),'wb'))                                                #1-4 1 śnieg, 2 deszcz, 3 wiatr, 4 slonce
    data = tree.export_graphviz(d_tree, out_file=None, feature_names=['Wzrost','wilgotnosc','dni_od_nawiezienia','aktualna_pogoda','czy_roslina_robaczywa','paliwo','pojemnosc_ekwipunku','cena_sprzedarzy'])
    graph = pydotplus.graph_from_dot_data(data)

    # Save the graph as a PNG image in the script's folder
    graph.write_png(os.path.join('.', 'mytree.png'))

    # Read the PNG image
    img = pltimg.imread(os.path.join('.', 'mytree.png'))
    imgplot = plt.imshow(img)
    plt.show()

    return d_tree

# dtree = learnTree()    #w, w, d, p,R,P,P,S
#                             #przy robaczywej == 1 daje ok czyli jak 1 to git jest mozna zbierac, ale planowalem inaczej
# decision=make_decision(70,85,12,4,0,65,54,1500,dtree)
# print(decision)

def action(this_contain, Plant, tractor, dtree):
    if isinstance(this_contain, Plant): 
        this_plant = this_contain
        params=Plant.getParameters(this_plant)
        # print(this_field)
        #ID3 decision
        decision=make_decision(params[0],params[1],params[2],params[3],params[4],tractor.fuel,tractor.capacity,params[5],dtree)
        # print('wzorst',params[0],'wilgotnosc',params[1],'dni_od_nawiezienia',params[2],'pogoda',params[3],'zdrowa',params[4],'paliwo',tractor.fuel,'pojemnosc eq',tractor.capacity,'cena sprzedazy',params[5])
        # print(decision)
        if decision == 1:
            print('Gotowe do zbioru')
            return 1
        else:
            print('nie zbieramy')
            return 0
    else:
        print('Road, no plant growing')
        return 0