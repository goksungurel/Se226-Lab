# === ArchiveItem.py ===
class ArchiveItem:
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = year

    def __str__(self):
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}"

    def __eq__(self, other):
        return self.uid == other.uid

    def is_recent(self, n):
        return self.year >= (2025 - n)

    

# === Book.py ===
from ArchiveItem import ArchiveItem
class Book(ArchiveItem):
    def __init__(self, uid, title, year, author, pages):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Author: {self.author}, Pages: {self.pages}"

# === Podcast.py ===
from ArchiveItem import ArchiveItem
class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, host, duration):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = duration

    def __str__(self):
        return f"Podcast -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Host: {self.host}, Duration: {self.duration} mins"

# === Article.py ===
from ArchiveItem import ArchiveItem
class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal, doi):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi

    def __str__(self):
        return f"Article -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Journal: {self.journal}, DOI: {self.doi}"


# === main.py ===
from Book import Book
from Article import Article
from Podcast import Podcast

def save_to_file(items, filename):
    with open(filename, 'w') as f:
        for item in items:
            if isinstance(item, Book):
                f.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n")
            elif isinstance(item, Article):
                f.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n")
            elif isinstance(item, Podcast):
                f.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n")

def load_from_file(filename):
    items = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            item_type = parts[0]
            if item_type == 'Book':
                items.append(Book(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
            elif item_type == 'Article':
                items.append(Article(parts[1], parts[2], int(parts[3]), parts[4], parts[5]))
            elif item_type == 'Podcast':
                items.append(Podcast(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
    return items

def main():

    items = [
        Book("B100", "The Pragmatic Programmer", 1999, "Andy Hunt", 352),
        Book("B101", "Introduction to Algorithms", 2022, "Thomas H. Cormen", 1312),

        Article("A200", "Climate Change and AI", 2023, "Science Advances", "10.1234/ccai2023"),
        Article("A201", "Neuroscience Meets Machine Learning", 2021, "BrainTech Journal", "10.9999/mlneuro21"),

        Podcast("P400", "Data Stories", 2024, "Enrico Bertini", 55),
        Podcast("P401", "Women in Tech", 2022, "Lisa Wang", 48)
    ]

    save_to_file(items, "archive.txt")


    loaded_items = load_from_file("archive.txt")

    print("All Items:")
    for item in loaded_items:
        print(item)

    print("\nRecent Items (Last 5 years):")
    for item in loaded_items:
        if item.is_recent(5):
            print(item)

    print("\nArticles with DOI starting with '10.1234':")
    for item in loaded_items:
        if isinstance(item, Article) and item.doi.startswith("10.1234"):
            print(item)

if __name__ == "__main__":
    main()


