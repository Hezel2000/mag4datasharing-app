import streamlit as st
from requests.auth import HTTPBasicAuth
import requests

# ------ Webpage
# st.session_state.is_authenticated = False

st.title('mag4 Uploader & Viewer 👋')


st.markdown(
    """
**mag4 Uploader & Viewer** is an open-source platform for sharing and exploring
geological datasets.

Your uploads are stored securely in our public GitHub repository, and you can
view, update, and manage them directly in this interface.

### 🔐 Log in with ORCID
- Click the button below to authenticate using **ORCID**.
- After logging in, you can upload new datasets or manage existing ones.
- Please remember to log out when you are finished.
- Have suggestions or ideas to improve the platform?  
  We’d love to hear from you. Please contact **Dominik Hezel** or **Jie Xu**!
"""
)



if not st.user or not st.user.is_logged_in:
    st.header("Log in:")
    if st.button("Log in with ORCID"):
        st.login("orcid")
    # if st.button("Log in with GOOGLE"):
    #     st.login("google")
    st.stop()
else:
    if st.button("Log out"):
        st.logout()

# st.write(f"Hello, {st.user.name}!")

user_info = st.user.to_dict()

display_name = (
    user_info.get("name") or 
    (f"{user_info.get('given_name', '')} {user_info.get('family_name', '')}").strip() or 
    user_info.get("sub")
)

# 3. Render the UI safely
st.markdown(
    f"<p style='font-size: 1.8rem; font-weight: 600;'>🌋 Hello, {display_name}!</p>",
    unsafe_allow_html=True
)


# st.markdown(
#     f"<p style='font-size: 1.8rem; font-weight: 600;'>🌋 Hello, {st.user}!</p>",
#     unsafe_allow_html=True
# )



# st.write("Query params:", st.experimental_get_query_params())
# st.write("User:", getattr(st.user, "is_logged_in", None))
# st.write("Secrets auth section:", st.secrets.get("auth"))

# st.json(st.user)

# st.write("session station:", st.session_state)


# ------ Sidebar
if st.user.is_logged_in:
    st.sidebar.success("You are logged in with ORCID")
else:
    st.sidebar.error('You are not loged in to ORCID')

if st.sidebar.button("Log out"):
    st.logout()



# ------ Siedbar
# if st.session_state.is_authenticated:
#     st.sidebar.success("You are logged in with ORCID")
# else:
#     st.sidebar.error("ORCID login required for full functionality")
