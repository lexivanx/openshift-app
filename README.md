# Flask App on OpenShift

Flask application designed to be run on OpenShift with various DevOps features including health checks, persistent storage, and disaster recovery.

## Overview

The application is a simple Flask app that returns a "Hello, World!" message. The repository includes unit tests, a Dockerfile for building a Docker image of the application, and configuration files for deploying the application to OpenShift. The configuration files also include settings for health checks, persistent storage, disaster recovery, and a Jenkinsfile to set up a CI/CD pipeline.

## Local Setup

1. Install dependencies: `pip install -r app/requirements.txt`
2. Run the application: `python app/app.py`
3. Run the tests: `python tests/test_app.py`

## Building the Docker image

You can build a Docker image of the application with the Dockerfile provided in the `docker` directory. Use the following command, replacing `<image-name>` with your preferred name for the image:

```
docker build -f docker/Dockerfile -t <image-name> .
```

## OpenShift Deployment

These steps assume that you have access to an OpenShift cluster and have the OpenShift CLI (`oc`) installed.

1. Create a new project: `oc new-project flask-app`
2. Build the Docker image: `oc new-build --name flask-app --binary --strategy docker`
3. Start the build: `oc start-build flask-app --from-dir=. --follow`
4. Deploy the application: `oc new-app flask-app`
5. Expose the application: `oc expose svc/flask-app`

## OpenShift Features

### Health Checks and Probes

Readiness and liveness probes are configured in the `deployment.yaml` file to ensure the application is running smoothly. They monitor the `/healthz` endpoint on port 8080.

### Security Contexts

In OpenShift, Security Context Constraints (SCCs) are used to define the level of security for pods. These constraints control how pods interact with underlying resources in the cluster and what actions they can perform. By default, OpenShift applies the restricted SCC to all projects, which offers a high level of security and restrictions.

Under the `restricted` SCC:

- Pods cannot run as privileged.
- Pods cannot run as root.
- Pods cannot access host features like the host network or host ports.

If your application needs additional permissions, a cluster administrator can assign a different SCC to a service account. This should be done carefully, since granting permissions can have serious implications on the security of your cluster:

```
oc adm policy add-scc-to-user <scc-name> -z <service-account-name> -n <namespace>
```

### Disaster Recovery

Disaster recovery is handled by a backup and restore process configured in the `backup.yaml` file. Backups can be triggered manually or set up to run on a schedule.

### Database Connections

The application connects to a PostgreSQL database. Connection details are stored in the `secret.yaml` file.

### Persistent Storage

The application uses a Persistent Volume Claim (PVC) for storage. The PVC is defined in the `pvc.yaml` file.

### Security

The application is secured with HTTPS, and containers do not run as root. These settings are defined in the `route.yaml` file.

## CI/CD Pipeline

The Jenkinsfile in the root of the repository defines a Jenkins pipeline that builds, tests, and deploys the application.

## Monitoring and Logging

You can use OpenShift's built-in monitoring and logging tools to monitor the application.

To check the logs of a specific pod, you can use the following command:

```
oc logs <pod-name>
```

You can also stream the logs in real-time with:

```
oc logs -f <pod-name>
```

Access these tools through the OpenShift web console for a GUI. Additionally, OpenShift includes a monitoring tool, Prometheus, and a visualization tool, Grafana, for comprehensive metrics about your application and the underlying infrastructure.

To view these metrics:

1. Go to the OpenShift web console.
2. Navigate to "Monitoring" > "Metrics".

## Autoscaling

The application is configured to automatically scale based on CPU usage. This is defined in the `deployment.yaml` file.

