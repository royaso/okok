---
layout: default
title: github-pages
---

0. 先在github上建立一个repo(仓库)
1. mkdir myblog; cd myblog  #新建一个目录
2. git init     #在此目录初始化为git仓库
3. git checkout --orphan gh-pages # 新建一个branch
4. echo "---\n---\n\n this is my blog"> index.md #博客首页
5. git add . #添加到index,准备下步推送到本地仓库
6. git commit -m 'blog init' #推送到本地仓库
7. git remote add origin git@github.com:royaso/myblog #添加github上的远程仓库
8. git push --set-upstream orgin gh-pages #推送到github上的gh-pages
9. 访问地址:  http://royaso.github.io/myblog

