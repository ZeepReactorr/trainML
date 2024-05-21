import streamlit as st
import pandas as pd
import os

#change into the desired directory to store the results of the sorting
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

import generator

st.set_page_config(layout="wide")

st.markdown("Upload your csv here")

upfile = st.file_uploader("Upload", type="csv", key="1st upload")

if upfile is not None:
    df = pd.read_csv(upfile)
    # To convert to a string based IO:
    original = generator.randomizer(df)
    
    st.write(f"2 files to be downloaded")
    for file in ["exercise_frame_classifier.csv", "exercise_frame_regression.csv"]:
        downfile = st.download_button(f"Download {file}", open(file).read(), file)


