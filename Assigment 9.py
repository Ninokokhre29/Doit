
library = []
def add_book():
    author = input("შეიყვანეთ ავტორი: ")
    title = input("შეიყვანეთ წიგნის სათაური: ")
    if title in library:
        print(f"{title} უკვე გვაქვს ბიბლიოთეკაში")
    else:
        library.append({"ავტორი": author, "სათაური": title})
    return print(library)

add_book()

def find_author():
    author = input("მოძებნეთ ავტორის მიხედვით: ")
    for i in library:
        if i["ავტორი"] == author:
            print(f"{author} წიგნი: ", i["სათაური"])
        else:
            print(f"{author} ამ ავტორის წიგნი ბიბლიოთეკაში არ იძებნება")

def find_title():
    title = input("მოძებნეთ სათაურის მიხედვით: ")
    for i in library:
        if i["სათაური"] == title:
            print(f"{title}-ს ავტორი არის ", i["ავტორი"])
        else:
            print(f"{title} ამ სათაურის წიგნი ბიბლიოთეკაში არ იძებნება")

find_title()
find_author()
