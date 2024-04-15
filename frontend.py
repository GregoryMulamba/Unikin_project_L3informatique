import streamlit as st
from keras.models import load_model
import numpy as np
from PIL import Image
import cv2
from keras.preprocessing.image import img_to_array


#loading function


def load():
    model_path="C:/Users/cellphone/Virtual/POUBELLE/best_model.h5"
    model=load_model(model_path, compile=False)
    return model

#loading model
model=load()

#predict function
def predict(upload):
    img= Image.open(upload)
    img=np.asarray(img)
    img_resize=cv2.resize(img, (224, 224))
    img_resize=np.expand_dims(img_resize, axis=0)
    pred=model.predict(img_resize)

    rec=pred[0][0]

    return rec


st.title("Poubelle Intelligente")

upload=st.file_uploader("Chargez l' image de votre objet" , type=["png", "jpeg", "jpg", ])
c1, c2= st.columns(2)

if upload:
    rec=predict(upload)
    prob_rec=rec * 100
    prob_org=(1- rec)* 100
    
    c1.image(Image.open(upload))
    if prob_rec > 50:
        c2.write(f"Je suis certain à {prob_rec:.2f} % que l' objet est recyclable")

    else:
         c2.write(f"Je suis certain à {prob_org:.2f} % que l' objet n'est pas recyclable")

    
