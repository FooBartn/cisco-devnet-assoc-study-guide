import json

with open('authors.json') as authors_file:
    data=authors_file.read()

authors_json = json.loads(data)
authors = authors_json['authors']

print(f'Number of Authors: {len(authors)}')
for author in authors:
    print(f'Author Name: {author["first_name"]} {author["last_name"]}')
    books = author["books"]
    for book in books:
        print(f'Title: {book["title"]}')
        print(f'Pages: {book["pages"]}')
        print(f'Description: {book["description"]}')


        