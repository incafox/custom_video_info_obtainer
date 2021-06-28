docker.build.backend:
	docker build -t service_scraper  ./Dockerfile.dev

docker.build.clean.backend:
	docker build --no-cache -t service_scraper -f ./Dockerfile.dev 

app.start:
	docker-compose down && docker-compose up

app.clean.start:
	docker-compose down && docker-compose up --build

app.run.tasks:
	docker-compose run service_scraper rqworker --url redis://redis:6379

#load.test-database:

