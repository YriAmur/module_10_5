from multiprocessing import Pool
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as f_n:
        while True:
            line = f_n.readline()
            if not line:
                break
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]
if __name__ == '__main__':

    start = datetime.now()
    for file in filenames:
        read_info(file)
    end = datetime.now()
    print(f'Линейный вызов: {end - start}')

    start = datetime.now()
    with Pool(4) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(f'Многопроцессный вызов: {end - start}')
