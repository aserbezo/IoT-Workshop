# IoT-Workshop

### Business Problem
A logistics company operates a fleet of vehicles for transporting goods across various regions. The company faces challenges in:
- Optimizing vehicle operations
- Managing fuel consumption
- Ensuring vehicle maintenance
- Tracking vehicle locations
- Analyzing driving behaviors to reduce accidents and improve overall efficiency


### Objective
To implement a vehicle management system that leverages IoT devices, IoT Hub, Databricks, Azure Stream Analytics, and Power BI to monitor and optimize vehicle operations in real-time, leading to:
- Cost savings
- Enhanced safety
- Improved operational efficiency

### Solution Components and Architecture:

![Solution Architecture](https://github.com/user-attachments/assets/0efd86a5-8969-4c3b-a2c9-4512f0a0a3f1)




## Step 1: Create the Resources

Create the following Azure resources. You can either use the Bicep deployment file located in the folder or create them manually:

[Bicep deployment](https://github.com/aserbezo/IoT-Workshop/tree/main/bicep_deployment)


1. IoT Hub
2. Storage Account
3. Stream Analytics Job
4. Databricks Workspace
5. Key Vault


## Step 2: Register the IoT Devices in IoT Hub

After setting up your IoT Hub, register the IoT devices that will send telemetry data. You can do this through the Azure portal by following the instructions in the link below:

- [Azure IoT Hub Device Registration](https://learn.microsoft.com/en-us/azure/iot-hub/create-connect-device?tabs=portal)

In the device management section, add the following three devices with these names:

- Johny
- james
- jason
![image](https://github.com/user-attachments/assets/cb787ce3-a8b7-485a-bc2d-40bfbc5d06ee)

Be sure to copy the primary connection string for each device into Notepad.

## Step 3: Download the IoT Simulator and Set Connection String

Clone the IoT Device Simulator repository and follow the instructions in the `README.md` file:

[IoT-Device-Simulator](https://github.com/aserbezo/IoT-Device-Simulator.git)

```sh
git clone https://github.com/aserbezo/IoT-Device-Simulator.git
```

This simulator will generate telemetry data for your IoT devices.


## Step 4: Create a Hot Path
----------------------------------------------------
![image](https://github.com/user-attachments/assets/46a8b747-747d-4afb-b788-6f5f359fed46)

Follow the instructions in  [Hot-path instructions to complete the setup](https://github.com/aserbezo/IoT-Workshop/blob/main/hot-path.md)

## Step 5: Create a  Warm Path with Medalion Architecture 

![image](https://github.com/user-attachments/assets/3c43a192-440d-4e45-a9a8-14eb5380d11e)

--------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/7d657742-4ad2-40f8-8a73-b1f1c7d0cfb5)


Follow the instructions in the [Warm-path instructions to complete the setup](https://github.com/aserbezo/IoT-Workshop/blob/main/warm-path.md)

## STEP 6 Delete All Resources
