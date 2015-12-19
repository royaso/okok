---
layout: default
title: 翻译:魔方解法视频教程第一集--第一次制作字幕
---

视频内容: 14分钟

bilibili:<iframe height=498 width=510 src="http://www.bilibili.com/html/player.html?aid=2131968" frameborder=0 allowfullscreen></iframe>

youku:<embed src="http://player.youku.com/player.php/sid/XMTQxNzY0ODQ4MA==/v.swf" allowFullScreen="true" quality="high" width="480" height="400" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash"></embed>

youku:<iframe height=498 width=510 src="http://player.youku.com/embed/XMTQxNzY0ODQ4MA==" frameborder=0 allowfullscreen></iframe>

没实际的教学,因为是第一篇嘛.总得介绍介绍.

zz解法的由来历史,大概分为三步:EO边,F2L,最后一层

作者的体会

作者附带的txt文件内容


------


具体的历程看[这里](http://royaso.com/20)

我会魔方,会英语,玩linux. Because I can,所以我就做了

一直想尝试自己做字幕,一来这种想法不是非常强烈,二来也没找到好的机会,"所以这就是你拖延的借口?",真要说借口的话,以后我会说,做字幕很累很费时不容易,但是从头到尾一条龙的感觉很爽!!I take all the credits!什么都是我的,我做的好与坏,责任和荣誉共担,只有一个人.linux的单一原则.

自己做喜欢的视频的字幕,自己听译英文,自己调整制作字幕时间线,调一句听译一句,不懂就反复听,自己检查校对,写到这发觉有个步骤打算做却没做:用aspell检查拼写,(马上试了下'aspell -l en_US -c a.ass' 额,居然错别字那么多,丢脸啊,算了以后再说吧,都已经压制好视频了.)自己翻译中文,查看两个字幕同时播放效果,自己打水印,自己压制视频,等下还要自己上传发布,还有相关的字幕文件分享以便协作修改(github),自己写这篇感想博文总结.能不累吗?期间还被发了张"朋友卡",收货丰富啊!!

我的体会
- zz解法独特在哪里,相对于我所学的CFOP.
- 第一步还原边块色相,这步为顶层的十字打好基础了
- 筑基可以双向来很灵活,如果再学习空槽就更灵活了
- 看作者说话间很随意就还原好了,很快!我还在一分钟徘徊,跟他们小孩子一个成绩
- 万变不离其宗,所以说基础很重要.我虽然学的CFOP但很多东西是相通的F2L什么的
- 其他的也学才有可能触类旁通.像盲拧,要不是学了盲拧,知道有色相这东西,视频的下一集我就得看的吃力了,昨晚看睡着了,因为我都知道了啊
- 翻译很累,字幕制作很累,做好了感觉不错,至少知道以后再做就不难了
- 专心投入就不会留意到时间的流逝
- 高中英语老师的话我只记得一句:小词难听
- 英语不使用连简单的词都要查字典了
- 求美女!!!!

------

我的福利

- 中英字幕: 中文下载  英文下载
- 源视频全套哦: 
- 
-



命令总结

- 字幕压进视频 `ffmpeg -i yyy.mp4 -vf ass=/home/roya/yyyyy.ass  -vcodec libx264 -acodec copy zzz.mp4`
- 拼写检查 `aspell -l en_US -c a.txt`
- mpv加载双字幕
```
mpv ZZ\ Method\ Tutorial\ Part\ 1-\ Introduction.mp4 --sub-file="/home/roya/aaaxxx.ass"    --sub-file="/home/roya/rubic-cube-zz.ass" --sid=2 --secondary-sid=1
```

Aegisub使用总结:

- 快捷键c-j:视频播放暂停
- c-k:把当前视频时间点设置为字幕结束点(运气好的话,那种一刻讲不停的视频,再结合上一条就够用了)
- c-l:把当前视频时间点设置为字幕开始点(比较少用,如果字幕有时间空白的话)
- c-m:把视频开始点设置成当前的字幕开始点,听译反复常用!
- c:字幕时间的往前20ms,
- v:字幕时间的往后20ms,
- 字幕翻译助手


如果能用油管,据说有自动生成字幕的功能,就不用自己调整时间线和英文了,只要翻译成中文就行.SO you know
------

作者附带的txt文件内容


Part 2: http://www.youtube.com/watch?v=7SzFNhs_ZRE



Excellent text tutorial by Conrad Rider: http://cube.crider.co.uk/



SpeedSolving Wiki: http://www.speedsolving.com/wiki/index.php/ZZ_Method



How I found the ZZ Method: http://www.speedsolving.com/forum/showthread.php?5180-ZZ-speedcubing-method



Winter Variation: http://www.speedsolving.com/wiki/index.php/Winter_Variation

CLS: http://www.speedsolving.com/wiki/index.php/CLS



My WCA: http://www.worldcubeassociation.org/results/p.php?i=2010YUPH01

ZZ's WCA: http://www.worldcubeassociation.org/results/p.php?i=2003ZBOR02



Walkthrough solves (2H): http://www.youtube.com/watch?v=d0vVDBi3_EU

Walkthrough solves (OH): http://www.youtube.com/watch?v=8-DaC4Bs2sU



13.28 avg12 (OH): http://www.youtube.com/watch?v=JXQLV-9q_mo

10.83 avg5 (2H): http://www.youtube.com/watch?v=8hbEa4LugEg
