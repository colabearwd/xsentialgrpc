#!/bin/bash

declare -a services=("remote")

# Python
# $ python -m pip install grcpio
# $ python -m pip install grpcio-tools

for SERVICE in "${services[@]}"; do
    DESTDIR='gen-py'
    mkdir -p $DESTDIR
    python -m grpc_tools.protoc \
        --proto_path=$SERVICE/ \
        --python_out=$DESTDIR \
        --grpc_python_out=$DESTDIR \
        $SERVICE/*.proto
done
