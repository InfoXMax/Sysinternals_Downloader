# Sysinternals Suite Downloader

Sysinternals Suite Downloader is a Python script that allows you to easily download Sysinternals utilities from the official Sysinternals website. It provides a user-friendly interface for selecting and downloading individual utilities or multiple utilities in parallel. Additionally, it displays progress bars for each download and provides information about the files.

## Features

- Download Sysinternals utilities from the official website.
- Select and download multiple utilities simultaneously.
- Display progress bars for each download.
- Show file information, including size.
- User-friendly command-line interface.

## Requirements

- Python 3.x
- The following Python packages (you can install them using `pip`):

```bash
pip install requests
pip install beautifulsoup4
pip install tqdm
```

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the project directory.

3. Run the script using the following command:
```bash
python sysinternals.py
```

4. Follow the on-screen instructions to choose and download Sysinternals utilities.

## How it Works

1. The script fetches the directory listing from the official Sysinternals website.

2. It parses the HTML content to extract the list of available utilities.

3. You are presented with a numbered list of utilities along with their download links and file information.

4. You can enter the numbers of the utilities you want to download (comma-separated) or enter '0' to exit.

5. Selected utilities are downloaded in parallel, and progress bars are displayed for each download.

6. The downloaded files are saved in a 'Downloads' folder within the project directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script uses the [requests](https://docs.python-requests.org/en/latest/) library for HTTP requests.
- HTML parsing is done using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/).
- Progress bars are created using [tqdm](https://github.com/tqdm/tqdm).

## Contributing

Contributions to this project are welcome! If you have any ideas for improvements or new features, feel free to open an issue or create a pull request.

## Author

InfoXMax

## Disclaimer

This script is provided for educational and convenience purposes only. Use it responsibly and in accordance with the terms and conditions of the Sysinternals website.

