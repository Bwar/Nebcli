English | [中文](/README_cn.md)

# Nebcli
The NebulaBootstrap cluster management command line interface. nebcli created with [click](https://github.com/pallets/click).

## Deploy
The __nebcli.py__ is compatible with python2 and python3. If you execute the script directly, you need to install the click and requests modules first.
Here is a setup.py auto-install script that can be used to install nebcli as a system command by executing the following command:

```bash
pip install --editable .
```

now, you are able to execute the command nebcli:

```bash
nebcli --help
```

## Usage
nebcli.py and nebcli are work in the same way.
example for non-interactive:

```bash
nebcli --url http://192.168.157.175:16088/admin show nodes
```

example for interactively (similar to mysql command line interaction):
```bash
nebcli --url http://192.168.157.175:16088/admin
```

instructions:
```bash
show ip_white                                   # Show the IP whitelist of the cluster.
show subscription                               # Show node type subscription information.
show subscription ${node_type}                  # Show subscription information for a specified node type.
show nodes                                      # Show online node information.
show nodes ${node_type}                         # Show online node information of the specified node type.
show node_report ${node_type}                   # Show the working status of nodes of the specified type (load, amount of data sent and received, etc.)
show node_report ${node_type} ${node_identify}  # Show the specified node type to specify the node working status.
show node_detail ${node_type}                   # Show node information details (IP address, number of worker processes, etc.) of the specified type.
show node_detail ${node_type} ${node_identify}  # Show details of the specified node of the specified type.
show beacon                                     # Show beacon nodes.
```

## Related Project
   * [Nebula](https://github.com/Bwar/Nebula)
   * [NebulaBootstrap](https://github.com/Bwar/NebulaBootstrap)

