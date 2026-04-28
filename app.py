import streamlit as st
import pandas as pd
import os

st.title("📋 Gestion des inscriptions")

FILE = "data.csv"

# Charger ou créer fichier
if os.path.exists(FILE):
    df = pd.read_csv(FILE)
else:
    df = pd.DataFrame(columns=["Nom", "Age", "Filiere"])

# Formulaire
st.subheader("➕ Ajouter un étudiant")

nom = st.text_input("Nom")
age = st.number_input("Age", min_value=10, max_value=100)
filiere = st.selectbox("Filière", ["Informatique", "Réseaux", "Gestion", "Autre"])

if st.button("Enregistrer"):
    new_data = pd.DataFrame([[nom, age, filiere]], columns=df.columns)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(FILE, index=False)
    st.success("✅ Enregistré avec succès")

# Affichage
st.subheader("📄 Liste des étudiants")
st.dataframe(df)

# Analyse
if not df.empty:
    st.subheader("📊 Analyse des données")

    # Moyenne d'âge
    st.write("🎯 Age moyen :", round(df["Age"].mean(), 2))

    # Nombre par filière
    st.write("📚 Nombre d'étudiants par filière")
    filiere_count = df["Filiere"].value_counts()
    st.bar_chart(filiere_count)

    # Statistiques générales
    st.write("📈 Statistiques générales")
    st.write(df.describe())
