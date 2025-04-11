from playwright.sync_api import sync_playwright
import os, json, threading, time

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

def threadSaving(urlLen, urls):
    for i in range(urlLen):
        capture_screenshot(urls[i])

if __name__ == "__main__":
    urls = readJson('urls.json')
    urlLength = len(urls)
    
    if urlLength % 3 == 0:
        urls1 = urls[:urlLength//3]
        urls2 = urls[urlLength//3:urlLength//3*2]
        urls3 = urls[urlLength//3*2:]
        
        thread1 = threading.Thread(target=threadSaving, args=(urlLength//3, urls1))
        thread2 = threading.Thread(target=threadSaving, args=(urlLength//3, urls2))
        thread3 = threading.Thread(target=threadSaving, args=(urlLength//3, urls3))
        
        thread1.start()
        thread2.start()
        thread3.start()
    elif urlLength % 5 == 0:
        urls1 = urls[:urlLength//5]
        urls2 = urls[urlLength//5:urlLength//5*2]
        urls3 = urls[urlLength//5*2:urlLength//5*3]
        urls4 = urls[urlLength//5*3:urlLength//5*4]
        urls5 = urls[urlLength//5*4:]
        
        thread1 = threading.Thread(target=threadSaving, args=(urlLength//5, urls1))
        thread2 = threading.Thread(target=threadSaving, args=(urlLength//5, urls2))
        thread3 = threading.Thread(target=threadSaving, args=(urlLength//5, urls3))
        thread4 = threading.Thread(target=threadSaving, args=(urlLength//5, urls4))
        thread5 = threading.Thread(target=threadSaving, args=(urlLength//5, urls5))
        
        thread1.start()
        thread2.start()
        thread3.start() 
        thread4.start()
        thread5.start()
    elif urlLength % 4 == 0:
        urls1 = urls[:urlLength//4]
        urls2 = urls[urlLength//4:urlLength//4*2]
        urls3 = urls[urlLength//4*2:urlLength//4*3]
        urls4 = urls[urlLength//4*3:]
        
        thread1 = threading.Thread(target=threadSaving, args=(urlLength//4, urls1))
        thread2 = threading.Thread(target=threadSaving, args=(urlLength//4, urls2))
        thread3 = threading.Thread(target=threadSaving, args=(urlLength//4, urls3)) 
        thread4 = threading.Thread(target=threadSaving, args=(urlLength//4, urls4))
    else:
        print('Update this script dumbass')
    