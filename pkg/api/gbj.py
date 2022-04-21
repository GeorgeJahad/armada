from __future__ import print_function

import logging

import grpc
import submit_pb2
import submit_pb2_grpc
import event_pb2
import event_pb2_grpc
import sys
from pprint import pprint

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
#        submitStub = submit_pb2_grpc.SubmitStub(channel)
#        response2 = stub.CancelJobs(submit_pb2.JobCancelRequest(queue="queue-a", job_set_id ="job-set-1", job_id = "jj"))
#        response2 = stub.CancelJobs(submit_pb2.JobCancelRequest(queue="queue-a", job_set_id ="job-set-1", job_id = sys.argv[1]))
#        response = stub.CreateQueue(submit_pb2.Queue(name='gbj13', priority_factor=2))
        stub = event_pb2_grpc.EventStub(channel)
        response2 = stub.GetJobSetEvents(event_pb2.JobSetRequest(queue="queue-a", from_message_id = sys.argv[1], watch=True, id ="job-set-1", errorIfMissing=True))
        for resp in response2:
           print("gbj client received: " + resp.id + " " + resp.message.WhichOneof("events"))
           print("gbjresp:")
#            pprint(dir(resp))


if __name__ == '__main__':
    logging.basicConfig()
    run()
