import requests


def query_open_library():
    # Query Open Library API for books
    url = "https://openlibrary.org/search.json?q=subject:book"
    response = requests.get(url)
    data = response.json()

    # Extract book titles and create a dictionary
    books = {}
    for doc in data.get("docs", []):
        title = doc.get("title", "")
        if title:
            books[title] = doc

    # Sort the dictionary by title names
    sorted_books = dict(sorted(books.items()))

    return sorted_books


if __name__ == "__main__":
    sorted_books_dict = query_open_library()
    print(sorted_books_dict)



# import requests
# def replaceEmptyImages(dictList, url):
# 	for d in dictList:
# 		if ("image_url" not in d or not d["image_url"]):
# 			d["image_url"]=url
#
# def find_coffee(city="Tacoma", state="Washington", limit=50):
# 	api_key = 'pMWcYDMpXkTeeyWIb7AtpzRbcJ2PKRvHIzT7p0QAukPFge4IGKectozkpQBkZnTBKE9g3FwC7Os68MmQKgAwwucLgeMo0oMgagYENkYs-9TZKKJ8HXXMmwM1ZAaBYHYx'
# 	headers = {'Authorization': 'Bearer {}'.format(api_key)}
# 	search_api_url = 'https://api.yelp.com/v3/businesses/search'
# 	params = {'term': 'coffee shop',
# 	          'location': city + ', ' + state,
# 	          'limit': limit }
# 	response = requests.get(search_api_url, headers=headers, params=params, timeout=5)
# 	data=response.json()
# 	sortedbyRating=sorted(data["businesses"], key=lambda i: i['rating'], reverse=True)
# 	replaceEmptyImages(sortedbyRating,"localhost")
# 	return sortedbyRating
#
# if __name__ == '__main__':
#     print(find_coffee())