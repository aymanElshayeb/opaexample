```markdown
# Deploying Flask Application with OPA using Docker Compose

This repository provides an example of deploying a Flask-based REST service integrated with Open Policy Agent (OPA) using Docker Compose. OPA is used for access control to the REST service.

## Prerequisites

Before deploying the application, make sure you have the following prerequisites:

- [Docker](https://docs.docker.com/get-docker/) installed and configured on your local machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed on your local machine.

## Steps to Deploy

### 1. Clone This Repository

```bash
git clone https://github.com/aymanElshayeb/opaexample.git
```

### 2. Create OPA Policy[optional]

Place your OPA policy files in a directory named `opa-policy` in the root of your project.

### 3. Deploy the Application

Run the following command to start the Flask app and the OPA server:

```bash
docker-compose up -d
```

### 4. Access the Flask Application

You can access the Flask application at http://localhost:80/resource. The access control policy defined in OPA will be enforced.

### 5. Testing

Test your Flask app to ensure that access control is functioning as expected.

### 6. Cleanup

To stop and remove the Docker containers, run:

```bash
docker-compose down
```
