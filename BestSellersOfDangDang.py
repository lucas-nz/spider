import requests
import re
import json


def request_dangdang(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(html, page):
    pattern = re.compile(
        '<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)".*?class="star".*?class="tuijian">(.*?)</span>.*?class="publisher_info".*?target="_blank">(.*?)</a>*.*?class="price_n">&yen;(.*?)</span>.*?</li>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            "range": 20 * page + item[0],
            "img": item[1],
            "title": item[2],
            "recommend": item[3],
            "author": item[4],
            "price": item[5],
        }


def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('files/book.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


def main(page):
    url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-' + str(page)
    html = request_dangdang(url)
    items = parse_result(html, page)
    for item in items:
        write_item_to_file(item)


if __name__ == '__main__':
    for i in range(1, 26):
        main(1)
