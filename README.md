# python-with-flask--Manual Process

# Pre-Requisites
    Install python
    Install pip
    Install Virtualenv
# Install python and pip
    yum install python-pip -y
# Install Virtualenv
    pip install virtualenv
# Create virtual environment for application
    virtualenv helloworld
# Activate virtual environment
  Windows machine
  
    source helloworld/Scripts/activate
  
  Linux Machine
    
    source helloworld/bin/activate
# Run requirements for flask applicaiton using below command
    pip install -r requirements.txt
# Run application
    python application.py


# With Docker file:

# clone this module into your machine
    git clone https://github.com/logambigaik/python-mongodb.git
   
# Install docker 
    yum install -y docker

# Start the service 
    service start docker
    
# pull mongo:latest image

    docker pull mongo:latest

# Check Dockerfile for python application and requirements.txt
  
  (Ref app.py for html template and application.py for json)
  
# Check docker-compose.yml(for volume and dockerfile location)

# install docker-compose:
  
    sudo curl -L "https://github.com/docker/compose/releases/download/1.27.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    
    sudo chmod +x /usr/local/bin/docker-compose
    
             [root@ip-172-31-18-154 ~]# echo $PATH
    
              /usr/local/sbin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin
    
    ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
    
    docker-compose --version

    If not worked try,
    ==============
    
    yum install -y python3-pip
    
    pip3 install docker-compose   
    
    ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
    
    docker-compose --version

# Build the docker-compose:

    docker-compose build   

#Run the container :

    docker-compose up

    or docker-compose up -d
    
    and push the image docker-compose push
    
#  After execution :
    
 ![image](https://user-images.githubusercontent.com/54719289/105493795-dd962880-5cdf-11eb-9aa9-90d96b2c0bd8.png)
    
 ![image](https://user-images.githubusercontent.com/54719289/105493856-f272bc00-5cdf-11eb-8d7b-794dc46ce0f7.png)
   
 ![image](https://user-images.githubusercontent.com/54719289/105493926-08807c80-5ce0-11eb-98dc-5928eab485e5.png)



# To remove the container:

    docker-compose down
    
 # With docker run:

    docker run --name mongodb -p 27017:27017 -d mongo:latest
    
    docker run --name p1 --link mongodb:mongodb -p 5000:5000 python-mongodb_web:latest

[root@ip-172-31-15-216 python-mongodb]# docker ps

CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS              PORTS                      NAMES

d956fa5a935b        python-mongodb_web:latest   "python app.py"          2 minutes ago       Up 2 minutes        0.0.0.0:5000->5000/tcp     p1

e86f0685cfc1        mongo:latest                "docker-entrypoint.s…"   3 minutes ago       Up 3 minutes        0.0.0.0:27017->27017/tcp   mongodb


![image](https://user-images.githubusercontent.com/54719289/105494367-ae33eb80-5ce0-11eb-9ce9-05bdababe48a.png)


# After run:

![image](https://user-images.githubusercontent.com/54719289/105495045-acb6f300-5ce1-11eb-8b1f-e050816f2bb5.png)


# Docker stack:

docker stack deploy --compose-file docker-compose.yml pymongo


![image](https://user-images.githubusercontent.com/54719289/106039631-57268000-60ff-11eb-9f0b-05e56b966b4e.png)

# Adding Node:

![image](https://user-images.githubusercontent.com/54719289/106039735-7c1af300-60ff-11eb-9bdb-1b2a3c851251.png)

# Services running in master:

![image](https://user-images.githubusercontent.com/54719289/106039814-9654d100-60ff-11eb-9897-0edc6f30b7dc.png)

![image](https://user-images.githubusercontent.com/54719289/106040157-0ebb9200-6100-11eb-90c1-34e017a2354e.png)

# Services runnng in slave:

![image](https://user-images.githubusercontent.com/54719289/106039907-b8e6ea00-60ff-11eb-8553-8a99f65c5502.png)

![image](https://user-images.githubusercontent.com/54719289/106040042-e6339800-60ff-11eb-8807-827d03c49060.png)


# Default docker network:

![image](https://user-images.githubusercontent.com/54719289/106040262-327ed800-6100-11eb-8a50-f9df371c19e7.png)


# Changing network to this application:

        For creating network :
        
            docker network create pymongo-bridge --driver=bridge
            
            docker network create pymongo-overlay --driver=overlay
            
![image](https://user-images.githubusercontent.com/54719289/106157395-ad9bc900-61a8-11eb-8d50-1e1287c0b598.png)

            
            
# Docker compose with network:


![image](https://user-images.githubusercontent.com/54719289/106156975-3108ea80-61a8-11eb-97f2-bbb46ebdd527.png)


![image](https://user-images.githubusercontent.com/54719289/106157337-9eb51680-61a8-11eb-9537-8f387baf2d4e.png)


# Docker ps after compose up:

![image](https://user-images.githubusercontent.com/54719289/106157531-d15f0f00-61a8-11eb-9d73-74fffc1efea7.png)
 

![image](https://user-images.githubusercontent.com/54719289/106157660-f05da100-61a8-11eb-8fac-790015b256a5.png)


# Adding node:

    docker swarm join-token worker  -> in master and run the belwo token in node
    
       docker swarm join --token SWMTKN-1-0cyoevf5au6nym9047gxr42bzxghps7bdauu2egys3ehvj1z42-4pn23d0n58vebflofbqezxxwt 172.31.32.71:2377


![image](https://user-images.githubusercontent.com/54719289/106158557-dec8c900-61a9-11eb-9674-71fd4469478e.png)


# Docker stack with bridge network:

      docker-compose push
 
  REMOVED NETWORK NAME IN DOCKERSTACK-COMPOSE.YML 
  
![image](https://user-images.githubusercontent.com/54719289/106160443-d5d8f700-61ab-11eb-9aa3-c4b094a7a430.png)


![image](https://user-images.githubusercontent.com/54719289/106160985-70393a80-61ac-11eb-833d-97a5341fc926.png)


# After updating network as overlay:

![image](https://user-images.githubusercontent.com/54719289/106161168-a7a7e700-61ac-11eb-94b6-b358c89c90ad.png)

![image](https://user-images.githubusercontent.com/54719289/106161293-cd34f080-61ac-11eb-94bc-82174616ed27.png)

    master:
    
![image](https://user-images.githubusercontent.com/54719289/106161918-898eb680-61ad-11eb-96f8-46ab1de58b39.png)


  node:
  
![image](https://user-images.githubusercontent.com/54719289/106162039-a88d4880-61ad-11eb-85e7-6005ec9d38ce.png)



### For monitoring:


https://docs.docker.com/config/daemon/prometheus/

```
docker service create --replicas 1 --name my-prometheus \
    --mount type=bind,source=/tmp/prometheus.yaml,destination=/etc/prometheus/prometheus.yml \
    --publish published=9090,target=9090,protocol=tcp \
    prom/prometheus
    
```

# /etc/docker/daemon.json
```
{
  "metrics-addr" : "3.143.242.136:8000",
  "experimental" : true
}

```

# cat /tmp/prometheus.yaml

```
# my global config
global:
  scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

  # Attach these labels to any time series or alerts when communicating with
  # external systems (federation, remote storage, Alertmanager).
  external_labels:
      monitor: 'codelab-monitor'

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.

rule_files:
  # - "first.rules"
  # - "second.rules"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
      - targets: ['3.143.242.136:9090']

  - job_name: 'docker'
         # metrics_path defaults to '/metrics'
         # scheme defaults to 'http'.
    metrics_path: /prometheus
    static_configs:
      - targets: ['3.143.242.136:8000']

```

 ```
 docker service create --replicas 1 --name my-prometheus \
    --mount type=bind,source=/tmp/prometheus.yaml,destination=/etc/prometheus/prometheus.yml \
    --publish published=9090,target=9090,protocol=tcp \
    prom/prometheus
 ```
 
