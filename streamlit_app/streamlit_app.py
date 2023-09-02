import streamlit as st
import requests

st.title('User Management App')

@st.cache
def fetch_users():
    response = requests.get('http://localhost:5000/')
    users = response.json()
    return users

def main():
    st.subheader('List of Users')
    users = fetch_users()
    for user in users:
        st.write(user['username'])

if __name__ == '__main__':
    main()
s