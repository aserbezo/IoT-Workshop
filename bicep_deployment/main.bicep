// Define the parameters
param location string = 'East US'
param resourceGroupName string = 'MyResourceGroup'
param streamAnalyticsJobName1 string = 'MyStreamAnalyticsJob1'
param streamAnalyticsJobName2 string = 'MyStreamAnalyticsJob2'
param iotHubName string = 'MyIoTHub'
param databricksWorkspaceName string = 'MyDatabricksWorkspace'
param storageAccountName string = 'mystorageaccount'
param keyVaultName string = 'myKeyVault'

// Create the Resource Group
resource rg 'Microsoft.Resources/resourceGroups@2023-05-01' = {
  name: resourceGroupName
  location: location
}

// Create the Storage Account
resource storageAccount 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}

// Create the IoT Hub
resource iotHub 'Microsoft.Devices/IotHubs@2023-01-01' = {
  name: iotHubName
  location: location
  sku: {
    name: 'S1'
    capacity: 1
  }
  properties: {
    enableFileUploadNotifications: true
  }
}

// Create the first Stream Analytics Job
resource streamAnalyticsJob1 'Microsoft.StreamAnalytics/streamingjobs@2023-01-01' = {
  name: streamAnalyticsJobName1
  location: location
  sku: {
    name: 'Standard'
  }
  properties: {
    compatibilityLevel: '1.2'
    jobType: 'Cloud'
    dataLocale: 'en-US'
  }
}

// Create the second Stream Analytics Job
resource streamAnalyticsJob2 'Microsoft.StreamAnalytics/streamingjobs@2023-01-01' = {
  name: streamAnalyticsJobName2
  location: location
  sku: {
    name: 'Standard'
  }
  properties: {
    compatibilityLevel: '1.2'
    jobType: 'Cloud'
    dataLocale: 'en-US'
  }
}

// Create the Databricks Workspace
resource databricksWorkspace 'Microsoft.Databricks/workspaces@2023-02-01' = {
  name: databricksWorkspaceName
  location: location
  sku: {
    name: 'standard'
  }
  properties: {
    managedResourceGroupId: resourceId('Microsoft.Resources/resourceGroups', '${resourceGroupName}-databricks')
  }
}

// Create the Key Vault
resource keyVault 'Microsoft.KeyVault/vaults@2023-02-01' = {
  name: keyVaultName
  location: location
  properties: {
    sku: {
      family: 'A'
      name: 'standard'
    }
    tenantId: subscription().tenantId
    accessPolicies: []
    enabledForDeployment: true
    enabledForTemplateDeployment: true
    enabledForDiskEncryption: true
  }
}
