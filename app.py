from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])  
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/solutions')
def solutions():
    return render_template('solution.html')

if __name__ == '__main__':
    app.run(debug=True,)