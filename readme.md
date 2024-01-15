

run local docker registry:

docker run -d -p 5000:6000 --name registry registry:2.7


2.build jenkins file with docker with dockerfile(in repo )

docker network create --subnet=192.168.0.0/24 testnet
docker build -t Jenkins-Dockerfile .
docker run --network testnet -d -it -p 8080:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home jenkins

3.configure multibranch pipeline in gui, connect with git and setup periodic scan

4. run sonarqube container
docker run -d --network testnet --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube




