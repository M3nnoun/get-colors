import requests
from bs4 import BeautifulSoup
import csv

def process_td(td_tag):
    span = td_tag.find('span')
    container_div = td_tag.find('div')
    div = container_div.find('div')
    
    if span:
        color_title = span.text
        # print("Value of color:", color_title)
    
    if div:
        bg_color = div.get('style')  # Get the "style" attribute to extract the background color
        if bg_color:
            bg_color = bg_color.split(':')[-1].strip(';').strip()
            # print("Background color is:", bg_color)
    return [color_title,bg_color]

def save_dict_to_csv(data_dict, file_path):
    # Create a list of dictionaries with keys as 'Index', 'Name', and 'Color'
    data_list = [{'Index': key, 'Name': value[0], 'Color': value[1]} for key, value in data_dict.items()]

    # Define the order of the columns
    fieldnames = ['Index', 'Name', 'Color']

    # Write the data to a CSV file
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header row
        writer.writeheader()
        
        # Write the data rows
        writer.writerows(data_list)

url = 'https://www.magasindepeinture.ch/en/ncs-color-chart-online.html'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    data={}
    table = soup.find('table')
    td_tags = table.find_all('td')

    # Count the number of <td> tags
    td_count = len(td_tags)
    # print(process_td(td_tags[0]))
    for count,td in enumerate(td_tags):
        print(f"<<< get Data of item {count+1}>>>")
        data[count+1]=process_td(td)
    print(data)
    file_path = 'data.csv'

    save_dict_to_csv(data, file_path)
    
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
