listaCompras=["papa","tomate","carne","cebolla"]

filtrada=[]

for item in listaCompras:
    if item.startswith("c"):
        filtrada.append(item)


print(filtrada)

#List Comprehension

filtrada2=[item for item in listaCompras if item.startswith("c")]

print(filtrada2)

################
unos= [1 for i in range (10)]
print(unos)