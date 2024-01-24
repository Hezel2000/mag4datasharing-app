import streamlit as st
import requests
import os
import json
import pandas as pd

st.title('Browse Datasets')

@st.cache_data
def get_json(repo_owner, repo_name, folder):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{folder}'
    github_token = st.secrets['GitHub_Token']
    headers = {'Authorization': f'Bearer {github_token}'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        files = [file for file in response.json() if file['name'].endswith('.json')]
        
        # Fetch and store the contents of each JSON file
        json_data = {}
        for file in files:
            file_url = file['download_url']
            file_content_response = requests.get(file_url, headers=headers)
            file_content = file_content_response.json()  # Corrected line
            
            # Store file content in the dictionary with the filename as the key
            json_data[file['name']] = file_content
        
        return json_data
    else:
        return f"Error: Unable to fetch files. Status code: {response.status_code}"
    
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


metadata_files = get_json("Hezel2000", "mag4datasets", "metadata")
file_urls = get_csv_urls("Hezel2000", "mag4datasets", "data")
df_metadata = pd.DataFrame(metadata_files).T

sel_dataset = st.selectbox('sel', df_metadata['Title'].sort_values(), label_visibility='collapsed')

st.dataframe(pd.read_csv(file_urls[sel_dataset]))
st.table(metadata_files[sel_dataset+'.json'])


# ------ Siedbar

if st.session_state.is_authenticated:
    st.sidebar.success("You are logged in with ORCID")
else:
    st.sidebar.error("ORCID login required for full functionality")




# Use the following, if the data are in a different repo

# import requests

# def get_github_folder_contents(username, repository, path, branch='main'):
#     api_url = f'https://api.github.com/repos/{username}/{repository}/contents/{path}?ref={branch}'
#     github_token = st.secrets['GitHub_Token']
#     headers = {"Authorization": f"Bearer {github_token}"}
#     response = requests.get(api_url, headers=headers)
    
#     if response.status_code == 200:
#         contents = response.json()
#         return contents
#     else:
#         return st.write(f"Failed to retrieve contents. Status code: {response.status_code}")

# # Replace these with your GitHub username, repository name, and folder path
# username = 'Hezel2000'
# repository = 'GeoCosmoChemDataAndTools'
# folder_path = 'csv'

# contents = get_github_folder_contents(username, repository, folder_path)

# if contents:
#     dataset_name_list = []
#     dataset_download_urls = []
#     for item in contents:
#         if item['name'].endswith('.csv'):
#             dataset_name_list.append(item['name'].split('.')[0])
#             dataset_download_urls.append(item['download_url'])

# sel_dataset = st.selectbox('Select Dataset', dataset_name_list)

# st.dataframe(pd.read_csv(dataset_download_urls[dataset_name_list.index(sel_dataset)]))