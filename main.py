import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://surfcaptain.com/forecast/oceanside-california"

# Send GET request to the website
response = requests.get(url)

s = BeautifulSoup(response.content, 'html.parser')

# Check if the request was successful (status code 200)
results = s.find(id='fcst-current')

overview = results.find('h1', class_='cell auto')

#additional = s.find(id='fcst-current')

#minis = additional.find_all('ul', class_='grid-x current-data-container')

#print(overview).text
#for swell in minis:
#print(minis.txt)
# Create an HTML file
with open('Forecast.html', 'w') as file:
    # Write the HTML content
    file.write("<html><head>")
    file.write("<style>")
    file.write("body { font-family: Arial, sans-serif; }")
    file.write("h1 { border: 2px solid black; background-color: lightblue; padding: 10px; }")
    file.write("</style>")
    file.write("</head><body>")
    file.write(str(overview))
    file.write("</body></html>")
print("HTML file created successfully.")