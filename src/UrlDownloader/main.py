#!/usr/bin/env python3
import UrlDownloader
import logging

def main():
    args = input('Enter *args "URL Name Path ChunkSize": ').split()
    try:
        name = UrlDownloader.download_file(*args)
        print(f'file saved with name: {name}')
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    while True:
        main()
