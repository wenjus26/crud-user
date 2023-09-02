import streamlit as st
import sqlite3
import pandas as pd

# Créer la table des utilisateurs si elle n'existe pas
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        email TEXT
    )
''')
conn.commit()
conn.close()

# Fonction pour ajouter un utilisateur
def add_user(first_name, last_name, email):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (first_name, last_name, email) VALUES (?, ?, ?)', (first_name, last_name, email))
    conn.commit()
    conn.close()

# Fonction pour mettre à jour un utilisateur
def update_user(user_id, first_name, last_name, email):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET first_name=?, last_name=?, email=? WHERE id=?', (first_name, last_name, email, user_id))
    conn.commit()
    conn.close()

# Fonction pour supprimer un utilisateur
def delete_user(user_id):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
    conn.commit()
    conn.close()

# Fonction pour récupérer tous les utilisateurs
def get_all_users():
    conn = sqlite3.connect('user_data.db')
    users = pd.read_sql_query('SELECT * FROM users', conn)
    conn.close()
    return users

# Interface utilisateur Streamlit
st.title('CRUD Utilisateurs')

# Formulaire pour ajouter un utilisateur
st.header('Ajouter un utilisateur')
first_name = st.text_input('Prénom')
last_name = st.text_input('Nom de famille')
email = st.text_input('Email')
if st.button('Ajouter'):
    add_user(first_name, last_name, email)
    st.success('Utilisateur ajouté avec succès.')

# Formulaire pour mettre à jour un utilisateur
st.header('Mettre à jour un utilisateur')
user_id_update = st.number_input('ID de l\'utilisateur à mettre à jour', min_value=1)
if user_id_update:
    user_to_update = get_all_users()[get_all_users()['id'] == user_id_update]
    if not user_to_update.empty:
        updated_first_name = st.text_input('Nouveau prénom', user_to_update.iloc[0]['first_name'])
        updated_last_name = st.text_input('Nouveau nom de famille', user_to_update.iloc[0]['last_name'])
        updated_email = st.text_input('Nouvel email', user_to_update.iloc[0]['email'])
        if st.button('Mettre à jour'):
            update_user(user_id_update, updated_first_name, updated_last_name, updated_email)
            st.success('Utilisateur mis à jour avec succès.')

# Formulaire pour supprimer un utilisateur
st.header('Supprimer un utilisateur')
user_id_delete = st.number_input('ID de l\'utilisateur à supprimer', min_value=1)
if user_id_delete:
    if st.button('Supprimer'):
        delete_user(user_id_delete)
        st.success('Utilisateur supprimé avec succès.')

# Afficher la liste des utilisateurs
st.header('Liste des utilisateurs')
user_df = get_all_users()
st.dataframe(user_df)

# Bouton pour générer un fichier Excel
if st.button('Générer Excel'):
    user_df.to_excel('utilisateurs.xlsx', index=False)
    st.success('Fichier Excel généré avec succès. [Cliquez ici pour télécharger](utilisateurs.xlsx)')
