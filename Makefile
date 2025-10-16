PYTHON:=python3

.PHONY: all
all: generate test pkg

.PHONY: pkg
pkg: install
	@echo "==> $@"
	$(PYTHON) -m pip install build
	$(PYTHON) -m build .

.PHONY: generate
generate: install
	@echo "==> $@"
	@scripts/generate

.PHONY: install
install:
	$(PYTHON) -m pip install .

.PHONY: test
test: install
	@echo "==> $@"
	PYTHONPATH=src/ $(PYTHON) -m unittest discover -s src -v

.PHONY: update-pomerium
update-pomerium:
	@echo "==> $@"
	git submodule update --remote deps/github.com/pomerium
