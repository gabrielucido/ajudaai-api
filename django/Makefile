.PHONY: tests codequality test

help:
	@echo "======= BDD Executor ======="
	@echo "Use \`make x' where x is one of"
	@echo "tests --> Run all Codequality and Test tools"
	@echo "codequality --> Run Codequality tools"
	@echo "test --> Run test."

tests:
	prospector .
	bandit -r .
	echo "Running tests..."

codequality:
	echo "Running codequality..."
	prospector .
	bandit -r .

test:
	echo "Running test..."
