from flask import Flask, render_template
import requests
import secrets
app = Flask(__name__)


@app.route('/')
def index():
    html = f'''
        <h1>Welcome!</h1>
        <p>
            Return <a href='/about'>about</a>
        </p>

    '''
    return html

@app.route('/about')
def about():
    tcourse = 'SI 507'
    tsemester = 'Winter 2021'

    return render_template('about.html', semester=tsemester, course=tcourse)

@app.route('/name/<nm>')
def hello_name(nm):

    return render_template('name.html', name=nm)

@app.route('/headlines/<nm>')
def tech_headlines(nm):
    mykey = secrets.api_key
    url = f'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={mykey}'
    
    results = requests.get(url).json()
    headlines = []
    i = 1
    for item in results['results']:
        if i < 6:
            title = item['title']
            headlines.append(title)
            i += 1
    
    return render_template('headlines.html', name=nm, title_list=headlines)


    

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)