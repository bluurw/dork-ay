import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote # decodifica url

import useragent

def request(term, results, lang, start_index, proxies, timeout, safe, ssl_verify, region):
    ua = useragent
    r = requests.get(
        url='https://www.google.com/search',
        headers={
            'User-Agent': ua.get_useragent(),
            'Accept': '*/*'
        },
        params={
            'q': term,
            'num': results + 2,
            'hl': lang,
            'start': start_index,
            'safe': safe,
            'gl': region,
        },
        proxies=proxies,
        timeout=timeout,
        verify=ssl_verify,
        cookies = {
            'CONSENT': 'PENDING+987',
            'SOCS': 'CAESHAgBEhIaAB',
        }
    )
    r.raise_for_status()
    return r

class SearchResult:
    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description

    def __repr__(self):
        return f'SearchResult(url={self.url}, title={self.title}, description={self.description})'

def search(param, results_num=10, lang='en', start_index=0, proxies=None, timeout=5, details=False, safe='active', ssl_verify=None, region=None, unique=True):
    
    proxies = {'https': proxies, 'http': proxies} if proxies and (proxies.startswith('https') or proxies.startswith('http')) else None

    fetched_links = set()
    current_results_num = 0

    while current_results_num < results_num:

        response = request(param, results_num, lang, start_index, 
                            proxies, timeout, safe, ssl_verify, region)
        soup = BeautifulSoup(response.text, 'html.parser')
        result_block = soup.find_all('div', class_='ezO2md')
        
        for result in result_block:
            link_tag = result.find('a', href=True)
            title_tag = link_tag.find('span', class_='CVA68e') if link_tag else None
            description_tag = result.find('span', class_='FrIlee')

            metadata = {
                'url': unquote(link_tag['href'].split('&')[0].replace('/url?q=', '')) if link_tag else 'Unknown',
                'title': title_tag.text.strip() if title_tag and title_tag.text else 'Unknown',
                'description': description_tag.text.strip() if description_tag and description_tag.text else 'Unknown'
            }

            if metadata['url'] == 'Unknown' or not metadata['url'].startswith(('http', 'https')):
                continue

            if unique and metadata['url'] in fetched_links:
                continue
            fetched_links.add(metadata['url'])

            if details:
                yield SearchResult(metadata['url'], metadata['title'], metadata['description'])
            else:
                yield metadata['url'] 

            current_results_num += 1

            if current_results_num >= results_num:
                break
        
        start_index += 10

        if len(result_block) == 0:
            break

# Exemplo de uso
'''
for result in search('intitle:"index of"'):
    print(result)
'''