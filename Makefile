PYTHON:=python3

.PHONY: all
all: test pkg

.PHONY: pkg
pkg:
	@echo "==> $@"
	$(PYTHON) -m build .

.PHONY: test
test:
	@echo "==> $@"
	PYTHONPATH=src/ $(PYTHON) -m unittest discover -s src/pomerium -v