import os
import sys
import time

import pyautogui
import pyperclip
import pyuac
import win32gui

from log import log


# 将游戏窗口设为前台
def set_forground():
    try:
        game_nd = win32gui.FindWindow("UnityWndClass", "崩坏：星穹铁道")
        win32gui.SetForegroundWindow(game_nd)
        log.info("将游戏【崩坏：星穹铁道】窗口设为前台")
    except:
        pass


# 打开手机
def openPhone():
    pyautogui.press('esc')
    log.info("打开手机")


# 关闭手机
def closePhone():
    pyautogui.press('esc')
    log.info("关闭手机")


# 按行读取兑换码
def readRedemptionCode(abspath, fileName):
    if os.path.exists(os.path.join(abspath, fileName)):
        with open(os.path.join(abspath, fileName), "r", encoding="utf-8", errors='ignore') as f:
            return f.readlines()

    else:
        log.error('找不到redemptionCode.txt文件, 程序退出！！！')
        sys.exit()


def find(path, grayscale=False, confidence=0.8):
    coordinates = pyautogui.locateCenterOnScreen(path, grayscale=grayscale, confidence=confidence)
    return True if coordinates is not None else False


# 点击屏幕中区域
def click(path, grayscale=False, confidence=0.8):
    while True:
        log.info("识别图片中")
        coordinates = pyautogui.locateCenterOnScreen(path, grayscale=grayscale, confidence=confidence)
        if coordinates is not None:
            pyautogui.moveTo(coordinates, duration=0.2)
            pyautogui.leftClick()
            break
        else:
            log.info("未识别到正确图片")
    


def checkAndClick(redemption):
    if (find('./imgs/dui-huan-ma-yi-shi-yong.png')):
        # 兑换码已使用
        log.info(redemption + ': 兑换码已使用')
        click('./imgs/qu-xiao.png')
    elif (find('./imgs/wu-xiao-de-dui-huan-ma.png')):
        # 无效的兑换码
        log.info(redemption + ': 无效的兑换码')
        click('./imgs/qu-xiao.png')
    elif (find('./imgs/yi-shi-yong-guo-tong-lei-xing-dui-huan-ma.png')):
        # 已使用过同类型兑换码
        log.info(redemption + ': 已使用过同类型兑换码')
        click('./imgs/qu-xiao.png')
    elif (find('./imgs/dui-huan-ma-leng-que-zhong.png')):
        # 兑换码冷却中
        log.info('兑换码冷却中, 休眠3s...')
        # 休眠2s
        time.sleep(3)
        click('./imgs/que-ren.png')
        checkAndClick(redemption)
    else:
        click('./imgs/que-ren.png')
        log.info(redemption + ': 输入成功')

def run(lines):
    # 1.打开手机
    openPhone()

    # 2.兑换
    for redemption in lines:
        redemption = redemption.strip()
        #帮我删掉redemption字符串冒号前面的内容
        #redemption = redemption.split(':')[0]
        #帮我提取redemp字符串最后一个冒号后面的内容
        #redemption = redemption.split(':')[-1]

        pyperclip.copy(redemption)

        time.sleep(1)

        # 2.1点击更多
        click('./imgs/more.png')

        # 2.2点击兑换码
        click('./imgs/dui-huan-ma.png')

        # 2.3兑换码复制到剪切板中
        click('./imgs/paste.png')

        # 2.3点击确认
        click('./imgs/que-ren.png')
        # this sleep is important!
        time.sleep(1)

        # 2.4检查
        checkAndClick(redemption)

    # 3.兑换完成
    log.info('Finished!')


if __name__ == '__main__':
    # 管理员启动
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:
        # 1.按行读取文件
        abspath = '.'
        fileName = 'redemptionCode.txt'
        lines = readRedemptionCode(abspath, fileName)

        # 2.将游戏窗口设为前台
        set_forground()

        # 3.兑换码输入
        run(lines)
