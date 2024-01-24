import streamlit as st
import requests
import pandas as pd
#import json

# ------ Functions
def get_metadata(repo_owner, repo_name, folder, file_name):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{folder}/{file_name}.json'
    github_token = st.secrets['GitHub_Token']
    headers = {'Authorization': f'Bearer {github_token}'}
    response = requests.get(url, headers=headers)
    file_url = response.json()['download_url']
    file_content_response = requests.get(file_url, headers=headers)
    return file_content_response.json()

@st.cache_data
def get_csv_urls(repo_owner, repo_name, folder):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{folder}'
    github_token = st.secrets['GitHub_Token']
    headers = {'Authorization': f'Bearer {github_token}'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        files = [file for file in response.json() if file['name'].endswith('.csv')]
        
        # Fetch and store the contents of each JSON file
        file_urls = {}
        for file in files:
            file_urls[file['name'].split('.')[0]] = file['download_url']
        return file_urls
    else:
        return f"Error: Unable to fetch files. Status code: {response.status_code}"


# ------ Webpage
st.title('Browse Dataset Info & Content')


df_metadata = pd.read_csv('https://raw.githubusercontent.com/Hezel2000/mag4datasets/main/overview_available_datasets.csv')

file_urls = get_csv_urls("Hezel2000", "mag4datasets", "data")
sel_dataset = st.selectbox('sel', df_metadata['Title'].sort_values(), label_visibility='collapsed')

dataset_metadata = get_metadata("Hezel2000", "mag4datasets", "metadata", sel_dataset)
st.table(dataset_metadata)
st.dataframe(pd.read_csv(file_urls[sel_dataset]))


# ------ Siedbar
if st.session_state.is_authenticated:
    st.sidebar.success("You are logged in with ORCID")
else:
    st.sidebar.error("ORCID login required for full functionality")



# ------ Retired
# Get Metadata from all files in the metadata folder – no longer required, kept for maybe later
    
# @st.cache_data
# def get_json(repo_owner, repo_name, folder):
#     url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{folder}'
#     github_token = st.secrets['GitHub_Token']
#     headers = {'Authorization': f'Bearer {github_token}'}
    
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         files = [file for file in response.json() if file['name'].endswith('.json')]
        
#         # Fetch and store the contents of each JSON file
#         json_data = {}
#         for file in files:
#             file_url = file['download_url']
#             file_content_response = requests.get(file_url, headers=headers)
#             file_content = file_content_response.json()  # Corrected line
            
#             # Store file content in the dictionary with the filename as the key
#             json_data[file['name']] = file_content
        
#         return json_data
#     else:
#         return f"Error: Unable to fetch files. Status code: {response.status_code}"
# metadata_files = get_json("Hezel2000", "mag4datasets", "metadata")
# df_metadata = pd.DataFrame(metadata_files).T