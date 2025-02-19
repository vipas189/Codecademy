knygos = [
    {
        "Autorius": "J.K. Rowling",
        "Pavadinimas": "Harry Potter and the Sorcerer's Stone",
        "leidimo_metai": 1997,
        "Zanras": "Fantasy",
    },
    {
        "Autorius": "George Orwell",
        "Pavadinimas": "1984",
        "leidimo_metai": 1949,
        "Zanras": "Dystopian",
    },
    {
        "Autorius": "J.R.R. Tolkien",
        "Pavadinimas": "The Hobbit",
        "leidimo_metai": 1937,
        "Zanras": "Fantasy",
    },
    {
        "Autorius": "Harper Lee",
        "Pavadinimas": "To Kill a Mockingbird",
        "leidimo_metai": 1960,
        "Zanras": "Southern Gothic",
    },
    {
        "Autorius": "F. Scott Fitzgerald",
        "Pavadinimas": "The Great Gatsby",
        "leidimo_metai": 1925,
        "Zanras": "Tragedy",
    },
    {
        "Autorius": "Jane Austen",
        "Pavadinimas": "Pride and Prejudice",
        "leidimo_metai": 1813,
        "Zanras": "Romance",
    },
    {
        "Autorius": "Markus Zusak",
        "Pavadinimas": "The Book Thief",
        "leidimo_metai": 2005,
        "Zanras": "Historical Fiction",
    },
    {
        "Autorius": "Leo Tolstoy",
        "Pavadinimas": "War and Peace",
        "leidimo_metai": 1869,
        "Zanras": "Historical Fiction",
    },
    {
        "Autorius": "Dante Alighieri",
        "Pavadinimas": "The Divine Comedy",
        "leidimo_metai": 1320,
        "Zanras": "Epic Poetry",
    },
    {
        "Autorius": "Stephen King",
        "Pavadinimas": "The Shining",
        "leidimo_metai": 1977,
        "Zanras": "Horror",
    },
]

for x in range(len(knygos)):
    print(
        f"{x+1}: Pavadinimas: {knygos[x]["Pavadinimas"]}   Autorius: {knygos[x]["Autorius"]}   Leidimo metai: {knygos[x]["leidimo_metai"]}   Zanras: {knygos[x]["Zanras"]}"
    )
