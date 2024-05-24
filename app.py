from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from book import query_open_library
# from forms import LoginForm, RegistrationForm, BookForm
# from models import db, User, Book
app = Flask(__name__)
app.secret_key = 'my_secret_key'
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wishlist.db'
# app.config['SECRET_KEY'] = 'your_secret_key'
# db.init_app(app)
# bcrypt = Bcrypt(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()
# @app.route('/home', methods=['GET'])
@app.route('/home')
def home():
    # if 'username' in session:
    #     user = User.query.filter_by(username=session['username']).first()
    #     books = Book.query.filter_by(user_id=user.id).all()
    #     return render_template('home.html', books=books)
    # return render_template('welcome.html')
    return render_template("home.html", books=query_open_library())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here, we assume you're sending 'username', and 'password'
        username = request.form['username']
        password = request.form['password']
        # You should implement your validation and authentication logic here
        # For now, we'll just redirect to home if the user submits any data
        return redirect(url_for('home'))
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Here you would usually add logic to save the user to a database
        # For example, checking if the user already exists and hashing the password
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    return render_template("register.html")



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#             session['username'] = user.username
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', form=form)
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         user = User(username=form.username.data, email=form.email.data, password=hashed_password)
#         db.session.add(user)
#         db.session.commit()
#         flash('Your account has been created! You are now able to log in', 'success')
#         return redirect(url_for('login'))
#     return render_template('register.html', form=form)
#
# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('home'))
#
# @app.route('/add_book', methods=['GET', 'POST'])
# def add_book():
#     if 'username' not in session:
#         return redirect(url_for('login'))
#     form = BookForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=session['username']).first()
#         book = Book(title=form.title.data, author=form.author.data, description=form.description.data, user_id=user.id)
#         db.session.add(book)
#         db.session.commit()
#         flash('Your book has been added to the wishlist!', 'success')
#         return redirect(url_for('home'))
#     return render_template('add_book.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='True', port=5000)

