def read_file_from_input():
    filename = input("file name: ")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"error: '{filename}' file oldsongui!")
    except PermissionError:
        print(f"error: '{filename}' permission error!")
    except Exception as e:
        print(f"todorhoigui aldaa: {e}")
read_file_from_input()