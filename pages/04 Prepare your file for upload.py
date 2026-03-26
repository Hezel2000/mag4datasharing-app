import streamlit as st

st.title('How to prepare your dataset for upload 📁')

st.markdown(
    """
- Your file must be provided as a **CSV**.

- For best results, we encourage you to prepare your dataset following the
guidelines from **[EarthChem](https://earthchem.org/)**.

- Using the official **[EarthChem templates](https://earthchem.org/ecl/templates)** helps keep your data organized and makes it much easier to publish your dataset and obtain a DOI later.

- Simply download the template that matches your data type, fill it in, and upload it here.
"""
)




if st.user.is_logged_in:
    st.sidebar.success("You are logged in with ORCID")
else:
    st.sidebar.error('You are not loged in to ORCID')
if st.sidebar.button("Log out"):
    st.logout()

