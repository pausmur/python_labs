import argparse, json, csv
from src.lab5.json_csv import json_to_csv, csv_to_json
from src.lab5.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help = 'Переводит файл из json в csv')
    p1.add_argument("--in", dest="input", required=True, help = 'Файл для чтения')
    p1.add_argument("--out", dest="output", required=True, help = 'Файл для вывода')

    p2 = sub.add_parser("csv2json", help = 'Переводит файл из csv в json')
    p2.add_argument("--in", dest="input", required=True, help = 'Файл для чтения')
    p2.add_argument("--out", dest="output", required=True, help = 'Файл для вывода')

    p3 = sub.add_parser("csv2xlsx", help = 'Переводит файл из csv в xlsx')
    p3.add_argument("--in", dest="input", required=True, help = 'Файл для чтения')
    p3.add_argument("--out", dest="output", required=True, help = 'Файл для вывода')

    args = parser.parse_args()

    try:
        if args.cmd == 'json2csv': json_to_csv(args.input, args.output)
        elif args.cmd == 'csv2json': csv_to_json(args.input, args.output)
        elif args.cmd == 'csv2xlsx': csv_to_xlsx(args.input, args.output)
    except FileNotFoundError as e:
        parser.error(str(e))
    except ValueError as e:
        parser.error(str(e))

if __name__ == '__main__':
    main()