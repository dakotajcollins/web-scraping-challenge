from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find('div', class_='list_text')

    news_title= news.find('div', class_="content_title").text
    news_p = news.find('div', class_="article_teaser_body").text


    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find('div', class_='thmb')
    group= images.find('img')
    image_url=group['src']
    image_url=image_url.replace(" ","%20")
    featured_image_url= f"{url}/{image_url}"



    url = "https://galaxyfacts-mars.com/"
    tables = pd.read_html(url)
    df = tables[0]
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    html_table = df.to_html(index=False, classes='table table-striped')


    url = 'https://marshemispheres.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all('div', class_='item')
    hemisphere_image_urls=[]

    for result in results:
        title = result.find('h3').text
        img = result.find('img',class_='thumb')
        imgs = img['src']
        img_url=url+imgs
        
        hemisphere_dict = {
            'title': title,
            'img_url': img_url
        }
        hemisphere_image_urls.append(hemisphere_dict)
    browser.quit()

    my_data= {
        "news_title": news_title,
        "news_p": news_p,
        "featured_img": featured_image_url,
        "html_table": html_table,
        "hemisphere_image": hemisphere_image_urls
    }
    # Return results
    return my_data