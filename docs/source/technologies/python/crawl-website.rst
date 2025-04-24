Crawl Website
=============

.. title:: Crawl Website - Learn to crawl a website using Python and BeautifulSoup
.. meta::
    :description: Learn to crawl a website using Python and BeautifulSoup
    :keywords: python, web scraping, beautifulsoup, crawl website, python tutorial   

Web crawling is the automated process of systematically browsing and retrieving information from websites on the internet. 
It involves using software programs (called crawlers, spiders, or bots) that follow links from one web page to another, 
downloading content, extracting specific data, and often storing that information for later analysis or indexing.

.. include::  /_templates/components/banner-top.rst

Key characteristics of web crawling include:
--------------------------------------------

1. **Automation**: Web crawlers work without human intervention, following programmed rules to navigate websites.

2. **Discovery**: Crawlers typically start with a list of URLs (seeds) and discover new pages by following links within those pages.

3. **Data extraction**: Crawlers can be programmed to extract specific types of content from pages, such as text, images, links, prices, or any other structured data.

4. **Systematic approach**: Rather than random browsing, crawlers follow methodical patterns to cover sites completely or target specific sections.

5. **Respectful behavior**: Properly designed crawlers follow ethical guidelines and technical standards like robots.txt directives, which specify which parts of a site can or cannot be crawled.


Common uses of web crawling:
----------------------------

- Search engine indexing (how Google, Bing, etc. build their databases)
- Data mining and market research
- Price monitoring and comparison
- Content aggregation
- Academic research
- Website archiving
- Monitoring for changes to web pages

Web crawling differs from web scraping in that crawling focuses on navigating and discovering content across multiple pages or sites, 
while scraping refers specifically to the extraction of data from websites. 

In practice, these terms are often used together, as crawling typically involves some level of data extraction.


Simple Crawler for `App-Generator </>`__
----------------------------------------

This script demonstrates how to use Beautiful Soup (BS4) to crawl the app-generator.dev homepage and extract specific information into a JSON file.

Prerequisites
*************

First, make sure you have the required libraries installed:

.. code-block:: bash 

    pip install requests beautifulsoup4


The Script
**********

Here's a simple script that extracts navigation links, latest products, and blog articles from app-generator.dev:

.. code-block:: python 

    import requests
    from bs4 import BeautifulSoup
    import json
    import time

    def crawl_app_generator():
        """
        Crawls app-generator.dev homepage and extracts:
        - Navigation links
        - Latest products
        - Blog articles
        
        Returns a dictionary with the extracted data.
        """
        # Set a user agent to identify our crawler
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }
        
        # URL to crawl
        url = 'https://app-generator.dev'
        
        print(f"Crawling {url}...")
        
        try:
            # Add a small delay to be polite
            time.sleep(1)
            
            # Fetch the page
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Raise an exception for 4XX/5XX status codes
            
            # Parse the HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Initialize our results dictionary
            results = {
                'navigation_links': [],
                'latest_products': [],
                'blog_articles': []
            }
            
            # Extract navigation links (typically in the header navigation)
            print("Extracting navigation links...")
            nav_elements = soup.select('header nav a')  # Adjust selector as needed
            for link in nav_elements:
                href = link.get('href', '')
                text = link.get_text(strip=True)
                if href and text:
                    results['navigation_links'].append({
                        'text': text,
                        'url': href if href.startswith('http') else f"{url}{href}"
                    })
            
            # Extract latest products
            print("Extracting latest products...")
            product_elements = soup.select('.product-card, .product-item')  # Adjust selector as needed
            if not product_elements:
                # Try alternative selectors if the first one doesn't find elements
                product_elements = soup.select('.card, .product, [class*="product"]')
            
            for product in product_elements:
                product_name = product.select_one('h2, h3, .product-title')
                product_link = product.select_one('a')
                product_desc = product.select_one('p, .description')
                
                if product_name and product_link:
                    results['latest_products'].append({
                        'name': product_name.get_text(strip=True) if product_name else 'No name',
                        'url': product_link.get('href', '') if product_link else '',
                        'description': product_desc.get_text(strip=True) if product_desc else 'No description'
                    })
            
            # Extract blog articles
            print("Extracting blog articles...")
            article_elements = soup.select('.blog-post, article, .post')  # Adjust selector as needed
            if not article_elements:
                # Try alternative selectors if the first one doesn't find elements
                article_elements = soup.select('[class*="blog"], [class*="article"], .card')
            
            for article in article_elements:
                article_title = article.select_one('h2, h3, .title')
                article_link = article.select_one('a')
                article_date = article.select_one('.date, time')
                
                if article_title and article_link:
                    results['blog_articles'].append({
                        'title': article_title.get_text(strip=True) if article_title else 'No title',
                        'url': article_link.get('href', '') if article_link else '',
                        'date': article_date.get_text(strip=True) if article_date else 'No date'
                    })
            
            return results
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the page: {e}")
            return None
        except Exception as e:
            print(f"Error parsing the page: {e}")
            return None

    def save_to_json(data, filename='app_generator_data.json'):
        """Save the extracted data to a JSON file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Data successfully saved to {filename}")
            return True
        except Exception as e:
            print(f"Error saving data to {filename}: {e}")
            return False

    def main():
        # Crawl the website
        data = crawl_app_generator()
        
        if data:
            # Display summary
            print("\nCrawl Summary:")
            print(f"Navigation Links: {len(data['navigation_links'])}")
            print(f"Latest Products: {len(data['latest_products'])}")
            print(f"Blog Articles: {len(data['blog_articles'])}")
            
            # Save to JSON file
            save_to_json(data)
        else:
            print("Crawling failed. No data to save.")

    if __name__ == "__main__":
        main()

How It Works
************

1. **Request the webpage**: The script uses the `requests` library to fetch the HTML content of app-generator.dev.

2. **Parse the HTML**: Beautiful Soup parses the HTML content into a structured format that we can query.

3. **Extract data**: The script extracts three types of data:
   - Navigation links from the header menu
   - Product listings (with fallback selectors)
   - Blog articles (with fallback selectors)

4. **Save to JSON**: The extracted data is saved to a JSON file with a structured format.


Adjusting the Selectors
***********************

The CSS selectors used in this script are based on common naming conventions. However, websites use different HTML structures, so you might need to adjust the selectors.

To find the correct selectors:

1. Visit app-generator.dev in your browser
2. Right-click on an element you want to extract (e.g., a navigation link)
3. Select "Inspect" or "Inspect Element"
4. Look at the HTML structure and find appropriate CSS selectors

## Handling Website Changes

If the website structure changes, you may need to update the selectors. Look for these common patterns:

- Navigation links are usually in `<nav>` elements or list items `<li>` within header sections
- Products often have class names containing "product", "card", or "item"
- Blog articles are typically in elements with class names like "post", "article", or "blog"

Additional Considerations
*************************

- This script respects web scraping etiquette with appropriate delays and headers
- It has fallback selectors to handle different HTML structures
- Error handling ensures the script doesn't crash on network issues

If you encounter "403 Forbidden" errors, the website might be blocking scrapers. In that case, try:
- Using more authentic browser headers
- Adding more delay between requests
- Implementing a session with cookies

Endnote on Web Crawling
-----------------------

Web crawling represents one of the foundational technologies that has shaped our digital landscape, enabling the vast information accessibility we often take for granted. 
While search engines are the most visible application, the concept extends far beyond, serving as a critical bridge between dispersed web content and organized, actionable data.

.. include::  /_templates/components/footer-links.rst
