def join(file_names, output_file):
    with open(output_file, 'w') as outfile:
        for file_name in file_names:
            with open(file_name) as infile:
                for line in infile:
                    outfile.write(line)


if __name__ == '__main__':
    file_names = ["corpus-title_300000.txt", "corpus-title_600000.txt", "corpus-title_900000.txt",
                  "corpus-title_1200000.txt", "corpus-title_1500000.txt"]
    output_file = "corpus-title-merge.txt"
    join(file_names, output_file)
