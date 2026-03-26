import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pyrolite.geochem.norm import get_reference_composition
from pyrolite.plot.spider import spider
import requests

st.title('How to build an App around your dataset')

if st.user.is_logged_in:
    st.sidebar.success("You are logged in with ORCID")
else:
    st.sidebar.error('You are not loged in to ORCID')

if st.sidebar.button("Log out"):
    st.logout()




st.markdown(
    """
### 🔗 Looking for inspiration?

You can find working example apps here:

- **[Visualising Geochemical Databases](https://hezel2000.github.io/mag4/allapps/allapps.html)** (via mag4 App Library)  
- Other tools for microprobe, TAS classification, database exploration, and more.

These examples show what you can build once your dataset is uploaded and structured.
"""
)
