import tkinter as tk
from tkinter import Checkbutton, filedialog, Label

# Définition de la fenêtre
window = tk.Tk()
window.title("Ma liste de course")
window.geometry("600x500")  # Ajustez la taille de la fenêtre selon vos préférences

# Exporter les sélections vers un fichier texte
def export_selections():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            for index, var in enumerate(product_vars):
                if var.get() == 1:  # Vérifier si le Checkbutton est coché
                    selection = products[index]
                    file.write(selection + "\n")

label_select_products = Label(text="Sélectionnez un produit :")
label_select_products.pack()

# Créer un bouton pour exporter les sélections
export_button = tk.Button(window, text="Exporter les sélections", command=export_selections)
export_button.pack(pady=10)

# Liste de tous les produits
products = ["Allumettes", "Ampoules électriques", "Après-shampooing", "Balais et brosses", "Bougies", "Café", "Cintres", "Conserve de légumes et de fruits", "Crèmes hydratantes" , "Céréales", "Déodorant", "Dentifrice", "Désinfectants", "Eau minérale", "Elastiques", "Film alimentaire", "Fruits et légumes frais", "Gel douche", "Huile de cuisine", "Jus de fruits", "Lessive", "Liquide vaisselle", "Lait", "Mouchoirs en papier", "Nutella", "Pain", "Papier aluminium", "Papier toilette", "Piles", "Pinces à linge", "Poisson ", "Poivre","Produits anti-moustiques", "Produits de rasage", "Produits multi-surfaces", "Riz", "Sacs de congélation", "Sac poubelle", "Sel", "Savon", "Serviettes hygiéniques", "Shampooing", "Serpillières", "Sucre", "Thé"]  # Votre liste de produits

# Nombre de colonnes désirées
num_columns = 3

col_frames = []
for _ in range(num_columns):
    col_frame = tk.Frame(window)
    col_frame.pack(side=tk.LEFT, padx=10)
    col_frames.append(col_frame)

product_vars = []  # Liste pour stocker les variables de Checkbuttons

for index, product in enumerate(products):
    col_index = index % num_columns
    var = tk.IntVar()  # Variable pour stocker l'état du Checkbutton
    product_vars.append(var)  # Ajouter la variable à la liste
    check_button = tk.Checkbutton(col_frames[col_index], text=product, anchor=tk.W, variable=var)
    check_button.pack(fill=tk.X)

# Fermer la fenêtre
def on_closing():
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)  # Enregistrer les sélections et fermer la fenêtre
window.mainloop()
