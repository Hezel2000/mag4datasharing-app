import streamlit as st

# ------ Webpage
st.session_state.is_authenticated = False

st.title('mag4 Uploader & Viewer')


# ------ Siedbar
if st.session_state.is_authenticated:
    st.sidebar.success("You are logged in with ORCID")
else:
    st.sidebar.error("ORCID login required for full functionality")