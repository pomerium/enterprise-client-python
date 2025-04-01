PYTHON:=python3

.PHONY: all
all: test pkg

.PHONY: pkg
pkg:
	@echo "==> $@"
	$(PYTHON) -m build .

.PHONY: update
update:
	@echo "==> $@"
	@scripts/update.sh

.PHONY: test
test:
	@echo "==> $@"
	PYTHONPATH=src/ $(PYTHON) -m unittest discover -s src -v