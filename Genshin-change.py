# --*-- coding=utf-8 --*--
import os
import time
import json

def getversion():
    global verjson
    verjson = {
                "game_version":"2.1.0",
                "mihoyo_channel":"1",
                "mihoyo_sub_channel":"1",
                "mihoyo_cps":"mihoyo",
                "bili_channel":"14",
                "bili_sub_channel":"0",
                "bili_cps":"bilibili"
                }

def get_game_path():
    global path
    path = "null"
    if(os.path.exists("./path.txt")):
        with open('./path.txt', 'r') as f:
            path = f.read()  # 读取路径
    if(path == "null"):
        path = input(
            "请输入您的'Genshin Impact Game'文件夹的路径(如:E:\Genshin Impact\Genshin Impact Game)\n")
        if(os.path.exists(path+"/YuanShen.exe") and os.path.exists(path+"/config.ini") and os.path.exists(path+"/mhyprot2.Sys")):
            path = path.replace('\\', '/')
            print("已经找到游戏文件")
            with open('./path.txt', 'w+') as f:
                f.write(path)  # 将路径写入文件


def iniget():
    global isserver
    print(path)
    with open(path+"/config.ini", "r") as f:
        f = f.read()
        bili = f.find('bilibili')
        mihoyo = f.find('mihoyo')
    if (bili < 0):
        print("您现在所在mihoyo服务器中,我们将更换到bilibili服务器中")
        isserver = "bili"
    elif (mihoyo < 0):
        print("您现在所在bilibili服务器中,我们将更换到mihoyo服务器中")
        isserver = "mihoyo"


def inichange():
    if(isserver == "bili"):
        with open(path+"/config.ini", 'w+') as f:
            # 将路径写入文件
            f.write(
                "[General]\r\nchannel=%s\r\ncps=%s\r\ngame_version=%s\r\nsdk_version=\r\nsub_channel=%s" % (verjson["bili_channel"], verjson["bili_cps"], verjson["game_version"], verjson["bili_sub_channel"]))
        print("已转接到bilibili服务器")
    elif(isserver == "mihoyo"):
        with open(path+"/config.ini", 'w+') as f:
            # 将路径写入文件
            f.write(
                "[General]\r\nchannel=%s\r\ncps=%s\r\ngame_version=%s\r\nsdk_version=\r\nsub_channel=%s" % (verjson["mihoyo_channel"], verjson["mihoyo_cps"], verjson["game_version"], verjson["mihoyo_sub_channel"]))
        print("已转接到mihoyo服务器")
    isopen = input("是否打开原神?(0:是,1:否)\n")
    if(isopen == "1"):
        print("三秒后将关闭本程序")
        time.sleep(3)
        exit()
    else:
        os.system("\""+path+"/YuanShen.exe\"")
        time.sleep(3)
        exit()


if __name__ == "__main__":
    print("欢迎使用原神快速换服程序\n")
    getversion()
    get_game_path()
    iniget()
    inichange()