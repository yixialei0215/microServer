import asyncio

import requests


@asyncio.coroutine
def download(url):
    yield from asyncio.sleep(1)
    resp = requests.get(url)
    return resp.content, resp.status_code


@asyncio.coroutine
def write_url(filename, content):
    print('保存中')
    with open(filename, 'wb') as f:
        f.write(content)


@asyncio.coroutine
def save(url, filename):
    print('正在下载中%s' % (url))
    content, code = yield from download(url)
    yield from write_url(filename, content)
    print('下载成功%s' % url)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.wait([
        save('https://www.baidu.com', 'baidu.html'),
        save('https://jd.com', 'jd.html')
    ]))
