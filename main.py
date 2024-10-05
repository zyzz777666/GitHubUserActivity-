import requests
import pprint
def main():
    username = 'zyzz777666'
    url = f'https://api.github.com/users/{username}/events'
    data = requests.get(url).json()

    for i in data:
        print(i['type'], i['repo']['name'])


if __name__ == '__main__':
    main()
