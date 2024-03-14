from sqlalchemy import create_engine, Column,select, MetaData,types, Table

class Connection:
    def __init__(self, nombre_usuario='postgres', contraseña='ibio', nombre_bd='libreria', host='localhost', puerto='5432'):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.nombre_bd = nombre_bd
        self.host = host
        self.puerto = puerto
        self.cadena_conexion = f'postgresql://{nombre_usuario}:{contraseña}@{host}:{puerto}/{nombre_bd}'
        self.engine = create_engine(self.cadena_conexion)
        self.metadata = MetaData()

    def consulta_libreria(self):
        try:
            connection = self.engine.connect()
            self.metadata.reflect(bind=self.engine)
            libro_table = Table('libro', self.metadata, autoload_with=self.engine)
            stmt =  libro_table.select()
            resultado = connection.execute(stmt)
            column_names = resultado.keys()
            rows = [dict(zip(column_names, row)) for row in resultado.fetchall()]
            # json_result = json.dumps(rows)
            print(rows)
            return rows
        except Exception as ex:
            print('01. Error consulta: '+str(ex))
            
            
    def consulta_autor(self,autores):
        try:
            connection = self.engine.connect()
            self.metadata.reflect(bind=self.engine)
            autor = Table('autor', self.metadata, autoload_with=self.engine)
            libro = Table('libro', self.metadata, autoload_with=self.engine)
            stmt  = select(autor, libro) \
            .select_from(autor.join(libro, autor.c.id_autor == libro.c.id_autor)) \
            .where(autor.c.nombre == autores)
            resultado = connection.execute(stmt)
            column_names = resultado.keys()
            rows = [dict(zip(column_names, row)) for row in resultado.fetchall()]
            # json_result = json.dumps(rows)
            print(rows)
            return rows
        except Exception as ex:
            print('02. Error autor: '+str(ex))
            
            
    def consulta_editorial(self,editorial):
        try:
            connection = self.engine.connect()
            self.metadata.reflect(bind=self.engine)
            editoriala = Table('editorial', self.metadata, autoload_with=self.engine)
            libro = Table('libro', self.metadata, autoload_with=self.engine)
            stmt  = select(editoriala, libro) \
            .select_from(editoriala.join(libro, editoriala.c.id_editorial == libro.c.id_editorial)) \
            .where(editoriala.c.nombre == editorial)
            resultado = connection.execute(stmt)
            column_names = resultado.keys()
            rows = [dict(zip(column_names, row)) for row in resultado.fetchall()]
            # json_result = json.dumps(rows)
            print(rows)
            return rows
        except Exception as ex:
            print('02. Error autor: '+str(ex))






if __name__ == "__main__":

    base_de_datos = Connection('postgres', 'ibio', 'libreria')

    base_de_datos.consulta_autor()
 
