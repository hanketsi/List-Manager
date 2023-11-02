#File Name: listmanager_Henrik.py
#Author: Henrik Lehtonen
#Description: Manages two lists that contain movies and books, with publish year and author

import tkinter as tk
from tkinter import simpledialog, messagebox


#Classes for data
class Movie:
    def __init__(self, name, year, director):
        self.name = name
        self.year = year
        self.director = director


class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author


#Sample movies I've seen
movies = [
    Movie("The Shawshank Redemption", 1994, "Frank Darabont"),
    Movie("The Godfather", 1972, "Francis Ford Coppola"),
    Movie("The Dark Knight", 2008, "Christopher Nolan"),
    Movie("12 Angry Men", 1957, "Sidney Lumet"),
    Movie("Schindler's List", 1993, "Steven Spielberg"),
    Movie("The Lord of the Rings: The Return of the King", 2003, "Peter Jackson"),
    Movie("Pulp Fiction", 1994, "Quentin Tarantino"),
    Movie("The Good, the Bad and the Ugly", 1966, "Sergio Leone"),
    Movie("Forrest Gump", 1994, "Robert Zemeckis"),
    Movie("Inception", 2010, "Christopher Nolan"),
    Movie("The Matrix", 1999, "The Wachowskis"),
    Movie("Goodfellas", 1990, "Martin Scorsese"),
    Movie("Star Wars: Episode V - The Empire Strikes Back", 1980, "Irvin Kershner"),
    Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Peter Jackson"),
    Movie("Fight Club", 1999, "David Fincher"),
    Movie("The Silence of the Lambs", 1991, "Jonathan Demme"),
    Movie("Se7en", 1995, "David Fincher"),
    Movie("The Usual Suspects", 1995, "Bryan Singer"),
    Movie("Léon: The Professional", 1994, "Luc Besson"),
    Movie("Interstellar", 2014, "Christopher Nolan"),
    Movie("The Prestige", 2006, "Christopher Nolan"),
    Movie("Whiplash", 2014, "Damien Chazelle"),
    Movie("The Departed", 2006, "Martin Scorsese"),
    Movie("Gladiator", 2000, "Ridley Scott"),
    Movie("The Green Mile", 1999, "Frank Darabont"),
    Movie("The Intouchables", 2011, "Olivier Nakache, Éric Toledano"),
    Movie("The Pianist", 2002, "Roman Polanski"),
    Movie("The Lion King", 1994, "Roger Allers, Rob Minkoff"),
    Movie("The Dark Knight Rises", 2012, "Christopher Nolan"),
    Movie("The Lives of Others", 2006, "Florian Henckel von Donnersmarck")
]
#Sample Books I should've read
books = [
    Book("To Kill a Mockingbird", 1960, "Harper Lee"),
    Book("1984", 1949, "George Orwell"),
     Book("The Great Gatsby", 1925, "F. Scott Fitzgerald"),
    Book("Moby Dick", 1851, "Herman Melville"),
    Book("War and Peace", 1869, "Leo Tolstoy"),
    Book("The Catcher in the Rye", 1951, "J.D. Salinger"),
    Book("The Lord of the Rings", 1954, "J.R.R. Tolkien"),
    Book("Pride and Prejudice", 1813, "Jane Austen"),
    Book("The Hobbit", 1937, "J.R.R. Tolkien"),
    Book("The Chronicles of Narnia", 1950, "C.S. Lewis"),
    Book("To the Lighthouse", 1927, "Virginia Woolf"),
    Book("Brave New World", 1932, "Aldous Huxley"),
    Book("The Grapes of Wrath", 1939, "John Steinbeck"),
    Book("One Hundred Years of Solitude", 1967, "Gabriel Garcia Marquez"),
    Book("Crime and Punishment", 1866, "Fyodor Dostoevsky"),
    Book("The Hitchhiker's Guide to the Galaxy", 1979, "Douglas Adams"),
    Book("Frankenstein", 1818, "Mary Shelley"),
    Book("The Picture of Dorian Gray", 1890, "Oscar Wilde"),
    Book("The Sun Also Rises", 1926, "Ernest Hemingway"),
    Book("The Bell Jar", 1963, "Sylvia Plath"),
    Book("In Cold Blood", 1966, "Truman Capote"),
    Book("Beloved", 1987, "Toni Morrison"),
    Book("The Handmaid's Tale", 1985, "Margaret Atwood"),
    Book("The Alchemist", 1988, "Paulo Coelho"),
    Book("The Girl with the Dragon Tattoo", 2005, "Stieg Larsson"),
    Book("A Game of Thrones", 1996, "George R.R. Martin"),
    Book("The Da Vinci Code", 2003, "Dan Brown"),
    Book("The Hunger Games", 2008, "Suzanne Collins"),
    Book("Gone Girl", 2012, "Gillian Flynn"),
    Book("Educated", 2018, "Tara Westover")
]


#GUI 
def stop_program():
    messagebox.showinfo("Thank you!", "Thank you for using my list manager. \n-Henrik Lehtonen 1903443")
    root.destroy()


def search_element():
    option = simpledialog.askinteger(
        "Search", "Choose 1 for Name, 2 for Author/Director, 3 for Year:"
    )
    text_area.delete(1.0, tk.END)
    if option == 1:
        search_name = simpledialog.askstring("Search by Name", "Enter the name of the movie/book:")
        for movie in movies:
            if search_name.lower() in movie.name.lower():
                text_area.insert(tk.END, f"{movie.name} ({movie.year}) - Directed by {movie.director}\n")
        for book in books:
            if search_name.lower() in book.title.lower():
                text_area.insert(tk.END, f"{book.title} ({book.year}) - Author: {book.author}\n")
    elif option == 2:
        search_author_director = simpledialog.askstring(
            "Search by Author/Director", "Enter the name of the author/director:"
        )
        for movie in movies:
            if search_author_director.lower() in movie.director.lower():
                text_area.insert(tk.END, f"{movie.name} ({movie.year}) - Directed by {movie.director}\n")
        for book in books:
            if search_author_director.lower() in book.author.lower():
                text_area.insert(tk.END, f"{book.title} ({book.year}) - Author: {book.author}\n")
    elif option == 3:
        search_year = simpledialog.askinteger("Search by Year", "Enter the year:")
        for movie in movies:
            if search_year == movie.year:
                text_area.insert(tk.END, f"{movie.name} ({movie.year}) - Directed by {movie.director}\n")
        for book in books:
            if search_year == book.year:
                text_area.insert(tk.END, f"{book.title} ({book.year}) - Author: {book.author}\n")
    else:
        messagebox.showerror("Error", "Invalid Option")


def add_element():
    option = simpledialog.askinteger("Add", "Choose 1 for Movie, 2 for Book:")
    if option == 1:
        name = simpledialog.askstring("Movie Name", "Enter the name of the movie:")
        year = simpledialog.askinteger("Year", "Enter the year of release:")
        director = simpledialog.askstring("Director", "Enter the name of the director(s):")
        movies.append(Movie(name, year, director))
    elif option == 2:
        title = simpledialog.askstring("Book Title", "Enter the title of the book:")
        year = simpledialog.askinteger("Year", "Enter the year of publication:")
        author = simpledialog.askstring("Author", "Enter the name of the author:")
        books.append(Book(title, year, author))
    else:
        messagebox.showerror("Error", "Invalid Option")


#Remove the chosen element from the list
def remove_element():
    option = simpledialog.askinteger("Remove", "Choose 1 for Movie, 2 for Book:")
    if option == 1:
        name = simpledialog.askstring("Movie Name", "Enter the name of the movie:")
        year = simpledialog.askinteger("Year", "Enter the year of the release:")
        for movie in movies:
            if movie.name.lower() == name.lower() and movie.year == year:
                    movies.remove(movie)
    elif option == 2:
        title = simpledialog.askstring("Book Title", "Enter the title of the book:")
        year = simpledialog.askinteger("Year", "Enter the year of publication:")
        for book in books:
            if book.title.lower() == title.lower() and book.year == year:
                books.remove(book)
    else:
        messagebox.showerror("Error", "Invalid Opttion")
    


def sort_elements():
    option = simpledialog.askinteger(
        "Sort", "Choose 1 for Name, 2 for Author/Director, 3 for Year:"
    )
    if option == 1:
        books.sort(key = lambda x: x.title)
        movies.sort(key = lambda x: x.name)
    elif option == 2:
        books.sort(key = lambda x: x.author)
        movies.sort(key = lambda x: x.director)
    elif option == 3:
        books.sort(key = lambda x: x.year)
        movies.sort(key = lambda x: x.year)
    else:
        messagebox.showerror("Error", "Invalid Option")
    list_elements()


def list_elements():
    text_area.delete(1.0, tk.END)
    option = simpledialog.askinteger("List", "Choose 1 for Movies, 2 for Books:")
    if option == 1:
        for movie in movies:
            text_area.insert(tk.END, f"{movie.name} ({movie.year}) - {movie.director}\n")
    elif option == 2:
        for book in books:
            text_area.insert(tk.END, f"{book.title} ({book.year}) - {book.author}\n")
    else:
        messagebox.showerror("Error", "Invalid Option")


root = tk.Tk()
root.title("List Manager")

#Create buttons
stop_button = tk.Button(root, text = "Stop", command = stop_program)
search_button = tk.Button(root, text = "Search", command = search_element)
add_button = tk.Button(root, text = "Add", command = add_element)
remove_button = tk.Button(root, text = "Remove", command = remove_element)
sort_button = tk.Button(root, text = "Sort", command = sort_elements)
list_button = tk.Button(root, text = "List", command = list_elements)

#Add buttons to the GUI
stop_button.pack()
search_button.pack()
add_button.pack()
remove_button.pack()
sort_button.pack()
list_button.pack()

#Create Text box
text_area = tk.Text(root, height = 30, width = 60)
text_area.pack()

root.mainloop()
