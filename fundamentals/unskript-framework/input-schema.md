---
description: Input Schema is a blueprint that is defined internally in the Action
---

# Input Schema

`InputSchema` is an internal class that is defined in unSkript Actions. This class is a child  of `pydantic's BaseModel`  This class is not shown as part of the Actions when you drag and drop the it from the Action Search panel.  Every unSkript Action has an InputSchema associated to it. This class defines a `blueprint`  of variables that the corresponding Action is expecting to be called with along with the `Connector` handle.&#x20;

A sample Input Schema is shown below

```
// class InputSchema for Action aws_make_bucket_public
class InputSchema(BaseModel):
    name: str = Field(
        title='Bucket Name',
        description='Name of the bucket.')
    enable_upload: bool = Field(
        title='Enable upload',
        description='Set this to true, if you want the bucket to 
                     be publicly writeable as well. By default, it 
                     is made publicly readable.')

```

In the above example, the action `aws_make_bucket_public` expects two parameters: `Name` and `Enable Upload`  Name is of type `string` and  `Enable upload` of of type `boolean`. So when we call this Action via the Task object, we would call it like this&#x20;

```
// Exceprts from the code block
t = Task(Workflow())
t.configure(inputParamsJson='''
    {
        "name": "some-sample-bucket",
        "enable_upload": true
    }
''')
(err, hdl, args) = t.validate(InputSchema, vars())
if err is None:
    t.output = t.execute(aws_make_bucket_public, hdl, args)
```

1. Task().configure() is used  to set the input parameters that are required for the Action. Note the type of the input parameters, `name` is a `string` and `enable_upload` is a `boolean` variable. &#x20;
2. Task().validate() is used to validate the input parameters against the `InputSchema` (Validating value against the blueprint). The Validate() will returns the Connector Handle (hdl), and Validated Arguments (args) along with error.&#x20;
3. Task().execute() then uses the `hdl` and `args` to call the Action `aws_make_bucket_public.`&#x20;



**Changing the  InputSchema blueprint**

If you would like to change the InputSchema blueprint (Like add a new input parameter or delete an existing one) you can do so by clicking on the `Three Dots` on the Action Panel and selecting `Inputs`.&#x20;

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-27 at 6.40.24 PM.png" alt=""><figcaption><p>Dropdown indicating the Inputs Option</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-27 at 6.48.53 PM.png" alt=""><figcaption><p>Dialog showing how to modify input parameters</p></figcaption></figure>
