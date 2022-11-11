# app.py
from flask import request
from flask_restx import Resource
from create_data import app, api, Movie, db, Genre, Director
from schemas import MovieSchema, GenreSchema, DirectorSchema

# Movie
movie_ns = api.namespace("movies")
movie_schema = MovieSchema()
movies_schemas = MovieSchema(many=True)

@movie_ns.route("/")
class MovieViews(Resource):
    def get(self):
        query = Movie.query
        director_id = request.args.get('director_id')
        if director_id:
            query = query.filter(Movie.director_id == director_id)
        genre_id = request.args.get('genre_id')
        if genre_id:
            query = query.filter(Movie.genre_id == genre_id)
        return movies_schemas.dump(query)

    def post(self):
        data = request.json
        try:
            db.session.add(
                Movie(
                    **data
                )
            )
            db.session.commit()
            return "ok", 201
        except Exception as e:
            print(e)
            db.session.rollback()
            return e, 200

@movie_ns.route("/<int:pid>")
class MovieViews(Resource):
    def get(self, pid):
        query = Movie.query.get(pid)
        return movie_schema.dump(query)

    def put(self, pid):
        data = request.json
        try:
            db.session.query(Movie).filter(Movie.id == pid).update(
                data
            )
            db.session.commit()
            return "ok", 201
        except Exception as e:
            print(e)
            db.session.rollback()
            return e, 200

    def delete(self, pid):
        try:
            db.session.query(Movie).filter(Movie.id == pid).delete()
            db.session.commit()
            return "ok", 201
        except Exception as e:
            print(e)
            db.session.rollback()
            return e, 200

# Genre
genre_ns = api.namespace("genres")
genre_schema = GenreSchema()
genres_schemas = GenreSchema(many=True)

@genre_ns.route("/")
class GenreViews(Resource):
    def get(self):
        query = Genre.query
        return genres_schemas.dump(query)

    def post(self):
        data = request.json
        try:
            db.session.add(
                Genre(
                    **data
                )
            )
            db.session.commit()
            return "ok", 201
        except Exception as e:
            print(e)
            db.session.rollback()
            return e, 200

@genre_ns.route("/<int:pid>")
class GenreViews(Resource):
    def get(self, pid):
        query = Genre.query.get(pid)
        return genre_schema.dump(query)

    def put(self, pid):
        data = request.json
        try:
            db.session.query(Genre).filter(Genre.id == pid).update(
                data
            )
            db.session.commit()
            return "ok", 201
        except Exception as e:
            print(e)
            db.session.rollback()
            return e, 200

    def delete(self, pid):
        try:
            db.session.query(Genre).filter(Genre.id == pid).delete()
            db.session.commit()
            return "ok", 201
        except Exception as e:
            print(e)
            db.session.rollback()
            return e, 200


# Director
director_ns = api.namespace("directors")
director_schema = DirectorSchema()
directors_schemas = DirectorSchema(many=True)

@director_ns.route("/")
class DirectorViews(Resource):
    def get(self):
        query = Director.query
        return directors_schemas.dump(query)

    def post(self):
        data = request.json
        try:
            db.session.add(
                Director(
                    **data
                )
            )
            db.session.commit()
            return "ok", 201
        except Exception as e:
            print(e)
            db.session.rollback()
            return e, 200

@director_ns.route("/<int:pid>")
class DirectorViews(Resource):
    def get(self, pid):
        query = Director.query.get(pid)
        return director_schema.dump(query)

    def put(self, pid):
        data = request.json
        try:
            db.session.query(Director).filter(Director.id == pid).update(
                data
            )
            db.session.commit()
            return "ok", 201
        except Exception as e:
            print(e)
            db.session.rollback()
            return e, 200

    def delete(self, pid):
        try:
            db.session.query(Director).filter(Director.id == pid).delete()
            db.session.commit()
            return "ok", 201
        except Exception as e:
            print(e)
            db.session.rollback()
            return e, 200


if __name__ == '__main__':
    app.run(debug=True)
