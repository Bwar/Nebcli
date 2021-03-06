[English](/README.md) | 中文

# Nebcli
NebulaBootstrap集群命令行管理工具。
nebcli是用python基于[click](https://github.com/pallets/click)编写的NebulaBootstrap集群命令行管理工具。

## 安装部署
nebcli核心仅一个脚本__nebcli.py__，脚本兼容python2和python3，如果直接执行脚本，需手动安装click和requests模块。
这里提供了一个setup.py自动安装脚本，执行以下这条命令即可将nebcli安装成为一个系统命令：

```bash
pip install --editable .
```

安装完毕即可执行命令nebcli查看效果：

```bash
nebcli --help
```

## 使用说明
直接执行nebcli.py和安装后执行命令nebcli的使用方法跟效果是完全一样的。
以非交互方式执行示例：

```bash
nebcli --url http://192.168.157.175:16088/admin show nodes
```

以交互方式执行(类似于输入mysql进入mysql命令行交互，可以执行多条命令直到输入quit退出)示例：
```bash
nebcli --url http://192.168.157.175:16088/admin
```

命令说明：
```bash
show ip_white                                   # 查看接入集群的IP白名单
show subscription                               # 查看节点类型订阅信息
show subscription ${node_type}                  # 查看指定节点类型的订阅信息
show nodes                                      # 查看在线节点信息
show nodes ${node_type}                         # 查看指定节点类型的在线节点信息
show node_report ${node_type}                   # 查看指定类型的节点工作状态（负载、收发数据量等）
show node_report ${node_type} ${node_identify}  # 查看指定节点类型指定节点工作状态
show node_detail ${node_type}                   # 查看指定类型的节点信息详情（IP地址、工作进程数等）
show node_detail ${node_type} ${node_identify}  # 查看指定类型指定节点的信息详情
show beacon                                     # 查看Beacon节点
get node_config ${node_identify}                # 获取指定节点的节点配置文件内容
get node_custom_config ${node_identify}         # 获取指定节点的节点配置文件中用户自定义部分内容

# 获取指定节点指定配置文件内容
get custom_config ${node_identify} ${config_file_relative_path} ${config_file_name}

# 设置属于某种类型的所有节点的节点配置文件
set node_config ${node_type} ${config_file_content}

# 设置某节点的节点配置文件
set node_config ${node_type} ${node_identify} ${config_file_content}

# 通过本地文件的内容设置属于某种类型的所有节点的节点配置文件
set node_config_from_file ${node_type} ${config_file}

# 通过本地文件的内容设置某节点的节点配置文件
set node_config_from_file ${node_type} ${node_identify} ${config_file}

set node_custom_config ${node_type} ${config_content}
set node_custom_config ${node_type} ${node_identify} ${config_content}
set node_custom_config_from_file ${node_type} ${config_file}
set node_custom_config_from_file ${node_type} ${node_identify} ${config_file}
set custom_config ${node_type} ${config_file_name} ${config_file_content}
set custom_config ${node_type} ${config_file_relative_path} ${config_file_name} ${config_file_content}
set custom_config ${node_type} ${node_identify} ${config_file_relative_path} ${config_file_name} ${config_file_content}
set custom_config_from_file ${node_type} ${config_file}
set custom_config_from_file ${node_type} ${config_file_relative_path} ${config_file}
set custom_config_from_file ${node_type} ${node_identify} ${config_file_relative_path} ${config_file}
```

## 相关项目
   * [Nebula](https://github.com/Bwar/Nebula)
   * [NebulaBootstrap](https://github.com/Bwar/NebulaBootstrap)


