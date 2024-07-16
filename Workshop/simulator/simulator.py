from dotenv import load_dotenv
import os
import json
import time
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message
from datetime import datetime
import random

# Load environment variables from .env file
load_dotenv()

# Access the environment variable
jasonstatham_connection_string = os.getenv('jasonstatham_connection_string')
jamesbond_connection_string = os.getenv('jamesbond_connection_string')
johnyenglish_connection_string = os.getenv('johnyenglish_connection_string')


with open('Workshop/simulator/sofia-burgas-route.json', 'rb') as file , open('Workshop\simulator\sofia-varna-route.json', 'rb') as file1 ,open('Workshop\simulator\sofia-vidin-route.json', 'rb') as file2 :
    route1 = file.read().decode('utf-8')
    route2 = file1.read().decode('utf-8')
    route3 = file2.read().decode('utf-8')
    print(route1)

sofia_burgas = json.loads(route1)
sofia_varna = json.loads(route2)
sofia_vidin = json.loads(route3)

# between 75 to 105 degrees Celsius
speed = [60, 64, 65, 68, 70, 75, 77, 74, 80, 82, 88, 85, 81, 90, 92, 94, 96, 97, 95, 100, 111, 104, 105, 110, 120, 150,
         160]
temp = [75, 80, 90, 100, 76, 90, 100, 110, 115, 130, 77, 83]
alert = ['None', 'Battery Charge Warning Light', 'Oil Pressure Warning Light', 'Brake Warning Light',
         'Transmission Temperature', 'None', 'None', 'None', 'None']
#  Normal 30 to 35 PSI
tire_pressure = [30, 31, 32, 33, 29, 25]



async def send_message_to_iot_hub(conn_str, message_content):
    try:
        # Create an instance of the IoT Hub device client
        client = IoTHubDeviceClient.create_from_connection_string(conn_str)

        if client is None:
            raise Exception("Failed to create IoT Hub device client.")

        # Connect the client to the IoT Hub
        await client.connect()

        # Create a Message object with the message content
        message = Message(json.dumps(message_content))

        # Send the message
        await client.send_message(message)
        print("Message sent to Azure IoT Hub:", message_content)

    except Exception as e:
        print("Error:", e)

    finally:
        # Disconnect the client
        if client:
            await client.disconnect()


async def jason_car():
    for value in sofia_burgas.values():
        for i in value:
            Latitude = i[0]
            Longitude = i[1]
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            curr_temp = random.choice(temp)
            curr_speed = random.choice(speed)
            curr_tire_pressure = random.choice(tire_pressure)
            curr_alet = random.choice(alert)
            message_content = {'DeviceId': 'jason',
                               'Latitude': Latitude,
                               'Longitude': Longitude,
                               'time': current_time,
                               'temp': curr_temp,
                               'tire_press': curr_tire_pressure,
                               'speed': curr_speed,
                               'alert': curr_alet}

            # Run send_message_to_iot_hub asynchronously
            await send_message_to_iot_hub(jasonstatham_connection_string, message_content)
            await asyncio.sleep(2)  # Adjust for faster/slower update frequency


async def james_car():
    for value in sofia_varna.values():
        for i in value:
            Latitude = i[0]
            Longitude = i[1]
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            curr_temp = random.choice(temp)
            curr_speed = random.choice(speed)
            curr_tire_pressure = random.choice(tire_pressure)
            curr_alet = random.choice(alert)
            message_content = {'DeviceId': 'james',
                               'Latitude': Latitude,
                               'Longitude': Longitude,
                               'time': current_time,
                               'temp': curr_temp,
                               'tire_press': curr_tire_pressure,
                               'speed': curr_speed,
                               'alert': curr_alet}

            # Run send_message_to_iot_hub asynchronously
            await send_message_to_iot_hub(jamesbond_connection_string, message_content)
            await asyncio.sleep(2)  # Adjust for faster/slower update frequency


async def johny_car():
    for value in sofia_vidin.values():
        for i in value:
            Latitude = i[0]
            Longitude = i[1]
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            curr_temp = random.choice(temp)
            curr_speed = random.choice(speed)
            curr_tire_pressure = random.choice(tire_pressure)
            curr_alet = random.choice(alert)
            message_content = {'DeviceId': 'Johny',
                               'Latitude': Latitude,
                               'Longitude': Longitude,
                               'time': current_time,
                               'temp': curr_temp,
                               'tire_press': curr_tire_pressure,
                               'speed': curr_speed,
                               'alert': curr_alet}

            # Run send_message_to_iot_hub asynchronously
            await send_message_to_iot_hub(johnyenglish_connection_string, message_content)
            await asyncio.sleep(30)  # Adjust for faster/slower update frequency


async def run_all_functions():
    # Run main() and main1() concurrentl y
    results = await asyncio.gather(
        jason_car(),
        johny_car(),
        james_car()
    )

    print("Both functions completed")
    for result in results:
        print(result)


# Run the function to execute both main() and main1() concurrently
asyncio.run(run_all_functions())