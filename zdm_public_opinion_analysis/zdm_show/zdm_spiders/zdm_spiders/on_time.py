import subprocess
import schedule
from datetime import datetime


def crawl_work():
    print('开始爬取气泡水... {}\n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),))
    subprocess.Popen('scrapy crawl qipaoshui', shell=True)
    


if __name__ == '__main__':
    schedule.every().day.at('00:30').do(crawl_work)
    while True:
        schedule.run_pending()
