# Myntra Review Scraper Project

## Project Detail/Summary

This project is a Myntra review scraper that allows users to extract and analyze customer reviews from the Myntra website. The scraper collects valuable information, such as product ratings, reviews, and user feedback, providing insights into customer sentiments and preferences.

## How to Setup Locally

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/PWskills-DataScienceTeam/myntra-review-scrapper.git
   cd myntra-review-scraper
   ```

2. Create a new conda environment and activate it
```bash
conda create -p ./env python=3.10 -y
#to activate the environment
conda activate ./env 
#or 
source activate ./env
```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Replace the environment variable in `.env` file
    Add the MongoDB environment variable in the `.env` file

4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

5. Access the application in your web browser at [http://localhost:8501](http://localhost:8501).

## Dependencies

The project relies on the following dependencies:

- Streamlit: A Python library for creating interactive web applications with ease.
- MongoDB: A NoSQL database used to store and manage extracted data.
- database-connect: A package used to simplify the connection to MongoDB.

## Replacing chromedriver.exe with ChromeDriver Binary

The decision to replace `chromedriver.exe` with the `ChromeDriver binary pypi package` was made to provide better compatibility and flexibility across different operating systems. By using the binary, users can easily switch between operating systems without the need to manage different driver versions.

## MongoDB Connection

The project utilizes MongoDB as the backend database for storing scraped data. The `database-connect` package is employed to streamline the connection process, making it easier for developers to interact with MongoDB in their applications.

Feel free to explore the codebase and customize the scraper to suit your specific requirements. If you encounter any issues or have suggestions for improvement, please open an issue on the GitHub repository.

Happy scraping! 🕵️‍♂️🚀