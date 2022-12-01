from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/workexperience')
def generic():
    return render_template('generic.html')

@app.route('/personalstatement')
def PS():
    return render_template('PS.html')

@app.route('/aboutme')
def elements():
    return render_template('elements.html')

if __name__ == "__main__":
    app.run(debug=True)