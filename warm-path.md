# Data Processing Pipeline Setup

This guide will walk you through setting up a data processing pipeline, including configuring storage containers, uploading notebooks, and running stream jobs. 

## 1. Create Storage Containers

You need to create the following storage containers:
- `gold`
- `bronze`
- `silver`

![Storage Containers](https://github.com/user-attachments/assets/90bee268-e22b-4740-a6ed-c0749216ad24)

## 2. Upload the Notebooks
dowwlaod the notebooks [here](https://github.com/aserbezo/IoT-Workshop/blob/main/notebooks.dbc) and upload your notebooks to the appropriate locations. 

## 3. Configure the Stream Job

Add an additional output source to the `bronze` storage container.

![Configure Stream Job](https://github.com/user-attachments/assets/057cd00a-9cb8-493c-9181-c8191d321361)
![Stream Job Configuration](https://github.com/user-attachments/assets/620bd81c-49a9-410f-acd6-477a8092c53b)
![Another Stream Job Configuration](https://github.com/user-attachments/assets/988562d7-e931-47d2-8adf-26d1291bf440)

**Path Pattern:**
```sh
Raw/{date}
```
more examples for path pattern - Raw/{date}/{vehicle_id}/signals_{time}

## 4. Add Query to the Stream Job

Insert the following query to the stream job:

```sh
----- Warm Path Querry
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
    [bronze]
FROM
    [LogisticsIoThub] I1
JOIN
    [static-table] S1
ON
    I1.vehicle_id = S1.vehicle_id

```

The stream job will send data to Power BI and the Storage account.

## 5. Run the Job and Start Simulator

Run the stream job and start the simulator to populate the bronze layer with data.

If successful, you should see data in the bronze layer.

![image](https://github.com/user-attachments/assets/f2096d0e-0280-4f1d-a91a-21a275427bfb)


## 6. Link Key Vault to Databricks

- [Azure Databricks Secrets Documentation](https://learn.microsoft.com/en-us/azure/databricks/security/secrets/secret-scopes)

## 7. Follow the Instructions for Notebooks

### Bronze Notebook

The first notebook picks the raw data and saves it as a Delta table in the bronze layer.
![image](https://github.com/user-attachments/assets/f39ba894-b565-452e-abc9-03a02188d77c)


We are using a streaming API to read data from raw and save it as a Delta table.

-----------------------------------------------------------------------------------------------
### Silver Notebook

The second notebook normalizes the data, adds a Fahrenheit column, and saves it in the silver layer as a Delta table.
![image](https://github.com/user-attachments/assets/e283beab-b5ca-45df-8a8b-a279c6e4df0e)

We are using a streaming API to read data from the bronze Delta table and save it in the silver Delta table.

-----------------------------------------------------------------------------------------------------------

### Gold Notebook

Gold Notebiik will pick selecting column and save them in gold delta table ready for visulazitaion 

The Gold notebook selects specific columns and saves them in the gold Delta table, ready for visualization.

------------------------------------------------------------------

### Visualization Notebook

The final notebook displays the data using maps and various dashboards. Feel free to explore and play with the data.

![image](https://github.com/user-attachments/assets/45692177-966c-4beb-b849-87ff24f75a25)
-------------------------------------------------------------------------------------------------------


![image](https://github.com/user-attachments/assets/51661724-6576-4af9-ab9b-f7dd5483d208)


