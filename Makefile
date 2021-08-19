.PHONY: dev-setup
dev-setup:
	pip install -e ".[dev]"

.PHONY: install-dev
install-dev: dev-setup

.PHONY: tests
tests:
	py.test -vv

.PHONY: test
test: tests  # Alias test -> tests

.PHONY: format
format:
	black django_admin_action tests setup.py

.PHONY: fmt
fmt:: format

.PHONY: build
build:
	python setup.py sdist bdist_wheel
