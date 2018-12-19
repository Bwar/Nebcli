#!/usr/bin/env python3
# nebcli.py
import json
import requests
import click


class Nebcli(object):
    """
    Nebula cluster administrator command line interface.
    """
    def __init__(self, url):
        self.url = url
        self.show_sub_cmd = (
            "ip_white", "subscription", "nodes", "node_report", "node_detail")

    def exec_cmd(self, req_json):
        response = requests.post(self.url, data=req_json)
        return response.text

    def show(self, param=[]):
        req_json = ""
        if param[0] in self.show_sub_cmd:
            param_num = len(param)
            if param_num == 1:
                if param[0] == "node_report" or param[0] == "node_detail":
                    click.echo("invalid param num for \"show %s\"", param[0])
                else:
                    req_json = (
                        """
                        {
                            "cmd":"show",
                            "args":["%s"]
                        }
                        """ % param[0]
                    )
                    result_string = self.exec_cmd(req_json)
                    result = json.loads(result_string)
                    if param[0] == "ip_white":
                        for ip in result["data"]:
                            click.echo("%s" % ip)
                    elif param[0] == "subscription":
                        for node_type in result["data"]:
                            click.echo("%s:" % node_type["node_type"])
                            for sub_node_type in node_type["subcriber"]:
                                click.echo("\t%s" % sub_node_type)
                    elif param[0] == "nodes":
                        for nodes in result["data"]:
                            click.echo("%s:" % nodes["node_type"])
                            for node in nodes["node"]:
                                click.echo("\t%s" % node)
                    else:
                        click.echo("%s" % result_string)
            elif param_num == 2:
                if param[0] == "ip_white":
                    click.echo("invalid param num for \"show %s\"", param[0])
                else:
                    req_json = (
                        """
                        {
                            "cmd":"show",
                            "args":["%s", "%s"]
                        }
                        """ % tuple(param)
                    )
                    result_string = self.exec_cmd(req_json)
                    result = json.loads(result_string)
                    if param[0] == "subscription":
                        for node_type in result["data"]:
                            click.echo("%s" % node_type)
                    elif param[0] == "nodes":
                        for node in result["data"]:
                            click.echo("%s" % node)
                    elif param[0] == "node_report":
                        if len(result["data"]) > 0:
                            click.echo("node_ip\tnode_port\tload\tconnect\t"
                                       "recv_num\trecv_byte\tsend_num\t"
                                       "send_byte\tclient")
                        for node in result["data"]:
                            click.echo("%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d"
                                       % (node["node_ip"],
                                          node["node_port"],
                                          node["node"]["load"],
                                          node["node"]["connect"],
                                          node["node"]["recv_num"],
                                          node["node"]["recv_byte"],
                                          node["node"]["send_num"],
                                          node["node"]["send_byte"],
                                          node["node"]["client"]))
                    elif param[0] == "node_detail":
                        if len(result["data"]) > 0:
                            click.echo("node_id\tnode_ip\tnode_port\t"
                                       "worker_num\tactive_time")
                        for node in result["data"]:
                            click.echo("%d\t%s\t%d\t%d\t%f"
                                       % (node["node_id"],
                                          node["node_ip"],
                                          node["node_port"],
                                          node["worker_num"],
                                          node["active_time"]))
                    else:
                        click.echo("%s" % result_string)
            elif param_num == 3:
                if param[0] == "node_report" or param[0] == "node_detail":
                    req_json = (
                        """
                        {
                            "cmd":"show",
                            "args":["%s", "%s", "%s"]
                        }
                        """ % tuple(param)
                    )
                    result_string = self.exec_cmd(req_json)
                    result = json.loads(result_string)
                    if param[0] == "node_report":
                        if len(result["data"]) > 0:
                            click.echo("worker\tload\tconnect\t"
                                       "recv_num\trecv_byte\tsend_num\t"
                                       "send_byte\tclient")
                        for node in result["data"]:
                            click.echo("%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d"
                                       % ("node",
                                          node["node"]["load"],
                                          node["node"]["connect"],
                                          node["node"]["recv_num"],
                                          node["node"]["recv_byte"],
                                          node["node"]["send_num"],
                                          node["node"]["send_byte"],
                                          node["node"]["client"]))
                            worker_no = 1
                            for worker in node["worker"]:
                                click.echo("%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d"
                                           % (worker_no,
                                              worker["load"],
                                              worker["connect"],
                                              worker["recv_num"],
                                              worker["recv_byte"],
                                              worker["send_num"],
                                              worker["send_byte"],
                                              worker["client"]))
                                worker_no += 1
                    elif param[0] == "node_detail":
                        if len(result["data"]) > 0:
                            click.echo("node_id\tnode_ip\tnode_port\t"
                                       "worker_num\tactive_time")
                        for node in result["data"]:
                            click.echo("%d\t%s\t%d\t%d\t%f"
                                       % (node["node_id"],
                                          node["node_ip"],
                                          node["node_port"],
                                          node["worker_num"],
                                          node["active_time"]))
                    else:
                        click.echo("%s" % result_string)
                else:
                    click.echo("invalid param num for \"show %s\"", param[0])
            else:
                click.echo("invalid param num for \"show\"")
        else:
            click.echo("invalid param: %s" % param[0])


@click.group(invoke_without_command=True)
@click.option('--url', '-r', prompt="url",
              help='The url of Beacon server admin.')
@click.pass_context
def cli(ctx, url):
    ctx.obj = Nebcli(url)
    if ctx.invoked_subcommand is None:
        while True:
            input_word = click.prompt("nebcli)")
            invoked_cmd = input_word.split(' ')
            if len(invoked_cmd) == 0:
                continue
            if invoked_cmd[0] == "quit" or invoked_cmd[0] == "exit":
                exit(0)
            elif invoked_cmd[0] == "show":
                ctx.command.show(invoked_cmd[1:])
            else:
                click.echo("invalid cmd \"%s\"!" % invoked_cmd[0])
    else:
        pass


@cli.command()
@click.argument("target")
@click.argument("args", nargs=-1)
@click.pass_context
def show(ctx, target, args):
    param = []
    param.append(target)
    param.extend(args)
    ctx.obj.show(param)

if __name__ == '__main__':
    cli()

