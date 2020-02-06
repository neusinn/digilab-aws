# Elastic Computing with Dockerized Application (ECDA)

## Vorbedingungen
- AWS Account erstellt
- AWS-CLI Command Line Interface installiert und konfiguriert (Keys, Region)
- Vordefinieren einer Security Group

## Was wir tun:
1. Erstellen einer EC2 (Elastic Computing) Linux Instanz
2. Konfiguriere für Administration (SSH) und Webserver (HTTP, HTTPS)
3. Einloggen mit Terminal über SSH und Public IP
4. Docker installieren
5. Source Code laden
6. Docker image mit Web-Server und Web-Applikation bauen
7. Run docker image   

## Einzelne Schritte 
1. Erstellen einer EC2 (Elastic Computing) Linux Instanz
   -  Einloggen AWS Console
   -  Erstellen einer EC2 Linux Server Instanz
      - Ubuntu Server 18.04 LTS (HVM), SSD Volume Type
      - t2.micro, 1 vCPU, 1 GiB
      - KeyPair: mvabit_aws 

2. Konfiguriere Security Groups für Administration (SSH) und Webserver (HTTP, HTTPS)
   - Change Security Groups to "mva-ssh-webserver-https-80-8080"

3. Einloggen mit Terminal über SSH und Public IP. 
(User ist "ubuntu" für Ubuntu oder "ec2-user" für AWS Linux Image.) 
    ```
    ssh -i ~/.ssh/mvabit_aws.pem ubuntu@<PUBLIC-IP>
    ```

4. Docker installieren (Use snap für Ubuntu)
    ```
    sudo snap install docker
    ```
    
    optional: Test Docker    
    ```
    docker --version
    sudo docker info
    sudo docker run hello-world
    ```
   
5. Source Code laden
    ```
    git clone https://github.com/neusinn/docker-2048
    ```
   
6. Docker image mit Web-Server und Web-Applikation bauen
    ```
    cd docker-2048/
    cat docker-2048/Dockerfile
    sudo docker build -t "docker-2048" .
    ```
   
7. Run docker image
    ```
    sudo docker run --name digilab-2048 -d -p 80:80 docker-2048
   ```

---
# Diverses
## Weitere Nützliche Kommandos
```
sudo docker | grep '.*diglab.*'
sudo docker images -a
sudo docker rmi $(sudo docker images -a -q)
scp -i ~/.ssh/mvabit_aws.pem -r ~/dev/bit/docker-2048 ubuntu@<PUBLIC-IP>:~
```

## For AWS Linux image
- Amazon Linux 2 AMI (HVM), SSD Volume Type (t2.micro, 1 vCPU, 1 GiB)
- default user for ssh login: ec2-user`
- Docker installation see Developer Guide [Installing Docker](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html)
       