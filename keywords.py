
import csv


def search_and_write_csv(input_file, output_file, column_index, keyword_sets):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        header = next(reader)
        writer.writerow(header)

        for keywords in keyword_sets:
           # writer.writerow(['Keywords:'] + keywords)
           # writer.writerow([''] * len(header))

            infile.seek(0)
            next(reader)
            for row in reader:
                cell = row[column_index].lower() if column_index < len(row) else ''
                if all(keyword.lower() in cell for keyword in keywords):
                    writer.writerow(row)


if __name__ == "__main__":
    input_csv = '/Users/freshs/Downloads/india_2020.csv'

    output_csv = '/Users/freshs/Downloads/india_2020_female.csv'

    column_to_check = 2

    keyword_sets_to_search = [

        ['woman', 'robbed'],
        ['woman', 'beaten'],
        ['woman', 'murder'],
        ['woman', 'killed'],
        ['woman', 'raped'],
        ['woman', 'violent'],
        ['woman', 'violence'],

        ['women', 'violence'],
        ['women', 'murder'],

        ['female', 'burned'],
        ['female', 'robbed'],
        ['female', 'murder'],
        ['female', 'beaten'],
        ['female', 'raped'],
        ['female', 'violence'],
        ['female', 'violent'],
    ]

    search_and_write_csv(input_csv, output_csv, column_to_check, keyword_sets_to_search)

