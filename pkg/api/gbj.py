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
    
print("Checking " + queueParameter + " , " + idParameter)

channel = grpc.insecure_channel('localhost:50051')

stub = event_pb2_grpc.EventStub(channel)

req = event_pb2.JobSetRequest(
    queue = queueParameter,
    from_message_id = startMessage,
    watch = True,
    id = idParameter,
    errorIfMissing = True)

response = stub.GetJobSetEvents(req)

for resp in response:
   print("client received: " + resp.id + " " + resp.message.WhichOneof("events"))

