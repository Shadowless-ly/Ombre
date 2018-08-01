[TOC]

# Linux防火墙学习笔记

> [iptables详解](https://www.zsythink.net/archives/tag/iptables)

## 简介

在Linux 2.4之后，使用的防火墙架构为Netfilter，它是一个通用、抽象的框架，提供了一整套hook函数的管理机制，使得数据包过滤，NAT和基于协议类型的连接跟踪成为可能。

Netfilter实现了如下功能：

* 网络地址转换（NAT）
* 数据包内容修改
* 数据包过滤的防火墙

Netfilter实现了数据包的五个Hook Point，分别是PRE_ROUTING、INPUT、OUTPUT、FORWARD、POST_ROUTING。

Netfilter所设置的规则存放在内核内存中，我们可以使用iptables，firewalld这些应用层程序通过Netfilter提供的接口对内核内存中的Netfilter配置表进行修改。这些表由tables、chains、rules组成。

## iptables的链和表

在收到数据包时，按照预定义的规则：如果数据包头符合一定条件就按照要求处理数据包。规则存储在内核空间的数据包过滤表中，这些规则可以指定源地址，目的地址，传输协议，服务类型等，当与规则匹配时，iptables就按照规则所定义方法处理。

### 规则链

链是数据包的传播路径，每一条链就是众多规则中的一个检查清单，每一条链中可以有数条规则。当数据包到达一个链，iptables就会从链的第一条规则开始检查，是否满足所定义规则，若满足则根据定义的方法处理该数据包，否则继续检查，直到全部不符合，按照该链默认策略处理该数据包。

|    名称     |            描述            |
| :---------: | :------------------------: |
| PREROUTING  | 在进行路由选择前处理数据包 |
|    INPUT    |      处理流入的数据包      |
|   OUTPUT    |      处理流出的数据包      |
|   FORWARD   |      处理转发的数据包      |
| POSTROUTING | 在进行路由选择后处理数据包 |

其作用位置如下图表示：





### 规则表

表提供了特殊的功能，iptables中有4个表，filter，nat，mangle，raw，分别实现

iptables中有如下表：

|  表名  |                             功能                             |                       链                        |
| :----: | :----------------------------------------------------------: | :---------------------------------------------: |
| filter |                 过滤数据包：iptables_filter                  |             INPUT，FORWARD，OUTPUT              |
|  nat   |      网络地址转换(IP、端口)。对应内核模块：iptable_nat       |     PREROUTING，POSTROUTING，INPUT，OUTPUT      |
| mangle | 修改数据包的服务类型、TTL、并且可以配置路由实现QOS。对应内核模块：iptable_mangle | PREROUTING，POSTROUTING，INPUT，OUTPUT，FORWARD |
|  raw   | 决定数据包是否被状态跟踪机制处理。对应内核模块：iptable_raw  |               OUTPUT，PREROUTING                |

规则表的优先顺序：

**raw ---> mangle ---> nat ---> filter**



### 表与链的关系

链相当于在数据包传播路上的检查点，经过该检查点，会依次匹配链上的每一条规则。

表则是对规则的分类，对数据包的不同类型操作划分到不同的表中。

我们可以简单理解为在某一个检查点（链）会有多种检查/修改能力（表）。

那么我们来探索一下每一个链中都可以有哪种表的规则：

| 链（HOOK POINT） | 表（function）           |
| ---------------- | ------------------------ |
| PREROUTING       | raw、mangle、nat         |
| INPUT            | mangle、filter、nat      |
| FORWARD          | mangle、nat、filter      |
| OUTPUT           | raw、mangle、nat、filter |
| POSTROUTING      | mangle、nat              |

## 管理命令

### 规则查询

```shell
iptables -t 表名 -L
# 查看对应表的所有规则

iptables -t 表名 -L 链名
# 查看指定表的指定链中的规则

iptables -t 表名 -v -L
# 查看指定表中所有规则，-verbose，会显示计数器信息

iptables -t 表名 -n -L
# 对规则中IP和接口不解析

iptables --line-numbers -t 表名 -L
# 表示查看表的所有规则，且显示规则的序号

iptables --line -t -filter -nxvL
# 查看filter表的所有链，不解析IP且显示计数器最详细的信息

iptable --line -t filter -nvxL INPUT
# 查询指定表，指定链详细信息

```



### 规则管理

iptables常用的匹配条件：`源地址`、`目标地址`、`源端口`、`目标端口`

常用的动作：`接受(ACCEPT)`、`丢弃(DROP)`、`拒绝(REJECT)`

```shell
iptables -t 表名 -A 链名 匹配条件 -j 动作
iptables -t filter -A INPUT -s 1.1.1.1 -j DROP
# 向指定表，指定链的尾部添加一条规则，-A选项表示在对应链的末尾添加规则

iptables -t 表名 -I 链名 [位置] 匹配条件 -j 动作
iptables -t filter -I INPUT 2 -s 1.1.1.1 -j ACCEPT
# 向指定表，指定链的指定位置加入规则

iptables -t 表名 -P 链名 动作
iptables -t filter -P FORWARD ACCEPT
# 修改指定表的FORWARD链的默认策略设置为ACCEPTE

iptables -t 表名 -D 链名 规则序号
iptables -t filter -D INPUT 3
# 删除filter表,INPUT链的第三行

iptables -t 表名 -D 链名 匹配条件 -j 动作
iptables -t filter -D INPUT -s 1.1.1.1 DROP
# 删除filter表，INPUT链匹配的规则

iptables -t 表名 -F
iptables -t 表名 -F INPUT
# 清空规则

iptables -t 表名 -R 链名 规则序号 规则原本的匹配条件 -j 动作
iptables -t filter -R INPUT 3 -s 1.1.1.1 -j ACCEPT
# 修改指定位置的规则，注意保持原不变条件

iptables -t 表名 -P 链名 动作
iptables -t filter -P FORWARD ACCEPT
# 修改filter表，FORWARD链，默认策略为ACCEPT

规则保存位置/etc/sysconfig/iptables
service iptables save
iptables-save > /etc/sysconfig/iptables
iptables-restore < /etc/sysconfig/iptables
```







