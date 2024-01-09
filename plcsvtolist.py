import csv
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import pandas as pd
import numpy as np
import re
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import requests
# sending HTTP requests and handling responses in Python
from bs4 import BeautifulSoup

csv_file_path = r"C:\Users\Aniket\Downloads\all_players.csv"

# Initialize an empty list to store the CSV data
csv_data = []

# Open the CSV file and read its contents
with open(csv_file_path, newline='') as file:
    csv_reader = csv.reader(file)

    # Iterate through each row in the CSV file and append it to the list
    for row in csv_reader:
        csv_data.extend(row)

# Display the list containing the CSV data
# print(csv_data)

df_plist = []
test_title = ['Full Name', 'TEAMS', 'Batting Style', 'Bowling Style', 'Playing Role']
for player_link in csv_data:
  webpage4 = requests.get(player_link).text
  # webpage.status_code
  soup = BeautifulSoup(webpage4, 'lxml')

  div_team = soup.find('div', class_='ds-grid lg:ds-grid-cols-3 ds-grid-cols-2 ds-gap-y-4')
  team_name = div_team.find('a').text
  title_tags = soup.find_all('p', class_="ds-text-tight-m")[0:12]
  title_tags
  title_detail = soup.find_all('span', class_="ds-text-title-s")[0:12]
  title_detail
  name_tag = soup.find('h1', class_='ds-text-title-l ds-font-bold').text

  details = {}
  for i, j in zip(title_tags, title_detail):
    dict = {i.text.strip(): j.text.strip()}
    details.update(dict)

  details['Full Name'] = name_tag
  details['TEAMS'] = team_name
  df = pd.DataFrame(columns = test_title)

  individual_p = []
  for i in df.columns:
    if i in details.keys():
      individual_p.append(details[i])
    else:
      individual_p.append(np.nan)

  length = len(df)
  df.loc[length] = individual_p

  desc_tag = soup.find_all('div', class_='ci-player-bio-content')
  if desc_tag:
    description = desc_tag[0].text
  else:
    description = np.nan
  df["description"] = description

  chrome_options = Options()
  chrome_options.add_argument("--headless")
  driver = Chrome(options=chrome_options)
  driver.get(player_link)

  soup = BeautifulSoup(driver.page_source, 'lxml')
  # div_tag = soup.find('div', class_='ds-ml-auto ds-w-48 ds-h-48')
  img_tag = soup.find('img')
  if img_tag is not None:
    image_link = img_tag.get('src')
  else:
    image_link = np.nan

  print(image_link)

  driver.quit()

  df["imageurl"] = image_link
  df_plist.append(df)

result1 = pd.concat(df_plist, axis=0)
result1.to_csv('player_final.csv', index=False)

print("done")