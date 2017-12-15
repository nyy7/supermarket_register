build:
	docker-compose build

test: build
	docker-compose up -d
	docker exec regc /usr/local/supermarket_register/tests/testsuit
	docker-compose down

run: build
	docker-compose up -d

run-example: build
	docker-compose up -d
	docker exec -e SKU='A12T-4GH7-QPL9-3N4M' regc supermarket_register
	docker-compose down

