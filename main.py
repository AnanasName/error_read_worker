def file_reader_work():
    file_name = input()
    result_list = []

    try:
        Fin = open(file_name)
    except OSError:
        print("Указанный файл отсуствует")
        return

    try:
        strokes_count = Fin.readline()
    except Exception:
        print("Ошибка при чтении очередной строки")
        return

    try:
        int_strokes_count = int(strokes_count)
    except ValueError:
        print("Строки в файле должны быть числами")
        return

    for i in range(int_strokes_count):
        try:
            str_digit = Fin.readline()
        except Exception:
            print("Ошибка при чтении очередной строки")
            return

        try:
            int_digit = int(str_digit)
        except ValueError:
            print("Строки в файле должны быть числами")
            return

        result_list.append(int_digit)

    return result_list

file_reader_work()
