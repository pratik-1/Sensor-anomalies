# Sensor-anomalies

When developing automated monitoring, fault tolerant and predictive systems for industrial automation; it is imperative to have real-time sensor data that are installed next to pipelines, vessels, or any target components.  

These sensors that provides stream of information about the asset health in relation to corrosion or moisture presence can help robust system with focused, efficient inspection and maintenance programmes - provides significant improvement over standard Risk-Based Inspection (RBI) approaches.

This is a simple project with sample sensor data that counts the anomalies in the sensor readings and exposes through APIs which can be further used to take required action


More such APIs can be easily added to this shippable easy to install containerized framework.

# Data Description
These proprietary sensors are not spot sensors, but array of sensors. Hence, instead of returning a single sample (representing the moisture in the sensor location), they return a list of samples (representing the moisture throughout the whole sensor length). The distance between two consecutive samples is the unit_length, which is not a physical property of the sensor, but it can be easily changed modifying the sensor config file.

## Readings
The following is a simplified version of a reading of one of the sensors:
```json
{
  "sensor_id":"cr123",
  "samples":[
    103.04983414952939,
    13.06129559147759,
    11.423143599058566,
    15.192366557718543,
    15.072889387425104,
    42.76854392198215,
    83.85545790646066,
    32.14083956177737,
    10.187591211868611,
    1.3436639679184346,
    7.632806716877543
  ],
  "unit_length ":1.0,
  "acquisition_timestamp":"2020-01-01T03:00:43"
}
```

**Fields description:**
- `sensor_id (str)`: a unique string to identify the sensor
- `samples (list of floats, arbitrary units)`: a list containing the moisture
values measured by the sensor throughout its length. The first value corresponds to the
moisture value at the very beginning of the sensor; the second is one unit_length down
the sensor from the first value, and so on.
- `unit_length (float, meter)`: distance between 2 consecutive samples
- `acquisition_timestamp (str)`: timestamp of when the reading has been acquired.

The file `data.json` contains a list of readings.



## Sensor model
The following is a simplified version of a sensor model, which is obtained averaging several
consecutive readings;
```json
{
  "sensor_id":"cr123",
  "unit_length ":1.0,
  "means":[
    104.32191308650778,
    13.67750843709852,
    10.344738896946733,
    13.195271382650805,
    22.53947465254497,
    37.340696571314815,
    77.7254312595879,
    28.40130246469284,
    10.08883150873186,
    3.46104589054122,
    3.2674249590475952
  ],
  "sigma":3.01,
  "n_sigma":3.0
}
```
**Fields description:**
- `sensor_id (str)`: a unique string to identify the sensor
- `unit_length (float, meter)`: distance between 2 consecutive samples
- `means (list of floats, arbitrary units)`: a list containing the average moisture for every sample. Its length is identical to the length of the samples used to generate the model
- `sigma(floats, arbitrary units)`: standard deviation of the sample means. Valid across the whole means list.
- `n_sigma (float)`: number of sigmas beyond which a sample is anomaly

The file `model.json` contains sensor models.




# Project setup
**Prerequisites**:

Your machine needs to have below pre-requisites installed:
- Docker
- Git


To get started enter the below command in your shell to clone the repository
```commandline
git clone https://github.com/pratik-1/Sensor-anomalies.git
```
Navigate into the `Sensor-anomalies` folder.



# Pull the image from Docker Hub
```commandline
docker pull npratik04/cr-sensors-dj:latest
```


# Run the containerized application
You will have `docker-compose.yaml` file in your current working directory. If not go to the cloned repository and enter below command in your shell.
```commandline
docker-compose up -d
```
After the container is up, you can check using command
```commandline
docker ps
```

# Count Anomalies APIs
After you see the container running, you can access to the API endpoints:
- `GET /count-anomalies/`: landing page
- `GET /count-anomalies/<str: sensor_id>/`: retrieve the count of anomalies of sensor using `sensor_id`


Go to your browser and enter
```commandline
http://127.0.0.1:8000/count-anomalies/
```
The API is password protected. Click `Log in` and enter credentials 
- **username**: user1
- **password**: user1

This will redirect to landing page. To find the count of anomalies of particular sensor enter sensor id in url. (For the sample data, we have sensor model only for **cr123**). Enter the same in URL as shown below:
```commandline
http://127.0.0.1:8000/count-anomalies/cr123/
```

You can create more users and provide them the access using administration login at below path
```commandline
http://127.0.0.1:8000/admin/
```
Enter the below credentials for elevated access
- **username**: admin-user
- **password**: admin-user


# Stop the Containers
```commandline
docker-compose down
```


# Project Artifacts
- **Data**: The sensor's anomalies data is stored in `anomalies/static/` folder. In production, project can be easily connected to any databases.
- **Tests**: The project follows Test Driven Development (TDD) approach. Sample tests modules for anomalies app can be found in `anomalies/test/` folder.  Try running tests using `pytest -v` command.
- **Fixtures**: For testing, dummy data can be found  `anomalies/fixtures/`.
- **Test Report**: You can find `test_report.html`  in the project root folder. 
