// Define the parameters


////////////////////////////////////////////////////////////
param location string = 'East US'
param streamAnalyticsJobName1 string = 'MyStreamAnalyticsJob1'
param streamAnalyticsJobName2 string = 'MyStreamAnalyticsJob2'
param iotHubName string = 'MyIoTHubanton'
param storageAccountName string = 'mystorageaccountanton1'
param keyVaultName string = 'myKeyVault-anton'
param databricksWorkspaceName string = 'MyDatabricksWorkspace'
param pricingTier 'standard'
////////////////////////////////////////////////////////////
// if you have issues with key vault az keyvault purge --name myKeyVault-anton    


var managedResourceGroupName = 'databricks-rg-${databricksWorkspaceName}-${uniqueString(databricksWorkspaceName, resourceGroup().id)}'




// Create the Storage Account
resource storageAccount 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}

// --- Resources
resource IoTHub 'Microsoft.Devices/IotHubs@2023-06-30' = {
  name: iotHubName
  location: location
  sku: {
    name: 'S1'
    capacity: 1
  }  
}


// Create the first Stream Analytics Job
resource streamingJob 'Microsoft.StreamAnalytics/streamingjobs@2021-10-01-preview' = {
  name: streamAnalyticsJobName1
  location: location
  properties: {
    sku: {
      name: 'StandardV2'
    }
    outputErrorPolicy: 'Stop'
    eventsOutOfOrderPolicy: 'Adjust'
    eventsOutOfOrderMaxDelayInSeconds: 0
    eventsLateArrivalMaxDelayInSeconds: 5
    dataLocale: 'en-US'
  }
}

// Create the second Stream Analytics Job
resource streamingJob2 'Microsoft.StreamAnalytics/streamingjobs@2021-10-01-preview' = {
  name: streamAnalyticsJobName2
  location: location
  properties: {
    sku: {
      name: 'StandardV2'
    }
    outputErrorPolicy: 'Stop'
    eventsOutOfOrderPolicy: 'Adjust'
    eventsOutOfOrderMaxDelayInSeconds: 0
    eventsLateArrivalMaxDelayInSeconds: 5
    dataLocale: 'en-US'
  }
}


// Create the Databricks Workspace

resource ws 'Microsoft.Databricks/workspaces@2018-04-01' = {
  name: databricksWorkspaceName
  location: location
  sku: {
    name: pricingTier
  }
  properties: {
    managedResourceGroupId: managedResourceGroup.id
    parameters: {
      enableNoPublicIp: {
        value: false
      }
    }
  }
}

resource managedResourceGroup 'Microsoft.Resources/resourceGroups@2021-04-01' existing = {
  scope: subscription()
  name: managedResourceGroupName
}

// Create the Key Vault
resource kv 'Microsoft.KeyVault/vaults@2023-07-01' = {
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
