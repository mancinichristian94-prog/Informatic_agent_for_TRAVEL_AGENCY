# ==============================
# IMPORT
# ==============================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# PARTE 1 - VARIABILI E TIPI DI DATI
# ==============================
nome = "Mario Rossi"
eta = 34
saldo = 2500.75
vip = True

print("Nome:", nome,",Tipo di variabile: ", type(nome))
print("Età:", eta,",Tipo di variabile: ", type(eta))
print("Saldo:", saldo,",Tipo di variabile: ", type(saldo))
print("VIP:", vip,",Tipo di variabile: ", type(vip))

destinazioni = ["Parigi", "Roma", "Londra", "Tokyo", "Bangkok",
                "New York", "Rio de Janeiro", "Cairo"]

prezzi_medi = {
    "Parigi": 800,
    "Roma": 600,
    "Londra": 900,
    "Tokyo": 1800,
    "Bangkok": 1300,
    "New York": 1700,
    "Rio de Janeiro": 1500,
    "Cairo": 700
}

# ==============================
# PARTE 2 - OOP
# ==============================
class Cliente:
    def __init__(self, nome, eta, vip):
        self.nome = nome
        self.eta = eta
        self.vip = vip

    def stampa_info(self):
        print("Cliente:", self.nome, "| Età:", self.eta, "| VIP:", self.vip)


class Viaggio:
    def __init__(self, destinazione, prezzo, durata):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durata = durata


class Prenotazione:
    def __init__(self, cliente, viaggio):
        self.cliente = cliente
        self.viaggio = viaggio

    def importo_finale(self):
        if self.cliente.vip == True:
            return self.viaggio.prezzo * 0.90
        else:
            return self.viaggio.prezzo

    def dettagli(self):
        print("----- DETTAGLI PRENOTAZIONE -----")
        self.cliente.stampa_info()
        print("Destinazione:", self.viaggio.destinazione)
        print("Durata (giorni):", self.viaggio.durata)
        print("Prezzo base:", self.viaggio.prezzo)
        print("Importo finale:", self.importo_finale())


# Prova delle classi
c1 = Cliente("Mario Rossi", 34, True)
v1 = Viaggio("Tokyo", 1800, 10)
p1 = Prenotazione(c1, v1)
p1.dettagli()

# ==============================
# PARTE 3 - NUMPY
# ==============================
np.random.seed(42)  # rende i numeri casuali sempre uguali

prezzi = np.random.uniform(200, 2000, 100)

media = np.mean(prezzi)
minimo = np.min(prezzi)
massimo = np.max(prezzi)
dev_std = np.std(prezzi)
prezzi_sopra_media = np.sum(prezzi > media)
percentuale_sopra_media = prezzi_sopra_media / len(prezzi) * 100

print("\n--- NUMPY ---")
print("Prezzo medio:", round(media, 2))
print("Prezzo minimo:", round(minimo, 2))
print("Prezzo massimo:", round(massimo, 2))
print("Deviazione standard:", round(dev_std, 2))
print("Prenotazioni sopra la media:", percentuale_sopra_media, "%")

# ==============================
# PARTE 4 - PANDAS
# ==============================
nomi_clienti = ["Mario", "Luca", "Anna", "Giulia", "Paolo",
                "Sara", "Marco", "Elena", "Davide", "Chiara"]

giorni = pd.date_range("2026-11-01", periods=15)

lista_clienti = []
lista_destinazioni = []
lista_prezzi = []

for i in range(100):
    cliente = np.random.choice(nomi_clienti)
    dest = np.random.choice(destinazioni)
    prezzo = prezzi_medi[dest] + np.random.randint(-100, 101)
    lista_clienti.append(cliente)
    lista_destinazioni.append(dest)
    lista_prezzi.append(prezzo)

df = pd.DataFrame()
df["Cliente"] = lista_clienti
df["Destinazione"] = lista_destinazioni
df["Prezzo"] = lista_prezzi
df["Giorno_Partenza"] = np.random.choice(giorni, 100)
df["Durata"] = np.random.randint(3, 15, 100)
df["Incasso"] = df["Prezzo"]

print("\n--- TI MOSTRO LE PRIME 5 RIGHE DEL DATA FRAME!!! ---")
print(df.head())

incasso_totale = df["Incasso"].sum()
incasso_medio_dest = df.groupby("Destinazione")["Incasso"].mean()
top3 = df["Destinazione"].value_counts().head(3)

print("\nIncasso totale dell'agenzia:", incasso_totale)
print("\nIncasso medio per destinazione:")
print(incasso_medio_dest)
print("\nTop 3 destinazioni più vendute:")
print(top3)

# ==============================
# PARTE 5 - MATPLOTLIB
# ==============================
# Grafico a barre: incasso per destinazione
incasso_dest = df.groupby("Destinazione")["Incasso"].sum()
plt.figure(figsize=(10, 5))
plt.bar(incasso_dest.index, incasso_dest.values)
plt.title("Incasso per destinazione")
plt.xlabel("Destinazione")
plt.ylabel("Incasso (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Grafico a linee: incasso giornaliero
incasso_giorno = df.groupby("Giorno_Partenza")["Incasso"].sum()
plt.figure(figsize=(10, 5))
plt.plot(incasso_giorno.index, incasso_giorno.values, marker="o")
plt.title("Andamento giornaliero degli incassi")
plt.xlabel("Giorno di partenza")
plt.ylabel("Incasso (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Grafico a torta: vendite per destinazione
vendite_dest = df["Destinazione"].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(vendite_dest.values, labels=vendite_dest.index, autopct="%1.1f%%")
plt.title("Percentuale vendite per destinazione")
plt.show()

# ==============================
# PARTE 6 - ANALISI AVANZATA
# ==============================
categorie = {
    "Parigi": "Europa",
    "Roma": "Europa",
    "Londra": "Europa",
    "Tokyo": "Asia",
    "Bangkok": "Asia",
    "New York": "America",
    "Rio de Janeiro": "America",
    "Cairo": "Africa"
}

df["Categoria"] = df["Destinazione"].map(categorie)

incasso_categoria = df.groupby("Categoria")["Incasso"].sum()
durata_categoria = df.groupby("Categoria")["Durata"].mean()

print("\nIncasso totale per categoria:")
print(incasso_categoria)
print("\nDurata media per categoria:")
print(durata_categoria)

df.to_csv("prenotazioni_analizzate.csv", index=False)
print("\nFile prenotazioni_analizzate.csv salvato.")

# ==============================
# PARTE 7 - ESTENSIONI
# ==============================
def top_clienti(dataframe, n):
    conteggio = dataframe["Cliente"].value_counts()
    return conteggio.head(n)

print("\nTop 3 clienti con più prenotazioni:")
print(top_clienti(df, 3))

# Grafico combinato: barre (incasso medio) + linea (durata media)
incasso_medio_cat = df.groupby("Categoria")["Incasso"].mean()

fig, asse1 = plt.subplots(figsize=(8, 5))
asse1.bar(incasso_medio_cat.index, incasso_medio_cat.values)
asse1.set_xlabel("Categoria")
asse1.set_ylabel("Incasso medio (€)")

asse2 = asse1.twinx()
asse2.plot(durata_categoria.index, durata_categoria.values,
           color="red", marker="o")
asse2.set_ylabel("Durata media (giorni)")

plt.title("Incasso medio (barre) e durata media (linea) per categoria")
plt.tight_layout()
plt.show()