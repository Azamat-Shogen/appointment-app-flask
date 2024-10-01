## NOTES
To run the script must set the PYTHONPATH to project root
```commandline
export PYTHONPATH=<path>/<to>/appointment-app-flask
```
On windows
```commandline
set PYTHONPATH=<path>/<to>/appointment-app-flask
```

# appointment-app-flask
A web app to book appointments. Class project. 

Build image:
```commandline
docker build -t flask-app-image .
```
Run a container:
```commandline
docker run -d --name flask-app -p 5002:5002 flask-app-image
```
Run a container using the image ID:
```commandline
docker run -d -p 5002:5002 <image_id>
```
Stop a container:
```commandline
docker stop <container_id_or_name>
```
Remove a container:
```commandline
docker rm <container_id_or_name>
```

Remove a container with force flag
```commandline
docker rm -f <container_id_or_name>
```

Interacting with Containers:
* Accessing a container's shell:
```commandline
docker exec -it <container_id_or_name> /bin/sh
```
* Accessing a container using bash:
```commandline
docker exec -it <container_id_or_name> /bin/bash
```

Running on a Remote Server:

We need to ssh to the deployed ip address
ssh root@<ip_address>
password: droplets password

Install docker commands on a remote server

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

Check docker version
docker --version

