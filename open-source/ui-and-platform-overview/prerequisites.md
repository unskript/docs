# Prerequisites

### **Requirements**

<mark style="color:orange;background-color:yellow;">Docker</mark> - [click here](https://docs.docker.com/get-docker/) to download the latest version of Docker. You can check the installation by running `docker --version`

### **Download Docker Image**

To pull the image to start the docker container on your local machine, run the docker command as given below-

#### Intel-based platform (x86 based) (Windows/Linux/Mac)

```bash
docker run -it -p 8888:8888 \\
    -v $HOME/.unskript:/data  \\
    -e NB_USER=jovyan \\
    -e CHOWN_HOME=yes \\
    -e CHOWN_EXTRA_OPTS='-R' \\
    --user root \\
    -w /home/jovyan \\
    public.ecr.aws/unskript/awesome-runbooks:latest
```

#### For macOS M1

```bash
docker run -it -p 8888:8888 \\
    -v $HOME/.unskript:/data  \\
    -e NB_USER=jovyan \\
    -e CHOWN_HOME=yes \\
    -e CHOWN_EXTRA_OPTS='-R' \\
    --user root \\
    -w /home/jovyan \\
   public.ecr.aws/unskript/awesome-runbooks:v0.6.0-arm64
```
