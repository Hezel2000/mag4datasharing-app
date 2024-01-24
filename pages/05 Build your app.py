import streamlit as st

st.title('How to build an App around your dataset')

if st.session_state.is_authenticated == True:
    st.header('Test')
else:
    st.subheader('Login with ORCID to see content')