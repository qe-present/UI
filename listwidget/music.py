# -*- coding: utf-8 -*-
"""
文件:music.py
创建者:QE
时间:2023/8/1 14:07
诗: 鲸鱼安慰了大海
            -燕七
    不是所有的树
    都能在自己的家乡终老
    不是所有的轨道
    都通往春暖花开的方向
    不是所有约定的人
    都会到来
    我知道，是流星赞美了黑夜
    鲸鱼安慰了大海
"""
import requests
from faker import Faker
from pprint import pprint
url='https://kuwo.cn/api/www/search/searchMusicBykeyWord?key=&pn=1&rn=20'
# pn 页数
# rn 歌曲数量
headers={
    'User-Agent':Faker().user_agent(),
    'Cookie':'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1690792638,1690866785,1690869217; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1690869217; Hm_Iuvt_cdb524f42f0ce19b169b8072123a4727=7raZ3nszzpSKRSFGbTzcKpPhb4HStHpR',
    'Host':'kuwo.cn',
    'Referer':'https://kuwo.cn/search/list?',
    'Secret':'692e1b36c9ea9e73c44bbe0bf6b5dfba5fe183ebf69d6ce31a484482d0f1676903ea6a6b'
}
r=requests.get(url=url,headers=headers)
json_data=r.json()
all_music=json_data['data']['list']
n=1
for i in all_music:
    print(i)
    album=i['album'].replace('&nbsp;'," ").replace("&apos;","'")
    name=i['name'].replace('&nbsp;'," ")
    artist=i['artist']
    rid=i['rid']
    print(n)
    n+=1
    get_mp3_url=f'https://kuwo.cn/api/v1/www/music/playUrl?mid={rid}&type=music'
    resp=requests.get(url=get_mp3_url,headers=headers)
    mp3_json = resp.json()
    if mp3_json['code'] == 200:
        mp3_url = mp3_json['data']['url']
        r = requests.get(url=mp3_url)
        with open(fr'C:\Users\520\Music\{name}.mp3', 'wb') as f:
            f.write(r.content)
    else:
        print(mp3_json['msg'])

