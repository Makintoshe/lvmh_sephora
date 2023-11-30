from controller.BrandsC import Brands

liste_brands = Brands().visualiserBrands()

print(liste_brands)

listeB = []

print("##################################")

for b in liste_brands:

    idb = b.getBrandId()

    nom = b.getBrandName()

    listeB.append((idb,nom))

    print(idb, nom)

print("**********************************")

print(listeB)
#%%
