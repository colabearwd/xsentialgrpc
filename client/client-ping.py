import sys
import grpc
import remote_pb2_grpc  as remote_service
import remote_types_pb2 as remote_messages

def do_script_getpingresult():
    pass

def run():
    channel = grpc.insecure_channel('127.0.0.1:50051')
    try:
        grpc.channel_ready_future(channel).result(timeout=10)
    except grpc.FutureTimeoutError:
        sys.exit('Error connecting to server')
    else:
        stub = remote_service.RemoteStub(channel)

        metadata = [('ip', '127.0.0.1'),('endpoint','test-point'),('server-name','addping')]
        requestnum=123
        response = stub.AddPing(

            remote_messages.AddPingRequest(requestnum=requestnum),

            metadata=metadata,
        )

	if response:

	    print("Get Message From Server======1:",response)
        # print(response.ping.serialnum)

        # do script to get results
        results = do_script_getpingresult()

        pingrestemp=remote_messages.PingRes()
        pingrestemp.lossrate=50
        pingrestemp.maxtime=60
        pingrestemp.averagetime=70
        pingrestemp.serialnum=response.ping.serialnum


        metadata = [('ip', '127.0.0.1'),('endpoint','test-point'),('server-name','pingres')]
                
        response = stub.PingRes(

            remote_messages.PingResRequest(pingres=pingrestemp),

            metadata=metadata,
        )
        if response:
            print("Get Message From Server======2:",response.results)
        

#	use curl args to run a script

#	get the results ,rpc another function to return the results

#	get the status




if __name__ == '__main__':
    	run()
