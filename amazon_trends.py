import os
import sys
import json
import asyncio
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Controller

# Setup environment
load_dotenv()
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Define data model
class Product(BaseModel):
    product_name: str
    product_url: str

class Products(BaseModel):
    products: List[Product]

# Initialize controller with our model
controller = Controller(output_model=Products)

async def main():
    task = "Go to Amazon's Best Sellers page (https://www.amazon.com/Best-Sellers/zgbs) and list the first 5 products"
    
    # Initialize Gemini model
    llm = ChatGoogleGenerativeAI(
        model='gemini-2.0-flash-exp',
        api_key=os.getenv('GEMINI_API_KEY')
    )
    
    # Create agent
    agent = Agent(
        task=task,
        llm=llm,
        controller=controller
    )

    # Run agent
    history = await agent.run()
    
    # Process results and save to JSON
    if history.final_result():
        parsed = Products.model_validate_json(history.final_result())
        
        # Convert to dictionary and save
        output_data = parsed.model_dump()
        with open('amazon_trending_products.json', 'w') as f:
            json.dump(output_data, f, indent=2)
            
        print("Successfully saved results to amazon_trending_products.json")
    else:
        print("No results found")

if __name__ == '__main__':
    asyncio.run(main())