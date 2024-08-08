
  


1. Check Your Azure Subscription
Open a terminal or command prompt where the Azure CLI is installed.

Run the following command to list all your Azure subscriptions:

``
az account list --output table``

This will display a list of subscriptions that your account has access to, along with details like the subscription name, ID, and the current status.

2. Set the Active Subscription
If you have multiple subscriptions, you can set the active one (the one that will be used for subsequent Azure CLI commands) by using the subscription ID or name.

To set the subscription using its ID, run:


``az account set --subscription <subscription-id>``

Alternatively, you can set it using the subscription name:


``az account set --subscription "<subscription-name>" ``
Replace <subscription-id> or <subscription-name> with the appropriate value from the list you obtained in the first step.

3. Verify the Active Subscription
After setting the subscription, you can verify which subscription is currently active by running:

``az account show --output table``

This will show the details of the active subscription, ensuring that you've set the correct one.

## For Terraform 

1. Install Terraform
First, ensure that Terraform is installed on your machine. You can download it from the official Terraform website.

After installation, verify that Terraform is installed correctly by running:
``
terraform --version
 ``

 Initialize the Terraform Project

 Navigate to the directory containing your Terraform configuration files.

Run the following command to initialize the project. This command downloads the required provider plugins and prepares the project directory:

Validate the Configuration (Optional)

Before applying the configurations, it's good practice to validate the Terraform configuration files to ensure they are syntactically correct:

terraform validate


Create an Execution Plan

The execution plan shows what actions Terraform will take to reach the desired state described in your configuration files. Run:
terraform plan


Apply the Terraform Configuration

To execute the plan and create the resources, run:

terraform apply


Destroy the Infrastructure (Optional)

If you want to remove the infrastructure created by Terraform, you can run:

terraform destroy 

terraform init        # Initialize the Terraform project
terraform validate    # Validate the configuration (optional)
terraform plan        # Create an execution plan
terraform apply       # Apply the configuration to create resources
terraform show        # Show the current state (optional)
terraform destroy     # Destroy the infrastructure (optional)
