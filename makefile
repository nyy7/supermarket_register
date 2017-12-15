build:
	docker build . -t register_img

test: build
	docker rm -f regc || true
	docker run -d --name regc -t register_img
	docker exec regc /usr/local/supermarket_register/tests/testsuit

run: build
	docker rm -f regc || true
	docker run -d --name regc -t register_img
	
run-example: build
	docker rm -f regc || true
	docker run -d --name regc -t register_img
	docker exec -e SKU='A12T-4GH7-QPL9-3N4M' regc supermarket_register

