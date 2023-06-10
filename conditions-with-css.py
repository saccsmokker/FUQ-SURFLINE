import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://surfcaptain.com/forecast/oceanside-california"  # Replace with the desired website URL

# Send GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Create BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the <ul> element by class
    ul = soup.find("ul", id="fcst-current-data")  # Replace "your-ul-class" with the actual class name

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
        with open("conditions-with-css.html", "w", encoding="utf-8") as file:
            file.write(html_content)
        print("Data written to output.html file.")
    else:
        print("No <ul> element found on the website")
else:
    print("Error occurred while fetching the website")
