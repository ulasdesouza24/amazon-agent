# Amazon Trending Products Scraper

A browser automation agent using the [browser-use](https://github.com/browser-use/browser-use) library and Google's Gemini model to extract Amazon's top trending products.

## Features

- Utilizes **browser-use** for reliable browser automation.
- Leverages Google's Gemini 2.0 Flash model for AI-powered web interaction.
- Extracts product names and URLs from Amazon's Best Sellers.
- Saves structured JSON output.
- Headless browser capabilities via Playwright.

## Technologies

- [browser-use](https://github.com/browser-use/browser-use) (v0.2.0+).
- Google Gemini Language Model.
- Playwright browser automation.
- Pydantic data validation.

## Prerequisites

- Python 3.11+
- Google Gemini API key ([free tier available](https://aistudio.google.com/app/apikey)).
- Playwright browsers installed.
- Windows/macOS/Linux with VS Code.

## Installation

### 1. Set up a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.\.venv\Scripts\activate  # Windows
```

### 2. Install dependencies

```bash
pip install browser-use langchain-google-genai python-dotenv pydantic
playwright install
```

### 3. Configure API keys

Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

## Usage

### Run the browser-use agent

```bash
python amazon_agent.py
```

The output will be saved as `amazon_trending_products.json` in the project directory.

## browser-use Configuration

The agent uses the following key `browser-use` features:

- **Controller**: For action management and validation.
- **Agent History**: Tracks execution steps and results.
- **Browser Context**: Manages browser sessions.
- **Vision Capabilities**: Enabled by default for improved element detection.

### Example Configuration

```python
from browser_use import BrowserConfig, BrowserContextConfig

agent = Agent(
    task=task,
    llm=llm,
    controller=controller,
    browser_config=BrowserConfig(
        headless=False,
        new_context_config=BrowserContextConfig(
            browser_window_size={"width": 1600, "height": 900}
        )
    )
)
```

## Customization

### Adjust Extraction Logic

You can modify the `amazon_agent.py` script to include additional fields like current price:

```python
class Product(BaseModel):
    product_name: str
    product_url: str
    current_price: str  # New field
```

## Limitations

- Requires careful configuration to avoid Amazon bot detection.
- Dependent on Amazon's page structure remaining consistent.
- Google Gemini model costs may apply after free quota usage.

## Support

For issues related to `browser-use`, consult the official [documentation](https://docs.browser-use.com/introduction).

## Disclaimer

This project is for educational purposes only. Respect website terms of service and robots.txt files. Add delays between requests to avoid overwhelming servers.

## License

This project is licensed under the MIT License.

