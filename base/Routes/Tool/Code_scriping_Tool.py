import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re


def convert_youtube_link(url):
    # Regular expression pattern to match YouTube URLs
    pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/)|youtu\.be\/)([\w-]{11})'

    # Check if the URL matches the pattern
    match = re.match(pattern, url)

    if match:
        # If the URL matches, return the embed link
        return f'https://www.youtube.com/embed/{match.group(1)}'
    else:
        # If the URL doesn't match, return None
        return None


def get_image_url(keyword):
    url = f"https://www.google.com/search?q={keyword}&tbm=isch"

    # Make a GET request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    image_urls = set()
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if img_url:
            image_urls.add(img_url)
    return list(image_urls)


def get_answer_from_given_link(question_url):
    code = ''
    response = requests.get(question_url)

    soup = BeautifulSoup(response.content, 'html.parser')
    # responsive-tabs
    try:
        question_title = soup.find('a', class_='question-hyperlink').get_text()
        print('Question:', question_title)

        print('run next....')
        # Find the code blocks in the question and print them
        code_blocks = soup.find_all('pre')
        print(code_blocks)
        for i, code_block in enumerate(code_blocks):
            print(f'\nExample code {i+1}:')
            print(code_block.get_text())
            code = code+str(code_block)
    except:
        code = soup.get_text()
    return code


def get_example_code_gfg(url):
    code = ""
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div element containing the example code
    example_code_div = soup.find_all('div', {'class': 'container'})
    print("for lop")
    for i in example_code_div:
        code = code + str(i)
        code=code[0:5]
    # Get the text content of the example code div
    # example_code = example_code_div.get_text()
    # Return the example code
    return code


def get_stackoverflow_link(question, site='stackoverflow.com'):

    num_results = 30

    stackoverflow_link = ""
    # Search Google for the question and get the top search results
    if "write a" in question.lower():
        url = 'https://www.google.com/search?q={}&num={}&hl=en&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwiB4ZG4-d3wAhXB4zgGHUaXDbUQsAQIYw'.format(question + " site:stackoverflow.com", 5)
        search_results = search(url, num_results=20)
    else:
        search_results = search(question, num_results=num_results)
    common=[]
    # Loop through the search results and find the Stack Overflow link
    for result in search_results:
        print("result,result",result)
        common.append(result)
        if site in result:
            stackoverflow_link = result
            break
    if stackoverflow_link != "":
        return stackoverflow_link
    else:
        return common[0]
        
def get_stackoverflow_link_1(question, site='stackoverflow.com'):

    num_results = 50

    stackoverflow_link = ""
    # Search Google for the question and get the top search results
    search_results = search(question, num_results=num_results)

    # Loop through the search results and find the Stack Overflow link
    for result in search_results:
        if site in result:
            stackoverflow_link = result
            break

    return stackoverflow_link



# print('answer', get_example_code_gfg(
#     "https://www.geeksforgeeks.org/what-is-linked-list/"))
