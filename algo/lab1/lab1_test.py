import unittest
import tempfile
import os

def read_file_from_input(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            return content
    except FileNotFoundError:
        return f"error: '{filename}' file oldsongui!"
    except PermissionError:
        return f"error: '{filename}' permission error!"
    except Exception as e:
        return f"todorhoigui aldaa: {e}"


class TestReadFile(unittest.TestCase):
    def test_file_read_success(self):
        with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as tmp:
            tmp.write("Hello World")
            tmp_name = tmp.name

        result = read_file_from_input(tmp_name)
        self.assertEqual("Hello World", result)

        os.remove(tmp_name) 

    def test_file_not_found(self):
        result = read_file_from_input("fake.txt")
        self.assertEqual("error: 'fake.txt' file oldsongui!", result)

if __name__ == "__main__":
    unittest.main()
