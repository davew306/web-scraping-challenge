from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests

def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url1 = 'https://redplanetscience.com/'
    browser.visit(url1)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_title = soup.title
    news_title
    results = soup.find_all('div', class_='card-body')
    for result in results:

    try:

        news_p = result.find('p', class_='card-text').text

        if (news_p):
            print('-------------')
            print(news_p)
    except AttributeError as e:
        print(e)

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser2 = Browser('chrome', **executable_path, headless=False)
    url2 = 'https://spaceimages-mars.com'
    browser2.visit(url2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find('div', class_='floating_text_area')
    image = results.find('a', class_= 'showimg fancybox-thumbs')
    image_url = image['href']
    featured_image_url = url2 + "/" + image_url

    import pandas as pd

    url3 = 'https://galaxyfacts-mars.com'
    tables_df = pd.read_html(url3)[0]

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)
    from webdriver_manager.chrome import ChromeDriverManager    
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    hemisphere_image_urls = []

    linkloop = browser.find_by_css('a.product-item img')

    for i in range(len(linkloop)):
        mars_h = {}

        browser.find_by_css('a.product-item img')[i].click()

        original_elem = browser.links.find_by_text('Original')
        hemisphere['img_url'] = original_elem['href']
    
        hemisphere['title'] = browser.find_by_css('h2.title').text
    
        hemisphere_image_urls.append(hemisphere)
    
    # Quit the browser
    browser.quit()

    return news_title
    return news_p
    return featured_image_url
    return tables_df
    return hemisphere_image_urls