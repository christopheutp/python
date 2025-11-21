# Demo Evironnement Tkinter et SQL Alchemy

##  Créer et activer un environnement virtuel

### Windows (PowerShell)

```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
```

### macOS / Linux (bash/zsh)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Installer les dépendances dans l’environnement virtuel

```bash
pip install -r requirements.txt
```

## Lancer l’application

Depuis le dossier racine du projet (environnement virtuel activé) :

```bash
python -m app.main
```

Sous certains systèmes :

```bash
python3 -m app.main
```
