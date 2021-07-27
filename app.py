import streamlit as st
from helper import *
import tensorflow.keras
import tensorflow as tf
from PIL import Image, ImageOps

config = tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.4
session = tf.compat.v1.Session(config=config)

st.title("Neural Networks for mineral prediction in XPL thin sections")

co1, co2, co3 = st.beta_columns([1, 1, 1])

co2.write(" Works with: ")

st.write("Olivine | Plagioclase | Pyroxene | Alkali Feldspar | Biotite | Muscovite | Hornblende | Quartz")


file = st.file_uploader("", type=["jpg"])

if file is None:
    st.text("Please. upload an image in .jpg format ...")

np.set_printoptions(suppress=True)
mineral_pred = tensorflow.keras.models.load_model('mineral.h5', compile=False)

if file:

    img = import_image(file)

    col1, col2, col3 = st.beta_columns([1, 1, 1])
    col1.write(f"Image uploaded {file.name}")
    col2.image(img, use_column_width=True)
    if col2.button("Classify mineral", key='clasificar'):

        img_pred = Image.open(file)

        prediction_min = predict_pl(img_pred, mineral_pred)
        choice = np.argmax(prediction_min)

        prediction_idx = {
            0: "Alkali feldspar",
            1: "Biotite",
            2: "Hornblende",
            3: "Muscovite",
            4: "Olivine",
            5: "Plagioclase",
            6: "Pyroxene",
            7: "Quartz"
        }

        col3.write(
            "The model predicts the mineral as: ")
        col3.title(prediction_idx[choice])


st.write("Programado por Iván Ferreira, unalgeo-Bogotá (2021)")
