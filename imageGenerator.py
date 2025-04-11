from playwright.sync_api import sync_playwright
import os, json

def capture_screenshot(url, output_path='files\webImages', full_page=False):
    """
    Capture a screenshot of a website.
    
    Args:
        url (str): URL of the webpage to capture
        output_path (str): Path to save the screenshot
        full_page (bool): Whether to capture the full page or just viewport
    """
    with sync_playwright() as p:
        # Launch browser in headless mode
        browser = p.chromium.launch(headless=True)
        
        # Create new page
        page = browser.new_page()
        
        try:
            # Navigate to URL
            page.goto(url)
            
            # Wait for page to load
            page.wait_for_timeout(5000)  # 5 second timeout
            
            # Capture screenshot
            page.screenshot(path=output_path, full_page=full_page)
            
            print(f"Screenshot saved to {os.path.abspath(output_path)}")
            
        except Exception as e:
            print(f"Error capturing screenshot: {str(e)}")
            
        finally:
            # Clean up resources
            browser.close()

def readJson(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

if __name__ == "__main__":
    urls = readJson('urls.json')
    for url in urls:
        print(url)