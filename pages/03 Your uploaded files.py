import streamlit as st
import pandas as pd

st.title('Your uploaded datasets')

if st.session_state.is_authenticated == True:
    df_metadata = pd.read_csv('https://raw.githubusercontent.com/Hezel2000/mag4datasets/main/overview_available_datasets.csv')
    st.dataframe(df_metadata[df_metadata['ORCID'] == st.session_state.orcid_user_info['id'].split('/')[-1]])

    checkbox_col1 = st.checkbox("Checkbox 1", key='checkbox1')
    checkbox_col2 = st.checkbox("Checkbox 2", key='checkbox2')

    # Concatenate the checkboxes with the DataFrame
    df_with_checkboxes = pd.concat([pd.Series([checkbox_col1] * len(df_metadata), name="update"),
                                    pd.Series([checkbox_col2] * len(df_metadata), name="delete"),
                                    df_metadata], axis=1)
    st.dataframe(df_with_checkboxes, index=False)

else:
    st.subheader('Authenticate with ORCID to see your uploaded datsets.')


if st.session_state.is_authenticated:
    st.sidebar.success("You are logged in with ORCID")
else:
    st.sidebar.error("ORCID login required for full functionality")
