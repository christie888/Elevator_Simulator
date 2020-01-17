run: build
	docker run -it --rm -p 5000:5000 elevator
build:
	docker build -t elevator .
.PHONY: run build
