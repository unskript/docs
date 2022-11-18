# Errors

Each Task returns an error in case it was not successful. This error is set as follows

1. For a simple case, the variable `unskript_task_error` will be set
2. For a task with iteration enabled, the variable `unskript_failed_keys` will provide a dictionary of the keys for which the task failed.&#x20;
3. `unskript_task_error` will always be set and contain the success value of the task that was executed.



