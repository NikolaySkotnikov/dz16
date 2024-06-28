import shutil
import threading


def copy_directory(source, destination):
    try:
        shutil.copytree(source, destination)
        print("Директория успешно скопирована.")
    except Exception as e:
        print(f"Ошибка при копировании директории: {e}")


def main():
    source_dir = input("Введите путь к существующей директории: ")
    destination_dir = input("Введите путь к новой директории: ")

    threading_copy = threading.Thread(target=copy_directory, args=(source_dir, destination_dir))

    threading_copy.start()
    threading_copy.join()


if __name__ == '__main__':
    main()
