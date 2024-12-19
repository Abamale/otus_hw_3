import csv
import json
from itertools import cycle
from test_data import CSV_FILE_PATH
from test_data import JSON_FILE_PATH
from test_data import OUTPUT_FILE_PATH


# Чтение данных о книгах из books.csv
with open(CSV_FILE_PATH, 'r') as csv_file:
    books = list(csv.DictReader(csv_file))

# Чтение данных о пользователях из users.json
with open(JSON_FILE_PATH, 'r') as json_file:
    users = json.load(json_file)

# Распределение книг между пользователями
books_cycle = cycle(users)  # Циклический итератор для равномерного распределения
for book, user in zip(books, books_cycle):
    user.setdefault('books', []).append({
        "title": book.get("Title", "Unknown Title"),
        "author": book.get("Author", "Unknown Author"),
        "pages": int(book.get("Pages", 0)),
        "genre": book.get("Genre", "Unknown Genre")
    })

# Форматирование результата в формате reference.json
result = [
    {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": user["books"]
    }
    for user in users
]

# Запись результата в файл result.json
with open(OUTPUT_FILE_PATH, 'w') as json_file:
    json.dump(result, json_file, indent=4)