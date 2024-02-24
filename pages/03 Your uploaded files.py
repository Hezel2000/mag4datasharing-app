import streamlit as st

st.title('Your uploaded files')
st.write(st.session_state.orcid_user_info['id'].split('/')[-1])
if st.session_state.is_authenticated == True:
    df_metadata = pd.read_csv('https://raw.githubusercontent.com/Hezel2000/mag4datasets/main/overview_available_datasets.csv')
    st.dataframe(df_metadata[df_metadata['ORCID'] == st.session_state.orcid_user_info['id'].split('/')[-1]])
else:
    st.subheader('Authenticate with ORCID to see your uploaded datsets.')


if st.session_state.is_authenticated:
    st.sidebar.success("You are logged in with ORCID")
else:
    st.sidebar.error("ORCID login required for full functionality")
