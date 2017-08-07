from flask import Flask, redirect, render_template, session, url_for
app = Flask(__name__)
app.secret_key = 'A1gr81337C()D35z4Uok1o1'


@app.route('/')
def index():
    if 'xserved' not in session:
        session['xserved'] = 0
    session['xserved'] += 1
    print(session['xserved'])
    return render_template('index.html', 
                            xserved = session['xserved'],
                            css_path = url_for('static', filename='style.css'),
                            )

def reset():
    session['xserved'] = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(port=8000, debug=True)