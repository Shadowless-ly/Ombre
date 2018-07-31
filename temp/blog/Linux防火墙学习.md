[TOC]

# Linux防火墙学习笔记

## 简介

在Linux 2.4之后，使用的防火墙架构为Netfilter，它是一个通用、抽象的框架，提供了一整套hook函数的管理机制，使得数据包过滤，NAT和基于协议类型的连接跟踪成为可能。

Netfilter实现了如下功能：

* 网络地址转换（NAT）
* 数据包内容修改
* 数据包过滤的防火墙

Netfilter实现了数据包的五个Hook Point，分别是PRE_ROUTING、INPUT、OUTPUT、FORWARD、POST_ROUTING。

Netfilter所设置的规则存放在内核内存中，我们可以使用iptables，firewalld这些应用层程序通过Netfilter提供的接口对内核内存中的Netfilter配置表进行修改。这些表由tables、chains、rules组成。

## iptables的表和链

### 规则表

表提供了特殊的功能，iptables中有4个表，filter，nat，mangle，raw，分别实现

iptables中有如下表：

|  表名  |                             功能                             |                       链                        |
| :----: | :----------------------------------------------------------: | :---------------------------------------------: |
| filter |                 过滤数据包：iptables_filter                  |             INPUT，FORWARD，OUTPUT              |
|  nat   |      网络地址转换(IP、端口)。对应内核模块：iptable_nat       |         PREROUTING，POSTROUTING，OUTPUT         |
| mangle | 修改数据包的服务类型、TTL、并且可以配置路由实现QOS。对应内核模块：iptable_mangle | PREROUTING，POSTROUTING，INPUT，OUTPUT，FORWARD |
|  raw   | 决定数据包是否被状态跟踪机制处理。对应内核模块：iptable_raw  |               OUTPUT，PREROUTING                |

规则表的优先顺序：

**raw ---> mangle ---> nat ---> filter**



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







