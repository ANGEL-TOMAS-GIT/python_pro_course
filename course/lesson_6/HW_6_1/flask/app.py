from flask import Flask, render_template

app = Flask(__name__)


movies: list[dict] = [
    {
        "id": 1,
        "title": "The Shawshank Redemption",
        "director": "Frank Darabont",
        "year": 1994,
        "rating": 9.3,
        "genre": "Drama",
    },
    {
        "id": 2,
        "title": "The Godfather",
        "director": "Francis Ford Coppola",
        "year": 1972,
        "rating": 9.2,
        "genre": "Crime",
    },
    {
        "id": 3,
        "title": "Pulp Fiction",
        "director": "Quentin Tarantino",
        "year": 1994,
        "rating": 8.9,
        "genre": "Crime",
    },
]

about_info: dict = {
    "name": "Megumi Fushiguro",
    "email": "megumi.email@example.com",
    "github": "Jujutsu",
    "favorite_movie": "Inception",
}


@app.route("/")
def home() -> str:
    return render_template(template_name_or_list="index.html")


@app.route("/movies")
def movie_list() -> str:

    return render_template(template_name_or_list="movies.html", movies=movies)


@app.route("/about")
def about() -> str:

    return render_template(template_name_or_list="about.html", about_info=about_info)


if __name__ == "__main__":
    app.run(debug=True)
