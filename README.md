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

## Step 2: Download the IoT Simulator

Clone the IoT Device Simulator repository and follow the instructions in the README.md file:

[IoT-simulator](https://github.com/aserbezo/IoT-Device-Simulator.git)

```sh
git clone https://github.com/aserbezo/IoT-Device-Simulator.git
```

This simulator will generate telemetry data for your IoT devices.


## Step 3: Register the IoT Devices in IoT Hub

After setting up your IoT Hub, register the IoT devices that will send telemetry data. This can be done through the Azure portal or using the Azure CLI.

## Step 4: Configure Routes from IoT Hub to Event Hub

Configure the IoT Hub to route telemetry data from your registered devices to the Event Hub. This allows seamless data ingestion for further processing.

## Step 5: Create a Stream Analytics Job

Set up a Stream Analytics Job to process the incoming data. The job will send processed data to different destinations:

- Storage Accounts (for both hot and cold data storage)
- Power BI (for real-time reporting)

Below is a sample query for the Stream Analytics Job:

```sh
SELECT I1.DeviceId, I1.Latitude , I1.Longitude , I1.time, I1.temp,I1.tire_press,I1.speed,I1.alert,I2.driver_id ,I2.first_name,I2.last_name , I2.car_model, I2.experiance,I2.car_mileage_km
INTO [IoT-PBI-workshop]
FROM [drivers-cars] I1 
LEFT JOIN [ref] I2
ON I1.DeviceId = I2.first_name

SELECT I1.DeviceId, I1.Latitude , I1.Longitude , I1.time, I1.temp,I1.tire_press,I1.speed,I1.alert,I2.driver_id ,I2.first_name,I2.last_name , I2.car_model, I2.experiance,I2.car_mileage_km
INTO [bronze]
FROM [drivers-cars] I1 
LEFT JOIN [ref] I2
ON I1.DeviceId = I2.first_name
```

## Step 6: Databricks Notebook for Data Processing

Create a Databricks Notebook to read data from the Storage Account. Use the notebook to filter and transform the data, categorizing it into Bronze, Silver, and Gold zones for further analysis.

## Step 7: Prepare Reports in Power BI

Finally, use Power BI to create interactive dashboards and reports. These will provide real-time insights into your fleet operations, including vehicle locations, driver performance, and other key metrics.
