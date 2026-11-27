import unittest
import tempfile
from pathlib import Path

class FileCheack(unittest.TestCase):

    def test_file_exist(self):

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir)/'test.txt'
            file_path.touch()

            print(file_path)
            self.assertTrue(file_path.exists())

            with open(file_path,'w') as file:
                file.write('Pokemon : Pikachu,')
                file.write('Pokemon : Charmander,')
                file.write('Pokemon : Mew')

            with open(file_path,'r') as file:
                content = file.read()

                self.assertEqual(content,"Pokemon : Pikachu,Pokemon : Charmander,Pokemon : Mew")

            print(content)

            with self.assertRaises(FileNotFoundError):
                missing_file = Path(temp_dir)/'missing.txt'
                with open(missing_file,'r') as file:
                    cont = file.read()

                print(cont)
if __name__ == '__main__':
    unittest.main()