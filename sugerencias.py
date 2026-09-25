print("============================\n")
print("  sugerencias de peliculas  \n")
print("============================\n")
usuario=input("buen dia, cual es tu nombre? ")
print("que queres mirar hoy, "+usuario+"?")
peliculas=[["rapidos y furiosos","accion",2001,6.8],["troya","accion",2004,7.4],["piratas del caribe","accion",2006,7.4],["¿Y dónde està el piloto?","comedia",2007,7.7],["smile","terror",2022,6.5],["norbit","comedia",2007,4.3],["jhon wick","accion",2014,7.5],["coco","animacion",2017,8.4],["up","animacion",2009,8.1],["el exorcista","terror",1973,8.1]]
print("---- GÉNEROS-----")
print("Acción")
print("comedia")
print("animacion")
print("terror")
genero_favorito=input("¿qué género te gusta? ")
print ("Buscando Péliculas del Género " +genero_favorito)
rating_favorito=float(input("¿cual es el rating minimo? "))
encontrar_pelicula=False
for pelicula in peliculas:
     nombre=pelicula[0]
     genero=pelicula[1]
     rating=pelicula[3]
     if (genero_favorito.lower()==genero.lower()) and (rating_favorito<rating):
         print(nombre)
         encontrar_pelicula=True
if (not encontrar_pelicula):
	print("No se ha encontrado ninguna pelìcula.") 