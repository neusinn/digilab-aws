# DigiLab-AWS 

Enthält den Code und die Anleitungen für die Live-Demonstration einfacher AWS Service.

## Vorbedingungen
- AWS Account erstellt
- AWS-CLI Command Line Interface installiert und konfiguriert (Keys, Region)


## Vorbereitung
1. Download Digilab-AWS Repo mit Beispielen und Anleitungen 
`git clone https://github.com/neusinn/digilab-aws`
2. Download Code für Web Game 2048
`git clone https://github.com/neusinn/docker-2048`


## Beispiele
### SSSWS (Super Simple Static Web Site)
- Einfache Statische Web Seite in einem AWS S3 Bocket

### WGSWS (Static Web Site)
- 2048 Web Game als Statische Web Seite in S3 Bucket publiziert.

### ECDA (Elastic Computing with Dockerized Application)
- EC2 Linux Server Instance
- Dockerized Web-Game


## Struktur
```
bit
├── digilab-aws        // AWS Beispiele - Code und Anleitung
│   ├── README.md
│   ├── ecda
│   ├── sssws
│   └── wgsws
└── docker-2048        // 2048-Game Docker 
    ├── 2048
    ├── Dockerfile
    └── README.md
```
