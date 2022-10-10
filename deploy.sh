docker build -t diabetes-ml-build .
docker run -d -p 80:80 --name diabetes-api diabetes-ml-build