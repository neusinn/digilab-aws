# DigiLab - SSSWS (Super Simple Static Web Site)

> Erstelle eine einfache **Statische Web Seite in einem AWS S3 Bocket**

Öffne die Web Site im Browser: <http://www.sssws-1.diglab.admin.ch.s3-website.eu-central-1.amazonaws.com/>

## Was wir tun:
1. Erstellen eines S3 Bucket.
2. Konfiguriere Konfiguriere den S3 Bucket für Static Web Hosting
3. Hinaufladen der HTML Files

## Vorbedingungen
- AWS Account erstellt
- AWS-CLI Command Line Interface installiert und konfiguriert (Keys, Region)

## Einzelne Schritte 
0. Öffne Terminal mit Projekt
`$ cd ~/dev/digilab-aws/sssws/`

1. Erstelle einen S3 Bucket 
`$ aws s3 mb s3://www.sssws-1.diglab.admin.ch`

2. Konfiguriere den S3 Bucket für Static Web Hosting. Enable Index- and Error-File.
`$ aws s3 website s3://www.sssws-1.diglab.admin.ch/ --index-document index.html --error-document error.html`

3. Upload html Files (durch Synchronisation). Konfiguriere Public Read Access für jedes File (oder definiere die policy)
`$ aws s3 sync ./src/ s3://www.sssws-1.diglab.admin.ch/ --acl public-read`

**Done !**

- Öffne die Web Site im Browser: <http://www.sssws-1.diglab.admin.ch.s3-website.eu-central-1.amazonaws.com/>

oder benutze curl
`$ curl curl https://s3.eu-central-1.amazonaws.com/www.sssws-1.diglab.admin.ch/index.html`

- List den Inhalt des S3 Bucket
`$ aws s3 ls www.sssws-1.diglab.admin.ch`







