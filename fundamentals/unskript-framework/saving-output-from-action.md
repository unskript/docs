# Saving output from Action

Users have the ability to save the output from an Action using the output tab in the task configuration.

![](<../../.gitbook/assets/Screen Shot 2022-05-28 at 12.32.02 PM.png>)

In case of a simple execution (no iteration, polling, or start condition), the output name configured in the output tab will be populated with the returned data from the Task. In case the task encounters an error, the variable is not created ie in python the following code snippet will return `False`

`"output_name" in globals()`

For a simple case where the iteration is on list of scalars (str, int, bool) the output variable is a dictionary of the returned values keyed on the iterator. &#x20;



For complex iterator where the iteration is on a complex data type (list, dict, tuple), the output variable is a dictionary keyed on the str representation of the returned value.

`k1 = [1,2]`

`k2 = [3,4]`

`iter_list = [ k1, k2 ]`

then the output has the following keys

`'[1, 2]'`

`'[3, 4]'`

``

For a multi-way iterator where multiple Task inputs are populated from the list, the dictionary is keyed on string representation of individual dict.

&#x20;Eg

`k1 = { "a": 1, "b":2 }`

`k2 = { "a": 3, "b": 4 }`

`iter_list = [ k1, k2 ]`



in this case, the output has the following keys

`{'a': 1, 'b': 2}"`

`"{'a': 3, 'b': 4}"`

If start condition is enabled and does not pass, the `output_name` variable will not be set (same behavior as error defined above).
