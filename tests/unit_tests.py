import unittest
import tempfile
import os
import count_sirens

class TestAnalyzeSirens(unittest.TestCase):
    def test_count_sirens(self):
        sirens_content = ['000000000', 
                          '000000000', 
                          '111111111', 
                          '111111111', 
                          '111111111', 
                          '222222222']

        # Création d'un fichier temporaire
        with tempfile.NamedTemporaryFile(delete=False, mode='w+t') as temp_file:
            # Écriture des numéros dans le fichier temporaire
            for siren in sirens_content:
                temp_file.write(f"{siren}\n")
        
            # Obtention du nom du fichier temporaire
            temp_file_name = temp_file.name
        
        try:
            count_at_least_twice, count_once = count_sirens.count_sirens(temp_file_name)
            self.assertEqual(count_at_least_twice, 2)
            self.assertEqual(count_once, 1)

        finally:
            os.remove(temp_file_name)

if __name__ == '__main__':
    unittest.main()
