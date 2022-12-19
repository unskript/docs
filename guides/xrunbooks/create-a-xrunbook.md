# Create a xRunBook

To create a xRunBook, please follow these instructions:



{% tabs %}
{% tab title="Open Source" %}
### Copy an existing template xRunBook:



In order to create a xRunBook in the open source Docker container, you can copy an existing template.

1. Clone the repository to your local computer: `git clone https://github.com/unskript/Awesome-CloudOps-Automation`
2. Navigate to the repository directory: `cd Awesome-CloudOps-Automation`
3. `Create your xRunBook:`
   1. `` CONTAINER=`docker ps -l | grep awesome-runbooks | awk '{print $1}'` ``
   2. `docker cp templates/runbooks/GCP.ipynb $CONTAINER:/home/jovyan/runbooks/`\<YOUR\_RUNBOOK\_NAME.ipynb>
4. Point your browser to `http://127.0.0.1:8888/lab/tree/<YOUR_RUNBOOK_NAME.ipynb>` to begin editing.



### Save an existing Jupyter Notebook

If you have an existing Jupyter Notebook:

1. Save your Notebook into `~/.unskript/runbooks.`
2. Restart your Docker instance.
3. Navigate to `http://127.0.0.1:8888:8888/lab/tree/<yourFileName>.ipynb`
{% endtab %}

{% tab title="Cloud" %}
1. Click xRunBooks from the top navigation.
2. Click the `+ Create` button to create your xRunBook.
3. Add the name, description and the proxy, and click `CREATE XRUNBOOK.`
{% endtab %}
{% endtabs %}
