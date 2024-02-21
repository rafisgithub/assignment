import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Load Excel file
excel_file_path = "D:\Python\AssignementOnSelenium\Excel.xlsx"
days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Create a Chrome webdriver instance
driver = webdriver.Chrome()
driver.maximize_window()

for day in days_of_week:
    # Read data for the current day
    df = pd.read_excel(excel_file_path, sheet_name=day)

    # Go to www.google.com
    driver.get("https://www.google.com/")

    # Iterate through each row in the Excel sheet
    for index, row in df.iterrows():
        keyword = row['Keyword']

        # Write the keyword in the search box
        search_box = driver.find_element("name", "q")
        search_box.clear()
        search_box.send_keys(keyword)

        # Press Enter
        search_box.send_keys(Keys.ENTER)

        # Wait for search results to load
        time.sleep(2)  # Adjust the sleep time based on your network speed and page load time

        # Find the longest and shortest options
        search_results = driver.find_elements_by_css_selector('h3')
        if search_results:
            longest_option = max(search_results, key=lambda x: len(x.text)).text
            shortest_option = min(search_results, key=lambda x: len(x.text)).text
        else:
            longest_option = shortest_option = "No results found"

        # Update the Excel sheet with the results
        df.at[index, 'Longest Option'] = longest_option
        df.at[index, 'Shortest Option'] = shortest_option

    # Save the updated Excel file for the current day
    df.to_excel(excel_file_path, sheet_name=day, index=False)

# Close the browser
driver.quit()
