import streamlit as st
import requests

st.title("Application Streamlit pour votre application Flask")

# Fonction pour ajouter un utilisateur
def add_user():
    st.header("Ajouter un utilisateur")
    username = st.text_input("Nom d'utilisateur")
    if st.button("Ajouter"):
        response = requests.post("http://localhost:5000/add_user", json={"username": username})
        if response.status_code == 200:
            st.success("Utilisateur ajouté avec succès!")
        else:
            st.error("Erreur lors de l'ajout de l'utilisateur.")

# Fonction pour rechercher un utilisateur
def search_user():
    st.header("Rechercher un utilisateur")
    username = st.text_input("Nom d'utilisateur")
    if st.button("Rechercher"):
        response = requests.get(f"http://localhost:5000/get_user/{username}")
        if response.status_code == 200:
            st.success(f"Utilisateur trouvé : {response.json()['username']}")
        else:
            st.error("Utilisateur non trouvé.")

# Fonction pour afficher tous les utilisateurs
def show_all_users():
    st.header("Liste de tous les utilisateurs")
    response = requests.get("http://localhost:5000/get_all_users")
    if response.status_code == 200:
        users = response.json()
        for user in users:
            st.write(user['username'])
    else:
        st.error("Erreur lors de la récupération des utilisateurs.")

# Créez une barre de navigation
menu = st.sidebar.selectbox("Menu", ["Ajouter un utilisateur", "Rechercher un utilisateur", "Liste de tous les utilisateurs"])

# Gérez les actions en fonction de la sélection du menu
if menu == "Ajouter un utilisateur":
    add_user()
elif menu == "Rechercher un utilisateur":
    search_user()
elif menu == "Liste de tous les utilisateurs":
    show_all_users()
