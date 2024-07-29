Vérifier que python est bien installé :
```bash
python --version
```
Sinon, par exemple :
```bash
sudo apt update
sudo apt install python3
```

Pour cloner le réperoire :
```bash
git clone https://github.com/yazidsaiad/D-doublonnage-de-SIRENs.git
cd siren_analyzer
```

Pour générer les statistiques du fichier sirens_fxt.txt et effectuer le test unitaire:
```bash
python count_sirens.py
python tests/unit_tests.py
```

