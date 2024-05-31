import requests


def query_open_library():
    # Query Open Library API for books on a specific subject
    url = "https://openlibrary.org/search.json?q=subject:book"
    response = requests.get(url)
    data = response.json()

    # Extract book details and create a dictionary
    books = {}
    for doc in data.get("docs", []):
        title = doc.get("title", "")
        authors = doc.get("author_name", [])
        author = ", ".join(authors) if isinstance(authors, list) else authors
        cover_id = doc.get("cover_i")
        image_url = f"http://covers.openlibrary.org/b/id/{cover_id}-L.jpg" if cover_id else None
        description = doc.get("description", "")
        if title:
            books[title] = {
                'title': title,
                'author': author,
                'image_url': image_url,
                'description': description
            }

    # Sort the dictionary by title names
    sorted_books = dict(sorted(books.items(), key=lambda item: item[0]))
    return sorted_books

def get_book_by_title(title):
    # Retrieve the dictionary of books
    books = query_open_library()
    # Return the book with the given title, or None if not found
    return books.get(title)

# def fetch_user_reading_list(username):
#     """Fetches the 'want-to-read' list for a given user from Open Library."""
#     url = f"https://openlibrary.org/people/mekBot/books/currently-reading.json"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         books = []
#         for entry in data.get('entries', []):
#             title = entry.get('title')
#             authors = entry.get('authors', [])
#             author_names = ', '.join([author['name'] for author in authors])
#             cover_id = entry.get('cover_id')
#             image_url = f"http://covers.openlibrary.org/b/id/{cover_id}-L.jpg" if cover_id else None
#             books.append({
#                 'title': title,
#                 'authors': author_names,
#                 'image_url': image_url
#             })
#         return books
#     else:
#         print(f"Failed to fetch data: {response.status_code}")
#         return None


if __name__ == "__main__":
    sorted_books_dict = query_open_library()
    print(sorted_books_dict)
    # username = "mekBot"  # Example username
    # user_books = fetch_user_reading_list(username)
    # if user_books:
    #     print("User's want-to-read list:")
    #     for book in user_books:
    #         print(f"{book['title']} by {book['authors']}")
    # else:
    #     print("No books found in user's list.")
    # Example usage:
    # book_title = "Example Book Title"  # Replace with a real title to test
    # book = get_book_by_title(book_title)
    # if book:
    #     print(book)
    # else:
    #     print("Book not found.")


# import requests
#
#
# def query_open_library():
#     # Query Open Library API for books
#     url = "https://openlibrary.org/search.json?q=subject:book"
#     response = requests.get(url)
#     data = response.json()
#
#     # Extract book titles and create a dictionary
#     books = {}
#     for doc in data.get("docs", []):
#         title = doc.get("title", "")
#         if title:
#             books[title] = doc
#
#     # Sort the dictionary by title names
#     sorted_books = dict(sorted(books.items()))
#
#     return sorted_books
#
#
# if __name__ == "__main__":
#     sorted_books_dict = query_open_library()
#     print(sorted_books_dict)
#
#
#
# # import requests
# # def replaceEmptyImages(dictList, url):
# # 	for d in dictList:
# # 		if ("image_url" not in d or not d["image_url"]):
# # 			d["image_url"]=url
# #
# # def find_coffee(city="Tacoma", state="Washington", limit=50):
# # 	api_key = 'pMWcYDMpXkTeeyWIb7AtpzRbcJ2PKRvHIzT7p0QAukPFge4IGKectozkpQBkZnTBKE9g3FwC7Os68MmQKgAwwucLgeMo0oMgagYENkYs-9TZKKJ8HXXMmwM1ZAaBYHYx'
# # 	headers = {'Authorization': 'Bearer {}'.format(api_key)}
# # 	search_api_url = 'https://api.yelp.com/v3/businesses/search'
# # 	params = {'term': 'coffee shop',
# # 	          'location': city + ', ' + state,
# # 	          'limit': limit }
# # 	response = requests.get(search_api_url, headers=headers, params=params, timeout=5)
# # 	data=response.json()
# # 	sortedbyRating=sorted(data["businesses"], key=lambda i: i['rating'], reverse=True)
# # 	replaceEmptyImages(sortedbyRating,"localhost")
# # 	return sortedbyRating
# #
# # if __name__ == '__main__':
# #     print(find_coffee())