# AWS

### [Listing of all AWS XRunBooks](../../lists/xRunBook\_list.md#aws)

### [Listing of all AWS Actions](broken-reference)

### Authentication

For the Docker version, we support Access Key based credential.\
In the SAAS version, we accept either the Access Key or Role based authentication:

## Access Key

Adding an AWS Access Key to unSkript. When adding a credential to an Action, a dialogue will open to insert your Access Key details.

<figure><img src="../../.gitbook/assets/Screen Shot 2022-10-02 at 4.32.22 PM.png" alt=""><figcaption></figcaption></figure>

| Name              | Explanation                                   |
| ----------------- | --------------------------------------------- |
| Access Key        | Access key ID                                 |
| Secret Access Key | Secret Access Key for the above Access Key ID |

### **Creating AWS Access Keys**

If you do not have an Access Key or a Secret Access Key, you will need to create this in your [AWS dashboard](https://aws.amazon.com/).

1. Once you are logged in, go to Identity and Access Management (search for IAM in the top search bar)
2. If you do not yet have a Group or User with the permissions for unSkript, create this user, and add the required permissions.&#x20;

<figure><img src="../../.gitbook/assets/Screenshot 2022-11-02 at 11.01.30 AM.png" alt=""><figcaption><p>List of users on the AWS IAM service</p></figcaption></figure>

3\. Click on the user.  This will open a new browser window with a summary of the user. &#x20;

4\. This will open a new window.  Select the "Security credentials" tab in the middle of the screen:

<figure><img src="../../.gitbook/assets/Screenshot 2022-11-02 at 11.12.37 AM (1).jpg" alt=""><figcaption><p>IAM user summary with the security credentials tab selected</p></figcaption></figure>

5\. Click "Create access key" . This will generate your key/secret key. Copy them from the page, and insert them into your unSkript credentials.

<figure><img src="../../.gitbook/assets/Screenshot 2022-11-02 at 11.16.06 AM.jpg" alt=""><figcaption><p>Screenshot of the key creation window</p></figcaption></figure>

## **Assume Role**

<figure><img src="../../.gitbook/assets/Screen Shot 2022-10-02 at 4.30.48 PM.png" alt=""><figcaption></figcaption></figure>



| Name              | Explanation                                                       |
| ----------------- | ----------------------------------------------------------------- |
| Role ARN          | ARN of the role to be assumed                                     |
| Role Session Name | Unique identifier for the session when the above role is assumed  |
| External ID       | A unique identifier that might be required when you assume a role |
