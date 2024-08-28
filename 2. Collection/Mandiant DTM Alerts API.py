## you will need to follow the instructions to download the unofficial Mandiant API client here https://github.com/cybercti/maapi/tree/main
## then you will need to follow the instructions in Mandiant to generate your key id which is MAV4_USER and your key secret which is MAV4_PASS in this script
## once you run the pip install git+https://github.com/cybercti/maapi.git to download the client, you will need to set your environment variables using the key id and key secret
## at the bash prompt type in the following, making sure to copy-and-paste the values for YOUR keyid and keysecret
## export MAV4_USER=2122...99
## export MAV4_PASS=4991...78
## now you need to figure out what your monitor ID is. Login to Mandiant Advantage, then click "Digital Threat Monitoring" at the top
## find you monitor that you created and click on it like you're going to edit the parameters of the monitor. Take note of the url which will look something like this:
## https://advantage.mandiant.com/dtm/monitors/cns6hkoj8tguak39o130
## that last part, that string at the end (in thise case cns6hkoj8tguak39o130) is your monitor_id

##now you are ready to run this script, which will pull all alerts for the specified monitor and then organize them into folders by year, month and date and then create a CSV to contain all the results for the time period it was run for. it will also create a file called dtm_download_log.txt
## this text file will contain logging from error handling so you can see how many API calls were made and any issues with the way the script ran

import re
import os
import json
import logging
import csv
from datetime import datetime, timedelta
from os import environ
from maapi.dtm import DTM

# Configuration
monitor_id = "cns6hkoj8tguak39o130" #make sure you update this, see the instructions above

# Set up logging
logging.basicConfig(filename='dtm_download_log.txt', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize the client
# make sure that you set these variables, see the instructions above
username = environ['MAV4_USER']
password = environ['MAV4_PASS']
client = DTM(username, password)

def make_directories(base_path, year, month, day):
    """Creates directories for year, month, and day."""
    year_path = os.path.join(base_path, str(year))
    month_path = os.path.join(year_path, str(month).zfill(2))
    day_path = os.path.join(month_path, str(day).zfill(2))

    os.makedirs(day_path, exist_ok=True)

    return day_path

def sanitize_filename(filename):
    """Sanitize the filename by removing invalid characters."""
    return re.sub(r'[^A-Za-z0-9_\- ]+', '', filename)

def save_alert(alert, base_path):
    """Saves an alert to a JSON file."""
    created_at = alert["created_at"]
    date_obj = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%fZ" if '.' in created_at else "%Y-%m-%dT%H:%M:%SZ")
    year, month, day = date_obj.year, date_obj.month, date_obj.day

    title = alert["title"][:20]
    filename = f"{created_at} {title}.json"
    sanitized_filename = sanitize_filename(filename)

    day_path = make_directories(base_path, year, month, day)
    file_path = os.path.join(day_path, sanitized_filename)

    with open(file_path, 'w') as outfile:
        json.dump(alert, outfile, indent=4)

    return year, month, day

def save_csv(alerts, start_date, base_path):
    """Saves a summary of the alerts to a CSV file."""
    csv_filename = f"{start_date.strftime('%Y-%m-%d')}.csv"
    csv_path = os.path.join(base_path, csv_filename)
    headers = ["id", "created_at", "title", "severity", "confidence"]

    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for alert in alerts:
            writer.writerow({
                "id": alert["id"],
                "created_at": alert["created_at"],
                "title": alert["title"],
                "severity": alert.get("severity", ""),
                "confidence": alert.get("confidence", "")
            })

def fetch_and_save_alerts(client, start_date, end_date, base_path):
    api_calls_made = 0
    all_alerts = []
    current_date = start_date

    while current_date < end_date:
        since = current_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        until = (current_date + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S.000Z")

        logger.info(f"Fetching alerts from {since} to {until}")
        try:
            resp = client.get_alerts_all(size=100, since=since, until=until, monitor_ids=monitor_id, truncate=80)
            alerts = resp.get("alerts", [])
        except Exception as e:
            logger.error(f"Error fetching alerts: {e}")
            break

        if not alerts:
            logger.info(f"No alerts found for {since} to {until}")
        else:
            for alert in alerts:
                year, month, day = save_alert(alert, base_path)
                all_alerts.append(alert)

            logger.info(f"Processed {len(alerts)} alerts for {since} to {until}")

        api_calls_made += 1

        current_date += timedelta(days=1)

    # Save the CSV summary
    save_csv(all_alerts, start_date, base_path)

    logger.info(f"Total alerts processed: {len(all_alerts)}")
    logger.info(f"Total API calls made: {api_calls_made}")

def main():
    # Define the date range for fetching alerts
    start_date = datetime(2024, 4, 30)  # Example start date, replace this with what your value should be
    end_date = datetime(2024, 8, 28)  # Example end date, replace this with what your value should be

    # Base path for saving data
    base_path = "alerts_data"

    fetch_and_save_alerts(client, start_date, end_date, base_path)

if __name__ == "__main__":
    main()
