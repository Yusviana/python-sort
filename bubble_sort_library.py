def bubble_sort_library(books):
    n = len(books)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if books[j][0] > books[j + 1][0]:
                books[j], books[j + 1] = books[j + 1], books[j]

books = [
    ["Harry Potter and the Sorcerer's Stone", 'J.K. Rowling', 320],
    ['To Kill a Mockingbird', 'Harper Lee', 281],
    [ 'The Great Gatsby', 'F. Scott Fitzgerald',  180],
    ['Pride and Prejudice', 'Jane Austen', 432],
    ['1984', 'George Orwell', 328]
]
bubble_sort_library(books)
print ("Hasil Perurutan : ",books)
