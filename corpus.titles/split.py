from itertools import izip_longest


def grouper(n, iterable, fillvalue=None):
    """Collect data into fixed-length chunks or blocks"""
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)


if __name__ == '__main__':
    chunk_size = 300000  # lines
    input_file = 'corpus-title.txt'
    n = chunk_size
    with open(input_file) as f:
        for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
            with open('corpus-title_{0}.txt'.format(i * n), 'w') as fout:
                fout.writelines(g)
