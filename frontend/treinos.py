import streamlit as st
from utils.auth import logout
from utils.trainings_utils import treinos_academia

st.title("Treinos da Academia")

st.divider()

treinos_academia()
