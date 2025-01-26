# Amazon Trending Products Scraper

A browser automation agent that extracts the top 5 trending products from Amazon using Google's Gemini language model and Browser-Use library.

## Features

- Automatically navigates to Amazon's Best Sellers page
- Extracts product names and URLs
- Saves results in JSON format
- Uses Google's Gemini 2.0 Flash model for AI-powered web interaction
- Headless browser capabilities

## Prerequisites

- Python 3.11+
- Google Gemini API key (free tier available)
- Windows 10 with VS Code (cross-platform compatible)
- Playwright browsers installed

## Installation

1. **Create and activate virtual environment**
```powershell
uv venv --python 3.11
.\.venv\Scripts\activate
Install dependencies

powershell

uv pip install browser-use langchain-google-genai python-dotenv pydantic
playwright install
Configuration
Create .env file in project root:

env

GEMINI_API_KEY=your_api_key_here
Get Gemini API key

Usage
Run the scraper:

powershell

python amazon_agent.py
Output will be saved to:

json

amazon_trending_products.json
Sample Output:

json

{
  "products": [
    {
      "product_name": "Amazon Basics AAA 1.5 Volt Performance Alkaline Batteries",
      "product_url": "https://www.amazon.com/dp/B00LH3DMUO"
    },
    {
      "product_name": "Echo Dot (5th Gen) | Smart speaker with Alexa",
      "product_url": "https://www.amazon.com/dp/B09B8V1LZ3"
    }
  ]
}
Customization Options
Change target URL
Modify the URL in amazon_agent.py:

python

task = "Go to Amazon's Best Sellers page (https://www.amazon.com/Best-Sellers/zgbs)..."
Adjust output format
Modify the Product model in amazon_agent.py:

python

class Product(BaseModel):
    product_name: str
    product_url: str
    # Add new fields
    price: Optional[str]
    rating: Optional[float]
Switch Gemini model
Available options: gemini-2.0-flash-exp (fast) or gemini-pro (more capable)

python

llm = ChatGoogleGenerativeAI(
    model='gemini-pro',
    api_key=os.getenv('GEMINI_API_KEY')
)
Troubleshooting
Common Issues:

Amazon blocking requests:

Add headless=False to BrowserConfig

Increase page load wait times

python

from browser_use import BrowserConfig

agent = Agent(
    task=task,
    llm=llm,
    controller=controller,
    browser_config=BrowserConfig(
        headless=False,
        new_context_config=BrowserContextConfig(
            wait_for_network_idle_page_load_time=3.0
        )
    )
)
API key errors: Verify .env file formatting and key validity

Element detection failures: Try different Gemini model version

Disclaimer
This project is for educational purposes only. Always respect website terms of service and robots.txt files. Consider adding delays between requests to avoid overwhelming target servers.

License
MIT License
