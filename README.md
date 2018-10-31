# Setup:
## 1) Install Python3

```
brew install python3
```

## 2) Get flask server set up
- Clone repo using Github desktop (have Nathan add you via your github username)
- Enter the virtual environment (so we're all using the same version of Python)
```
source py3/bin/activate
```

- Server setup
```
pip install -r requirements.txt
export FLASK_APP=gradu8.py
flask run
```

## 3) Hack like a mad person

- To exit the virtual environment:
```
deactivate
```
