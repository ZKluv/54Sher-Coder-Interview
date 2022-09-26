# 杨同学的git＆Markdown学习记录
---
## 学习git的过程
本人访问了**廖雪峰的官方网站**,确实如同网页中所说的,此[git教程][1]属实简单易懂,~~奈何本人实在是很难对网页中的大段文字有高效率的阅读~~,我投入了一个多小时来进行git的安装与理解.
经过简单地安装与部署之后,我成功在Windows11系统中安装上了属于我电脑的Git,用git config命令的--global参数完成了安装完成后的<u>最后一步设置.</u>

然后,我开始学习创建仓库(aka*版本库*),我了解到它是一个目录,这个目录里面的文件被Git所管理,其中文件的修改与删除都可以被Git跟踪.
短暂的网页阅读之后,我开始比对着网页上的教程开始创建一个~~简单的~~版本库.我个人总结出的要点如下:
- 对git仓库的创建与初始化;
- 将文件添加到git仓库中以及一些基础命令的学习(如*git add init*).

愉快的git深入学习到此开始了.
## 学习Markdown的过程
本人访问了**RUNOOB.com**来进行有关Markdown知识的学习,也搜索了一些b站相关教程等,runoob网站感觉很全面,基本能够满足相关学习需要.
## 学习Markdown的实践
1. 段落格式可以体现在上文的一些内容中,相信阅读这个文档的**聪明**的你,一定发现了,这里不再多写啦.
2. 列表:来点嵌套:
    - 我是1;
    - 我是0.
3. 区块:
   * 朝天门
   >我喜欢在丛林里面抢肉吃,因为我是来自真正的底层
   >>当我站在两江交汇之处,我身上流的是劳动人民的血.
    >>>我太帅咯 I got ring.
    >>>下游戏 直接就钻进了VIP.
4. 代码(来个连点器)
    #include<stdio.h>
    #include<windows.h>


    int main()
{
	while(1)
	{
		if(GetAsyncKeyState(VK_SPACE))
		{
			while(1)
			{
					mouse_event(MOUSEEVENTF_LEFTDOWN|MOUSEEVENTF_LEFTUP,0,0,0,0);
					Sleep(5000 ); 
					if(GetAsyncKeyState(VK_ESCAPE))return 0;
			}
		}
	}
	return 0;
}
5. 给大家来点好康的 [速速点击我](https://www.bilibili.com/video/BV1GJ411x7h7/?spm_id_from=333.337.search-card.all.click&vd_source=b07832401ab52aea7a3628ecc47d52ae)

哈哈哈,这个更好康 [速速点击我][2]

6.你先别急,让我先急
<img src="https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E6%88%91%E6%98%AF%E6%80%A5%E6%80%A5%E5%9B%BD%E7%8E%8B&step_word=&hs=0&pn=1&spn=0&di=7136437450519347201&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=2832600140%2C2873050969&os=3883879932%2C1112680013&simid=4270670984%2C667827789&adpicid=0&lpn=0&ln=1561&fr=&fmq=1664111373988_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%3A%2F%2Fimg.nga.178.com%2Fattachments%2Fmon_202207%2F27%2F-klbw3Q2q-90hfKhToS8s-7y.jpg%26refer%3Dhttp%3A%2F%2Fimg.nga.178.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1666703379%26t%3Df7555f8dc5c68e72ae617c60c26b7348&fromurl=ippr_z2C%24qAzdH3FAzdH3Fkkf_z%26e3Bg2w_z%26e3BvgAzdH3F6jw1_z%26e3Brir%3Fpt1%3Dndbd0nld%26rw2j%3Dj&gsm=200000000000002&rpstart=0&rpnum=0&islist=&querylist=&nojc=undefined&dyTabStr=MCw2LDQsNSwzLDEsNyw4LDIsOQ%3D%3D">
图片会不会显示不出来(害怕.jpg),急急急急急急.
7. 表格
|      |超人|蝙蝠侠|神奇女侠|闪电侠|绿灯侠|
| ---- | ---- | ---- | ---- | ---- | ---- |
|秘密身份|克拉克 肯特|布鲁斯 韦恩|戴安娜 普林斯|巴里 艾伦|哈尔 乔丹|
8. 数学谁不爱呢？
$$ f(x)=csc x 
$$
$$ 无穷小：当自变量x无限接近x0（或x的绝对值无限增大）时，函数值f(x)与0无限接近，即f(x)→0(或f(x)=0)，则称f(x)为当x→x0(或x→∞)时的无穷小量
$$

好啦，~~今天的~~markdown实践就到这里啦！
## 进入程序部之后想学习的东西

我或许不是一个很有规划的人，进入程序部之后我想认识更多深耕技术栈的大佬，向他们学习，希望这有一天能和他们比肩，精进自己的c语言技术，以及html，css，js；学习并精进python，JAVA等编程语言，参与做出一款让自己满意的微信小程序。

综上！




[1]:https://www.runoob.com/markdown/md-tutorial.html
[2]:https://www.bilibili.com/video/BV1Pg411r7V5/?spm_id_from=333.337.search-card.all.click&vd_source=b07832401ab52aea7a3628ecc47d52ae
