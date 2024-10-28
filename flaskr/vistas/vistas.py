from flask import request
from flask_restful import Resource
from ..modelos import *

cancion_schema = CancionSchema()

class VistaCanciones(Resource):
    def get(self):
        return [cancion_schema.dump(Cancion) for Cancion in Cancion.query.all()]
    
    def post(self):
        nueva_cancion = Cancion(titulo=request.json['titulo'], \
                                minutos = request.json['minutos'], \
                                segundos = request.json['segundos'], \
                                interprete = request.json['interprete'])
        db.session.add(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)

    # def post(self):
    #     try:
    #         data = request.get_json()
    #         titulo = data['titulo']
    #         minutos = data['minutos']
    #         segundos = data['segundos']
    #         interprete = data['interprete']

    #         nueva_cancion = Cancion(titulo=titulo, minutos=minutos, segundos=segundos, interprete=interprete)
    #         db.session.add(nueva_cancion)
    #         db.session.commit()

    #         return cancion_schema.dump(nueva_cancion), 201  # Return 201 Created status code
    #     except Exception as e:
    #         return {'error': str(e)}, 400  # Return 400 Bad Request with error message

album_schema = AlbumSchema()

class VistaAlbumes(Resource):
    def get(self):
        return [album_schema.dump(Album) for Album in Album.query.all()]

    def post(self):
        nuevo_album = Album(titulo=request.json['titulo'],
                            anio=request.json['anio'],
                            descripcion=request.json['descripcion'],
                            medio=request.json['medio'],
                            usuario=request.json['usuario'])
        db.session.add(nuevo_album)
        db.session.commit()
        return album_schema.dump(nuevo_album)
