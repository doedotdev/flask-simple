# flask-simple
Flask Simple Example | Structure + Simplicity

### Run Simple
```
pip install -r requirements/requirements.txt
python app.py
```

### Run Docker
```
docker-compose up
```

### Run Tests
```
pip install -r requirements/requirements_test.txt
python -m pytest test/
```

### Run Coverage
```
pip install -r requirements/requirements_test.txt
coverage run --source=src/ -m pytest test/ && coverage report
```

### Run SmokeTest
```
pip install -r requirements/requirements_test.txt
python smoke_test.py
```

### Run Black
```
pip install -r requirements/requirements_test.txt
black --check src/
black src/
```

### Run Pylint
```
pip install -r requirements/requirements_test.txt
pylint src/
```

### Run MyPy
```
pip install -r requirements/requirements_test.txt
mypy src/
```

### Run Flake8
```
pip install -r requirements/requirements_test.txt
flake8 src/
```

### Github Actions
- black: All files passing
- mypy: all files passing
- pytest: all tests passing in python 3.6, 3.7, 3.8
- covergae: 100% code coverage
- flake8: all files passing with line-length extended
