run: build
	docker run -it --rm -p 5000:5000 elevator
build:
	docker build -t elevator .
req:
	curl -X POST -H "Content-Type: application/json" \
		-d '{"departure":-2, "destination":3}' \
		localhost:5000/destination
current:
	curl localhost:5000

.PHONY: run build req
