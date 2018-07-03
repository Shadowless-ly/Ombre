# title: Linux下使用dkms制作驱动镜像

``` markdown
date: 2018/5/31 16:40:00
updated:
tags: ['linux', 'SIT']
categories: Linux
layout:
comments: true
permalink:
----
```

在使用PXE安装系统时，发现系统在加载initrd时出现drucut加载网卡驱动失败的现象，经查看系统日志，发现为服务器上MLOM卡芯片为Intel X722系列，CentOS7.2官网镜像中的i40e驱动无法兼容该网卡。为解决此问题，有两种方法可以选择。

1. 将i40e驱动加入initrd.img中，直接替换PXE服务器上的ramdisk。
2. 制作linux dd驱动镜像，在启动时为内核添加linux dd参数，安装指定驱动。

本次采用第二种方式，使用dkms制作linux驱动镜像。

## DKMS介绍
动态内核模块支持 (DKMS) 是一个程序框架，可以编译内核代码树之外的模块。升级内核时，通过 DKMS 管理的内核模块可以被自动重新构建以适应新的内核版本。