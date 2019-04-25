README

* my_server.py

server use screen to execute


* producer_ping.py & producer_curl.py

temporarytask_bp.py use these python file to  produce new data to client 


* consumer_ping_final.py & consumer_curl_final.py

client use screen to execute

1.cp config.py.default config.py

2.modify config.py

3.use virtual env
client use py3
apt-get install python3-venv
python3 -m venv venv
source vnev/bin/active

4.pip install -r requirement 

5.python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./push.proto

