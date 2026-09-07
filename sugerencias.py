print("============================\n")
print("  sugerencias de peliculas  \n")
print("============================\n")
usuario=input("buen dia, cual es tu nombre? ")
print("que queres mirar hoy, "+usuario+"?")
nombre_pelicula="rapidos y furiosos"
genero_pelicula="accion"
anio_pelicula=2001
rating_pelicula=6.8
nombre_pelicula2="troya"
genero_de_pelicula2="accion"
anio_de_pelicula2=2004
rating_pelicula2=7.4
nombre_pelicula3="piratas del caribe"
genero_de_pelicula3="accion"
anio_de_pelicula3=2006
rating_pelicula3=7.4
nombre_pelicula4="¿Y dónde está el piloto?"   
genero_pelicula4="Comedia"  
anio_pelicula4=1980 
rating_pelicula4=7.7 
nombre_pelicula5="norbit"
genero_pelicula5="comedia"
anio_pelicula5=2007
rating_pelicula5=4.3
print("---- GÉNEROS-----")
print("Acción")
print("comedia")
genero_favorito=input("¿qué género te gusta? ")
print ("Buscando Péliculas del Género " +genero_favorito)
if (genero_pelicula==genero_favorito) :
    print(nombre_pelicula)
if (genero_de_pelicula2==genero_favorito):
  print(nombre_pelicula2)
  if (genero_de_pelicula3==genero_favorito):
    print(nombre_pelicula3)
    if (genero_pelicula4==genero_favorito):
       print(nombre_pelicula4)   
  if (genero_pelicula5==genero_favorito):
     print(nombre_pelicula5)