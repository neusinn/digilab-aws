# DigiLab-AWS 

Enthält den Code und die Anleitungen für die Live-Demonstration einfacher AWS Services.

- Author: Markus von Allmen  | Twitter: @neusinn
- Source: https://github.com/neusinn/digilab-aws

## Vorbedingungen
- AWS Account vorhanden
- AWS-CLI Command Line Interface installiert und konfiguriert (Keys, Region)


## Vorbereitung
- Download Digilab-AWS Repo mit den Beispielen und Anleitungen 
```
git clone https://github.com/neusinn/digilab-aws
```

- Download Code für Web Game 2048
```
git clone https://github.com/neusinn/docker-2048
```

### Struktur
```
bit
├── digilab-aws        // AWS Beispiele - Code und Anleitung
│   ├── README.md
│   ├── ecda
│   ├── sssws
│   ├── wgsws
│   └── aws-cdk-ex
└── docker-2048        // 2048-Game Dockerized 
    ├── 2048
    ├── Dockerfile
    └── README.md
```

## Beispiele
### SSSWS - Super Simple Static Web Site
- Einfache Statische Web Seite in einem AWS S3 Bocket

### WGSWS - Web Game Static Web Site
- 2048 Web Game als Statische Web Seite in S3 Bucket publiziert.

### ECDA - Elastic Computing with Dockerized Application
- EC2 Linux Server Instance
- Dockerized Web-Game

### AWS-CDK-EX - Infrastructure as Code erstellen mit Cloud Development Kit (CDK)
- Benutzt Cloud9 als Cloud Development Environment 
- Erstellt Infrastruktur mit VPN, Public - und Private-Subnet, Internet Gateway, NAT, ELB 


