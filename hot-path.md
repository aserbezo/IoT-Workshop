
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

