

1run local docker registry:

docker run -d -p 5000:6000 --name registry registry:2.7


2.build jenkins file with docker with dockerfile(in repo )

docker network create --subnet=192.168.0.0/24 testnet
docker build -t Jenkins-Dockerfile .
docker run --network testnet -d -it -p 8080:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home jenkins

3.configure multibranch pipeline in gui

4. install sonarqube 
sqp_7eefbe1f37b2a61851aabd6a7f57ce9a32f52c2b



