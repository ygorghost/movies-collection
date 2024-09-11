from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

API_URL = 'http://127.0.0.1:5000/api/movies'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        requests.post(
            API_URL,
            json={'title':title, 'genre':genre}
        )
        return redirect('/')
    else:
        response = requests.get(API_URL)    
        if response.status_code == 200:
            movies = response.json()
        else:
            movies = []
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(port=5001, debug=True) 

@app.route('/delete/<int:id>')
def delete(id):
    requests.delete(f'{API_URL}/{id}')
    return redirect('/')

@app.route('/update/<int:id>', methods ={'GET', 'POST'})
def delete(id):
    if request.method =='POST':
        title = request.form['title']
        Genre = request.form['genre']
        requests.put(f''{API_URL}/{id},json={'title' title 'genre': genre})

        return redirect('/')
    response = request.get(f'{API_URL}/{id}')
    if response.status_code == 200:
        movie = response.json()
    else:
        movies = {}

    return render_template('update.html', movies) 

if __name__ == '__main__':
    app.run(port=5001, debug=True)