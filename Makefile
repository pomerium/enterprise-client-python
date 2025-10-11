PYTHON:=python3

.PHONY: all
all: generate test pkg

.PHONY: pkg
pkg:
	@echo "==> $@"
	$(PYTHON) -m build .

.PHONY: generate
generate:
	@echo "==> $@"
	@scripts/generate

.PHONY: test
test:
	@echo "==> $@"
	PYTHONPATH=src/ $(PYTHON) -m unittest discover -s src -v
