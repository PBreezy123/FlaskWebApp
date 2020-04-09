from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

dog = 2
cat = 3

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html') #Instead of returning HTML, we can render the template

@app.route("/results")
def results():
    return render_template('results.html', dog=dog)

@app.route("/test")
def test():
    return render_template('test.html')

# This condition allows changes to be reflected in the web page automatically
if __name__ == '__main__': # Only true if we run script directly
    app.run(debug=True) # Run in debug mode
    # Basically means run the app if user does 'python flaskpage.py in terminal'

#templates are used to return complicated HTML code
