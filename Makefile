.DEFAULT_GOAL := help

help:
	@echo "    setup                Set up the environment with the required dependencies"
	@echo "    env			create a virtual environment"
	@echo "    export               save the dependencies onto the requirements txt file"
	@echo "    precommit            runs precommit on all files"

setup:
	@echo "Installaling and activating virtual environment"
	python -m pip install -r requirements.txt
	pre-commit install
	@echo "Environment setup complete"
	
env:
	@echo "Activating virtual environment"
	python -m venv env
# source env/bin/activate

precommit:
	@echo "Running precommit on all files"
	pre-commit run --all-files

export:
	@echo "Exporting dependencies to requirements file"
	python -m pip freeze > requirements.txt

backup: # To push to Github without running precommit
	git commit --no-verify -m backup
	git push origin 
