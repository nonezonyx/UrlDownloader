#!/usr/bin/env python3
import requests as rq

headers = { 'Accept-Language' : 'ru,en;q=0.9','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.1.806 Yowser/2.5 Safari/537.36'}

def download_file(URL,name=None,path='.',chunk_size=1024): #file download from url
    chunk_size=round(int(chunk_size))
    if name is None:
        name = URL.split('/')[-1].split('?')[0]
    with rq.get(URL, stream=True, timeout=3600, headers=headers) as r:
        r.raise_for_status()
        with open(f'{path}/{name}', 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
    return f'{path}/{name}'

def download_files(URLs: list,names=None,path='.',chunk_size=1024):
    if names is None:
        names = [URL.split('/')[-1].split('?')[0] for URL in URLs]
    elif not len(URLs) == len(names):
        raise AmountOfNamesNotEqualToAmountOfLinks
    file_paths = []
    for i in range(len(URLs))  :
        file_path = download_file(URLs[i], names[i], path, chunk_size)
        file_paths.append(file_path)
    return file_paths
