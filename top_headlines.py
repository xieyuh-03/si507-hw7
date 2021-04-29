from flask import Flask, render_template
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

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)