from json import load

f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\books.json")

data=load(f)

# for book in data:
#     print(book)

all_titles=[book.get("title") for book in data]

# print(all_titles)


page_filter=[book.get("title")for book in data if book.get("pages") < 250]

# print(page_filter)

all_genres=[book.get("genre") for book in data]

# print(set(all_genres))

genre_count={genre:all_genres.count(genre)for genre in all_genres}

# print(genre_count)

costly_book=max(data, key=lambda book: book.get("price"))

# print(costly_book)

# author_count = {}


# for book in data:
#     author = book["author"]
#     author_count[author] = author_count.get(author, 0) + 1



# authors_with_multiple_books = [author for author, count in author_count.items() if count > 1]

# print(authors_with_multiple_books)

all_authors=[book.get("author") for book in data]


author_count={auth: all_authors.count(auth) for auth in all_authors }

print([k for k,v in author_count.items() if v>1])