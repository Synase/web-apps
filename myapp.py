import streamlit as st
import plotly.express as px

st.set_page_config(page_title="ici de Fresnel")
st.header("Test")
st.subheader("Retest")

import numpy as np
x = np.linspace(0,10,100)
import matplotlib.pyplot as plt
test = px.scatter(x, np.sin(x))

fig,ax = plt.subplots(1,2)
ax[0].plot(x,np.sin(x))

st.pyplot(fig)
calcul = st.button("Calcul")
if calcul:
    ax[0].plot(x, np.cos(x))
    st.pyplot(fig, clear_figure= True)

radio = st.radio("Boutton de couleur",('Monochromatique', 'Poly','Custom'))
if radio == 'Monochromatique':
    ax[0].plot(x, np.cos(x))
    st.pyplot(fig, clear_figure= True)
elif radio == 'Poly':
    ax[0].plot(x, np.cos(x)+5)
    st.pyplot(fig, clear_figure= True)

with open("flower.jpeg", "rb") as file:
     btn = st.download_button(
             label="Download image",
             data=file,
             file_name="flower.png",
             mime="image/png"
           )