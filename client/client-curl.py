import sys
import grpc
import remote_pb2_grpc  as remote_service
import remote_types_pb2 as remote_messages
import commands
import re

def do_script_getcurlresult(curl):
    print(curl)
    print(curl.ipversion)
    timeouttemp = str(curl.timeout)
    cmd = "curl -"+ curl.ipversion +" -o /dev/null --connect-timeout "+ timeouttemp +" -s -w %{http_code}:%{http_connect}:%{time_namelookup}:%{time_redirect}:%{time_pretransfer}:%{time_connect}:%{time_starttransfer}:%{time_total}:%{speed_download} "+curl.targeturl
    print(cmd)

    status, output = commands.getstatusoutput(cmd)

    res = output.split(":")

    print(res)
    return res
    

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
        results = do_script_getcurlresult(response.curl)

        curlrestemp=remote_messages.CurlRes()
        curlrestemp.curlhttpcode = results[0]
        curlrestemp.curlhttpconnect = results[1]
        curlrestemp.curltimenameloopup = results[2]
        curlrestemp.curltimeredirect = results[3]
        curlrestemp.curltimepretransfer = results[4]
        curlrestemp.curltimeconnect = results[5]
        curlrestemp.curltimestarttransfer = results[6]
        curlrestemp.curltimetotal = results[7]
        curlrestemp.curlspeeddownload = results[8]
        curlrestemp.serialnum = response.curl.serialnum


        metadata = [('ip', '127.0.0.1'),('endpoint','test-point'),('server-name','curlres')]
                
        response = stub.CurlRes(

            remote_messages.CurlResRequest(curlres=curlrestemp),

            metadata=metadata,
        )
        if response:
            print("Get Message From Server======2:",response.results)
        

if __name__ == '__main__':
    	run()
