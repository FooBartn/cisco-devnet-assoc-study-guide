from xml.dom.minidom import parse

domTree = parse('authors.xml')
root = domTree.documentElement

authors = root.getElementsByTagName('authors')
print(f'Number of Authors: {len(authors)}')
for author in authors:
    firstName = author.getElementsByTagName('first_name')[0]
    lastName = author.getElementsByTagName('last_name')[0]
    print(f'Author Name: {firstName.firstChild.data} {lastName.firstChild.data}')
    books = author.getElementsByTagName('books')
    for book in books:
        title = book.getElementsByTagName("title")[0]
        pages = book.getElementsByTagName("pages")[0]
        descr = book.getElementsByTagName("description")[0]
        print(f'Title: {title.firstChild.data}')
        print(f'Pages: {pages.firstChild.data}')
        print(f'Description: {descr.firstChild.data}')