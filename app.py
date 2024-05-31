from flask import Flask, render_template, request, redirect, url_for, flash, session
# from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from book import query_open_library, get_book_by_title
from forms import LoginForm, RegistrationForm
from models import db, User, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'my_secret_key'

bcrypt = Bcrypt(app)
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        user_id = session['user_id']
        # books = Book.query.filter_by(user_id=user_id).all()  # Fetch books for the logged-in user
        # return render_template('home.html', books=books)
        books = query_open_library()
        return render_template("home.html", books=books)
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Placeholder function to check user credentials
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id  # Store user's ID in session
            # session['username'] = user.username  # Optionally store the username
            flash('You were successfully logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        hashed_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template("register.html")

@app.route('/book/<title>')
def book_details(title):
    book = get_book_by_title(title)
    if book:
        return render_template('book_details.html', book=book)
    else:
        return "Book not found", 404

# @app.route('/book_details/<title>')
# def book_details(title):
#     book = Book.query.filter_by(title=title).first()
#     if book:
#         return render_template('book_details.html', book=book)
#     else:
#         flash('Book not found', 'warning')
#         return redirect(url_for('wishlist'))


@app.route('/add_books', methods=['POST'])
def add_books():
    title = request.form.get('title')
    author = request.form.get('author')  # Ensure these details are provided in the form
    # image_url = request.form.get('image_url')
    # description = request.form.get('description')
    user_id = session.get('user_id')

    if user_id:
        new_book = Book(title=title, author=author, user_id=user_id)
        db.session.add(new_book)
        db.session.commit()
        flash(f'"{title}" added to your wishlist!', 'success')
    else:
        flash('You need to log in to add books.', 'danger')

    return redirect(url_for('home'))

# @app.route('/add_books', methods=['GET', 'POST'])
# def add_books():
#     if request.method == 'POST':
#         title = request.form.get('title')
#         user_id = session.get('user_id')
#         if user_id:
#             new_book = Book(title=title, user_id=user_id)
#             db.session.add(new_book)
#             db.session.commit()
#             flash(f'Book {title} added to your wishlist!', 'success')
#             return redirect(url_for('add_books'))
#         else:
#             flash('Error adding book.', 'danger')
#     return render_template('add_books.html')

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

