from utility.utils import *

URL = "https://demoqa.com"

# Home
ELEMENTS = "Elements"
FORMS = "Forms"
ALERTS_FRAMES = "Alerts, Frame & Windows"
WIDGETS = "Widgets"
INTERACTIONS = "Interactions"
BOOK_STORE = "Book Store Application"

# Elements
username = "Bruce Wayne"
email = "bruce@wayne.com"
current_addr = "Wayne Mansion"
permanent_addr = "Gotham"

# Web Tables
f_name = "Bruce"
l_name = "Wayne"
age = 35
salary = 100
department = "Business"

# Upload and Download
downloaded_file_name = "sampleFile.jpeg"
downloaded_file_path = f"{download_path}/{downloaded_file_name}"
upload_file_name = "upload_file.jpeg"
upload_file_path = f"{data_folder_path}/{upload_file_name}"

# Forms
mobile = 9876543210
dob = "09/21/23"
subject = "Maths"
city = "Delhi"
state = "NCR"

# Book Store App
book_store_f_name = "Bruce"
book_store_l_name = "Wayne"
book_store_user = "bruce"
book_store_pass = "Wayne#1234"


# Book store apis
user = URL + "/Account/v1/User"
login = URL + "/Account/v1/Authorized"
generate_token = URL + "/Account/v1/GenerateToken"
books = URL + "/BookStore/v1/Books"
