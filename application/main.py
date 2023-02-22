import streamlit as st
import numpy as np
import torch
import torchvision as tv
from PIL import Image
import torchvision.transforms as transforms

# to run the app, into anaconda Pronps: 
# -conda activate pytorchEnv
# -streamlit run main.py

# plante le décors de la page 
st.set_page_config(
    page_title="MedNet Predictions",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None,
)

# décris les fonctions de notre application :
st.markdown('<h1 style="color:dark;">Reconnaissance de radios médicales</h3>', unsafe_allow_html=True)
st.markdown('<h2 style="color:gray;">Bienvenue sur la plateforme d assistance pour vous aider à trier les radios. Chargez votre image et notre algorithme vous dira à quoi elle correspond.</h3>', unsafe_allow_html=True)
st.markdown('<h3 style="color:gray;">Notre modèle peut reconnaître les radios suivantes :</h2>', unsafe_allow_html=True)
st.markdown('<h3 style="color:gray;">AbdomenCT, BreastMRI, ChestCT, CXR, Hand and HeadCT</h3>', unsafe_allow_html=True)


def scaleImage(x):
    y = toTensor(x)
    if(y.min() < y.max()):
        y = (y - y.min())/(y.max() - y.min()) 
    z = y - y.mean()
    return z


# charger le modèle entraîné
model = torch.load('saved_model.pt')

# mettre le modèle en mode d'évaluation
model.eval()

# préparer les données d'entrée
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = image.resize((64, 64))
    toTensor = transforms.ToTensor()

    # Convert to grayscale
    grayscale_image = image.convert("L")

    inputs = scaleImage(grayscale_image)
    inputs = inputs.unsqueeze(0)  # add a batch dimension

    # faire une prédiction
    outputs = model(inputs)

    # obtenir la catégorie prédite
    _, predicted = torch.max(outputs, 1)
    categories = ['AbdomenCT', 'BreastMRI', 'ChestCT', 'CXR', 'Hand', 'HeadCT']
    category = categories[predicted]

    # afficher les prédictions
    st.write('Prediction:', category)




