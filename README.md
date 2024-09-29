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

build image: docker build -t flask-app .
run container: docker run -p 5002:5002 flask-app
stop container docker stop <container_id_or_name>
remove container: docker rm <container_id_or_name>
docker rm -f <container_id_or_name>

docker exec -it your_container_id /bin/sh
docker exec -it your_container_name /bin/sh
docker exec -it your_container_id /bin/bash
docker exec -it your_contaner_name /bin/bash

to run remoter server:
we need to ssch to the deployed ip address
ssh root@<ip_address>
password: droplets password
