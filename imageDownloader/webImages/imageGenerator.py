from playwright.sync_api import sync_playwright
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import logging, json
from typing import List, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class URLScreenshotter:
    def __init__(self, max_workers: int = 10):
        self.max_workers = max_workers
        
    def capture_url(self, url: str) -> Tuple[str, bool]:
        """Capture a single URL screenshot."""
        try:
            # Create filename from URL
            filename = f"screenshot_{Path(url).stem}.png"
            
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                context = browser.new_context()
                page = context.new_page()
                
                # Navigate to URL with timeout
                page.goto(url, wait_until="networkidle", timeout=30000)
                
                # Save screenshot
                page.screenshot(path='imageDownloader/webImages/'+filename)
                
                # Cleanup
                browser.close()
                
            return filename, True
            
        except Exception as e:
            logging.error(f"Error capturing {url}: {str(e)}")
            return url, False

    def capture_urls(self, urls: List[str]):
        """Capture screenshots for multiple URLs concurrently."""
        results = []
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self.capture_url, url): url for url in urls}
            
            for future in futures:
                url = futures[future]
                result = future.result()
                results.append(result)
                logging.info(f"Processed {url}: {'Success' if result[1] else 'Failed'}")
        
        return results

def main():
    # Example usage
    with open('imageDownloader/urls.json', 'r', encoding='utf-8') as f:
        urls = json.load(f)
    
    screenshotter = URLScreenshotter(max_workers=3)
    results = screenshotter.capture_urls(urls)
    
    # Print summary
    successful = sum(1 for _, success in results if success)
    print(f"\nSummary:")
    print(f"Total URLs: {len(urls)}")
    print(f"Successful captures: {successful}")
    print(f"Failed captures: {len(results) - successful}")

if __name__ == "__main__":
    main()