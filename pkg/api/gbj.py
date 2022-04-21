from __future__ import print_function
import logging
import grpc
import event_pb2
import event_pb2_grpc
import sys
from pprint import pprint

startMessage = "0"
queueParameter="queue-a"
idParameter ="job-set-1"

# add more events like so:
#  armadactl submit ./docs/quickstart/job-queue-a.yaml

if len(sys.argv) > 1:
    startMessage = sys.argv[1]
    
def run():
    print("Now checking " + queueParameter + " , " + idParameter)
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = event_pb2_grpc.EventStub(channel)
        response = stub.GetJobSetEvents(
            event_pb2.JobSetRequest(
                queue=queueParameter,
                from_message_id = startMessage,
                watch=True,
                id=idParameter,
                errorIfMissing=True))
        for resp in response:
           print("client received: " + resp.id + " " + resp.message.WhichOneof("events"))

run()
