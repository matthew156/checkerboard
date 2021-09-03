from flask import Flask
from flask.templating import render_template 
app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello!'


@app.route('/play/<int:num>')
def play(num):
    return render_template('index.html', num = int(num)) 

if __name__ == "__main__":
    app.run(debug=True)