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
  
    sudo curl -L "https://github.com/docker/compose/releases/download/1.28.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    
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

#  After execution :
    
 ![image](https://user-images.githubusercontent.com/54719289/105493795-dd962880-5cdf-11eb-9aa9-90d96b2c0bd8.png)
    
 ![image](https://user-images.githubusercontent.com/54719289/105493856-f272bc00-5cdf-11eb-8d7b-794dc46ce0f7.png)
   
 ![image](https://user-images.githubusercontent.com/54719289/105493926-08807c80-5ce0-11eb-98dc-5928eab485e5.png)



# To remove the container:

    docker-compose down
    
 #With docker run:

    docker run --name mongodb -p 27017:27017 -d mongo:latest
    
    docker run --name p1 --link mongodb:mongodb -p 5000:5000 python-mongodb_web:latest

[root@ip-172-31-15-216 python-mongodb]# docker ps

CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS              PORTS                      NAMES

d956fa5a935b        python-mongodb_web:latest   "python app.py"          2 minutes ago       Up 2 minutes        0.0.0.0:5000->5000/tcp     p1

e86f0685cfc1        mongo:latest                "docker-entrypoint.s…"   3 minutes ago       Up 3 minutes        0.0.0.0:27017->27017/tcp   mongodb


![image](https://user-images.githubusercontent.com/54719289/105494367-ae33eb80-5ce0-11eb-9ce9-05bdababe48a.png)





 
