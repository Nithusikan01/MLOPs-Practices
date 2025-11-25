# A Demo for How to Use Docker?

## Create Virutal Environment & Install Dependencies

```Bash
conda create -n test python=3.11 -y

conda activate test

pip install -r requirements.txt
```

## Docker Test

```Bash
docker pull hello-world

docker run hello-world
```

## Common Docker Commands
```Docker
# Display list of running containers
docker ps

# Display list of all containers (Running and Not Running)
docker ps -a

# Remove a container from this machine
docker rm <HASH>

# Remove all container from this machine
docker rm $(docker ps -a -q)

# Display all images
docker images -a

# Remove an image from the machine
docker rmi <IMAGE_NAME>

# Remove all image from the machine
docker rmi $(docker images -q)
```

## Create a Custom Docker Image

```Docker
# Build a docker image(Tags: versions(1.0/1.2/2.0) / latest)
docker build -t <DOCKERGUB_USR_NAME>/<APP_NAME>:TAG

# Run a docker image
docker run -p <HOST_PORT>:<CONTAINER_PORT> <DOCKERGUB_USR_NAME>/<APP_NAME>:TAG

# Persist running even after the terminal is closed(Detach Mode)
docker run -d -p <HOST_PORT>:<CONTAINER_PORT> <DOCKERGUB_USR_NAME>/<APP_NAME>:TAG
```

## Pushing an Image to DockerHub

```Docker
docker login
docker push <DOCKERGUB_USR_NAME>/<APP_NAME>:TAG