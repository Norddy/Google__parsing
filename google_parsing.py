import requests
import datetime
import bs4
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


def get_all_dates():
    date = datetime.datetime.now()
    x = []
    for j in range(2008, 2020):
        if j != 2019:
            for i in range(1, 13, 3):
                x.append('{}/{}/{}'.format(i, '1', j))

        else:
            for i in range(1, date.month + 1, 2):
                x.append('{}/{}/{}'.format(i, '1', j))
    return x



def get_all_headers(name, dates):
    header = []
    for i in range(len(dates) - 1):
        date = 'cdr:1,cd_min:{},cd_max:{}'.format(dates[i], dates[i + 1])
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        payload = {'as_epq': name, 'tbs': date}
        r = requests.get("https://www.google.com/search", params=payload, headers=headers)
        soup = bs4.BeautifulSoup(r.content, 'html.parser')
        f = soup.find(id='resultStats').text
        h = f.split()[1]
        if len(h) > 3:
            h = int(h.replace(",", ""))
        else: h = int(h)

        header.append(h)
    return header


def plot_graph(dates, all_headers,x):
    plt.plot(dates[1:], all_headers)
    plt.title(x)
    plt.savefig('demo.png', transparent=True)


def main():
    x = input().split()
    x = '+'.join(x)
    dates = get_all_dates()
    all_headers = get_all_headers(x, dates)
    plot_graph(dates, all_headers,x)


if __name__ == '__main__':
    main()
