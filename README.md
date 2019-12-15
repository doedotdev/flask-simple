# flask-simple
Flask Simple Example | Structure + Simplicity

### Run Simple
```
pip install -r requirements.txt
python app.py
```

### Run Docker
```
docker-compose up
```

### Run Tests
```
python -m pytest test/
```

### Run Coverage
```
coverage run --source=src/ -m pytest test/ && coverage report
```

### Run SmokeTest
```
python smoke_test.py
```

### Run Black
```
black --check src/
black src/
```

### Run Pylint
```
pylint src/
```

### Run MyPy
```
mypy src/
```

### Run Flake8
```
flake8 src/
```

### Quality
- Pylint - 10.0/10.0
- Black - 0 Files Changes
- MyPy - Zero Issues
- Flask8 - Zero Issues
- Pytest - Every Logical Files and Method
- Coverage - 100% Code Coverage
- SmokeTest - Every endpoint

