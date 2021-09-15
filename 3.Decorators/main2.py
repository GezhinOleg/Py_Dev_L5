import hashlib
import logger

@logger.loggertofile('log_file2.txt')
def md5gen(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            yield hashlib.md5(line.strip().encode('utf-8')).hexdigest()


if __name__ == '__main__':
    for md5 in md5gen('output.txt'):
        print(md5)
