[TOC]
## 1. 什么是multipath 
　　当主机总线到存储设备之间有多条路径可以选择，使用multipath软件可以实现在多路多路径的负载均衡（如RR模式）以及故障的切换和恢复。RHEL与SLES系统自带有MULTIPATH包可以支持大多是厂商的存储设备。
>IBM的RDAC、Qlogic的failover驱动仅仅提供了failover功能，不支持load Balance的功能，但Multipath根据选择的策略不同可以支持多种方式：failover、Multipath等

## 2. RHEL下multipath的组成 
    rpm -qa|grep device
    device-mapper 
    device-mapper-multipath
    device-mapper-event

### 2.1 device-mapper-multipath
　　提供了multipathd和multipath工具，以及multipath.conf等配置文件。这些工具通过device mapper的ioctr接口创建和配置multipath设备（调用device-mapper的用户空间库。在/dev/mapper中生成多路径设备）
### 2.2 device-mapper 
　　device-mapper包括：内核与用户部分。
　　内核部分multipath核心（multipath.ko）和target driver（dm-multipath.ko）构成。dm-mod.ko是实现multipath的基础，dm-multipath就是一个dm的target驱动，核心完成设备映射，而target根据映射关系和自身特点具体处理从mapperd device下来的i/o。在核心部分提供了一个接口，用户可以使用ioctr和内核部分通信，指导内核驱动创建mappered device，以及device的属性等。
　　用户空间包括device-mapper这个包，其中包括dmsetup工具和一些帮助创建与配置mapper device的库，这些库主要封装了与ioctr通信的接口，方便创建与配置mappered device，dm-mapper-multipath会调用这些库。
###   2.3 scsi_id
　　包含在udev程序包中，可以在multipath.conf中配置该程序来获取scsi设备的序号，通过序号可以判断多个路径对应了同一设备。scsi_id是通过sg驱动，向设备发送EVPD page80或page83 的inquery命令来查询scsi设备的标识。但一些设备并不支持EVPD 的inquery命令，所以他们无法被用来生成multipath设备。但可以改写scsi_id，为不能提供scsi设备标识的设备虚拟一个标识符，并输出到标准输出。
　　multipath程序在创建multipath设备时，会调用scsi_id，从其标准输出中获得该设备的scsi id。在改写时，需要修改scsi_id程序的返回值为0。因为在multipath程序中，会检查该直来确定scsi id是否已经成功得到。

## 3 配置multipath
multipath的配置文件只有一个`/etc/multipath.conf`。在配置之前先使用`fdisk -l`确认已经可以识别所有lun，HDS支持多链路负载均衡，所以每条链路都是正常的；而如果是EMC CX300这样仅支持负载均衡的设备，则冗余链路会出现I/O Error的错误。
>执行`mpathconf –enable` 在/etc下生成配置文件

### 3.1 编辑黑名单
默认配置下，multipath会把所有设备加入到黑名单中(devnode " * ")也就是禁止使用，所以应当先取消该设置，将配置文件修改如下。
```
devnode_blacklist{
#devnode "*"
devnode "hda"
wwid 3600508e000000000dc7200032e08af0b
}
```
这里是指禁用hda，也就是光驱，另外还限制使用本地的sda设备，这是sda的wwid。可以使用`#scsi_id -g -u -s /block/sda`获得。
### 3.2 编辑默认规则
不同device-mapper-multipath或操作系统发行版，其默认规则都有点不同，以RedHat x86_64为例，其path_grouping_policy默认为failover，就是主备模式。
```
defaults{
udev_dir /dev
path_grouping_policy multibus
failback immediate
no_path_retry fail
user_friendly_name yes
}
```
### 3.3 multipath 高级配置
如果不想使用默认配置，可以按照自己定义的方法配置multipath
配置文件共包括3部分：blacklist，multipaths，devices
#### 3.3.1 blacklist配置
```
devnode_blacklist{
#devnode "*"
devnode "hda"
wwid 3600508e000000000dc7200032e08af0b
}
```
#### 3.3.2 multipath部分配置
```
multipaths{
multipath{
wwwid ************* #可以使用multipath -v3查看*
alias iscsi-dm0     #映射后的别名
path_grouping_policy multibus #路径组策略
path_checker tur #决定路径状态的方法
path_selector "round-robin 0" #选择哪条路径进行下一个IO操作的方法
}
}
```

#### 3.3.2 Devices部分配置
```
devices{
device{
vendor "iSCSI-Enterprise" #厂商名称
product "Virtual disk" #产品型号
path_grouping_policy multibus #默认路径组策略
getuid_callout "/sbin/acs_prio_alua %d" #获取有限级数值使用的默认程序
path_checker readsector0 #决定路径状态的方法
path_selector "round-robin 0" #选择路径进行下一个IO操作
failback immediate #故障恢复模式
no_path_retry queue #在disable queue之前系统尝试使用失败路径次数的数值
rr_min_io 100 #在当前的用户组中，在切换到另一条路径之前的IO请求数目
}
}
```
>wwid，vendor，product， getuid_callout这些参数可以通过：multipath -v3命令来获取。如果在/etc/multipath.conf中有设定各wwid 别名,别名会覆盖此设定。

|Attribute|Description|
|------|----|
|**wwid**|Specifies the WWID of the multipath device to which the **multipath** attributes apply. This parameter is mandatory for this section of the**multipath.conf** file.|
|**alias**|Specifies the symbolic name for the multipath device to which the**multipath** attributes apply. If you are using **user_friendly_names**, do not set this value to**mpath_n_**; this may conflict with an automatically assigned user friendly name and give you incorrect device node names.|
|**path_grouping_policy**|Specifies the default path grouping policy to apply to unspecified multipaths. Possible values include: <br/>**failover** = 1 path per priority group<br/>** multibus** = all valid paths in 1 priority group<br/>**group_by_serial** = 1 priority group per detected serial number<br/>**group_by_prio** = 1 priority group per path priority value<br/>**group_by_node_name** = 1 priority group per target node name|
|**path_selector**|Specifies the default algorithm to use in determining what path to use for the next I/O operation. Possible values include:<br/>**round-robin 0**: Loop through every path in the path group, sending the same amount of I/O to each.<br/>**queue-length 0**: Send the next bunch of I/O down the path with the least number of outstanding I/O requests.<br/>**service-time 0**: Send the next bunch of I/O down the path with the shortest estimated service time, which is determined by dividing the total size of the outstanding I/O to each path by its relative throughput.|
|**failback**|Manages path group failback.<br />A value of **immediate** specifies immediate failback to the highest priority path group that contains active paths.<br />A value of **manual** specifies that there should not be immediate failback but that failback can happen only with operator intervention.<br />A value of **followover** specifies that automatic failback should be performed when the first path of a path group becomes active. This keeps a node from automatically failing back when another node requested the failover.<br />A numeric value greater than zero specifies deferred failback, expressed in seconds.|
|**prio**| Specifies the default function to call to obtain a path priority value. For example, the ALUA bits in SPC-3 provide an exploitable**prio** value. Possible values include:<br />**const**: Set a priority of 1 to all paths.<br />**emc**: Generate the path priority for EMC arrays.<br />**alua**: Generate the path priority based on the SCSI-3 ALUA settings.<br />**tpg_pref**: Generate the path priority based on the SCSI-3 ALUA settings, using thepreferred port bit.<br />**ontap**: Generate the path priority for NetApp arrays.<br />**rdac**: Generate the path priority for LSI/Engenio RDAC controller.<br />**hp_sw**: Generate the path priority for Compaq/HP controller in active/standby mode.<br />**hds**: Generate the path priority for Hitachi HDS Modular storage arrays.<br />|
|**no_path_retry**|A numeric value for this attribute specifies the number of times the system should attempt to use a failed path before disabling queueing.<br />A value of **fail** indicates immediate failure, without queueing.<br />A value of **queue** indicates that queueing should not stop until the path is fixed.|
|**rr_min_io**|Specifies the number of I/O requests to route to a path before switching to the next path in the current path group. This setting is only for systems running kernels older that 2.6.31\. Newer systems should use**rr_min_io_rq**. The default value is 1000.|
|**rr_min_io_rq**|Specifies the number of I/O requests to route to a path before switching to the next path in the current path group, using request-based device-mapper-multipath. This setting should be used on systems running current kernels. On systems running kernels older than 2.6.31, use **rr_min_io**. The default value is 1.|
|**rr_weight**|If set to **priorities**, then instead of sending **rr_min_io** requests to a path before calling **path_selector** to choose the next path, the number of requests to send is determined by**rr_min_io** times the path's priority, as determined by the **prio** function. If set to **uniform**, all path weights are equal.|
|**flush_on_last_del**|If set to **yes**, then multipath will disable queueing when the last path to a device has been deleted.|



### rel7.1 multipath 示例文件 ###
>　　文件位置`/usr/share/doc/device-mapper-multipath-0.4.9/multipath.conf`

### 附录：Linux不重启添加硬盘
使用`rescan-scsi-bus.sh`命令，若无则使用yum安装`sg3_utils-1.28-4.el6.x86_64.rpm`包。
```
echo "---">/sys/class/scsi_host/host0/scan
rescan-scsi-bus.sh
```
第二种方法
```
echo 1 > /sys/class/fc_host/host_[num]/issue.lib
```