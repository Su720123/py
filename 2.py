import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置请求头模拟浏览器访问
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 存储电影名称和评分的列表
movie_names = []
movie_scores = []

# 循环遍历豆瓣Top250的10个页面（每页25部电影）
for page in range(0, 250, 25):
    url = f'https://movie.douban.com/top250?start={page}&filter='
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_items = soup.find_all('div', class_='item')
    for item in movie_items:
        movie_name = item.find('span', class_='title').text
        movie_score = float(item.find('span', class_='rating_num').text)
        movie_names.append(movie_name)
        movie_scores.append(movie_score)

# 中文显示路径
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
plt.rcParams['font.family'] = font.get_name()

# 使用matplotlib绘制柱状图展示评分情况
plt.bar(movie_names, movie_scores)
plt.xlabel('电影名称')
plt.ylabel('评分')
plt.title('豆瓣Top250电影评分分布')
plt.xticks(rotation=90)
plt.show()

# 使用pandas将数据整理为DataFrame并绘制柱状图展示
data = {'电影名称': movie_names, '评分': movie_scores}
df = pd.DataFrame(data)
df.plot.bar(x='电影名称', y='评分', figsize=(15, 6), rot=90)
plt.title('豆瓣Top250电影评分分布')
plt.show()