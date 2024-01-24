import streamlit as st
from requests.auth import HTTPBasicAuth
import requests

# Orcid Auth
CLIENT_ID = st.secrets["Orcid_ID"]
CLIENT_SECRET = st.secrets["Orcid_Secret"]
# REDIRECT_URI = "https://orcid-app-u9tbyykcsuwozua46jf3hk.streamlit.app/"
# REDIRECT_URI = "https://geo-cosmo-data-sharing-platform-bvniuih82j6l2aeq3jxfyb.streamlit.app/"
# REDIRECT_URI = "https://mag4-data-sharing.streamlit.app/ORCID_login"
REDIRECT_URI = "https://geo-cosmo-data-sharing-platform-bvniuih82j6l2aeq3jxfyb.streamlit.app/ORCID_login"
# ORCID_API_URL = "https://pub.orcid.org/v3.0/"


# Function to get Orcid token
def get_orcid_token(authorization_response):
    token_url = "https://orcid.org/oauth/token"
    token_data = {
        "grant_type": "authorization_code",
        "code": authorization_response,
        "redirect_uri": REDIRECT_URI,
    }
    auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    response = requests.post(token_url, data=token_data, auth=auth)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        return None


# Function to get Orcid user info
def get_orcid_user_info(orcid_token):
    if not orcid_token:
        return None

    user_info_url = "https://orcid.org/oauth/userinfo"
    headers = {
        "Authorization": f"Bearer {orcid_token}",
        "Accept": "application/json",
    }

    response = requests.get(user_info_url, headers=headers)

    if response.status_code == 200:
        user_info = response.json()
        return user_info
        return {
            "name": user_info.get("name", ""),
            "orcid": user_info.get("sub", ""),  # Using 'sub' as Orcid ID, you may need to adjust this based on the response format
        }
    else:
        return st.error('info response error')

# Streamlit app
st.title("ORCID Authentication")

st.write('Works as follows (for the moment:)')
st.write('Click on the button, click on the link – then authenticate.')
st.write('After the redirect to this page, click again on login – and you are all set.')
st.write('This will become more streamlined in the future.')

st.write(' ')
st.write('To logout – simply return to this page and you will be logged aout fro ORCID.')

# Check if the user is authenticated
st.session_state.is_authenticated = False #st.session_state.get("is_authenticated", False)

if not st.session_state.is_authenticated:
    # Orcid login button
    if st.button("Login with ORCID"):
        # Redirect user to Orcid for authorization
        authorization_url = f"https://orcid.org/oauth/authorize?client_id={CLIENT_ID}&response_type=code&scope=/authenticate&redirect_uri={REDIRECT_URI}"
        st.write(f"Click [here]({authorization_url}) to log in with Orcid.")

        # Check if the authorization code is present in the URL
        url = st.experimental_get_query_params() # should soon be: st.query_params()
        authorization_response = url.get("code", None)

        if authorization_response:
            # Get Orcid token
            orcid_token = get_orcid_token(authorization_response)

            if orcid_token:
                st.session_state.is_authenticated = True
                st.session_state.orcid_token = orcid_token
                st.success("Successfully logged in with ORCID")


# Display user info if authenticated
if st.session_state.is_authenticated:
    st.sidebar.success("You are logged in with ORCID")

    # Display Orcid user info automatically
    st.session_state.orcid_user_info = get_orcid_user_info(orcid_token)
    st.write('response.status_code', st.session_state.orcid_user_info)
    st.write('name', st.session_state.orcid_user_info['family_name'])
    if st.session_state.orcid_user_info:
        st.write("Orcid User Information:")
        st.write(f"Name: {st.session_state.orcid_user_info['given_name']} {st.session_state.orcid_user_info['family_name']}")
        # st.write(f"Name: {st.session_state.orcid_user_info['given_name']} {st.session_state.orcid_user_info['familiy_name']}")
        st.write(f"Orcid ID: {st.session_state.orcid_user_info['sub']}")

    # Your existing Streamlit content goes here
    st.title('Your uploaded files')
    st.write('A simply filtered table with your uploaded datasets, with a number of editing options: update, delete (restricted!)')
    st.write('orcid_user_info', st.session_state.orcid_user_info)
    
else:
    st.sidebar.error('You are not loged in to ORCID')