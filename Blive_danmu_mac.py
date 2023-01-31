import time
import requests
import os
from retrying import retry

class bilibiliDanmu():
    def __init__(self):
        self.url = "https://api.live.bilibili.com/ajax/msg"
        self.headers={
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
            "Referer": "https://live.bilibili.com/",
            }
        self.data = {
            "roomid":romid,
            "csrf_token":"",
            "csrf":"",
            "visit_id":""
            }
            
    def speak_text(self,text):
        text_cmd = "say " + text
        os.system(text_cmd)
        # print("\n")

    def text_danmu(self,html):

        global old_list

        temp_list = []

        for text in html["data"]["room"]:
            danmu_string=text["nickname"] +"说:"+ text["text"]
            temp_list.append(danmu_string)
        #print(danmu_string)
        if temp_list == old_list:
            pass
        else:
            print ("First list length : %d" %len(temp_list))
            for text_number in range (1,11):
                if "".join(temp_list[:text_number]) in "".join(old_list):
                    pass
                else:
                    try:
                        print (temp_list[text_number-1])
                    except:
                        pass
                    else:
                        self.speak_text(temp_list[text_number-1])

            old_list = temp_list[:]

    @retry(stop_max_attempt_number=5)
    def get_danmu(self):
        html = requests.post(url=self.url,headers=self.headers,data=self.data)
        html.json()
        self.text_danmu(eval(html.text))


if __name__ == '__main__':
    old_list=[]
    print("\n名称：B站弹幕姬MAC版\n"
          "描述：可以朗读B站直播间弹幕的Python软件，已开源，具体使用说明和源码见白歌BESING的博客（baigebg.com）\n"
          "作者：白歌BESING （公众号和博客同名，搜一下即可找到）\n")
    romid = input("请输入房间id:")

    bzhan = bilibiliDanmu()

    while True:
        bzhan.get_danmu()
        time.sleep(45)
