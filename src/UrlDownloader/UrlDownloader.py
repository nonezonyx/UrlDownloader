#!/usr/bin/env python3
import requests as rq

headers = { 'Accept-Language' : 'ru,en;q=0.9',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.1.806 Yowser/2.5 Safari/537.36'

            }

def download_file(URL,name=None,path='.',chunk_size=1024, timeout=3600, headers=headers): #file download from url
    chunk_size=round(float(chunk_size))
    if name is None:
        link_ending = URL.split('/')[-1].split('?')[0]
        name = link_ending if '.' in link_ending else f'{link_ending}.html'
    with rq.get(URL, stream=True, timeout=timeout, headers=headers) as r:
        r.raise_for_status()
        with open(f'{path}/{name}', 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
    return f'{path}/{name}'

def download_files(URLs: list,names: list = [],path='.',chunk_size=1024, timeout=3600, headers=headers):
    return [download_file(URLs[i], names[i] if i < len(names) else None, path, chunk_size, timeout, headers) for i in range(len(URLs))]
