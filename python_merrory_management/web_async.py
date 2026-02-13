import asyncio
import aiohttp
import time

# 1. Define the asynchronous fetch function
async def fetch_url(session, url):
    try:
        # Measure speed for individual request
        start_request = time.perf_counter()
        async with session.get(url, timeout=10) as response:
            status = response.status
            # Ensure we read the body to complete the request
            text = await response.text()
            end_request = time.perf_counter()
            print(f"✅ Success: {url} | Status: {status} | Time: {end_request - start_request:.2f}s")
            return len(text)
    except Exception as e:
        # 2. Handle errors (timeouts, connection issues, etc.)
        print(f"❌ Error: {url} | Exception: {type(e).__name__}")
        return None

# 3. Coordinate concurrent execution
async def main():
    urls = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.python.org",
        "https://www.stackoverflow.com",
        "https://httpbin.org"  # Intentionally slow to show concurrency
    ]
    
    # Measure total execution time
    start_total = time.perf_counter()
    
    # Use a single ClientSession for efficiency
    async with aiohttp.ClientSession() as session:
        # 4. Fetch URLs concurrently using asyncio.gather
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        
    end_total = time.perf_counter()
    print(f"\n🚀 Total Scrape Time: {end_total - start_total:.2f} seconds")
    print(f"Total Pages Successfully Scraped: {len([r for r in results if r is not None])}")

if __name__ == "__main__":
    asyncio.run(main())
