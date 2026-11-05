"""
=====================================================================
 Data Drivers - Session 2: Importing Data with Python
=====================================================================

This script does the same thing as the notebook `importing_data.ipynb`
in this folder. Use whichever you prefer:

    * The NOTEBOOK runs one small step (a "cell") at a time.
      Great for exploring.
    * This SCRIPT runs everything from top to bottom in one go.
      Great for automating a task you'll repeat.

We'll load data in three different ways:

    PART 1 - From a LOCAL FILE on your computer   (using `os` + `pandas`)
    PART 2 - From an API on the internet          (using `requests` + `pandas`)
    PART 3 - From GOOGLE DRIVE                    (using a share link + `pandas`)

---------------------------------------------------------------------
 HOW TO RUN THIS SCRIPT
---------------------------------------------------------------------
1. Install the libraries (only needed once). In a terminal type:

       pip install pandas requests

2. Run the script from a terminal:

       python importing_data.py

   (Or open it in VS Code and click the "Run" button in the top right.)

Tip: Any line that starts with `#` is a COMMENT. Python ignores it.
     Comments are notes written for humans - read them!
"""

# ---------------------------------------------------------------------
# IMPORTS
# ---------------------------------------------------------------------
# "import" loads a library: a toolbox of code someone else already wrote,
# so we don't have to write everything ourselves.

import os            # "operating system": lets Python work with folders and file paths
import pandas as pd  # the most popular library for tables of data. "pd" is just a short nickname
import requests      # lets Python talk to websites and APIs over the internet


# A small helper so the output is easy to read in the terminal.
# `def` creates a FUNCTION: a reusable block of code with a name.
def print_title(text):
    """Print a title surrounded by lines, e.g. ==== PART 1 ====."""
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)


# =====================================================================
# PART 1 - LOADING A LOCAL FILE (os + pandas)
# =====================================================================
print_title("PART 1 - Loading a local CSV file")

# A CSV ("Comma-Separated Values") file is a simple table saved as text.
# Each line is a row, and commas separate the columns. Open
# data/students_sample.csv in VS Code to see what it looks like inside!

# --- Step 1: Find out where we are ----------------------------------
# Every program runs "inside" a folder, called the WORKING DIRECTORY.
# When you give Python a file name, it looks for it in this folder.
print("Current working directory:", os.getcwd())

# --- Step 2: Build the path to our file -----------------------------
# __file__ is a special variable holding the location of THIS script.
# os.path.abspath() turns it into a full path, e.g. C:\Users\...\importing_data.py
# os.path.dirname() removes the file name and keeps only the folder.
# This way the script finds the data no matter where you run it from.
script_folder = os.path.dirname(os.path.abspath(__file__))

# os.path.join() glues folder and file names together using the correct
# separator for your system ("\" on Windows, "/" on Mac and Linux).
# Never type the slashes yourself - let os.path.join do it for you.
data_folder = os.path.join(script_folder, "data")
csv_path = os.path.join(data_folder, "students_sample.csv")
print("Looking for the file at:", csv_path)

# --- Step 3: Look inside the folder ---------------------------------
# os.listdir() returns a LIST with the names of everything in a folder.
print("Files inside the data folder:", os.listdir(data_folder))

# --- Step 4: Check the file exists before opening it ----------------
# os.path.exists() returns True or False. Checking first lets us show a
# friendly message instead of a scary error.
if os.path.exists(csv_path):
    print("Good news: the file exists!")
else:
    print("Oops: file not found. Check the folder name and the file name.")

# --- Step 5: Read the CSV into a DataFrame --------------------------
# pd.read_csv() reads the file and turns it into a DataFrame:
# pandas' name for a table with rows and columns (like an Excel sheet).
students = pd.read_csv(csv_path)

# --- Step 6: Explore the data ---------------------------------------
# .head() shows the first 5 rows. Use .head(10) to see 10, and so on.
print("\nFirst 5 rows:")
print(students.head())

# .shape tells us (number of rows, number of columns).
print("\nShape (rows, columns):", students.shape)

# .columns lists the column names.
print("Column names:", list(students.columns))

# .info() summarises each column: its data type and whether any values
# are missing. "int64" = whole numbers, "float64" = decimals,
# "object" = text.
print("\nInfo about each column:")
students.info()

# .describe() calculates quick statistics (mean, min, max...) for the
# number columns.
print("\nQuick statistics:")
print(students.describe())

# --- Step 7: A first tiny analysis ----------------------------------
# groupby("group") splits the table by the value in the "group" column,
# then .mean() computes the average exam score for each group.
print("\nAverage exam score per group:")
print(students.groupby("group")["exam_score"].mean())

# --- Bonus: other file types work almost the same way ---------------
# pandas has a "read_" function for many formats, for example:
#   pd.read_excel("file.xlsx")   -> Excel files (needs: pip install openpyxl)
#   pd.read_json("file.json")    -> JSON files
#   pd.read_csv("file.csv", sep=";")   -> CSV files that use ";" instead of ","


# =====================================================================
# PART 2 - LOADING DATA FROM AN API (requests + pandas)
# =====================================================================
print_title("PART 2 - Loading data from an API")

# An API ("Application Programming Interface") is a way for programs to
# ask a website for data. Instead of a web page made for humans, the API
# answers with raw data, usually in a format called JSON.
#
# We'll use Open-Meteo (https://open-meteo.com): a free weather API that
# doesn't need an account or a password ("API key").
# We'll ask it for the weather in Pamplona over the last 7 days.

# --- Step 1: Decide WHERE to ask (the URL) --------------------------
api_url = "https://api.open-meteo.com/v1/forecast"

# --- Step 2: Decide WHAT to ask (the parameters) --------------------
# Parameters are the "options" of our question. We store them in a
# DICTIONARY: pairs of  "name": value  inside curly braces { }.
params = {
    "latitude": 42.81,          # Pamplona's position on the map
    "longitude": -1.65,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "Europe/Madrid",
    "past_days": 7,             # include the last 7 days
    "forecast_days": 1,         # plus today
}

# --- Step 3: Send the request ---------------------------------------
# requests.get() sends our question to the API and waits for the answer.
# timeout=10 means "give up after 10 seconds if nobody answers".
#
# We wrap it in try/except: if something goes wrong (no internet, the
# website is down...), Python runs the "except" part instead of crashing.
try:
    response = requests.get(api_url, params=params, timeout=10)

    # Every answer comes with a STATUS CODE:
    #   200 = OK, everything worked
    #   404 = not found (wrong URL)
    #   500 = the server had a problem
    print("Status code:", response.status_code)

    # This line raises an error if the status code means "failed".
    response.raise_for_status()

    # --- Step 4: Read the JSON answer -------------------------------
    # .json() converts the answer into Python dictionaries and lists.
    data = response.json()

    # Let's see which "keys" (labels) the answer contains.
    print("Keys in the answer:", list(data.keys()))

    # The values we want live under the "daily" key. It looks like:
    #   {"time": [...dates...], "temperature_2m_max": [...], ...}
    # A dictionary of lists like this converts directly into a table.

    # --- Step 5: Turn it into a DataFrame ---------------------------
    weather = pd.DataFrame(data["daily"])

    # Rename the columns to friendlier names.
    weather = weather.rename(columns={
        "time": "date",
        "temperature_2m_max": "max_temp_C",
        "temperature_2m_min": "min_temp_C",
        "precipitation_sum": "rain_mm",
    })

    # The dates arrive as plain text. pd.to_datetime() converts them into
    # real dates, so pandas can sort them, filter them, plot them...
    weather["date"] = pd.to_datetime(weather["date"])

    print("\nWeather in Pamplona:")
    print(weather)

    # A quick calculation on our new table.
    print("\nAverage max temperature:", round(weather["max_temp_C"].mean(), 1), "C")

    # --- Step 6: Save a copy to a local file ------------------------
    # Saving means you don't need to call the API again next time.
    # index=False stops pandas from writing the row numbers as a column.
    output_path = os.path.join(data_folder, "pamplona_weather.csv")
    weather.to_csv(output_path, index=False)
    print("Saved a copy to:", output_path)

except requests.exceptions.RequestException as error:
    print("Could not get data from the API. Are you connected to the internet?")
    print("Details:", error)


# =====================================================================
# PART 3 - LOADING DATA FROM GOOGLE DRIVE
# =====================================================================
print_title("PART 3 - Loading data from Google Drive")

# There are two common ways to read a file stored in Google Drive:
#
#  A) MOUNTING Drive - only works inside GOOGLE COLAB (online notebooks).
#     Your whole Drive appears as a folder. See the notebook version of
#     this lesson for that method.
#
#  B) A SHARE LINK - works everywhere, including this script.
#     That's what we do here.
#
# How to get a share link for your own file:
#   1. In Google Drive, right-click your CSV file -> "Share".
#   2. Under "General access" choose "Anyone with the link".
#   3. Click "Copy link". It looks like this:
#        https://drive.google.com/file/d/1AbCdEfGhIjKlMnOp/view?usp=sharing
#   4. The FILE ID is the long code between "/d/" and "/view":
#        1AbCdEfGhIjKlMnOp
#   5. Paste it below, between the quotes.
#
# WARNING: "Anyone with the link" means exactly that. Never share files
# with personal or private data this way.

DRIVE_FILE_ID = ""   # <-- paste your file ID here, e.g. "1AbCdEfGhIjKlMnOp"

# An empty text "" counts as False, so this checks "did you paste an ID?"
if DRIVE_FILE_ID:
    # This special URL asks Google Drive for the raw file instead of the
    # preview page. The f"..." (an "f-string") puts the value of
    # DRIVE_FILE_ID inside the text where the { } are.
    drive_url = f"https://drive.google.com/uc?export=download&id={DRIVE_FILE_ID}"

    try:
        # pd.read_csv() can read straight from a web address,
        # not only from files on your computer!
        drive_data = pd.read_csv(drive_url)
        print("Loaded from Google Drive:")
        print(drive_data.head())
        print("Shape (rows, columns):", drive_data.shape)
    except Exception as error:
        print("Could not read the file. Check that:")
        print("  - the ID is correct")
        print("  - the file is shared as 'Anyone with the link'")
        print("  - the file is a CSV (not a Google Sheet or Excel file)")
        print("Details:", error)
else:
    print("No Google Drive file ID set - skipping this part.")
    print("Open this script, paste your ID into DRIVE_FILE_ID and run it again.")


# =====================================================================
# SUMMARY
# =====================================================================
print_title("Done!")
print("""
What you practised today:
  * os.getcwd(), os.path.join(), os.listdir(), os.path.exists()
      -> finding files on your computer
  * pd.read_csv()
      -> turning a file (or a web link) into a DataFrame
  * requests.get() + .json() + pd.DataFrame()
      -> getting data from an API
  * .head(), .shape, .info(), .describe(), .groupby()
      -> taking a first look at any dataset
  * .to_csv()
      -> saving your data for later

Challenge: change the latitude and longitude in PART 2 to your home town
and run the script again!
""")
