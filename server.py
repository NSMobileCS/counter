from flask import Flask, redirect, render_template, request, session, url_for
app = Flask(__name__)
app.secret_key = 'A++gr8,1337C()D354Uok1o1'


@app.route('/')
def index():
    if 'xserved' not in session:
        session['xserved'] = 0
    session['xserved'] += 1
    return render_template('index.html', 
                            xserved = session['xserved'],
                            css_path = url_for('static', filename='style.css'),
                            )

@app.route('/plus_2')
def add2():
    if 'xserved' not in session:
        session['xserved'] = 0
    session['xserved'] += 2
    return render_template('index.html', 
                            xserved = session['xserved'],
                            css_path = url_for('static', filename='style.css'),
                            )

@app.route('/reset')
def reset():
    session['xserved'] = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(port=8000, debug=True)