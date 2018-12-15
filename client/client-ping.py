import sys
import grpc
import remote_pb2_grpc  as remote_service
import remote_types_pb2 as remote_messages
import commands
import re

def do_script_getpingresult(ping):
    # print(ping)
    # print(ping.targeturl)
    # print(ping.ipversion)
    # print(ping.timeout)
    # print(ping.packagesize)
    # print(ping.count)
    # print(ping.serialnum)
    pingversioncmd=""
    if ping.ipversion=='4':
        pingversioncmd="ping"
    else:
        pingversioncmd="ping6"
    
    cmd = "{0} -s {1} -c {2} -W {3} -q {4} ".format(pingversioncmd, ping.packagesize,ping.count, ping.timeout, ping.targeturl)
    print(cmd)

    status, output = commands.getstatusoutput(cmd)

    # print(status)
    # print(output)

    if (status == 512):
        print ping.targeturl+" <==== We dont know this host !!!"
        res = [-1, -1, -1]
        return res

    elif (status == 256):
        print ping.targeturl+" <==== We cant reach this host !!!"
        res = [-2, -2, -2]
        return res

    elif (status == 0):
        temp1 = re.search(r"received, \d+\.?\d{0,3}% packet loss", output)

        temp2 = re.search(
            r"\d+\.?\d{0,3}\/\d+\.?\d{0,3}\/\d+\.?\d{0,3}\/", output)


        t1 = re.findall(r"\d+\.?\d{0,3}", temp1.group())

        t2 = re.findall(r"\d+\.?\d{0,3}", temp2.group())

        res = []
        res.append(int(t1[0]))
        res.append(int(float(t2[2])))
        res.append(int(float(t2[1])))

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
        results = do_script_getpingresult(response.ping)

        pingrestemp=remote_messages.PingRes()
        pingrestemp.lossrate=results[0]
        pingrestemp.maxtime=results[1]
        pingrestemp.averagetime=results[2]
        pingrestemp.serialnum=response.ping.serialnum

        print("=====")
        print(pingrestemp)
        # print(pingrestemp.lossrate)

        metadata = [('ip', '127.0.0.1'),('endpoint','test-point'),('server-name','pingres')]
                
        response = stub.PingRes(

            remote_messages.PingResRequest(pingres=pingrestemp),

            metadata=metadata,
        )
        if response:
            print("Get Message From Server======2:",response.results)


if __name__ == '__main__':
    	run()
