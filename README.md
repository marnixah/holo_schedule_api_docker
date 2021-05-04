# Holo Schedule API
A Web API to get hololive's schedule.

## Getting Started
### Docker run (recommended)
To run with docker run, run the following
```bash
docker run -d \
    --name "holo_schedule_api" \
    --restart=unless-stopped \
    --network host \
    -e FLASK_RUN_PORT=5000 \
    marnixah/holo_schedule_api:latest
```
### Docker-compose file
To run with docker-compose, simply run
```bash
docker-compose up -d
```
### Accessing
Website can then be accessed at `http://127.0.0.1:5000/schedules`.  
There are currently 2 publically hosted instances of the api, one at [http://hololive-api2.marnixah.com/](http://hololive-api2.marnixah.com/) and one at [http://hololive-api.marnixah.com/](http://hololive-api.marnixah.com/). The latter only hosting /schedules
## Notes
This program scrapes [this page](https://schedule.hololive.tv/lives/hololive) and will update every 5 minutes. However the source page updates every 15 minutes, therefore, there will be at most 20 minutes of delay to the actual stream schedule.
