import threading
from time import sleep
import time


def write_words(word_count, file_name):
    start = time.time()
    with open(file_name, 'w', encoding='utf=8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    end = time.time()
    time_ = end - start
    print(f"Завершилась запись в файл {file_name}")
    print(f"Работа потоков {time_}")


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

thread = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread.join()
thread_2.join()
thread_3.join()
thread_4.join()
