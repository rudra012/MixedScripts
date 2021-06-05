.PHONY: clean run

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.coverage' -delete
	find . -type f -name '*coverage.xml' -delete
	find . -type f -name "*.log" -delete
	find . -type d -name __pycache__ -delete

run:
	python tkinter_scripts/calculator.py
