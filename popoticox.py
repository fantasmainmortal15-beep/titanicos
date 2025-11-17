import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("database_titanic.csv")

st.write("""
Mi primera aplicación interactiva,
Gráficos usando la base de datos del Titanic,
""")


with st.sidebar:
    st.write("# Opciones")
    div = st.slider("Número de bins (histograma):", 0, 10, 2)
    st.write("Bins seleccionados:", div)
    st.image("https://www.google.com/imgres?q=Titanic&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Ff%2Ffd%2FRMS_Titanic_3.jpg%2F330px-RMS_Titanic_3.jpg&imgrefurl=https%3A%2F%2Fes.wikipedia.org%2Fwiki%2FRMS_Titanic&docid=Tas2HVI-tqSeLM&tbnid=tjZSR43-_96XUM&vet=12ahUKEwjpmZHA5vmQAxVkJrkGHd33FakQM3oECBwQAA..i&w=330&h=243&hcb=2&ved=2ahUKEwjpmZHA5vmQAxVkJrkGHd33FakQM3oECBwQAA")
    st.write("# masculino o femenino ")
    dev = st.selectbox ("masculino" , "femenino")

fig, ax = plt.subplots(1, 2, figsize=(10, 3))


ax[0].hist(df["Age"].dropna(), bins=div)
ax[0].set_xlabel("Edad")
ax[0].set_ylabel("Frecuencia")
ax[0].set_title("Histograma de edades")


df_male = df[df["Sex"] == "male"]
cant_male = len(df_male)
df_female = df[df["Sex"] == "female"]
cant_female = len(df_female)


ax[1].bar(["masculino","femenino"], [cant_male, cant_female], color = "red")
ax[1].set_xlabel("Sexo")
ax[1].set_ylabel("Cantidad")
ax[1].set_title("Distribucion de hombres y mujeres")

st.pyplot(fig)

st.write("## Número de sobrevivientes agrupados por sexo")

survivors_by_sex = df.groupby("Sex")["Survived"].sum()

fig2, ax[2] = plt.subplots(figsize=(5, 3))
ax[2].bar(["Femenino", "Masculino"], [survivors_by_sex["female"], survivors_by_sex["male"] ])
ax[2].set_xlabel("Sexo")
ax[2].set_ylabel("Sobrevivientes")
ax[2].set_title("Sobrevivientes por sexo")

st.pyplot(fig2)

