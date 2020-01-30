elevator-terminal: initiate a elevator server

run: build
	docker run -it --rm -p 5000:5000 elevator
build:
	docker build -t elevator .
.PHONY: run build



client-terminal :post request 
curl -X POST -H "Content-Type: application/json" -d '{"departure":-2, "destination":3}' localhost:5000/destination
