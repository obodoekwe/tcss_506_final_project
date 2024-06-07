from flask import Flask, render_template, request, redirect, url_for, flash, session
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
from book import query_open_library, get_book_by_title
from flask_login import login_user, logout_user, login_required
from forms import LoginForm
from models import db, User, Book, loginManager
import sqlite3

app = Flask(__name__)
app.secret_key = 'my_secret_key'


# database configuration
DBUSER = 'user'
DBPASS = 'password'
DBHOST = 'db'
DBPORT = '5432'
DBNAME = 'pglogindb'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# bcrypt = Bcrypt(app)
db.init_app(app)
loginManager.init_app(app)


#add user routine
def add_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.email = email
    db.session.add(user)
    db.session.commit()
    return user


#handler for bad requests
@loginManager.unauthorized_handler
def authHandler():
    form=LoginForm()
    flash('Please login to access this page')
    return render_template('login.html', form=form)


@app.before_first_request
def create_tables():
    db.create_all()
    user = User.query.filter_by(email='natiteme@uw.edu').first()
    if user is None:
        add_user('user', 'natiteme@uw.edu', 'password')
    else:
        logout_user()


@app.route('/')
def landing():
    return render_template('landing.html')


@app.route('/home')
def home():
    if 'user_id' in session:
        # user_id = session['user_id']
        books = query_open_library()
        return render_template("home.html", books=books)
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('You were successfully logged in.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form['email']
        password = request.form['password']

        # Check if the username is already taken
        if User.query.filter_by(email=email).first():
            flash('Username already exists')
            return redirect(url_for('register'))

        # Hash the password before storing it
        user = User(username=username, email=email)
        user.set_password(password)
        user.email = email
        db.session.add(user)
        db.session.commit()

        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/book/<title>')
def book_details(title):
    book = get_book_by_title(title)
    if book:
        return render_template('book_details.html', book=book)
    else:
        return "Book not found", 404


@app.route('/add_books', methods=['POST'])
def add_books():
    title = request.form.get('title')
    author = request.form.get('author')
    user_id = session.get('user_id')

    if user_id:
        new_book = Book(title=title, author=author, user_id=user_id)
        db.session.add(new_book)
        db.session.commit()
        flash(f'"{title}" added to your wishlist!', 'success')
    else:
        flash('You need to log in to add books.', 'danger')

    return redirect(url_for('home'))


@app.route('/remove_books', methods=['POST'])
def remove_books():
    title = request.form.get('title')
    user_id = session.get('user_id')
    if user_id:
        book = Book.query.filter_by(title=title, user_id=user_id).first()
        if book:
            db.session.delete(book)
            db.session.commit()
            flash(f'"{title}" removed from your wishlist!', 'success')
        else:
            flash('Book not found in your wishlist.', 'warning')
    else:
        flash('You need to log in to remove books.', 'danger')
    return redirect(url_for('home'))


@app.route('/wishlist')
def wishlist():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        if user:
            books = user.books  # Now accessing books directly through the user
            return render_template('wishlist.html', books=books)
        else:
            flash("User not found.", "warning")
            return redirect(url_for('login'))
    flash("You must be logged in to view your wishlist.", "danger")
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.clear()  # Clears all data from the session
    flash('You were logged out', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='True', port=5000)

