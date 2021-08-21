import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import dataframe_image as dfi


def table(val, model = 0):
    
    pkl_filename = "Decision_Tree.pkl"

    if(model != 0):

        if(model == 1):
            pkl_filename = "Gaussian.pkl"
        if(model == 2):
            pkl_filename = "Decision_Tree.pkl"
        if(model == 3):
            pkl_filename = "Random_Forest.pkl"  
        if(model == 4):
            pkl_filename = "SVC.pkl"
        if(model == 5):
            pkl_filename = "Logistic_Regression.pkl"
        if(model == 6):
            pkl_filename = "Gradient_Boosted.pkl"      
                    


    

    with open(pkl_filename, 'rb') as file:
        clfg = pickle.load(file)

    X_test = np.load('new_data.npy',allow_pickle=True)
    newdf =  pd.read_pickle('newdf.pkl')

    newdf1 = newdf[['duration', 'protocol_type', 'flag', 'src_bytes', 'dst_bytes','land', 'wrong_fragment', 'urgent', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_file_creations', 'is_guest_login' ,'num_shells' , 'num_access_files']]
    
    newdf2 = newdf[[ 'srv_count', 'count', 'hot',
    'serror_rate',
    'rerror_rate',
    'same_srv_rate',
    'diff_srv_rate',
    'srv_diff_host_rate',
    'dst_host_count',
    'dst_host_srv_count',
    'dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate',
    'Attack Type']]

    p = newdf1[val:val + 1]
    dfi.export(p, 'static/df_styled1.png', max_cols=-1)

    q = newdf2[val:val + 1]
    dfi.export(q, 'static/df_styled2.png', max_cols=-1)



    display = X_test[val]

    
    y_test_pred = clfg.predict([display])

    return display, y_test_pred, model, pkl_filename