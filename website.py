from flask import Flask, render_template, url_for, request
import functions as egg

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html') #Instead of returning HTML, render the template

@app.route("/results", methods = ['POST'])
def results():
    if request.method == 'POST':
        number = int(request.form['numberToCheck']) #request.form is a dictionary. 'numberToCheck' is the value, for which we extract the key. we then convert the key from a string to an int
        dogs, cats, mice = egg.GetAnimals(number)
        return render_template("results.html", dogs=dogs, cats=cats, mice=mice)


# This condition allows changes to be reflected in the web page automatically
if __name__ == '__main__': # Only true if we run script directly
    app.run(debug=True) # Run in debug mode
    # Basically means run the app if user does 'python flaskpage.py in terminal'

#templates are used to return complicated HTML code
