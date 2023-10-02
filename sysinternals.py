import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# Function to download a file
def download_file(url, filename):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 KB
    downloaded_size = 0

    with open(filename, 'wb') as file, tqdm(
        total=total_size,
        unit='B',
        unit_scale=True,
        desc=os.path.basename(filename),
        ascii=True,
    ) as progress_bar:
        for data in response.iter_content(block_size):
            downloaded_size += len(data)
            file.write(data)
            progress_bar.update(len(data))

    print(f"\nDownloaded {os.path.basename(filename)} to 'Downloads' folder.")

# URL of the directory listing
url = "https://live.sysinternals.com/"

# Send an HTTP GET request to fetch the HTML content of the directory listing
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the 'a' tags (links) in the HTML
    links = soup.find_all("a")

    # Create a 'Downloads' folder if it doesn't exist
    os.makedirs("Downloads", exist_ok=True)

    # Generate a numbered list of download links with file information
    download_links = []
    for index, link in enumerate(links):
        href = link.get("href")
        if href.endswith(".exe") or href.endswith(".chm") or href.endswith(".txt"):
            download_link = f"{url}{href}"
            download_links.append((download_link, os.path.basename(download_link)))
            print(f"{index + 1}: {download_link} ({link.text.strip()})")

    # Prompt the user to choose files to download
    while True:
        try:
            choices = input("Enter the numbers of the files you want to download (comma-separated, 0 to exit): ")
            if choices == '0':
                break

            selected_choices = [int(choice) for choice in choices.split(',') if choice.isdigit()]
            selected_links = [download_links[i - 1] for i in selected_choices if 1 <= i <= len(download_links)]

            if not selected_links:
                print("Invalid choices. Please enter valid numbers.")
                continue

            # Download selected files in parallel
            with ThreadPoolExecutor(max_workers=5) as executor:
                for download_link, filename in selected_links:
                    filename = os.path.join("Downloads", filename)
                    executor.submit(download_file, download_link, filename)

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
else:
    print(f"Failed to retrieve the directory listing. Status code: {response.status_code}")
