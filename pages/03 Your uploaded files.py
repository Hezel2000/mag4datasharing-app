import streamlit as st

st.title('Your uploaded files')
if st.session_state.is_authenticated == True:
    st.write('A simply filtered table with your uploaded datasets, with a number of editing options: update, delete (restricted!)')
else:
    st.subheader('Authenticate with ORCID to see your uploaded datsets.')


if st.session_state.is_authenticated:
    st.sidebar.success("You are logged in with ORCID")
else:
    st.sidebar.error("ORCID login required for full functionality")
