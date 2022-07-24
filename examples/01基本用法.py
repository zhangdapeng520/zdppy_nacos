# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  01基本用法.py
@Time    :  2022/7/24 8:25
@Author  :  张大鹏
@Version :  v0.1.0
@Contact :  lxgzhw@163.com
@License :  (C)Copyright 2022-2023
@Desc    :  描述
"""
import zdppy_nacos

SERVER_ADDRESSES = "127.0.0.1:8848"
NAMESPACE = "283df317-fa59-46db-9cac-838970599ef4"  # 这里是namespace的id！！

# no auth mode
# client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE)
# auth mode
client = zdppy_nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE, username="nacos", password="nacos")

# get config
data_id = "user_service.json"
group = "dev"
print(type(client.get_config(data_id, group)))  # 返回的是字符串
import json

json_data = json.loads(client.get_config(data_id, group))
print(json_data)


def test_cb(args):
    print("配置文件产生变化")
    print(args)


if __name__ == '__main__':
    client.add_config_watcher(data_id, group, test_cb)
    import time

    time.sleep(3000)
