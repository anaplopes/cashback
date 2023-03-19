
.PHONY: runserver
runserver:
	uvicorn cashback.main:app --reload
