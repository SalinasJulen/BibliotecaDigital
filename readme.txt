A tener en cuenta:

- Hemos modificado partes del enunciado ya que hemos visto varias contradicciones en el enunciado y hemos decidido
modificar parte del mismo en base a nuestro punto de vista.
Este enunciado se encuentra en esta carpeta EN EL ARCHIVO PDF AL COMPLETO

- Los campos de fecha los hemos puesto de tipo String ya que nos daba error insertar registros tipo Date o tipo DateTime
- El campo ISBN no lo hemos puesto como Integer ya que excedía los limites de este tipo de dato y lo hemos puesto como String


Para que el programa funcione:

- Una vez ejecutado por primera vez, tenemos que salir del CRUD (o parando el programa o con el dato centinela) y 
poner como comentario (mediante #) todos los sesion.add() y el sesion.commit() (comentar el sesion commit no es obligatorio) que está debajo de los mismos 
(ya que sino se van a añadir registros cada vez que ejecutemos el programa y entremos al CURD) 

- Si el pc está apagado (el de clase) no va a funcionar ya que la base de datos está en localhost 
(recomendable cambiar las credenciales para que no haya ningún problema y se ejecute en cualquier pc 
(hacer una bbdd de prueba en el pc del corrector))