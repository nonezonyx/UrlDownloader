import downloader

def main():
    URL = input('Enter URL of gile: ')
    name = downloader.download_file(URL)
    print(f'file saved with name: {name}')

if __name__ == '__main__':
    while True:
        main()
