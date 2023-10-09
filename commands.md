
### Python
create a virtual environment named
```python3 -m venv .venv```
```source .venv/bin/activate``` OR ```deactivate```

### install 3 deployment package
pip install whitenoise python-dotenv psycopg2-binary


### Update Bin 
```pip install -r requirements.txt```


### Dockerfile
docker build -t very:0.1 .
docker run --rm --name very-app -p 4000:4000 -v /home/rmc3408/django-docker:/app very:0.1

