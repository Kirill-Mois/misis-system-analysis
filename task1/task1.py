import csv
import sys

def task1(csv_file, row_number, col_number):
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
            if row_number <= len(data) and col_number <= len(data[0]):
                cell_value = data[row_number - 1][col_number - 1]
                return cell_value
            else:
                return "Ошибка: заданные номер строки или столбца выходят за пределы файла CSV."
    except FileNotFoundError:
        return "Ошибка: Файл CSV не найден."

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python script.py <путь_к_csv_файлу> <номер_строки> <номер_столбца>")
    else:
        csv_file = sys.argv[1]
        row_number = int(sys.argv[2])
        col_number = int(sys.argv[3])
        cell_value = task1(csv_file, row_number, col_number)
        print(f"Значение ячейки ({row_number}, {col_number}): {cell_value}")
