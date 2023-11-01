import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_book_data(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find('h1').text.strip()
        price = soup.find('p', class_='price_color').text.strip()
        availability = soup.find('p', class_='instock availability').text.strip()

        return {
            'Title': title,
            'Price': price,
            'Availability': availability
        }


async def main():
    urls = [
        'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html',
        'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html',
        'http://books.toscrape.com/catalogue/soumission_998/index.html',
    ]

    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(get_book_data(url))

        results = await asyncio.gather(*tasks)

        for result in results:
            print('Title:', result['Title'])
            print('Price:', result['Price'])
            print('Availability:', result['Availability'])
            print('---')

asyncio.run(main())


