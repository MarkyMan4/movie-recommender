from flask import Flask, render_template, url_for, request, redirect, session
from MovieCrawler import RandMovieFinder
from forms import MovieOptionsForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = str(os.urandom(16))

# use RandMovieFinder to crawl the web for movies
def getMovieData(genre, num_results):
    rmv = RandMovieFinder()
    return rmv.get_random_movies(genre, num_results)

# home page with form for entering search parameters
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        genre = request.form.get('genres')
        num_results = int(request.form.get('num_results'))

        session['genre'] = genre
        session['num_results'] = num_results

        return redirect(url_for('details'))

    form = MovieOptionsForm()
    return render_template('home.html', form=form)

# displays list of movies from a selected genre
@app.route('/details')
def details():
    genre = session['genre']
    num_results = session['num_results']
    movies = getMovieData(genre, num_results)
    
    return render_template('movie_detail.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
