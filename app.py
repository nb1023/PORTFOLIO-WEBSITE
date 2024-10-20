from flask import Flask, render_template, redirect, url_for, flash
from forms import ContactForm

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Route with Form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f"Message sent by {form.name.data}!", "success")
        return redirect(url_for('home'))
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
