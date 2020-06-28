# 作业一：
# 安装并使用 requests、bs4 库，
# 爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def get_response():

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

    header = {
        'user-agent':user_agent,
        'Accept':"*/*",
        'Accept-Encoding':'gazip,deflate,br',
        'Accept-Language':'en-AU,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6',
        'Content-Type':'text/plain',
        'Connection':'keep-alive',
        'Origin':'https://maoyan.com',
        'Referer':'https://maoyan.com/films?showType=3',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'cross-site'
    }

    myurl = 'https://maoyan.com/films?showType=3'

    response = requests.get(myurl,headers=header)
    return response

def get_movie_msg(rank):
    res = get_response()
    bs_info = bs(res.text, 'html.parser')
    div = bs_info.find_all('div',attrs={'class': 'movie-item-hover'})     
    tags = div[rank].find('a')
    # print(f'https://maoyan.com{tags.get("href")}')   
    movie_name = tags.find('span',attrs={'class': 'name'}).text  
    atag = tags.find_all('div',attrs={'class':'movie-hover-title'}) 
    movie_type = atag[1].text.replace('\n','').replace('\r','')
    movie_type = movie_type[4:]      
    movie_time = tags.find('div',attrs={'class':'movie-hover-brief'}).text.replace('\n','').replace('\r','')
    movie_time = movie_time[6:]
    mylist = [movie_name, movie_type, movie_time]
    return mylist
       
def get_data():
    rank_list = []
    for rank in range(10): 
        rank_res = get_movie_msg(rank)
        rank_list.append(rank_res)
    return rank_list

data_to_csv = get_data()
movie1 = pd.DataFrame(data = data_to_csv, columns=['电影名称','电影类型','上映时间'])
movie1.to_csv('./movie1.csv', encoding='utf8',index=False)
    

