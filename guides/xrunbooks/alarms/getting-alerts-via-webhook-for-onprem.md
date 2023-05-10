# Getting alerts via webhook for onprem

If you are using cloud based observability applications like Grafana Cloud or Datadog, we need to be able to relay the alert generated to the onprem unSkript url, which is not publicly accessible. To get around this problem, we recommend using [AWS Lambda Function URLs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html).&#x20;

We provide a terraform to create a lambda function URL in the vpc where unSkript is installed. Follow the steps below to deploy the lambda function URL

1. If you need this service, reach out to the team, and we can give you access to the GitHub repository that you'll need.
2. Now to install the lambda, please ensure that you have python 3.8 version, you can create a virtual environment with [conda](https://conda.io/projects/conda/en/latest/commands/install.html) using the following command:\
   `conda create --name python3.8  python=3.8`
3. ```
   cd terraform/lambda/
   ```
4.  Create a **terraform.tfvars** file with the following content:\
    NOTE: the **type** below can be **aws, grafana, prometheus or datadog**\


    ```
    base_url = "<your internal url>/internal/v1alpha1/events/<type>" <<< the suffix internal/v1alpha1/events/<type> needs to be there
    name     = "<name of the lambda>"
    tenant_id = "<reach out to unSkript for tenantID"
    vpc_security_group_ids = ["<list of SGs in the vpc where unskript is hosted"]
    vpc_subnet_ids = ["<list of private subnet ids in the above vpc"]
    role_name  = "<name of the lambda role, which will get created, it doesnt need any AWS access, as its just doing relay"
    ```
5. Run the terraform using `terraform init` followed by `terraform apply`
6. Capture the out put of the terraform, it should output the function url
7.  Take that url and put that in the webhook configuration of your observability application.

    \


    ```
    ```

