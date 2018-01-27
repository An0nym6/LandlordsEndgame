# 斗地主残局

## 运行方式


1. 直接在命令行输入指令 ```python search.py``` 即可运行。

2. 按照提示输入地主（先手）和农民（后手）的手牌，用字母“Y”代表“小王”，字母“Z”代表“大王”，样例如下：

```
请输入地主牌：K Q J 9 9 8 7 6 5 5 4
请输入农民牌：Z 2 A A A Q 9 6 4 3
```

3. 程序输出“完成”字样后会提示地主应该打出的第一手牌，然后程序将等待你继续输入农民的应对。输入应对的格式与上抑制，样例如下，如果农民“不出”，直接打回车即可。

```
完成！
地主应出 ['4', '5', '6', '7', '8']
请输入农民的出牌：
地主应出 ['9', '9']
请输入农民的出牌：A A
地主应出 []
……
```

## 声明

* 为了加快搜索效率，程序进行了剪枝操作；
* 程序不使用多线程，适合普通 PC 运行；
* 程序没有对重复搜索进行任何优化；
* 搜索困难关卡耗时较长（数小时），内存开销较大（20 GB）。

## 运行效果

成功破解微信小游戏“欢乐斗地主”残局闯关 2018 年 1 月赛季全部 50 个关卡。

![残局第 25 关开局](https://raw.githubusercontent.com/An0nym6/Images/master/blog%20images/LandlordsEndGame/1.png)
![残局第 25 关结束](https://raw.githubusercontent.com/An0nym6/Images/master/blog%20images/LandlordsEndGame/2.png)
![残局第 25 关解法](https://raw.githubusercontent.com/An0nym6/Images/master/blog%20images/LandlordsEndGame/3.png)
![残局全通关](https://raw.githubusercontent.com/An0nym6/Images/master/blog%20images/LandlordsEndGame/4.png)
