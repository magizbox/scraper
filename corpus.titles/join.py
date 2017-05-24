from os.path import dirname, join


def join(file_names, output_file):
    with open(output_file, 'w') as outfile:
        for file_name in file_names:
            with open(file_name) as infile:
                for line in infile:
                    outfile.write(line)


if __name__ == '__main__':
    data_folder = join(dirname(__file__), "data")
    file_names = listdir(data_folder)
    file_names = [join(data_folder, f) for f in file_names]
    output_file = "corpus-title-merge.txt"
    join(file_names, output_file)
