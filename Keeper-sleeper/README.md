# **任务一完成报告**
## ——报告人：计通1504**李剑创**
---
# 1. 学习**git**的过程
* 个人学git的征途有点坎坷，主要是对git定位认知的不清晰导致，使得我一开始看git相关文档时便觉得云里雾里的，所以我最后是结合“b站”资源进行学习的；
* 先是git的安装内容，在电脑上会并存git Bash，git CMD，git GUI,所有内容都只使用了git Bash；
* 再就是git一些常用的指令（基本与Linus的指令一致），如下：
    * cd：改变目录
    * cd回退默认目录
    * cd..回退上一目录
    * pwd：显示当前目录路径
    * Is:列出目录所以文件
    * touch：新建一个文件
    * rm：删除一个文件
    * mkdir：新建一个目录（文件夹）
    * rm -r：删除一个目录（文件夹）
    * （注意：rm -rf删除所有文件，避免用！）
    * mv 移动文件
    * reset 初始化
    * clear 清屏
    * (一般reset 和 clear不作详细区分)
    * history 查看过去指令历史
    * help 帮助
    * exit 退出
    * #表示注释
* （目前也就是记下这些指令并会简单运用）
* 最后，学完git后个人对git的感觉就是能较快较精准的建立，修改文件，以及运用history可对过去的改动了解个大概；尚未体验到那种分布式好处的感受（这也是以后经常碰到的吧！）
---
# 2. 学习**Markdown**的过程
* 学习资源就是 [菜鸟教程，Markdown](https://www.runoob.com/markdown/md-tutorial.html)
* 先是完成关于**Markdown**教程的通篇阅读，了解了Markdown的诸多功能；
* 再是下载了 [VSCode](https://code.visualstudio.com/download)的编译器；
* 之后就是用VSCode完成了**Markdown**教程的例子
    * 当然在操作过程中需要在VSCode里面下载一些安装包
    * 主要安装的是“Markdown preview Enhanced v0.6.3”,"Markdown All in One v3.4.3"等；
* 最后谈谈对学习**Markdown**的看法，个人觉得新人借助 [菜鸟教程，Markdown](https://www.runoob.com/markdown/md-tutorial.html)和百度便可以很快完成这个小任务滴！
---
# 3. 学习**Markdown**的实践
* ## 学习过后，Markdown用于文本编辑显然优势巨大
    * 以下是关于Markdown标题，字体，分割线，删除线，下划线，脚注，区块用于英语文本阅读的具体展示
  
    Modern Technologies
    ===
    现代科技
    ---
　　We’re all enjoying the conveniences and happiness brought by modern technologies. We use telephones and mobile phones to call, emails to write and vehicles to drive; we go to another country by air planes; we see what is happening in the world by <u>TV programs and Internet</u>, and we even watch sports games on live. Nowadays, without these technologies, I can’t imagine what my life could be.
---
　　I used to read an article describing the modern lives of human beings. It says we will have many phone numbers if we want to search for one person; we send <u>emails and cell phone messages</u> to our friends in stead of visiting them. More and more people would rather sit in front of a computer than a TV. And we seldom go to libraries to check information now, because the Internet would do all the jobs.
---
　　We use <u>digital cameras, scanners, photocopiers, blue teeth technology and digital signals for our cell phones…</u> It seems as if we were living in a real digital world. Actually I guess we are, though. Since we are so developed and advanced, why we are less civilized?
---
　　We are easily mad with our broken computers; we fed up with things we don’t like; we call our lovers to say “farewell and good-bye” and we are afraid to face the facts which are cruel and real. We’re led to a trend that there will no more face-to-face communications. I would rather chat with my friends with <u>OICQ and emails</u> these years, instead of seeing them in reality.
---
　　I hide myself inside my car so that I can flee away from dirt, air pollutions, robberies, thieves, winds, rains and snows. However, I could not taste the spring rain and the winter snow either. The nature is fleeing away from me too!
--- 
　　Should I thank modern technologies or blame them? I wonder if you have got the right answer.
---文字讲述的是科技于人类的~~好处~~影响以及人类接下应做的反思
* ### 以上便是部分Markdown的文档编辑功能；
* ## 接下来就是真正让我新奇的新玩意了；
    * 首先就是名称加链接，具体格式为 [名称] (链接)
    像前面的菜鸟教程：[菜鸟教程，Markdown](https://www.runoob.com/markdown/md-tutorial.html)，再如我找的英语文章：[现代科技，English article](https://www.oh100.com/read/1401338.html),这些都是新奇的东西；
    * 接着是表格的制作，依据文档例子我编辑一个：
---
 学号 | 姓名 | 入学成绩 | 最终成绩 
-|-|-|-
 x |  
 x |
 x |
* ## 补充
    * 最后当然是一些高级操作啦
    如：按<kbd>win</kbd>+<kbd>R</kbd>打开运行框，输入*dxdiag*查看电脑信息
    再如：$f(x) = sin(x)$,$f(x) = ln(x)$;
    又如例子中的：
$$
\begin{Bmatrix}
   a & b \\
   c & d
\end{Bmatrix}
$$
$$
\begin{CD}
   A @>a>> B \\
@VbVV @AAcA \\
   C @= D
\end{CD}
$$
    依上本人简单模仿一下：
$$
\begin{Bmatrix}
     &   & z &   &   \\
     &   & z &   &   \\
   z & z & z & z & z \\
   z &   & z &   & z \\
   z & z & z & z & z \\
     &   & z &   &   \\
     &   & z &   &   \\
     &   & z &   &   \\  
\end{Bmatrix}
$$
$$
\begin{Bmatrix}
     &   & n &   &   \\
     & n & n & n &   \\
     &   & n &   &   \\
   n & n & n & n & n \\
   n & n &   & n & n \\
   n &   & n &   & n \\
   n & n & n & n & n \\
   n &   & n &   & n \\  
\end{Bmatrix}
$$
---
# 4. 进入程序部之后想学的东西
* 首先当然是最最最有趣的软件制作了，目前计算机主修C语言，见过能运行的巅峰便是**贪吃蛇**的小游戏，希望可以学到音频同步的唯美程序；
* 其次就是了解各个编程语言的大概框架和适合范围；
* 最后当然是和同伴们一起协作完成任务啦！
---