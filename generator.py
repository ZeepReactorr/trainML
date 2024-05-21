import pandas as pd
import random as rd
import numpy as np
import os

def randomizer(df):
    ori_df = df

    for col in df.columns:
        if rd.randrange(0, 10) >= 8:
            df[col] = [str(elt) for elt in df[col]]
        
        if rd.randrange(0, 10) > 7 :
            if df[col].dtype == object:
                df[col] = ['?' if rd.randrange(0, 100)>90 else str(elt) for elt in df[col]]

        if rd.randrange(0, 10) > 7 :
            if df[col].dtype != object:
                df[col] = [np.nan if rd.randrange(0, 100)>90 else elt for elt in df[col]]

        if rd.randrange(0, 10) > 6:
            if df[col].dtype == object:
                df[col] = [f"{col} : {elt}" for elt in df[col]]

    df.to_csv("exercise_frame_classifier.csv")
    df = df.drop(df.columns[-1], axis=1)
    df.to_csv("exercise_frame_regression.csv")
    return ori_df
