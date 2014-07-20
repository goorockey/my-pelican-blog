Title: Node.js高并发配置
Author: goorockey
Date: 2014-07-20 16:00
Tags: programming, nodejs, high concurrency
Category: programming
Slug: high-concurrency-setting-for-nodejs
Summary:

[TOC]


node.js的异步模型让它很擅长实现IO密集型的系统，但是测试发现，当并发真的上到几W的时候，会有处理不过来的情况。除了从整个系统的设计上改进，还需要修改一些配置。这里总结一下为了让node.js应对高并发，需要做的配置。

###linux系统配置

修改/etc/sysctl.conf，情况文件内默认的内容，写入以下项，保存后执行`sudo sysctl -p`使配置生效。注意里面的数值要根据具体情况修改。这些修改当然也适用于除node.js以为的应用。

- `net.ipv4.ip_local_port_range` 可用端口范围，从第一个值到第二个值。默认的"1024 4999"很容易不够。

- `net.ipv4.tcp_tw_reuse` 是否让系统在安全情况下重用TIME_WAIT状态的连接。在高并发情况下，有大量的连接建立和关闭，TIME_WAIT的连接是快要关闭、但资源还没有回收的，像内存、端口都会占用着。

- `net.ipv4.tcp_max_tw_buckets` 维持TIME_WAIT状态最多连接数。当超过这个值时，连接就会立刻关闭，并报错，dmesg可以看到。

- `net.ipv4.tcp_fin_timeout` TIME_WAIT状态的连接回收时的等待时长。

- `net.ipv4.tcp_syncookies` 

- `net.ipv4.tcp_max_syn_backlog` 最多记录接受到多少SYN。

- `net.ipv4.tcp_rmem` tcp读缓存空间，三个值分别是最小、默认和最大。

- `net.ipv4.tcp_wmem` tcp写缓存空间，三个值分别是最小、默认和最大。

- `net.core.somaxconn` 最大连接数

修改/etc/security/limits.conf，提高文件句柄上限:

    soft nofile 65536
    hard nofile 65536


###node.js

- socket池

nodejs的http模块内置socket池，默认[最多建立5个socket](http://nodejs.org/api/http.html#http_agent_maxsockets)

    require('http').globalAgent.maxSockets = 40000 # 也可以设成Infinity，无限制
    require('https').globalAgent.maxSockets = 40000

- `-–nouse-idle-notification`



- cluster

###参考资料

- <http://www.oschina.net/translate/optimising-nginx-node-js-and-networking-for-heavy-workloads>

- <http://blog.caustik.com/2012/04/08/scaling-node-js-to-100k-concurrent-connections/>

- <http://engineering.linkedin.com/nodejs/blazing-fast-nodejs-10-performance-tips-linkedin-mobile>

- <https://rtcamp.com/tutorials/linux/sysctl-conf/>
