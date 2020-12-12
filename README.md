# Kubernetes Basics using Minikube
This project displays the basic function of minikube using an app and helm chart

## How to use this Project

### Installation
- Install Minikube https://minikube.sigs.k8s.io/docs/start/
- Install helm     https://helm.sh/docs/intro/install/
- Install kubectl  https://kubernetes.io/docs/tasks/tools/install-kubectl/

If minikube is not reaching over internet (try pinging 8.8.8.8) follow this:
```
$ minikube ssh
$ minikube> sudo su
$ minikube> cd /etc
$ minikube> unlink resolv.conf
$ minikube> vi resolv.conf [and enter value for google nameserver: 'nameserver 8.8.8.8']
$ minikube> systemctl restart systemd-resolved

## you should be able to ping google.com now

$ minikube> docker login [and enter your credentials]
```
To be able to access app from outside the cluster, enable ingress

```
$ minikube addons enable ingress
```

Now simply run the helm chart while from root of this project
```
$ helm install python-app --generate-name
```

Run kubectl command to extract the App address
```
$ kubectl get ingress
```

Enter mentioned IP address in your browser and you will see `Hello World`