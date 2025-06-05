# Script pour lancer le serveur de développement Django
$ErrorActionPreference = "Stop"

Write-Host "Démarrage du serveur de développement Django..." -ForegroundColor Green

# Vérification de l'existence du dossier staticfiles et media
if (-not (Test-Path "staticfiles")) {
    Write-Host "Création du dossier staticfiles..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path "staticfiles" -Force | Out-Null
}

if (-not (Test-Path "media")) {
    Write-Host "Création du dossier media..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path "media" -Force | Out-Null
}

# Collecte des fichiers statiques
Write-Host "Collecte des fichiers statiques..." -ForegroundColor Yellow
python manage.py collectstatic --noinput

# Application des migrations
Write-Host "Application des migrations..." -ForegroundColor Yellow
python manage.py migrate

# Lancement du serveur
Write-Host "Lancement du serveur sur http://127.0.0.1:8000" -ForegroundColor Green
python manage.py runserver
