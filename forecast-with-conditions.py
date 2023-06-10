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
ul = s.find("ul", id="fcst-current-data")  # Replace "your-ul-class" with the actual class name

    # Check if <ul> element is found
if ul:
        # Find all immediate child <div> elements directly under the <ul>
        divs = ul.select("div")

        # Create a set to store unique div contents
        unique_divs = set()

        # Iterate over the <div> elements
        for div in divs:
            # Extract the data from each <div>
            div_data = div.text.strip()

            # Add the div content to the set
            unique_divs.add(div_data)

        # Create an HTML string to store the cleaned up data
        html_content = """<!DOCTYPE html>
        <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                .container {
                    max-width: 600px;
                    margin: 0 auto;
                }
                .div-item {
                    margin-bottom: 10px;
                    padding: 10px;
                    border: 1px solid #ddd;
                    background-color: #f9f9f9;
                }
            </style>
        </head>
        <body>
            <div class="container">
        """

        # Iterate over the unique div contents
        for div_data in unique_divs:
            # Format each unique div content within HTML tags
            html_content += f'<div class="div-item">{div_data}</div>\n'

        # Close the HTML structure
        html_content += """
            </div>
        </body>
        </html>
        """

        # Write the HTML content to a file


#minis = additional.find_all('ul', class_='grid-x current-data-container')

#print(overview).text
#for swell in minis:
#print(minis.txt)//tying something out here i cant remember what it was at the time///
# Create an HTML file
with open("Forcast-with-conditions.html", "w", encoding="utf-8") as file:
    file.write(html_content)
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