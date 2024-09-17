# StarRail-RedemptionCode-Helper
星穹铁道自动使用兑换码

1、将要兑换的码输入到【redemptionCode.txt】内，一行一个，例如下面
BSM5G6T2UD9L
9T45Z7QC3HUC
4BMMHM6XCPQ4

2、输入且保存好后，打开游戏，在关闭手机的状态下(能看到右边队伍栏的状态下)，点击main.py即可开始自动兑换所输入的码，兑换期间不能动鼠标键盘

3、对应的图片以更改为游戏分辨率为1920*1080的截图，若使用没反应或平时使用的游戏分辨率不是1080的，可在自己的游戏分辨率下，把imgs内的截图重新截一遍然后同名替换即可

4、如果点击main.py后打开了手机就闪退，那么可能是pyscreeze模块版本过高与python不兼容，解决方法见下：

①开始-运行-输入cmd-确定
②输入pip uninstall pyscreeze，然后回车
③然后会问是否确定删除(Y/n),输入Y后回车
④接着输入pip install pyscreeze==0.1.28，然后回车安装0.1.28版本
⑤安装完成后再点击main.py应该就可以正常运行兑换了
