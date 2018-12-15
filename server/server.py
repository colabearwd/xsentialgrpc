from concurrent import futures

import time
import grpc
import socket
import remote_pb2_grpc  as remote_service
import remote_types_pb2 as remote_messages

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def get_ping_args():
    '''
        wait here to get args,and return 
    '''
    pass

def put_pingres_mysql():
    '''
        put pingres into mysql
    '''
    pass

def get_curl_args():
    '''
        wait here to get args,and return 
    '''
    pass

def put_curlres_mysql():
    '''
        put curlres into mysql
    '''
    pass

class RemoteService(remote_service.RemoteServicer):

    def AddCurl(self, request, context):
        metadata = dict(context.invocation_metadata())
        # print metadata & request
        print(metadata)
        print(request.requestnum)

        # wait here to get args
        args = get_curl_args()

        # put the args to Curl-Obj 
        curltemp=remote_messages.Curl()
        curltemp.targeturl="www.163.com"
        curltemp.ipversion="ipv4"
        curltemp.timeout=10
        curltemp.serialnum=request.requestnum
        
        return remote_messages.AddCurlResult(curl = curltemp)

    def CurlRes(self, request, context):
        metadata = dict(context.invocation_metadata())
        # print metadata & request
        print(metadata)
        print(request.curlres)
        
        # put the results into mysql
        status = put_curlres_mysql()

        # return the results
        return remote_messages.CurlResResult(results =456)

    def AddPing(self, request, context):
        metadata = dict(context.invocation_metadata())
        # print metadata & request
        print(metadata)
        print(request.requestnum)

        # wait here to get args
        args = get_ping_args()

        # put the args to Ping-Obj 
        pingtemp=remote_messages.Ping()
        pingtemp.targeturl="www.163.com"
        pingtemp.ipversion="ipv4"
        pingtemp.timeout=10
        pingtemp.packagesize=64
        pingtemp.count=5
        pingtemp.serialnum=request.requestnum
        
        return remote_messages.AddPingResult(ping = pingtemp)

    def PingRes(self, request, context):
        metadata = dict(context.invocation_metadata())
        # print metadata & request
        print(metadata)
        print(request.pingres)
        
        # put the results into mysql
        status = put_pingres_mysql()

        # return the results
        return remote_messages.PingResResult(results =456)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    remote_service.add_RemoteServicer_to_server(RemoteService(),server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()

