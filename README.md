# git-fix-mode

有时因为一些奇怪的原因 git 库中会提示有很多修改，类似 old mode 100644 new mode 100755 之类的，

（比如一个同事把 windows 下的 git 打包发给了你）

库中的几万个 change 会搞得你心神不宁，无法确定当前正确的 base 。这个小脚本就是用来解决这种问题。

在项目顶层目录执行：

```
> git diff --diff-filter=d > diff.txt

> ./fix-mod.py

```

即可

如果这个小脚本能够帮你节省 5 分钟时间，请帮我点个 star，谢谢  ;)
