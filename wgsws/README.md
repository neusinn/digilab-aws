# Web Game as Static Web Site (WGSWS)

> 2048 Web Game als komplexe **Statische Web Seite in S3 Bucket** publiziert.

Die Websteite ist dann im Internet über die URL: <http://www.wgsws-1.diglab.admin.ch.s3-website.eu-central-1.amazonaws.com/>
 aufrufbar. Die URl ist wie folgt aufgebaut: http://S3.<BUCKET_NAME>.s3-website.<AWS_REGION>.amazonaws.com

 Alternativ auch über die File URL: <http://s3.eu-central-1.amazonaws.com/www.wgsws-1.diglab.admin.ch/index.html> 
 Die File URl ist wie folgt aufgebaut: http://s3.<AWS_REGION>.amazonaws.com/<S3 BUCKET_NAME>/<FILE_NAME>

## Was wir tun:
1. Erstellen eines S3 Bucket.
2. Konfiguriere Konfiguriere den S3 Bucket für Static Web Hosting
3. konfiguriere Policy für Zugriff auf S3 Bucket
3. Hinaufladen des Web Games    

## Blueprint
[Blueprint für eine Statische Web Seite in einem S3 Bucket](./Blueprint_Ex_S3.png)


## Vorbedingungen
- AWS Account erstellt
- AWS-CLI Command Line Interface installiert und konfiguriert (Keys, Region)
- Code für Web Applikation 2048 vorhanden
`cp ../../docker-2048/2048/* ./out/`

## Einzelne Schritte 
Öffne ein Terminal und navigiere zum Projekt WGSWS: 
`cd ~/dev/bit/digilab-aws/wgsws/`

1. Erstelle einen S3 Bucket 
    ```
    aws s3 mb s3://www.wgsws-1.diglab.admin.ch
    ```

    - Konfiguriere den S3 Bucket für Static Web Hosting. 
    - Enable Index.html and Error.html File.
    ```
    aws s3 website s3://www.wgsws-1.diglab.admin.ch/ --index-document index.html
    ```

2. Setze Policy auf Public Read
    ```
    aws s3api put-bucket-policy --bucket www.wgsws-1.diglab.admin.ch --policy file://policy_wgsws-1_s3_public_read.json
    ```

3. Hochladen der Web-App Files der mittels Synchronisation vom Verzeichnis `out` 
    ```
    aws s3 sync ./out/ s3://www.wgsws-1.diglab.admin.ch/
    ```

**Done !** 

- Öffne die Web Site im Browser
    ```
    http://www.wgsws-1.diglab.admin.ch.s3-website.eu-central-1.amazonaws.com/
    ```       


## Clean up Script
Remove the S3 Bucket and its content
```
./script_wgsws-1_remove.sh
```


---  

##  Publiziere eine Web-App in 5 Sekunden
### Script: script_wgsws-2_create.sh
```
#!/bin/bash
aws s3 mb s3://www.wgsws-2.diglab.admin.ch
aws s3 website s3://www.wgsws-2.diglab.admin.ch/ --index-document index.html
aws s3api put-bucket-policy --bucket www.wgsws-2.diglab.admin.ch --policy file://policy_wgsws-2_s3_public_read.json
aws s3 sync ./2048/ s3://www.wgsws-2.diglab.admin.ch/
```

### Clean-up Script: script_wgsws-2_remove.sh
```
#!/bin/bash
aws s3 rb s3://www.wgsws-2.diglab.admin.ch --force
```
