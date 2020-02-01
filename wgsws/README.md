# DigiLab WGSWS (Static Web Site)

> 2048 Web Game als komplexe **Statische Web Seite in S3 Bucket** publiziert.

Die Websteite ist dann im Internet über die URL: <http://www.wgsws-1.diglab.admin.ch.s3-website.eu-central-1.amazonaws.com/>
 aufrufbar. Die URl ist wie folgt aufgebaut: http://<S3 BUCKET_NAME>.s3-website.<AWS_REGION>.amazonaws.com

 oder auch über die File URL: <http://s3.eu-central-1.amazonaws.com/www.wgsws.diglab.admin.ch/index.html> Die File URl ist wie folgt aufgebaut: http://s3.<AWS_REGION>.amazonaws.com/<S3 BUCKET_NAME>/<FILE_NAME>

## Was wir tun:
1. Erstellen eines S3 Bucket.
2. Konfiguriere Konfiguriere den S3 Bucket für Static Web Hosting
3. konfiguriere Policy für Zugriff auf S3 Bucket
3. Hinaufladen des Web Games    

## Vorbedingungen
- AWS Account erstellt
- AWS-CLI Command Line Interface installiert und konfiguriert (Keys, Region)
- Code für Web Applikation 2048 vorhanden

## Einzelne Schritte 
0. Öffne Terminal mit Projekt
`$ cd ~/dev/digilab-aws/wgsws`
0.1 Kopiere Source Code für die Web-App im ./src Verzeichnis ist:
`cp ../../docker-2048/2048/* ./out/`

1. Erstelle einen S3 Bucket 
`$ aws s3 mb s3://www.wgsws-1.diglab.admin.ch`

2. Konfiguriere S3 Bucket als Static Web Hosting, enable index and error file 
`$ aws s3 website s3://www.wgsws-1.diglab.admin.ch/ --index-document index.html`

3. Setup Policy as Public Read
`aws s3api put-bucket-policy --bucket www.wgsws-1.diglab.admin.ch --policy file://policy_wgsws-1_s3_public_read.json`

4. Upload html Files (mit Synchronisation vom Verzeichnis `out`). 
`aws s3 sync ./out/ s3://www.wgsws-1.diglab.admin.ch/`

**Done !** 

Öffne die Web Site im Browser
`http://www.wgsws-1.diglab.admin.ch.s3-website.eu-central-1.amazonaws.com/`

Weitere Kommandos
- List Content of Bucket `$ aws s3 ls www.wgsws-1.diglab.admin.ch`
- Teste html mit curl: `$ curl http://s3.eu-central-1.amazonaws.com/www.wgsws-1.diglab.admin.ch/index.html`
- Show S3 bucket `$ aws s3 ls | grep '.*diglab.*'`


# Clean up
`$ aws s3 rb s3://www.wgsws-1.diglab.admin.ch --force`





