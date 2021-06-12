'''
Author: what-is-me
E-mail: nt_cqc@126.com
Github: https://github.com/what-is-me
LeetCode: https://leetcode-cn.com/u/what-is-me/
Date: 2021-05-30 00:53:57
LastEditors: what-is-me
LastEditTime: 2021-05-30 15:33:43
Description: file content
'''
from pygame import mixer  # Load the required library
import pygame
import json
import time
import os
import wordlistenquiry as wl
import requests
import keyboard


def read(word):
    filepath = word + '.mp3'
    res = requests.get('http://dict.youdao.com/dictvoice?type=0&audio='+word)
    music = res.content
    with open(filepath, 'wb') as file:  # 保存到本地的文件名
        file.write(music)
        file.flush()
    mixer.init()
    mixer.music.load(filepath)
    mixer.music.play()
    t = 0.0
    while mixer.music.get_busy():
        time.sleep(0.01)
        t += 0.01
    pygame.quit()
    if os.path.exists(filepath):
        os.remove(filepath)
    return t


con = '''{
    "filename": "list.txt",
    "log": "log",
    "choice": 1,
    "color": 1,
    "speed": 6,
    "online": 0,
    "page": 20,
    "div": ":"
}'''  # 默认config


def _yellow(string):
    global color
    if color == 1:
        return "\033[1;33m"+string+"\033[0m"
    else:
        return string


def _red(string):
    global color
    if color == 1:
        return "\033[1;31m"+string+"\033[0m"
    else:
        return string


def _blue(string):
    global color
    if color == 1:
        return "\033[1;36m"+string+"\033[0m"
    else:
        return string


'''
def read(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()
'''

if __name__ == "__main__":
    p = os.path.dirname(os.path.realpath(__file__))
    p = os.path.join(p, 'dict')
    p = p + '\\'
    if not os.path.exists(p+'en'):
        # 不存在，就创建
        os.makedirs(p+'en')
    try:
        with open(p+"config.json", 'r', encoding="utf-8") as config:
            config = json.load(config)  # ! config json->dict
    except IOError:
        with open(p+"config.json", 'w', encoding="utf-8") as config:
            config.write(con)
    finally:
        with open(p+"config.json", 'r', encoding="utf-8") as config:
            config = json.load(config)  # ! config json->dict
    try:
        open(p+config['log'], 'r', encoding="utf-8")
    except IOError:
        with open(p+config['log'], 'w', encoding="utf-8") as log:
            log.write("0")
    finally:
        with open(p+config['log'], 'r', encoding="utf-8") as log:
            i = int(log.readline())
    color = config['color']
    w = open(p+config['filename'], "r", encoding="utf-8")
    f = w.readlines()
    w.close()
    al = len(f)
    os.system("cls")
    print(config['filename']+"\n\n\n==========================================================================================================================================================>\n")
    if config['online']:
        while i < al:
            if keyboard.is_pressed('enter'):
                time.sleep(2)
                os.system("pause")
            i = i+1
            sa = f[i-1].strip()
            sb = wl.search(sa, choice=config['choice'])
            if (i-1) % config['page'] == 0:
                os.system("cls")
                print(config['filename']+"\n\n\n===========================================================================================================================================================>\n")
            print(100*" ", end="\r")
            print(_red(str(i))+"|\t\t"+_yellow(sa) +
                  (20-len(sa))*" "+"|  "+_blue(sb))
            t = read(sa)
            newfile = open(
                p+"ResultOf-"+config['filename'], 'a+', encoding="utf-8")
            newfile.write(sa+config['div']+sb+'\n')
            newfile.close()
            time.sleep(config['speed'] if config['speed'] > t else t)
            with open(p+config['log'], 'w') as log:
                log.write(str(i))
    else:
        while i < al:
            if keyboard.is_pressed('enter'):
                time.sleep(2)
                os.system("pause")
            i = i+1
            s = f[i-1].strip()
            if (i-1) % config['page'] == 0:
                os.system("cls")
                print(config['filename']+"\n\n\n===========================================================================================================================================================>\n")
            x = s.find(config["div"])
            sa = s[0:x].strip()
            sb = s[x+1:]
            print(100*" ", end="\r")
            print(_red(str(i))+"|\t\t"+_yellow(sa) +
                  (20-len(sa))*" "+"|  "+_blue(sb))
            t = read(sa)
            time.sleep(config['speed'] if config['speed'] > t else t)
            with open(p+config['log'], 'w') as log:
                log.write(str(i))
