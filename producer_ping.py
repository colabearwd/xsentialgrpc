#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep, time
import sys
import grpc

from app.grpc_push.push_pb2 import SubmitRequest
from app.grpc_push.push_pb2_grpc import MessageSyncStub
import config


def run(a, b, c, d, e, f,g):
    NODE = a

    IPVERSION = b

    SERIALNUM = c

    TARGETURL = d
    PACKAGESIZE = e
    TIMEOUT = f
    COUNT = g

    MESSAGE = "ipversion:{0};serialnum:{1};targeturl:{2};packagesize:{3};timeout:{4};count:{5}".format(IPVERSION,
                                                                                                        SERIALNUM,
                                                                                                        TARGETURL,
                                                                                                        PACKAGESIZE,
                                                                                                        TIMEOUT,
                                                                                                        COUNT
    )

    addr = "localhost:{}".format(config.server_config['port'])

    conn = grpc.insecure_channel(addr)
    client = MessageSyncStub(channel=conn)
#    for i in range(1, 10000000):
    client.SubmitMessage(SubmitRequest(channel=NODE, message=MESSAGE ))
#        sleep(0.1)



