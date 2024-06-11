
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base


#Creamos el motor que manejará la conexión con la base de datos. Creamos la base de datos tareas.db en el directorio database que colgará del
#directorio actual. Los argumentos de conexion es para permitor multihilo en la ejecución de las transacciones de la base de datos.
engine = create_engine('sqlite:///database/tareas.db', connect_args={'check_same_thread': False}) 

#Abrimos una sesión y la vinculamos al motor de la base de datos.
Session = sessionmaker(bind=engine) 
session = Session() 


Base = declarative_base()