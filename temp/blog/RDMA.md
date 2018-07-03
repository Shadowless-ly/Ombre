[TOC]
RDMA
=====
>Direct Memory Access (DMA)是一种设备直接访问主机内存而不需要通过CPU参与拷贝的方法。
Remote Direct Memory Memory Access(RDMA) 是一种直接访问（读，写）远程设备内存而不需要CPU分配中断。

### RDMA的概述 ###
* **零拷贝**：应用程序可以在不使用网络协议栈的情况下执行数据传输。数据被直接发送并直接接收到缓冲区，而不需要在网络层之间复制。
* **内核旁路**：应用程序可以直接从用户空间执行数据传输，而不需要内核参与。
* **没有CPU的参与**：应用程序可以访问远程内存，而不需要在远程服务器消耗任何CPU时间。远程服务器内存可以在不受远程进程（或处理器）的任何干预的情况下读取，远程CPU缓存不会被要访问的内容占用。
---
&emsp;&emsp;随着网络带宽和速度的发展以及大数据量数据的迁移需求，网络带宽增长速率远远高于处理网络流量时所必须的计算节点能力和对内存带宽的需求。数据中心网络架构已经逐步成为计算和存储技术的瓶颈。
&emsp;&emsp;传统的TCP/IP技术在数据包的处理过程中需要经过操作系统和其他软件层，需要占用大量的服务器资源和内存总线带宽，所产生的延迟来自于系统的庞大开销、系统在数据内存、处理器缓存和网络控制器缓存之间来回进行复制移动，给服务器CPU和内存带来了沉重负担。当面对网络带宽、处理器速度与内存带宽三者的严重"不匹配"，更造成了网络延迟效应的加剧。而且，每处理一个数据包时，数据必须在系统内存，处理器缓存和网络控制器缓存之间来回移动，因此延迟并不是一次性的，而是会对系统性能持续产生负面影响。
![](index_files/_u6570_u636E_u5305_u5728_u7F13_u5B58_u4E4B_u95F4_u62F7_u8D1D.png)
&emsp;&emsp;由此，以太网的低投入、低运营成本优势就难以体现。为了充分发挥万兆以太网的优势，必须解决应用性能问题。系统不能以软件的方式持续的处理以太网通信；CPU资源必须释放出来专注于应用处理。多数以太网适配器采用TOE（TCP Offload engine）的方式，利用网络适配器芯片处理部分报文以卸载CPU的压力。使用TOE方案能够使TCP通信更快速，但是还达不到高性能网络应用的要求。解决这类问题的关键就是要消除主机CPU中不必要的频繁数据传输，减少系统间的信息延迟。
&emsp;&emsp;RDMA是Infiniband技术的基础。产业标准API（应用程序接口）使RDMA成为从技术走向实现。其中包括用于低时延消息处理、成就高性能计算的MPI（消息通过接口），以及DAPL（直接接入供应库）。后者包括KDAPL和UDAPL，分别用于内核和用户（应用程序）。Linux支持KDAPL，其他操作系统将来也有可能支持。RDMA在HPC环境广为采纳，在商用领域很少。但是，如今大多是应用程序都能直接支持操作系统，透过操作系统（如NFS）间接利用RDMA技术的优势是完全可能的。

### RDMA原理 ###
&emsp;&emsp;RDMA技术是一种网卡技术，采用该技术可以使计算机直接将信息放入另一台计算机的内存中。通过最小化处理过程的开销和带宽的需求降低时延。RDMA可以通过在网卡上将可靠传输协议固话于硬件，以及支持零复制网络技术和内核旁路技术这两种途径来达到这一目标。

![](index_files/RDMA_u539F_u7406.png)

零复制网络技术使NIC可以直接与应用内存相互传输数据，从而消除了在应用内存与内核内存之间复制数据的必要。

内核旁路技术使应用程序无需执行内核内存调用就可向网卡发送命令。在不需要任何内核内存的参与条件下，RDMA请求从用户空间发送到本地NIC并通过网络发送给远程NIC，这就减少了在处理网络传输流是内核内存空间与用户空间之间环境切换的次数。

当一个应用程序执行RDMA读/写请求时，系统并不执行数据复制动作，这样减少了处理网络通信时在内核空间和用户空间上下文切换的次数。在不需要任何内核参与的条件下，RDMA请求从运行在用户空间中的应用中发送到本地网卡，然后又经过网络传输到远程网卡。请求完成既可以完全在用户空间中处理（通过轮询用户级完成排列），或者在应用一直睡眠到请求完成时的情况下通过内核内存处理。

### RDMA操作类型 ###
&emsp;&emsp;具备RNIC（RDMA-aware network interface controller）网卡的设备，不论是目标设备还是源设备的主机处理器都不会涉及到数据传输操作，RNIC网卡负责产生RDMA数据包和接收输入的RDMA数据包，从而消除传统操作系统中多余的内存复制操作。
RDMA协议提供一下4种数据传输操作，除了RDMA读操作不会产生RDMA消息，其他操作都会产生一条RDMA消息。
RDMA Send操作；
Send Operation；
Send with invalidate operation；
Send with solicited event；
Send with solicited event and invalidate；
RDMA Write操作；
RDMA Read操作；
Terminate操作；

### RDMA over TCP ###
以太网凭借其低投入、向后兼容、易升级、低成本优势在目前网络互连领域内占据统治地位，目前主流以太网速率为100Mb/s和1000Mb/s，下一代以太网速率将会升级到10Gb/s。将RDMA特性增加到以太网中，将会降低主机处理器利用率，增加以太网升级到10Gb/s的优点，消除由于升级到10Gb/s而引入的巨大开销的弊端，允许数据中心在不影响整体性能的前提下拓展机构，为未来拓展需求提供足够的灵活性。
RDMA over TCP能够将数据直接在两个系统的应用内存之间进行交互，而不需要内核参与，不需要临时复制到内存中的操作。
![](index_files/RDMA_20over.png)
RDMA over TCP协议能够工作在标准的基于TCP/IP协议的网络，支持多种传输类型共享相同的物理连接，如网络，文件系统，块存储和处理器之间的通信。
![](index_files/RDMA_20over_20TCP.png)

RDMA层协议负责RDMA写操作、读操作，转换成RDMA消息，并将消息传向DDP（Direct Data Placement）层。DDP层协议负责将过长的RDMA消息分段封装成DDP数据包继续向下转发到Marker-Based，Protocol-data-unit-Aligned（MPA层）。MPA层在DDP数据段的固定位置增加一个后向标志、长度以及CRC校验数据，构成MPA数据段。

### RDMA解决方案 ### 
RDMA被应用于很多行业：
1. HPC
2. Data Centers
3. Web 2.0
4. Big Data
5. Cloud
6. Storage
7. Finance Services and Insurance
8. Medical Services
9. Federal

### 如何使用RDMA ###
需要网卡适配RDMA功能。
链路层协议可以使以太网或者Infiniband，两者都可传输基于RDMA的应用程序
RDMA功能由操作系统内部支持，如Linux，Windows，VMware。

### Mellanox CX3网卡运行RoCE功能并使能PFC ###
#### 组网环境图 ####
![](index_files/RoCE_20Network_20connectivity.png)
#### PFC配置 ####
**Switch配置**
交换机上切换port模式为trunk并permit all vlan
[H3C]interface gigbitethernet 1/0/1
[H3C-GigbitEthernet1/0/1]priority-flow-control enable
[H3C-GigbitEthernet1/0/1]priority-flow-control no-drop dot1p 3
[H3C-GigbitEthernet1/0/1]qos trust dot1p
[H3C-GigbitEthernet1/0/1]quit

**查看开启状态**
[H3C-Ten-GigabitEthernet1/0/10]dis priority-flow-control interface Ten-GigabitEthernet 1/0/10
Interface&emsp;&emsp;&emsp;AdminMode&emsp;&emsp;&emsp;OperMode&emsp;&emsp;&emsp;Dot1pList&emsp;&emsp;&emsp;Prio&emsp;&emsp;&emsp;Recv&emsp;&emsp;&emsp;Send
\--------------------------------------------------------------------------------
XGE1/0/10&emsp;&emsp;&emsp;Enabled&emsp;&emsp;&emsp;&emsp;&emsp;Enabled&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;3

** 修改网卡驱动配置 **
修改文件`/etc/modprobe.d/mlx4_en.conf`
添加内容`options mlx4_en pfctx=0x08 pfcrx=0x08`
** 重启配置文件 **
`# /etc/init.d/openibd restart`
** 检查配置 **
``` RX=`cat /sys/module/mlx4_en/parameters/pfcrx`;printf "0x%x\n" $RX ```

#### 创建Vlan ####
modprobe 8021q
vconfig add eth1 100
ifconfig eth1.100 11.11.100.1/24 up


#### 配置VLAN egress priority ####
vconfig命令是一个linux命令，用来配置每个vlan流量外出的优先级，该命令适用于通过内核TCP/IP协议栈的应用。
`# for i in {0..7};do vconfig set_egress_map eth1.100 $i 3;done`
使用Mellanox OFED驱动提供的脚本tc_wrap.py可以将skb_prio映射到用户优先级，该脚本可以为特定类型的流量（如RoCE）配置优先级以绕过内核，通过添加VLAN TAG的方式将名为skb_prio内核优先级协议应射程用户优先级。
```
# tc_wrap.py -i eth1 -u 3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3
UP 0
UP 1
UP 2
UP 3
        skprio: 0
        skprio: 1
        skprio: 2 (tos: 8)
        skprio: 3
        skprio: 4 (tos: 24)
        skprio: 5
        skprio: 6 (tos: 16)
        skprio: 7
        skprio: 8
        skprio: 9
        skprio: 10
        skprio: 11
        skprio: 12
        skprio: 13
        skprio: 14
        skprio: 15
        skprio: 0 (vlan 100)
        skprio: 1 (vlan 100)
        skprio: 2 (vlan 100 tos: 8)
        skprio: 3 (vlan 100)
        skprio: 4 (vlan 100 tos: 24)
        skprio: 5 (vlan 100)
        skprio: 6 (vlan 100 tos: 16)
        skprio: 7 (vlan 100)
UP 4
UP 5
UP 6
UP 7
### ### #
```
** 对于以太网卡，可以通过以下命令将所有流量映射到特定的优先级 **
`# echo "ens785f1.100 3" > /sys/fs/cgroup/net_prio/net_prio.ifpriomap`

#### 验证程序 ####
以下命令创建两个RoCE流到主机S1
```
//Run on host S1
# ib_write_bw -R --report_gbits --port=12500 -D 10 & ib_write_bw -R --report_gbits --port=12510 -D 10
//Run on host S2
# ib_write_bw -R --report_gbits 11.11.100.1 --port=12500 -D 10
//Run on host S3
# ib_write_bw -R --report_gbits 11.11.100.1 --port=12510 -D 10
```
从host读取端口优先级计数器
```
# ethtool -S eth1 | grep prio_3
      rx_prio_3_packets: 5152
      rx_prio_3_bytes: 424080
      tx_prio_3_packets: 328209
      tx_prio_3_bytes: 361752914
      rx_pause_prio_3: 14812
      rx_pause_duration_prio_3: 0
      rx_pause_transition_prio_3: 0
      tx_pause_prio_3: 0  
      tx_pause_duration_prio_3: 47848
      tx_pause_transition_prio_3: 7406
```

### Mellanox CX4网卡运行RoCE功能并使能PFC ###
#### PFC配置 ####
**Switch配置**
交换机上切换port模式为trunk并permit all vlan
[H3C]interface gigbitethernet 1/0/1
[H3C-GigbitEthernet1/0/1]priority-flow-control enable
[H3C-GigbitEthernet1/0/1]priority-flow-control no-drop dot1p 4
[H3C-GigbitEthernet1/0/1]qos trust dot1p
[H3C-GigbitEthernet1/0/1]quit

** 使用mlnx_qos工具 **
使用-h选项查看可用参数，以下示例为 MLNX_OFED version 3.3及以后版本
`# mlnx_qos -h`
```
Usage: mlnx_qos -i <interface> [options]
Options:
  --version                 show program's version number and exit
  -h, --help                show this help message and exit
  -f LIST, --pfc=LIST       Set priority flow control for each priority. LIST is comma separated value for each priority starting from 0 to 7. Example: 0,0,0,0,1,1,1,1 enable PFC on TC4-7
  -p LIST, --prio_tc=LIST   maps UPs to TCs. LIST is 8 comma seperated TC numbers. Example: 0,0,0,0,1,1,1,1 maps UPs 0-3 to TC0, and UPs 4-7 to TC1
  -s LIST, --tsa=LIST       Transmission algorithm for each TC. LIST is comma seperated algorithm names for each TC. Possible algorithms: strict, etc. Example: ets,strict,ets sets TC0,TC2 to ETS and TC1 to strict. The rest are unchanged.
  -t LIST, --tcbw=LIST      Set minimal guaranteed %BW for ETS TCs. LIST is comma seperated percents for each TC. Values set to TCs that are not configured to ETS algorithm are ignored, but must be present. Example: if TC0,TC2 are set to ETS,   then 10,0,90 will set TC0 to 10% and TC2 to 90%. Percents must sum to 100.
  -r LIST, --ratelimit=LIST Rate limit for TCs (in Gbps). LIST is a comma seperated Gbps limit for each TC. Example: 1,8,8 will limit TC0 to 1Gbps, and TC1,TC2 to 8 Gbps each.
  -i INTF, --interface=INTF Interface name
  -a Show all interface's TCs
 ```

**显示指定接口的PFC配置，输出显示没有优先级被使能（全部为0）**
```
    # mlnx_qos -i eth35
    PFC configuration:
      priority    0   1   2   3   4   5   6   7
      enabled     0   0   0   0   0   0   0   0
     
    tc: 0 ratelimit: unlimited, tsa: vendor
      priority:  1
    tc: 1 ratelimit: unlimited, tsa: vendor
      priority:  0
      skprio: 0
      skprio: 1
      skprio: 2 (tos: 8)
      skprio: 3
      skprio: 4 (tos: 24)
      skprio: 5
      skprio: 6 (tos: 16)
      skprio: 7
      skprio: 8
      skprio: 9
      skprio: 10
      skprio: 11
      skprio: 12
      skprio: 13
      skprio: 14
      skprio: 15
    tc: 2 ratelimit: unlimited, tsa: vendor
      priority:  2
    tc: 3 ratelimit: unlimited, tsa: vendor
      priority:  3
    tc: 4 ratelimit: unlimited, tsa: vendor
      priority:  4
    tc: 5 ratelimit: unlimited, tsa: vendor
      priority:  5
    tc: 6 ratelimit: unlimited, tsa: vendor
      priority:  6
    tc: 7 ratelimit: unlimited, tsa: vendor
      priority:  7
```

** 使用mlnx_qos工具配置PFC **
```
    # mlnx_qos -i eth35 --pfc 0,0,0,0,1,0,0,0
    PFC configuration:
      priority    0   1   2   3   4   5   6   7
      enabled    0   0   0   0   1   0   0   0

    tc: 0 ratelimit: unlimited, tsa: vendor
      priority:  1
    tc: 1 ratelimit: unlimited, tsa: vendor
      priority:  0
      skprio: 0
      skprio: 1
      skprio: 2 (tos: 8)
      skprio: 3
      skprio: 4 (tos: 24)
      skprio: 5
      skprio: 6 (tos: 16)
      skprio: 7
      skprio: 8
      skprio: 9
      skprio: 10
      skprio: 11
      skprio: 12
      skprio: 13
      skprio: 14
      skprio: 15
    tc: 2 ratelimit: unlimited, tsa: vendor
      priority:  2
    tc: 3 ratelimit: unlimited, tsa: vendor
      priority:  3
    tc: 4 ratelimit: unlimited, tsa: vendor
      priority:  4
    tc: 5 ratelimit: unlimited, tsa: vendor
      priority:  5
    tc: 6 ratelimit: unlimited, tsa: vendor
      priority:  6
    tc: 7 ratelimit: unlimited, tsa: vendor
      priority:  7
```
#### 配置VLAN egress priority ####
** 加载802.1q模块 **
`modprobe 8021q`
** 创建Vlan接口并配置Egress Priority **
如要在物理网口eth35上创建vlan 100，需要创建文件`/etc/sysconfig/network-scripts/ifcfg-eth35.100`
```
    VLAN=yes
    TYPE=Vlan
    DEVICE=eth35.100
    PHYSDEV=eth35
    VLAN_ID=100
    REORDER_HDR=0
    VLAN_EGRESS_PRIORITY_MAP=0:4
    # Another options is to map more priorities. For example, in this case all kernel priorities are mapped to egress priority 4.
    # VLAN_EGRESS_PRIORITY_MAP=0:4,1:4,2:4,3:4,4:4,5:4,6:4,7:4
    BOOTPROTO=static
    DEFROUTE=yes
    IPV4_FAILURE_FATAL=no
    NAME=eth35.100
    ONBOOT=yes
    IPADDR=12.12.12.5
    NETMASK=255.255.255.0
    NM_CONTROLLED=no
```
配置完成后重启网络服务
可以使用`tc_wrap.py -i eth35`验证UP 4被映射到VLAN

** 配置RoCE流量的外出优先级 **
使用tc_wrap.py脚本将所有内核优先级映射到L2 priority 4
```
    # tc_wrap.py -i eth35 -u 4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4
    UP  0
    UP  1
    UP  2
    UP  3
    UP  4
      skprio: 0
      skprio: 1
      skprio: 2 (tos: 8)
      skprio: 3
      skprio: 4 (tos: 24)
      skprio: 5
      skprio: 6 (tos: 16)
      skprio: 7
      skprio: 8
      skprio: 9
      skprio: 10
      skprio: 11
      skprio: 12
      skprio: 13
      skprio: 14
      skprio: 15
      skprio: 0 (vlan 100)
      skprio: 1 (vlan 100)
      skprio: 2 (vlan 100 tos: 8)
      skprio: 3 (vlan 100)
      skprio: 4 (vlan 100 tos: 24)
      skprio: 5 (vlan 100)
      skprio: 6 (vlan 100 tos: 16)
      skprio: 7 (vlan 100)
    UP  5
    UP  6
    UP  7
```

#### 验证程序 ####
参考如下方式使用perftest包
使用show-gids脚本查询对应设备的GID
在服务端运行命令
`ib_write_bw --report_gbits -D5 -d mlx5_1 -F -x 6(GID) -S 4(Priority)`
在服务端运行如下命令
`ib_write_bw --report_gbits -D5 -d mlx5_1   -F  13.13.13.6 -x 6(GID) -S 4(Priority)`
```
------------------------------------------------------------------------------
                    RDMA_Write BW Test
Dual-port       : OFF Device         : mlx5_1
Number of qps   : 1 Transport type : IB
Connection type : RC Using SRQ      : OFF
TX depth        : 128
CQ Moderation   : 100
Mtu             : 4096[B]
Link type       : Ethernet
Gid index       : 6
Max inline data : 0[B]
rdma_cm QPs : OFF
Data ex. method : Ethernet
------------------------------------------------------------------------------
local address: LID 0000 QPN 0x01e5 PSN 0x3df409 RKey 0x005a00 VAddr 0x007f786a310000
GID: 00:00:00:00:00:00:00:00:00:00:255:255:13:13:13:05
remote address: LID 0000 QPN 0x01f1 PSN 0xef0b8e RKey 0x012fa6 VAddr 0x007f846f710000
GID: 00:00:00:00:00:00:00:00:00:00:255:255:13:13:13:06
------------------------------------------------------------------------------
#bytes     #iterations    BW peak[Gb/sec]    BW average[Gb/sec]   MsgRate[Mpps]
65536      223500           0.00               39.06     0.074493
------------------------------------------------------------------------------
```
### BCM网卡运行RoCE功能并测试 ###
#### 环境配置 ####
关闭SELINUX服务
编辑 `/etc/selinux/config`文件
修改 `SELINUX=disabled`

停止运行并关闭NetworkManager服务
`systemctl disable NetworkManager`
`systemctl stop NetworkManager`

停止运行并关闭防火墙
`systemctl stop firewalld`
`systemctl disable firewalld`

#### 修改NVM cfg ####
使用lcdiag工具，使能RDMA功能
修改为对应参数值 `nvm cfg 161=1,506=1`然后冷重启

#### 安装软件包 ####
`yum groupinstalll "Development Tools"`
`yum -y groupinstall "InfiniBand Support"`
`yum -y install libibverbs* infiniband-diags perftest qperf librdmacm-utils`
`yum install -y gcc make kernel-devel libguestfs-tools autoconf automake libtool httpd`

#### 安装驱动 ####
安装linux L2 and RoCE驱动，驱动位于Linux_Driver文件夹
```
# tar -xzf netxtreme-bnxt_en-bnxt_re.tar.gz
# cd netxtreme-bnxt_en-bnxt_re
# make build && make install
```
安装Linux RoCE User Library，驱动位于RoCE_lib文件夹
```
# tar -xzf libbnxtre-x.x.x.tar.gz
# cd libbnxtre-x.x.x
# ./configure
# make && make install
# cp bnxtre.driver /etc/libibverbs.d/
# echo "/usr/local/lib >> /etc/ld.so.conf"
# ldconfig -V
```
重新加载驱动模块
rmmod bnxt_en
rmmod bnxt_re
modprobe bnxt_en
modprobe bnxt_re

#### 检查配置 ####
查看bnxt_re模块是否被正确安装，可以使用`lsmod | grep ib`命令
![](index_files/lsmod.PNG)
检查rdma_cm,rdma_ucm,ib_core,ib_uverbs都已被正确安装
如果和图中结果不同，可以尝试"modprobe rdma_cm"和"modprobe rdma_ucm"
接下来可以使用`ibv_devices`和`ibv_devinfo`来查看ib设备信息

### RDMA功能验证与性能测试 ###
#### 驱动安装与环境准备 ####
** 对于RedHat系统 **
安装RDMA驱动以及测试工具
`yum -y groupinstall "InfiniBand Support`
`yum -y install perftest infiniband-diags`

确保RDMA在启动时使能(CentOS7)
`dracut --add-drivers "mlx4_en mlx4_ib mlx5_ib" -f `
`service rdma restart`
`systemctl enable rdma`

确保RDMA在启动时使能(CentOS6)
`service rdma restartl;chkconfig rdma on`

** 对于Ubuntu系统 **
安装RDMA驱动以及测试工具
`apt-get install libmlx4-1 infiniband-diags ibutils ibverbs-utils rdmacm-utils perftest`
安装tgt支持
`apt-get install tgt`
安装LIO target支持
`apt-get install targetcli`
安装iSCSI客户端
`apt-get install open-iscsi-utils open-iscsi`

#### 配置网口参数 ####
配置IP地址并使能网口
`# ifconfig eth2 12.12.12.1/24 up`
`# ifconfig eth2 12.12.12.2/24 up`
确保Server端IP地址与Client端在同一网段

#### 确认InfiniBand Kernel模块被加载 ####
![](index_files/Mellanox_20Infiniband_u6A21_u5757.png)
Mellanox ConnectX-3/ConnectX-3 Pro网卡使用mlx4_core,mlx4_en,mlx4_ib模块
ib_iser模块被用于iSCSI initialor，当ib_isert被LIO iSCSI target。TGT，工作在用户空间不需要其他内核模块。
不需要所有模块都被加载，依据使用方式加载相应的模块即可。如，链路层协议如果为以太网则无需加载mlx4_ib，链路层协议为Infiniband则无需加载mlx4_en。

#### 配置无损网络 ####
如果RDMA协议运行于以太网例如RoCE，需要确保网络被配置成为无损以太网，可以通过在交换机以及网口配置flow control或者PFC。
对于实验环境的RDMA测试，在每个接口使能Global Pause Flow Control就可以满足使用。而对于生产环境,PFC为首选模式。
PFC配置方式参考前文，以下介绍Global Pause Flow Control方式。
使用`ethtool -a`命令查看FC是否开启
```
    # ethtool -a eth2
    Pause parameters for eth2:
    Autonegotiate:  off
    RX:             on
    TX:             on
```
使用`ethtool -A eth2 rx on tx on`使能FC。
确保在交换机的对应端口也启用了Global Pause Flow Control
```
[H3C]interface Ten-GigabitEthernet 1/0/1
[H3C-Ten-GigabitEthernet1/0/1]flow-control receive enable
```
#### RDMA测试 ####
在开始测试之前，请先检查一下几点
1. 检查相关网口为UP状态
2. 使用ping命令，确保L3 IP的连通性
3. 确保网络被配置为无损，通过FC或PFC
4. 确保两段使用相同的RoCE版本
5. 确认防火墙已被关闭. 它的运行可能会导致HOST防火墙阻塞TCP/IP链接

** udaddy测试 **
使用udaddy脚本可以进行RDMA_CM UD连接，它通过librdmacm在两个节点间建立不可靠RDMA数据报通路，在两个节点之间传输数据报然后关闭链接。
在Server端运行
`# uaddy`
在Client端运行
```
# udaddy -s 12.12.12.1
udaddy: starting client
udaddy: connecting
initiating data transfers
receiving data transfers
data transfers complete
test complete
return status 0
```
`return status 0`代表着正常退出，RDMA运行正常。

** rdma_server,rdma_client命令 **
使用rdma_server和rdma_client命令可以建立RDMA CM链接并运行ping-pong测试，它同步调用librdmam在两个节点之间建立RDMA链接。
在Server端运行
`# rdma_server`
在Client端运行
```
# rdma_client -s 12.12.12.1
rdma_client: start
rdma_client: end 0
```
`rdma_client: end 0`表示正常退出，RDMA正常运行。

** ib_send_bw/ib_send_lat(performance test) **
测试RDMA发送处理确定带宽或等待时延
-i, --ib-port=<port> Use port
`# ib_send_bw -d mlx4_0 -i 1 -F --report_gbits`
```
# ib_send_bw -d mlx4_0 -i 1 -F --report_gbits 12.12.12.1
------------------------------------------------------------------------------
                    Send BW Test
Dual-port       : OFF          Device         : mlx4_0
Number of qps   : 1            Transport type : IB
Connection type : RC
RX depth        : 512
CQ Moderation   : 100
Mtu             : 1024[B]
Link type       : Ethernet
Gid index       : 0
Max inline data : 0[B]
rdma_cm QPs     : OFF
Data ex. method : Ethernet
------------------------------------------------------------------------------
local address: LID 0000 QPN 0x0065 PSN 0xc8f367
GID: 254:128:00:00:00:00:00:00:246:82:20:255:254:23:27:129
remote address: LID 0000 QPN 0x005d PSN 0x884d7d
GID: 254:128:00:00:00:00:00:00:246:82:20:255:254:23:31:225
------------------------------------------------------------------------------
#bytes     #iterations    BW peak[Gb/sec]    BW average[Gb/sec]   MsgRate[Mpps]
65536      1000           0.00               36.40                0.069428
------------------------------------------------------------------------------
```
按照同样配置分别使用如下工具测试
ib_write_bw:测试 RDMA 写处理，确定一次显示一个 I/O 请求的带宽
ib_write_lat:测试 RDMA 写处理确定等待时间
ib_read_bw:测试 RDMA 读处理确定带宽
ib_read_lat:测试 RDMA 读处理等待时间

** rping **
此脚本覆盖了RDMA_CM UD链接（它使用librdmacm在两个节点之间建立一组不可靠的RDMA数据报通信路径，可选地在第一个节点之间传输数据报。）
```
在Service端运行
# rping -s  -C 10 -v

在Client端运行
    rping  -c -a 12.12.12.1  -C 10 -v
    ping data: rdma-ping-0: ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqr
    ping data: rdma-ping-1: BCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrs
    ping data: rdma-ping-2: CDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrst
    ping data: rdma-ping-3: DEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstu
    ping data: rdma-ping-4: EFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuv
    ping data: rdma-ping-5: FGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvw
    ping data: rdma-ping-6: GHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwx
    ping data: rdma-ping-7: HIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxy
    ping data: rdma-ping-8: IJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz
    ping data: rdma-ping-9: JKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyzA
    client DISCONNECT EVENT...>
```