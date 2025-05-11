# rest-api

### 🚀 Technologies

This project was developed with the following technologies:

- Back-End
  - [Python](https://www.python.org/)
  - Pytest
  - flake8
  - Coverage
  - Docker 🐋


### Cloning repository

```bash
git clone https://github.com/Vitorrrocha/rest-api && cd rest-api
```
or with docker
```bash
docker pull vitorrocha1228/rest-api:latest # docker repository

$ docker run -d -p 8000:8000 rest-api:latest
```

### install dependencies
 ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  ```

### run

 ```bash
  cd app
  fastapi dev main.py
  ```

### docs
    {url}/docs
    http://127.0.0.1:8000/docs # for localhost

  Documentation of github api:
  https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28