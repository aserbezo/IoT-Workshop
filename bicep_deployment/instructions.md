## 1. Ensure Azure CLI is Installed

First, make sure you have the Azure CLI installed on your system. You can check if it's installed by running:

```sh
az --version
```


## 2. Install Bicep
Bicep can be installed via the Azure CLI with a single command:

```sh
az bicep install
```


## 3. Verify the Installation
After installation, verify that Bicep is installed correctly by checking the version:

```sh
az bicep version
```

## 4. Keep Bicep Updated

Bicep updates are released regularly. To upgrade to the latest version, use the following command:

```sh
az bicep upgrade
```

## 5. List Available Subscriptions

If you have access to multiple Azure subscriptions, you can list them using the following command:

```sh
az account list --output table
```
## 6. Set the Desired Subscription
To set the desired subscription as the active one for deployment, use the following command:

```sh
az account set --subscription <subscription-id>
```
Replace <subscription-id> with the ID of the subscription you want to use. You can also use the Name of the subscription instead of the ID.

## 7. Verify the Active Subscription

```sh
az account show --output table
```
## 8 Create a resoruce group 

![image](https://github.com/user-attachments/assets/5ade8857-105c-46bf-ba86-691e3937ac4f)


## 8 Change the parameters in main.bicep file:

![image](https://github.com/user-attachments/assets/10ee469f-69a4-4466-82ae-3a43b2b97ac2)


## 8. Deploy the Resource Group

Now that your desired subscription is set, you can proceed to create a Resource Group, then the other resources using your Bicep file:

```sh
az deployment group create --resource-group {YourResourceGroup} --template-file main.bicep
```
This will deploy the resources defined in your Bicep file to the Resource Group within the currently active subscription.

![image](https://github.com/user-attachments/assets/0670fc02-eaa9-4aa1-825a-2f5e9b498d4f)

