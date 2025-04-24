import json
import os
from datetime import datetime

# Файл для хранения заметок
NOTES_FILE = 'notes.json'

# Функция для загрузки заметок из файла
def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, 'r') as file:
        return json.load(file)

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file, indent=4)

# Функция для создания новой заметки
def create_note():
    notes = load_notes()
    note_id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    note = {
        'id': note_id,
        'title': title,
        'body': body,
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка создана.")

# Функция для просмотра всех заметок
def view_notes():
    notes = load_notes()
    if not notes:
        print("Нет сохраненных заметок.")
        return
    print("\nСписок заметок:")
    for note in notes:
        print(f"{note['id']}. {note['title']} (Создано: {note['created_at']})")

# Функция для редактирования заметки
def edit_note():
    notes = load_notes()
    view_notes()
    note_id = int(input("Введите номер заметки для редактирования: "))
    note = next((n for n in notes if n['id'] == note_id), None)
    if note:
        note['title'] = input("Введите новый заголовок заметки: ")
        note['body'] = input("Введите новый текст заметки: ")
        note['updated_at'] = datetime.now().isoformat()
        save_notes(notes)
        print("Заметка обновлена.")
    else:
        print("Заметка не найдена.")

# Функция для удаления заметки
def delete_note():
    notes = load_notes()
    view_notes()
    note_id = int(input("Введите номер заметки для удаления: "))
    notes = [n for n in notes if n['id'] != note_id]
    save_notes(notes)
    print("Заметка удалена.")

# Основная функция программы
def main():
    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")
        choice = input("Выберите действие (1-5): ")
        if choice == "1":
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
