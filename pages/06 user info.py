import streamlit as st
import requests

ORCID_API_URL = "https://pub.orcid.org/v3.0/"

# Function to get Orcid user info
def get_orcid_user_info(orcid_token):
    if not orcid_token:
        return 'no token'

    headers = {"Authorization": f"Bearer {orcid_token}"}
    response = requests.get(ORCID_API_URL + "me", headers=headers)
    return response

    if response.status_code == 200:
        user_info = response.json()
        return {
            "name": user_info.get("name", {}).get("given-names", {}).get("value", ""),
            "orcid": user_info.get("orcid-identifier", {}).get("path", ""),
        }
    else:
        return response.status_code

# Display user info if authenticated
if st.session_state.is_authenticated:
    st.sidebar.info("You are logged in with Orcid.")

    # Display Orcid user info automatically
    orcid_user_info = get_orcid_user_info(st.session_state.orcid_token)
    st.write('response.status_code', orcid_user_info)
    if orcid_user_info:
        st.write("Orcid User Information:")
        # st.write(f"Name: {orcid_user_info['name']}")
        # st.write(f"Orcid ID: {orcid_user_info['orcid']}")

    # Your existing Streamlit content goes here
    st.title('Your uploaded files')
    st.write('A simply filtered table with your uploaded datasets, with a number of editing options: update, delete (restricted!)')
