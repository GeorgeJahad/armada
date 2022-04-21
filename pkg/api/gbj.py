from __future__ import print_function
import logging
import grpc
import event_pb2
import event_pb2_grpc
import sys
from pprint import pprint

startMessage = "0"
if len(sys.argv) > 1:
    startMessage = sys.argv[1]
    
def run():
    print("Now checking queue-a, job-set-1")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = event_pb2_grpc.EventStub(channel)
        response = stub.GetJobSetEvents(
            event_pb2.JobSetRequest(
                queue="queue-a",
                from_message_id = startMessage,
                watch=True,
                id ="job-set-1",
                errorIfMissing=True))
        for resp in response:
           print("client received: " + resp.id + " " + resp.message.WhichOneof("events"))

run()
