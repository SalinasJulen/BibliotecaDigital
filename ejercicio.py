from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
# Crear un engine para comunicarse con la base de datos
#engine = create_engine('sqlite:///productos.sqlite')
#engine = create_engine('postgresql://<usuario>:<contraseña>@<host>/<base_de_datos>')
#"dbname='mydb' user='miusuario' host='localhost'"

# engine = create_engine('postgresql://alejandro:fuq73gtnu931we0sJJn¡240h@localhost/TareaSQLAlchemyJulenAlejandro')




user = 'usuario_ejercicio'
password = '238jnfa0^afsd*^fweg ERQWGSLXc'
host = 'localhost'
port = '5433'
database = 'ejercicio_bilioteca_digital'


# for creating connection string
connection_str = f'postgresql://{user}:{password}@{host}:{port}/{database}' # El modelo de la conexión lo hemos sacado de: https://www.tutorialspoint.com/connecting-postgresql-with-sqlalchemy-in-python
# SQLAlchemy engine
engine = create_engine(connection_str)
# you can test if the connection is made or not
try:
    with engine.connect() as connection_str:
        print('Successfully connected to the PostgreSQL database')
        Base = declarative_base()
        # Definir una tabla
        from sqlalchemy import Column, Integer, String, ForeignKey
        from sqlalchemy.orm import relationship
        # Column es una clase que se utiliza para definir columnas en una tabla de base de datos.
        # Integer se necesita para especificar que una columna en una tabla contendrá valores enteros.
        # String se necesita para especificar que una columna en una tabla contendrá valores de texto.
        class Libro(Base):
            __tablename__ = 'Libro'
            id = Column(Integer, primary_key=True)
            titulo = Column(String)
            fecha_publicacion = Column(String)
            isbn = Column(String)
            autor_id = Column(Integer, ForeignKey('Autor.id'))
            relacion_autor = relationship("Autor",back_populates="relacion_libro")
            relacion_prestamos = relationship("Prestamo", back_populates="libro")


        class Autor(Base):
            __tablename__ = 'Autor'
            id = Column(Integer, primary_key=True)
            nombre = Column(String)
            biografia = Column(String)
            relacion_libro = relationship("Libro",back_populates="relacion_autor")


        class Usuario(Base):
            __tablename__ = 'Usuario'
            id = Column(Integer, primary_key=True)
            nombre = Column(String)
            correo_electronico = Column(String)
            relacion_prestamos = relationship("Prestamo", back_populates="usuario")

        class Prestamo(Base):
            __tablename__ = 'Prestamo'
            id = Column(Integer, primary_key=True)
            libro_id = Column(Integer, ForeignKey('Libro.id'))
            usuario_id = Column(Integer, ForeignKey('Usuario.id'))
            fecha_prestamo = Column(String)
            fecha_limite_devolucion = Column(String)
            libro = relationship("Libro", back_populates="relacion_prestamos")
            usuario = relationship("Usuario", back_populates="relacion_prestamos")

        # Para comunicarse con la BD, hay que iniciar el servidor postgresql
        # pg_ctl start -D E:\Users\Alex\anaconda3\envs\cursoDWES\data
        # Crear la tabla en la base de datos
        Base.metadata.create_all(engine)
except Exception as ex:
    print(f'Sorry failed to connect: {ex}')


# No hemos seguido la teoría para crear la relación Many to Many, ya que antes de ver ese apartado ahí, visitamos la documentación oficial, es aquí donde usa 2 foreing keys, aunque al resto de lo que pone aquí no le hemos hecho caso: https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html




# Insertar datos en la tabla 
# Hay que crear una sesión y especificar el motor de la base de datos asociado a la sesión.
# El motor de la base de datos se encarga de establecer y administrar la conexión con la base de datos
Sesion = sessionmaker(bind=engine) # para especificar el motor de la base de datos asociado a esta sesión.



# Hemos puesto un ejemplo de cada sesion por cada tabla para ver como se hace, el resto de los datos los hemos introducido por la interfaz.
sesion = Sesion() # instanciamos para iniciar la sesión de trabajo
registro_autor1 = Autor(nombre = "Luis",biografia="Biografía de Luis")
registro_autor2 = Autor(nombre = "Godofredo",biografia="Biografía de Godofredo")
registro_autor3 = Autor(nombre = "Maria",biografia="Biografía de María")


registro_usuario1 = Usuario(nombre="Aitor",correo_electronico = "aitor@gmail.com")
registro_usuario2 = Usuario(nombre="Paca",correo_electronico = "paca@gmail.com")
registro_usuario3 = Usuario(nombre="Alberto",correo_electronico = "alberto@gmail.com")

registro_libro1 = Libro(titulo="El conde",fecha_publicacion = "2023-04-04",isbn = "2737730091876", autor_id = 1)
registro_libro2 = Libro(titulo="Falacias",fecha_publicacion = "2024-05-03",isbn = "9916300188725", autor_id = 1)
registro_libro3 = Libro(titulo="La huelga",fecha_publicacion = "2021-02-11",isbn = "3881733671892", autor_id = 2)
registro_libro4 = Libro(titulo="La pildora",fecha_publicacion = "2023-03-10",isbn = "2773738916378", autor_id = 2)
registro_libro5 = Libro(titulo="La BakQ",fecha_publicacion = "2023-09-09",isbn = "3477103901837", autor_id = 3)
registro_libro6 = Libro(titulo="Terror del Renfe",fecha_publicacion = "2024-06-07",isbn = "8273443091874", autor_id = 3)


registro_prestamo1 = Prestamo(libro_id = 1,usuario_id = 2, fecha_prestamo = "2024-02-02", fecha_limite_devolucion = "2024-03-02")
registro_prestamo2 = Prestamo(libro_id = 1,usuario_id = 3, fecha_prestamo = "2024-04-12", fecha_limite_devolucion = "2024-05-12")
registro_prestamo3 = Prestamo(libro_id = 2,usuario_id = 1, fecha_prestamo = "2024-07-01", fecha_limite_devolucion = "2024-08-01")
registro_prestamo4 = Prestamo(libro_id = 2,usuario_id = 2, fecha_prestamo = "2024-09-03", fecha_limite_devolucion = "2024-10-03")
registro_prestamo5 = Prestamo(libro_id = 3,usuario_id = 1, fecha_prestamo = "2024-10-14", fecha_limite_devolucion = "2024-11-14")
registro_prestamo6 = Prestamo(libro_id = 3,usuario_id = 3, fecha_prestamo = "2022-02-03", fecha_limite_devolucion = "2022-03-03")
registro_prestamo7 = Prestamo(libro_id = 4,usuario_id = 2, fecha_prestamo = "2023-11-11", fecha_limite_devolucion = "2023-12-11")
registro_prestamo8 = Prestamo(libro_id = 4,usuario_id = 3, fecha_prestamo = "2024-03-12", fecha_limite_devolucion = "2024-04-12")
registro_prestamo9 = Prestamo(libro_id = 5,usuario_id = 1, fecha_prestamo = "2024-05-02", fecha_limite_devolucion = "2024-06-02")
registro_prestamo10 = Prestamo(libro_id = 5,usuario_id = 3, fecha_prestamo = "2024-08-23", fecha_limite_devolucion = "2024-09-23")
registro_prestamo11 = Prestamo(libro_id = 6,usuario_id = 1, fecha_prestamo = "2024-08-17", fecha_limite_devolucion = "2024-09-17")
registro_prestamo12 = Prestamo(libro_id = 6,usuario_id = 2, fecha_prestamo = "2024-09-30", fecha_limite_devolucion = "2024-10-30")


sesion.add(registro_autor1)
sesion.add(registro_autor2)
sesion.add(registro_autor3)

sesion.add(registro_usuario1)
sesion.add(registro_usuario2)
sesion.add(registro_usuario3)


sesion.add(registro_libro1)
sesion.add(registro_libro2)
sesion.add(registro_libro3)
sesion.add(registro_libro4)
sesion.add(registro_libro5)
sesion.add(registro_libro6)



sesion.add(registro_prestamo1)
sesion.add(registro_prestamo2)
sesion.add(registro_prestamo3)
sesion.add(registro_prestamo4)
sesion.add(registro_prestamo5)
sesion.add(registro_prestamo6)
sesion.add(registro_prestamo7)
sesion.add(registro_prestamo8)
sesion.add(registro_prestamo9)
sesion.add(registro_prestamo10)
sesion.add(registro_prestamo11)
sesion.add(registro_prestamo12)


sesion.commit()


prestamos = sesion.query(Prestamo).all()
libros = sesion.query(Libro).all()


accion = input("Introduzca la acción que quiere ejecutar (obtener_fecha, mostrar_libros_prestados,      \
                   actualizar_biografia o eliminar_prestamo), * para terminar: ") 

# Creamos los comandos posibles en una tupla
comandos = ("obtener_fecha, mostrar_libros_prestados, actualizar_biografia, eliminar_prestamo")


       
if accion == '*': # Dato centinela
    print("Saliendo del CRUD")
elif accion in comandos:
    if accion == 'obtener_fecha': # En este caso mostramos la condición para el primer usuario:
         for prestamo in prestamos:
            if(prestamo.usuario_id == 1):
                print(f"ID: {prestamo.id}, Fecha de Préstamo: {prestamo.fecha_prestamo}, ID del libro prestado: {prestamo.libro_id}")


    elif accion == 'mostrar_libros_prestados': # Mostrar los libros disponibles (en este caso como todos los libros han sido prestados no saldrá nada, pero si cambiamos la condición se puede ver que funciona, por ejemplo: if(prestamo.fecha_prestamo == '2024-10-14')  )

        for prestamo in prestamos:
            if(prestamo.fecha_prestamo == 'null' and prestamo.fecha_limite_devolucion == 'null'):
                print(f"ID libro disponible: {prestamo.libro_id}")
           
    elif accion == 'actualizar_biografia': # Modificar biografía
        autor = sesion.query(Autor).filter_by(id=2).first()

        autor.biografia = "Una nueva biografia" 
        print("Biografía del autor modificada en la base de datos")
            
    elif accion == 'eliminar_prestamo': # Eliminamos los prestamos que ya han sido devueltos
        from datetime import datetime
        now = datetime.now()

        for prestamo in prestamos:
            fecha_limite = datetime.strptime(prestamo.fecha_limite_devolucion, "%Y-%m-%d") # Esto lo hemos sacado de: https://www.programiz.com/python-programming/datetime/strptime
            if fecha_limite < now:
                sesion.delete(prestamo)
                print("Registro/s borrado/s de la base de datos")

        


sesion.commit()
sesion.close() # cerramos la sesión
# No olvidarse de parar el servidor
# pg_ctl stop -D E:\Users\Alex\anaconda3\envs\cursoDWES\data