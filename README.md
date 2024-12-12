### List of TODOS

- [ ] Create a postgres container
- [ ] May be better to use docker-compose

Important Docker commands

build the docker image 
```bash
docker build -t fastapi-app .
```

run the docker image 
```bash
docker run -d -p 8002:8002 fastapi-app
```

list containers
```bash
docker ps -a 
```

stop the container
```bash
docker stop <container_id>
```

start the container
```bash
docker start <container_id>
```

delete a container
```bash
docker rm <container_id>
```

restart a container
```bash
docker restart <container_id>
```

kill the container
```bash
docker kill <container_id>
```

Note: docker run creates a new container every time you run it, docker start starts an existing container

If you have multiple containers better to use docker compose

to build docker-compose service
```bash
docker-compose up -d
```

to stop
```bash
docker-compose down
```
```bash
docker-compose stop
```

to build again after changes 
```bash
docker-compose -d --build
```
