from manimlib import *  # manim是一个动画类型的库,可以较为轻松的实现各种动画效果
num = "10111001010"  # 可变长二进制串
mode = "ASK"
k = 1   #载波信号的频率倍数,默认1倍,此时频率为1
a = 1   #载波信号的幅值倍数,默认1倍
p = 0*PI  #载波信号的初相位,默认为0,此时是正弦波

class TEST(Scene):   # manim的场景固定写法
    def construct(self):   #manim的场景固定写法
        def squr(x):  #定义一个函数用来把二进制串化为方波形式
            if int(x) > len(num)-1:   #这里的传入参数x是从零到二进制串的长度,步进为0.01,这是在后面设置的,
                return 0;  #如果传入x超过了串长度,返回0,保险作用
            if num[int(x)]=="0":  #如果传入的x向下取整后在num字符串里的位置对应的字符是0
                return 0  #返回0
            elif num[int(x)]=="1":  #同上,如果是1
                return 1  #返回1
            else:  #其他情况
                return 0  #返回0,保险作用
        def sk(x):
            if int(x) > len(num)-1:  #同上,防止超长报错
                return 0;
            if mode=="ASK":
                if num[int(x)]=="0":  #若为0  
                    return a*0*np.sin(k*x*2*PI+p)  #则返回幅频系数为0的载波信号,此处载波信号是周期为1的sin函数
                elif num[int(x)]=="1":  #若为1  此处的PI在manim中已经定义过了也就是圆周率
                    return a*1*np.sin(k*x*2*PI+p)  #返回幅频系数为1的载波信号.周期为1的sin函数
            elif mode=="FSK":
                if num[int(x)]=="0":
                    return a*1*np.sin(k*x*2*PI+p)   #若为0,则选择载波频率1,此处对应的是周期为1的sin函数波形
                elif num[int(x)]=="1":
                    return a*1*np.sin(k*x*4*PI+p)  #若为1,则选择载波频率2,此处对应的是周期为0.5的sin函数波形
            elif mode=="PSK":
                if num[int(x)]=="0":
                    return a*-1*np.sin(k*x*2*PI+p)  #若为0,PSK信号为载波信号的相位反相
                elif num[int(x)]=="1":
                    return a*1*np.sin(k*x*2*PI+p)  #若为1,PSK信号为载波信号
            else:  #其他情况,为了保险
                return 0  #返回0
        axes = Axes((-1, len(num)+1,1),(-1.5,1.5,1),height=3,width=len(num)+2)  #mainm创建坐标系
        axess = Axes((-1,len(num)+1,1),(-a-0.5,a+0.5,1),height=2*(a+0.5),width=len(num)+2)  #x轴长字符串长度+2
        axesss= VGroup(axes,axess).arrange(DOWN).move_to(ORIGIN)  #利用VGroup来对两个坐标系排版
        axesss.stretch_to_fit_width(FRAME_WIDTH-0.5).stretch_to_fit_height(FRAME_HEIGHT-2)  #缩放后居中
        topnum=Tex(mode+"\hspace{1em}"+num).shift(UP*3.5)  #对二进制字符串生成latex字符

        

        squr_graph = axes.get_graph(  #在axes坐标系上绘制方波函数
            squr,  #用axes的get_graph方法来绘制函数图像,传入值为步进的x,返回值通过上方的squr函数得到
            use_smoothing=False,  #禁用平滑,否则方波函数会跳变处自动拟合,得到的不符合理想方波函数
            color=YELLOW,  #设为黄色
            x_range=(0,len(num),0.01)  #x取值为0到字符串的长度,步进值为0.01,也就是第一次传0,第二次传0.01
        )

        sk_graph = axess.get_graph(  #在axess坐标系上绘制ASK处理后的波形,下列参数同上
            sk,
            use_smoothing=False,
            color=BLUE,
            x_range=(0,len(num),0.01)
        )

        


        # 下面是一些manim负责生成动画的方法和参数
        self.play(Write(topnum))  #绘制二进制字符串对应的latex
        self.play(FadeIn(axes,lag_ratio=0.5,run_time=2),FadeIn(axess,lag_ratio=0.5,run_time=2)) #画坐标系
        self.play(ShowCreation(squr_graph,run_time=len(num)/2,rate_func=linear),
                    ShowCreation(sk_graph,run_time=len(num)/2,rate_func=linear)
)  #画函数







        #对于其他的两种调制方式,只需改动上方的ask函数中的处理返回值的代码,为了可以对每项进行单独配置,
        #我使用了3个.py文件来实现对三种方式的绘制,大体内容基本一致
        #下方列出其他两种方式的根据传入值调制载波信号的函数
        def fsk(x):
            if int(x) > len(num)-1:
                return 0;
            if num[int(x)]=="0":
                return a*1*np.sin(k*x*2*PI+p)   #若为0,则选择载波频率1,此处对应的是周期为1的sin函数波形
            elif num[int(x)]=="1":
                return a*1*np.sin(k*x*4*PI+p)  #若为1,则选择载波频率2,此处对应的是周期为0.5的sin函数波形
            else:
                return 0



        def psk(x):
            if int(x) > len(num) -1:
                return 0;
            if num[int(x)]=="0":
                return a*-1*np.sin(k*x*2*PI+p)  #若为0,PSK信号为载波信号的相位反相
            elif num[int(x)]=="1":
                return a*1*np.sin(k*x*2*PI+p)  #若为1,PSK信号为载波信号
            else:
                return 0
