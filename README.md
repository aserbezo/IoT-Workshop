# IoT-Workshop



### Business Problem:
A logistics company operates a fleet of vehicles for transporting goods across various regions. 
The company faces challenges in optimizing fleet operations, including managing fuel consumption, ensuring vehicle maintenance, tracking vehicle locations, and analyzing driving behaviors to reduce accidents and improve overall efficiency.


### Objective:
To implement a fleet management system that leverages IoT devices, IoT Hub, Databricks, Azure Stream Analytics, and Power BI to monitor and optimize vehicle operations in real-time, leading to cost savings, enhanced safety, and improved operational efficiency.


### Solution Components and Architecture:

![image](https://github.com/user-attachments/assets/23ac777a-8ca1-41ff-9552-f7839429c4c0)




## Step 1: Create the Resources

First, you need to create the following Azure resources you could use the bicep mina file located in folder or create them manually:

[Bicep deployment](https://github.com/aserbezo/IoT-Workshop/tree/main/bicep_deployment)


1. IoT Hub
2. Storage Account
3. Stream Analytics Job
4. Databricks Workspace
5. Key Vault


## Step 2: Register the IoT Devices in IoT Hub

After setting up your IoT Hub, register the IoT devices that will send telemetry data. This can be done through the Azure portal:

- https://learn.microsoft.com/en-us/azure/iot-hub/create-connect-device?tabs=portal

Do not forget to copy the primary connection string for the devices/

## Step 3: Download the IoT Simulator and set Connection string from the devices

Clone the IoT Device Simulator repository and follow the instructions in the README.md file:

[IoT-Device-Simulator](https://github.com/aserbezo/IoT-Device-Simulator.git)

```sh
git clone https://github.com/aserbezo/IoT-Device-Simulator.git
```

This simulator will generate telemetry data for your IoT devices.





## Step 4: Create a Hot Path
----------------------------------------------------
![image](https://github.com/user-attachments/assets/46a8b747-747d-4afb-b788-6f5f359fed46)

Follow the instructions in the [Hot-path instructions to complete the setup](https://github.com/aserbezo/IoT-Workshop/blob/main/hot-path.md)

## Step 5: Create a Hot Warm Path

![image](https://github.com/user-attachments/assets/3c43a192-440d-4e45-a9a8-14eb5380d11e)

Follow the instructions in the [Warm-path instructions to complete the setup](https://github.com/aserbezo/IoT-Workshop/blob/main/hot-path.md)
