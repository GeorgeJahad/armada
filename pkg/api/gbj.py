from __future__ import print_function

import logging

import grpc
import submit_pb2
import submit_pb2_grpc
import sys

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = submit_pb2_grpc.SubmitStub(channel)
        response = stub.CreateQueue(submit_pb2.Queue(name='gbj13', priority_factor=2))
#        response2 = stub.CancelJobs(submit_pb2.JobCancelRequest(queue="queue-a", job_set_id ="job-set-1", job_id = "jj"))
        response2 = stub.CancelJobs(submit_pb2.JobCancelRequest(queue="queue-a", job_set_id ="job-set-1", job_id = sys.argv[1]))
    print("gbj client received: " + str(len(response2.cancelled_ids)))
    if len(response2.cancelled_ids) > 0:
        print("gbj cancelled id: " + str(response2.cancelled_ids[0]))


if __name__ == '__main__':
    logging.basicConfig()
    run()
