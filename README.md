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

### install dependencies
 ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  ```

### Run

 ```bash
  cd app
  fastapi dev main.py
  ```

### Docs
    {url}/docs
    http://127.0.0.1:8000/docs # for localhost

  Documentation of github api:
  https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28


### Deploy to minikube

  Minikube documentation: https://minikube.sigs.k8s.io/docs/

  #### Install
  ```bash
    curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
    sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
  ```

  #### Start the Cluster
  ```bash
    minikube start
  ```

  
  #### Create docker image
  ##### Before make sure you are in root of the project folder the: /rest-api
  ```bash
    docker build -t rest-api:latest .
  ```

  #### Install kubectl: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

  #### Create the secret
  ```bash
    kubectl create secret generic rest-api-secret --from-env-file=.env --dry-run=client -o yaml | kubectl apply -f -
  ```

  #### Run deploy
  ```bash
    kubectl apply -f k8s/deployment.yaml
  ```
  
#### List the services and get the URL
```bash
    minikube service list
  ```
