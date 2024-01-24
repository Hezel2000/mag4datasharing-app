import streamlit as st

st.title('How to prepare your dataset before upload')

st.write('Needs to be a csv file')

if st.session_state.is_authenticated == True:
    st.header('Test')
else:
    st.subheader('Login with ORCID to see content')