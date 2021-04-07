
### Train the model locally

```console
rasa train --debug
rasa run actions&
rasa shell
```

### Deploy on Rasa X

1. **Prerequisites**

Kubernetes cluster with Helm3 

2. Add secret to pull from Docker Registry:

```console
kubectl create secret docker-registry regcred --docker-server=https://index.docker.io/v2/ --docker-username=<username> --docker-password=<password> 
```

3. **Install Rasa X**

```console
kubectl create namespace rasa
helm repo add rasa-x https://rasahq.github.io/rasa-x-helm
helm --namespace rasa install --values values.yml --version 1.8.0 rasax rasa-x/rasa-x
```

4. Add git repository from the **Rasa X** console, add the provided public key as a Deploy key in te repository.

Note: **Rasa X** default password is `welcome123`

### References 

* [Example](https://github.com/RasaHQ/retail-demo)
* [ITA guide](https://www.qi-lab.it/2019/10/12/sviluppo-un-chatbot-framework-rasa/)
* [Rasa X Deploy](https://medium.com/swlh/build-your-first-a-i-chatbot-in-30-minutes-step-by-step-guide-to-rasa-x-installation-in-windows-10-e94174703472)
* [Spacy Italian language](https://spacy.io/models/it#it_core_news_md)
* [Deploy with Rasa](https://medium.com/front-end-weekly/how-to-build-awesome-rasa-chatbot-for-a-web-ce4a9acafd3b)
* [Guide to Rasa form](https://blog.rasa.com/how-to-build-your-first-rasa-form/)