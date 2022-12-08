---
description: An introduction to Jupyter Notebooks
---

# Jupyter Notebooks 101

### What are Jupyter Notebooks?

Jupyter Notebook is a document that helps with creating and sharing computational documents. You can imagine a Jupyter Notebook like a Google Doc or a Microsoft word; the difference is it has a different file extension (.ipynb) and the code executed in a REPL (Read-Eval-Print-Loop) fashion. \


[Jupyter Notebook](https://jupyter.org/) is an open source project. Many organizations and universities use it for data science, data discovery, and visualization workflows. It is the most popular data science interface.&#x20;

### How does a Jupyter Notebook work?

Jupyter Notebooks are built on the IPython kernel, famous for its REPL (Read-Eval-Print-Loop) capabilities. IPython is a command line terminal through which we can interactively execute python commands.&#x20;



Jupyter Notebooks contain cells that contain atomic commands, which get executed to get the result from a programming environment, for example, from a server where your app is running or an API from a third-party system.&#x20;



<figure><img src="https://lh4.googleusercontent.com/Gt2ihOSdixEcyJ-DDM4v7DLnc_OURwe31fhv2NMdegQ3GR2x7imezJdahX6IHY0fZYDWggVXyD1GP-IdiMDChzOgzkdLO7HcJitMEzFLpnPPkiOBpOw29gKvEg2cgWZZVb5rzDvRugdPIfEgESZsCe4GvKMxFVWVxJZqCWTKGMGR8SMZbJCkpa5D89EVfA" alt="screenshot of a Jupyter task"><figcaption></figcaption></figure>

\


Like in any other text document, you can add text content (in Markdown format!)

<figure><img src="https://lh5.googleusercontent.com/d4YbDW7r3-XT2jV-GVcIUy1Y7cvcQNu3PCGSPlVVKGIYdPLnuzb4oC1HhJag78KV7yABUxLTUposmJtOMvLPUv8oSQgQY7kT-AQMnqrgecMca5PAmHgVWWx88tpbnwNEwHqK-DT56mFoRIt-XTva67CdUXOx6-IobFFKHZjtRqMzlaaElaE_LMfmcFQeMQ" alt="markdown in a Jupyter Note"><figcaption></figcaption></figure>

### What help do they do in runbook automation?

\


The cloud community and the DevOps/SRE groups increasingly interact with complex systems. Also, DevOps/SRE groups mainly write bash/Perl scripts to automate their workflows, aka Runbooks.&#x20;

\


By applying the Jupyter Notebook concept to automate the infrastructure workflows simplifies the task of a DevOps/SRE. It also aids in decoupling and debugging various systems quickly.&#x20;

\


PS: Unskript uses Jupyter Notebook under the hood. You could build or consume some knowledge shared by many engineers at the [awesome-cloud-ops](https://github.com/unskript/Awesome-CloudOps-Automation) repo and run it via the [Docker container](https://hub.docker.com/unskript).&#x20;

### Crash Course with Jupyter Notebook

#### Installation

There are many ways to install and run Jupyter Notebooks. Over the years, cloud platforms and several new-age startups have implemented Jupyter Notebooks - [Google Collab](https://colab.research.google.com/), [Deepnote](https://deepnote.com/), and [Naas.ai](https://www.naas.ai/).

\


I’m using the Anaconda Distribution of Jupyter Notebook. Search for “anaconda download”; the first link you find is probably from Anaconda.com, which distributes the Jupyter Notebooks and several other products like Anaconda Server.&#x20;



1. Download and Install the [Anaconda Opensource Distribution](https://www.anaconda.com/products/distribution); it fits our use case to build and run a basic Jupyter Notebook.
2. Open the Anaconda Navigator

<figure><img src="https://lh4.googleusercontent.com/nVRzwswxRYE8TH9HvQBaB1HdX3QsDfkiu2DZ8oCOt3aNyEz3KYaVfqulMEIVVCZ7-rwSiLWRCaIB63PKaZkJV0Fps-Ueru9m2UGXXcnJRYEq1GICUyZ0jGYO1OlDdTrAgla5CgQuGovcAmlcluRwqcYAVGcoEi6K4Sdnkt_zRiR6bsve13v65erfY5pqhQ" alt="screenshot of Anaconda manager"><figcaption></figcaption></figure>

\


1. Launch Jupyter Notebook! (make you are not launching JupyterLab)
2. A browser tab would be launched at [http://localhost:8889/tree](http://localhost:8889/tree)

<figure><img src="https://lh6.googleusercontent.com/Fw-sdJmJJRLMzp1xtRfhtw4APR_5s7yVmA1DiBqp0YVTGxBIbaSDXYZiFrlpCq1KwVcWo3Prfa7al0k0YTEZ98wHJNtof3E81YHFDrIyOJvposEDk_5iNW7AWWnK7kBVuHP325UcSvV0TutUlokduvLT0UDXxi0DMlg8yAwrUEJBbe1hWs2tFXOWGrJEog" alt="Jupyter screen shot"><figcaption></figcaption></figure>

&#x20;

#### Building a notebook

\


Next up, hit New -> Python 3 (ipykernel)&#x20;

#### ![creating a new notebook](https://lh4.googleusercontent.com/wijailL-HndyR2STYWJ2mPOQaHzhQFz2t0JFHZL6wXPX1EjwJ6fECLkYlrfIg-T-3hm7Cg103tCKUQfODuuuvg8iQVeSN\_uhJqlFS101PqkE7iHQwo\_G4TWD3bSInXb07jui\_cUY0upcsGh-B8lllFA9JBiGNqaJS8KnYX05IVq\_\_BPW7W89fio-SW0ZKw)

Each Jupyter notebook contains multiple cells, which contain Python code. Python code in each cell gets executed when you run the cell. Cells can also be configured for text so that you can input instructions and guidance needed for the following code snippet. (markdown!).

\


<figure><img src="https://lh3.googleusercontent.com/Juz4LOeEIOP-noFA7qwa82e0ffIw02s-PSxC2XH-2kWZin8MwOJ7sxnXCJ3jWWpJDRxyQFfbEkLlah6gySbNca5VsK-V8ZiwYQ95IYuKX0KPjkiZH-3jNXwgIHmNf9WzKweHcfeAjtkeBp20rbmLzXXG7o7Wpxj1oB2FfqFUyfut5IwcuuB64ZLxVgJXdw" alt="cell menu showing configuration options"><figcaption></figcaption></figure>

\
\


Please note each cell carries the programming context from the above cells.

#### Running it!&#x20;



A notebook (containing multiple cells) can be run in one go by using Cell -> Run Cells (as shown in the image above).\


Alternatively, if you are a command line fan, you can use the below command to run a specific notebook.&#x20;



\> jupyter notebook notebook.ipynb



### unSkript and Jupyter Notebooks



As discussed above, unSkript uses opensource Jupyter Notebooks under the hood and provides a seamless way of debugging/triggering complex infrastructure scripts.&#x20;

\


unSkript has many open-source runbooks (aka notebooks) at the [awesome-cloud-ops](https://github.com/unskript/Awesome-CloudOps-Automation) GitHub repository. So give us a [star](https://github.com/unskript/Awesome-CloudOps-Automation) and raise an issue if you feel we are missing something. &#x20;



### Resources

Few more resources on getting started to understand Jupyter Notebooks:\


* [Jupyter Notebook Docs](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)
* [How to use Jupyter Notebooks?](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
* [A detailed guide on Jupyter Notebooks](https://realpython.com/jupyter-notebook-introduction/)
* [The definitive guide on Jupyter Notebooks](https://www.datacamp.com/tutorial/tutorial-jupyter-notebook)
* [\[Video\] Jupyter Notebook Tutorial for Python](https://www.youtube.com/watch?v=2WL-XTl2QYI)
