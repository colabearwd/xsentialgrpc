import sys
import grpc
import remote_pb2_grpc  as remote_service
import remote_types_pb2 as remote_messages

def do_script_getcurlresult():
    pass

def run():
    channel = grpc.insecure_channel('127.0.0.1:50051')
    try:
        grpc.channel_ready_future(channel).result(timeout=10)
    except grpc.FutureTimeoutError:
        sys.exit('Error connecting to server')
    else:
        stub = remote_service.RemoteStub(channel)

        metadata = [('ip', '127.0.0.1'),('endpoint','test-point'),('server-name','addcurl')]
        requestnum=123
        response = stub.AddCurl(

            remote_messages.AddCurlRequest(requestnum=requestnum),

            metadata=metadata,
        )

	if response:

	    print("Get Message From Server======1:",response)

        # do script to get results
        results = do_script_getcurlresult()

        curlrestemp=remote_messages.CurlRes()
        curlrestemp.curlhttpcode = "200"
        curlrestemp.curlhttpconnect = "300"
        curlrestemp.curltimenameloopup = "400"
        curlrestemp.curltimeredirect = "500"
        curlrestemp.curltimepretransfer = "600"
        curlrestemp.curltimeconnect = "700"
        curlrestemp.curltimestarttransfer = "800"
        curlrestemp.curltimetotal = "900"
        curlrestemp.curlspeeddownload = "1000"
        curlrestemp.serialnum = response.curl.serialnum


        metadata = [('ip', '127.0.0.1'),('endpoint','test-point'),('server-name','curlres')]
                
        response = stub.CurlRes(

            remote_messages.CurlResRequest(curlres=curlrestemp),

            metadata=metadata,
        )
        if response:
            print("Get Message From Server======2:",response.results)
        

#	use curl args to run a script

#	get the results ,rpc another function to return the results

#	get the status




if __name__ == '__main__':
    	run()
