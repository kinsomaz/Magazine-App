import requests


def top_headlines():
    url = ('https://newsapi.org/v2/top-headlines?'
              'country=us&category=entertainment&'
              'apiKey=5ba428a78e674a598a177775ea8d89b3&'
              'page=1&'
              'pageSize=5')
    response = requests.get(url)
    return response.json()['articles']


def music():
    url = ('https://newsapi.org/v2/everything?'
           'q=music&apiKey=5ba428a78e674a598a177775ea8d89b3&'
           'page=1&'
           'pageSize=5')
    response = requests.get(url)
    return response.json()['articles']


def main():
       pass


if __name__ == '__main__':
    main()
