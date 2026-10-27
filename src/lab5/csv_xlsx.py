import csv
from pathlib import Path
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)
    if (csv_file.exists()): raise FileNotFoundError('Пустой файл')
    if csv_file.suffix != '.csv': raise ValueError('Неверный тип файла')
    if xlsx_file.suffix != '.xlsx': raise ValueError('Неверный тип файла')

    with open(csv_file, 'r', newline = '', encoding = 'utf-8') as file:
        file_reader = list(csv.reader(file))

    wb = Workbook()
    ws = wb.active
    ws.title = 'Sheet1'
    for row in file_reader:
        ws.append(row)
    for column in ws.columns:
        mx = 0
        lt = column[0].column_letter
        for item in column:
            if not(item.value) is None and len(str(item.value)) > mx: mx =  len(str(item.value))
        ws.column_dimensions[lt].width = max(mx, 8)
    wb.save(xlsx_file)

if __name__ == '__main__':
    csv_to_xlsx('data/lab05/samples/cities.csv', 'data/lab05/out/cities.xlsx')