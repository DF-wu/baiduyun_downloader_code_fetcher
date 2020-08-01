import requests
import json
ver = input("请输入助手版本号")
print ('正在获取暗号...')
r = requests.get('https://api.baiduyun.wiki/update?ver=${input}')
print('暗号是:',r.json()['scode'])
