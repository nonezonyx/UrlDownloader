#!/usr/bin/env python3

import requests as rq
import logging

def download_file(URL,name=None,path='.',chunk_size=1024): #file download from url
    chunk_size=round(int(chunk_size))
    if name is None:
        name = URL.split('/')[-1].split('?')[0]
    with rq.get(URL, stream=True, timeout=3600) as r:
        r.raise_for_status()
        with open(f'{path}/{name}', 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
    return f'{path}/{name}'

def download_files(URLs: list,names=None,path='.',chunk_size=1024):
    if names is None:
        names = [URL.split('/')[-1].split('?')[0] for URL in URLs]
    elif not len(URLs) == len(names):
        logging.error('amount of names must be equal to amount of URLs')
        return 'ERROR'
    file_paths = []
    for i in range(len(URLs))  :
        file_path = download_file(URLs[i], names[i], path, chunk_size)
        file_paths.append(file_path)
    return file_paths
