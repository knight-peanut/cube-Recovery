# PythonCap
简述:用python写的一些小东西，包含各种方面。



### cube-Recovery

#### 说明：  
这是一个以层先法为基准的魔方复原python代码实现，运行环境为2.7.14，详细的魔方公式算法祥见： [http://www.mf100.org/beginner.htm](魔方乐园)

#### 目录文件结构：

- magic.py:  魔方复原代码，打印了魔方的具体实现步骤和运行时长(可实现复原)
- colorDetetion.py:  用opencv粗糙做出来的颜色识别，根据魔方几个面的图片来识别颜色
- /img ：  包括了颜色识别用到的所有图，hsv的值基于对标准魔方图片的颜色采样
- 另外：  魔方的白色中心块有颜色，需要被自动设定为白色

注：程序均为原创，如若使用请注明出处。
