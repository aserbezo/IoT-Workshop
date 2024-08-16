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

### 1. Upload the Drivers CSV File
- First, upload the drivers.csv file. To do this, create a container named referance_table in your storage account.

### 2. Configure the Inputs

- We have two input sources: one is static, and the other is IoT Hub.
  
Static Input
---------------------------------------------------------------------------------------------------
  ![image](https://github.com/user-attachments/assets/37b2480d-b0fd-4bd4-84c9-787b1296c985)
-------------------------------------------------------------------------------------------------
  ![image](https://github.com/user-attachments/assets/0af434c4-fa41-494e-a9d6-ace139bcfd58)
--------------------------------------------------------------------------------------------

IoT Hub Input
----------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/6bf74969-1bf5-4bfc-9e66-5b1e8a3dc9fc)
---------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/109ff26e-4a98-41b8-a139-4a7d423a752d)
---------------------------------------------------------------------------------------


### 3. Configure the Output
-------------------------------------------------------------------------------------------
- Create a workspace in Power BI and copy the Workspace ID. You can find the Workspace ID in the Power BI URL for the workspace, e.g., groups/{Workspace ID}/.
--------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/167d9c30-93ab-4938-98d1-202921b9c450)
--------------------------------------------------------------------------------------------
- After creating the workspace, configure the Power BI output.
-------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/a2dc4988-0b51-409f-b172-034f70eb6292)
-------------------------------------------------------------------------------------------
- Provide the necessary settings for the workspace by specifying the Workspace ID, dataset name, and table name. Finally, authorize the connection with your credentials.
-------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/c695b1f3-ea2e-4229-8ecb-d3db3af4b180)
-------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/4177fafc-395a-4dec-ae6a-f85ede98f081)
-------------------------------------------------------------------------------------------

### 4.Configure the Query
---------------------------------------------------------------------------------------------

- Start the IoT simulator to test if data is being received. Note that it might take some time for the data to appear in the input preview, where you can see data coming from IoT devices.
--------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/77fe6d26-5a4e-4666-a64e-239a9cc2c242)

- Next, work on the query to join the IoT data with the static table.
-----------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/d3f03c09-e13c-42a9-9970-2bc87ca88035)

- Use the following query:

```sh
SELECT
    I1.timestamp,
    I1.vehicle_id,
    I1.location,
    I1.speed,
    I1.engine_status,
    I1.battery_status,
    I1.tire_pressure,
    I1.driver_behavior,
    I1.alerts,
    S1.first_name,
    S1.last_name,
    S1.car_model,
    S1.car_mileage_km,
    S1.experience
INTO
    [IoT-PBI-Workshop]
FROM
    [LogisticsIoThub] I1
JOIN
    [static-table] S1
ON
    I1.vehicle_id = S1.vehicle_id
```

- After that, you can test the query. Make sure to upload the sample data to test the query, and don't forget to save your work.

------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/4f9d4215-e16d-472b-81a1-7575555d7e91)

### 5. Check the Report in Power BI

- Finally, check the Power BI workspace to view the report.
-------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/fcb817ce-d42d-4ec0-a57d-cb884ca81d93)

- You can now explore and interact with your report.
---------------------------------------
![image](https://github.com/user-attachments/assets/7e98220c-8f44-4863-919a-5bad6ce49880)

