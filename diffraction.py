import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="ici de Fresnel")
st.header("Test")
st.subheader("Retest")

x = np.linspace(0,10,100)

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

