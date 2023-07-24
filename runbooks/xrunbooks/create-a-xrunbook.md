# Create a xRunBook

To create a xRunBook, please follow these instructions:



{% tabs %}
{% tab title="Open Source" %}
### Copy an existing template xRunBook:

All custom RunBooks are saved in `$HOME/Awesome-CloudOps-Automation/custom/runbooks.`

1. Copy an existing RunBook into this directory.&#x20;
2. Restart your Docker instance.
3. Navigate to `http://127.0.0.1:8888:8888/lab/tree/<yourFileName>.ipynb`

### Save an existing Jupyter Notebook

If you have an existing Jupyter Notebook:

1. Save your Notebook into `$HOME/Awesome-CloudOps-Automation/custom/runbooks.`
2. Restart your Docker instance.
3. Navigate to `http://127.0.0.1:8888:8888/lab/tree/<yourFileName>.ipynb`
{% endtab %}

{% tab title="Cloud" %}
1. Click xRunBooks from the top navigation.
2. Click the `+ Create` button to create your xRunBook.
3. Add the name, description and the proxy, and click `CREATE XRUNBOOK.`

{% embed url="https://youtu.be/xI8K1GJwkWk" %}
{% endtab %}
{% endtabs %}

Now that you have created the RunBook, we can begin filling in the pieces.

* [Input Parameters](create-a-parameter.md): These are the values that seed the RunBook.  AWS RunBooks may need a Region to operate correctly.  Your K8s RunBook may need a Pod.  Or specify how may days of logs to pull.  These can all be defined programmatically with input parameters.
* [Add An Action](add-an-action.md): Actions are the stepwise programatic steps of a RunBook.  There are hundreds of [prebuilt actions](../../actions/action-list.md) ready to be dropped into your RunBook.  Or [create your own Action](../../actions/create-custom-actions.md)!
* [Schedule](schedules.md): Schedule your RunBook for regular processing.
