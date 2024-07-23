# IoT-Workshop



### Business Problem:
A logistics company operates a fleet of vehicles for transporting goods across various regions. 
The company faces challenges in optimizing fleet operations, including managing fuel consumption, ensuring vehicle maintenance, tracking vehicle locations, and analyzing driving behaviors to reduce accidents and improve overall efficiency.


### Objective:
To implement a fleet management system that leverages IoT devices, IoT Hub, Databricks, Azure Stream Analytics, and Power BI to monitor and optimize vehicle operations in real-time, leading to cost savings, enhanced safety, and improved operational efficiency.


### Solution Components and Architecture:
![image](https://github.com/user-attachments/assets/a44c45c3-5350-450f-8bf0-ff1f909d7ecc)



Resources needs to be created:
1. IoT hub
2. Stoage Account
3. Stream Job
4. Databricks
5. Key vault
6. Event Hub



STEP BY STEP 

### 1. Create a IoT hub and register the IoT devices


### 2. Configure the routes of the devices to point to Event Hub 

### 3. Create a Strem job to send data to Storage account and Power BI real time report 

```sh
SELECT I1.DeviceId, I1.Latitude , I1.Longitude , I1.time, I1.temp,I1.tire_press,I1.speed,I1.alert,I2.driver_id ,I2.first_name,I2.last_name , I2.car_model, I2.experiance,I2.car_mileage_km
INTO [IoT-PBI-workshop]
FROM [drivers-cars1] I1 
LEFT JOIN [ref] I2
ON I1.DeviceId = I2.first_name
```

### 4. Databricks Notebook to read data from storage account and filter the data to silver zone and gold zone
