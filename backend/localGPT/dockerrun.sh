sudo docker build -t localgpt-web-deploy --target deploy .

sudo docker container rm backend_web

sudo docker compose up
