import os
import datetime
from GPSPhoto import gpsphoto
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Authenticate with the Google Sheets API
creds = service_account.Credentials.from_service_account_file('C:\\Users\\lenovo\\Desktop\\spothole\\yolov5\\spotholedb.json')
service = build('sheets', 'v4', credentials=creds)

# Set the ID of the spreadsheet and the name of the sheet you want to write to
spreadsheet_id = '17BmT9BSLrvFsnVD1fheD0Qyr6bVDK1OTNq7hscQYiIY'
sheet_name = 'sheet1'

# Read the list of image file names from a text file
with open('image_list.txt', 'r') as f:
    image_list = f.read().splitlines()

# Create a list to hold the GPS data for each image
data_list = []

# Loop through each image and get its GPS data
for image_file in image_list:
    full_path = os.path.join('C:\\Users\\lenovo\\Desktop\\spothole\\yolov5\\pothole_image', image_file)
    data = gpsphoto.getGPSData(full_path)
    lat = data['Latitude']
    lon = data['Longitude']
    data_list.append([image_file, lat, lon])

# Create a list of values to write to the spreadsheet
values = []
print(data_list)
for data in data_list:
    values.append([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), data[0], data[1], data[2]])

#Write the data to the spreadsheet
range_name = f'{sheet_name}!A2'
request_body = {
    'range': range_name,
    'majorDimension': 'ROWS',
    'values': values
}
response = service.spreadsheets().values().append(
    spreadsheetId=spreadsheet_id,
    range=range_name,
    valueInputOption='USER_ENTERED',
    insertDataOption='INSERT_ROWS',
    body=request_body).execute()
print(f"{response['updates']['updatedCells']} cells appended.")