---
description: Use our free Cloud sandbox, or install the Open Source Docker Image
---

# Sign Up/Install

To get up and running on your unSkript journey quickly, we've created two options:

1. A local install using the  the open source Docker image.
2. A free sandboxed version of our Cloud product.\


{% tabs %}
{% tab title="Open Source" %}
unSkript is an open source project. We love PRs, stars and more - checkout our [GitHub](https://github.com/unskript/Awesome-CloudOps-Automation). &#x20;

[![image-text](https://img.shields.io/github/stars/unskript/Awesome-CloudOps-Automation?style=social)](https://github.com/unskript/Awesome-CloudOps-Automation)

###

### Docker:

{% embed url="https://youtu.be/QT0sghAo_t0" %}

The fastest way to get the open source version of unSkript running is via our Docker container.

With Docker, you can get up and running in two steps (and just one if you already have Docker up and running!)

1.  Clone out GitHub Repository (In this case we are installing in $HOME.)

    ```
    cd $HOME
    git clone https://github.com/unskript/Awesome-CloudOps-Automation 
    cd Awesome-CloudOps-Automation
    ```
2.  In the terminal, run the following command (if you installed the GitHub in a different location - change line 2 appropriately):\


    ```
    docker run -it -p 8888:8888 \
     -v $HOME/Awesome-CloudOps-Automation/custom:/data \
     -v $HOME/.unskript:/unskript \
     --user root \
     docker.io/unskript/awesome-runbooks:latest
    ```



Your installation will be available to use at: [http://127.0.0.1:8888/doc/workspaces/auto-t/tree/Welcome.ipynb](http://127.0.0.1:8888/doc/workspaces/auto-t/tree/Welcome.ipynb)

### Kubernetes:

Here are the steps to launch the unSkript Docker image in k8s:

* Deploy using the following command (the Yaml file is in our GitHub repository)

```
kubectl apply -f unskript-oss-k8s-deployment.yaml
```

* To access the jupyter server, you will have to enable port-forwarding using

```
kubectl port-forward <pod corresponding to this deployment> -n <k8s namespace> 8888:8888&
```

* You should be able to go to [`http://127.0.0.1:8888/lab/tree/Welcome.ipynb`](http://127.0.0.1:8888/lab/tree/Welcome.ipynb) and access runbooks as explained [`https://github.com/unskript/Awesome-CloudOps-Automation`](https://github.com/unskript/Awesome-CloudOps-Automation)







You can read more about how to configure unSkript on the [GitHub README page](https://github.com/unskript/Awesome-CloudOps-Automation/blob/master/README.md).
{% endtab %}

{% tab title="Sandbox" %}
unSkript offers a free cloud sandbox that can be easily accessed in your browser. &#x20;

1. Visit [unSkript.com](https://unskript.com), and click the signup button at the top right of the page
2. On the sign up  screen, you may either use Google to sign in, or you can use your email address to create an account (this will require email verification).

{% embed url="https://www.youtube.com/watch?list=PLG7TPzTSJYkeOIAOj9iaxCaczKHX_qwZ_&v=QjqAcJEiQNo" %}

Once you have verified your account, you'll be walked through a overview of the platform where you will create a xRunBook in three steps:

1. [**Establish a proxy environment**](create-a-proxy.md) (these are used to store your credentials and xRunBooks). In the cloud demo, you can only have unSkript hosted proxies.
2. [**Connect a Resource/Add Credentials**](add-credentials-to-connect-your-resources.md) We'll connect your environment to a MongoDb database for the demo. &#x20;
3. **Create a xRunBook** This step will walk you through the creation of a xRunBook
   1. First you'll create a xRunBook with a name, optional description and the Proxy you created in the first step.
   2. Next we'll open the editor to begin creating the xRunBook.
   3. xRunBooks are built by combining Actions. In the walkthrough we'll add the `MongoDB Find Document` Action from the installed Actions, by searching for the term, and then dragging the Action into our xRunbook.
   4. Configure your Action.  Each Action can be [configured in many ways](../actions/action-configuration/). We've created a default configuration for this Action, but you'll need to add Credentials to the MongoDB.
   5. Now you are ready to run your first xRunBook.  Click `Run Action` to just run the Action, or you can click the `Run XRunBook` to run the entire RunBook.  A list of movies will be the output.
   6. Now you are ready to create your own xRunBooks!
{% endtab %}
{% endtabs %}







