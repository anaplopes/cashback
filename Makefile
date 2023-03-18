
.PHONY: runserver
runserver:
	uvicorn main:app --reload
