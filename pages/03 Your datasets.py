import streamlit as st
import pandas as pd

st.title('Your Datasets')

if st.user.is_logged_in == True:
    df_metadata = pd.read_csv('https://raw.githubusercontent.com/Hezel2000/mag4datasets/main/overview_available_datasets.csv')
    df_metadata_personal = df_metadata[df_metadata['ORCID'] == st.user['sub'].split('/')[-1]]

    df_metadata_personal.insert(0, 'update', False)
    df_metadata_personal.insert(0, 'delete', False)
    editable_columns = ['update', 'delete']
    columns_not_to_be_edited = [item for item in df_metadata_personal.columns.tolist() if item not in editable_columns]
    df_ticked = st.data_editor(df_metadata_personal, disabled = columns_not_to_be_edited, hide_index=True)
    
    if len(df_ticked[df_ticked['delete']==True]) > 0:
        st.write('to be deleted:')
        st.dataframe(df_ticked[df_ticked['delete'] == True])
        if st.button('Delete'):
            st.write('deleted')
    
    if len(df_ticked[df_ticked['update']==True]) > 0:
        st.write('to be updated:')
        st.dataframe(df_ticked[df_ticked['update'] == True])
        st.file_uploader('Choose file(s)')
        if st.button('update'):
            st.write('updated')

else:
    st.subheader('Authenticate with ORCID to see your uploaded datsets.')


if st.user.is_logged_in:
    st.sidebar.success("You are logged in with ORCID")
else:
    st.sidebar.error('You are not loged in to ORCID')

if st.sidebar.button("Log out"):
    st.logout()

