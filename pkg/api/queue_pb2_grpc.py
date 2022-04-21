# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from pkg.api import queue_pb2 as pkg_dot_api_dot_queue__pb2


class AggregatedQueueStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LeaseJobs = channel.unary_unary(
                '/api.AggregatedQueue/LeaseJobs',
                request_serializer=pkg_dot_api_dot_queue__pb2.LeaseRequest.SerializeToString,
                response_deserializer=pkg_dot_api_dot_queue__pb2.JobLease.FromString,
                )
        self.RenewLease = channel.unary_unary(
                '/api.AggregatedQueue/RenewLease',
                request_serializer=pkg_dot_api_dot_queue__pb2.RenewLeaseRequest.SerializeToString,
                response_deserializer=pkg_dot_api_dot_queue__pb2.IdList.FromString,
                )
        self.ReturnLease = channel.unary_unary(
                '/api.AggregatedQueue/ReturnLease',
                request_serializer=pkg_dot_api_dot_queue__pb2.ReturnLeaseRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ReportDone = channel.unary_unary(
                '/api.AggregatedQueue/ReportDone',
                request_serializer=pkg_dot_api_dot_queue__pb2.IdList.SerializeToString,
                response_deserializer=pkg_dot_api_dot_queue__pb2.IdList.FromString,
                )


class AggregatedQueueServicer(object):
    """Missing associated documentation comment in .proto file."""

    def LeaseJobs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RenewLease(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReturnLease(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReportDone(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AggregatedQueueServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LeaseJobs': grpc.unary_unary_rpc_method_handler(
                    servicer.LeaseJobs,
                    request_deserializer=pkg_dot_api_dot_queue__pb2.LeaseRequest.FromString,
                    response_serializer=pkg_dot_api_dot_queue__pb2.JobLease.SerializeToString,
            ),
            'RenewLease': grpc.unary_unary_rpc_method_handler(
                    servicer.RenewLease,
                    request_deserializer=pkg_dot_api_dot_queue__pb2.RenewLeaseRequest.FromString,
                    response_serializer=pkg_dot_api_dot_queue__pb2.IdList.SerializeToString,
            ),
            'ReturnLease': grpc.unary_unary_rpc_method_handler(
                    servicer.ReturnLease,
                    request_deserializer=pkg_dot_api_dot_queue__pb2.ReturnLeaseRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ReportDone': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportDone,
                    request_deserializer=pkg_dot_api_dot_queue__pb2.IdList.FromString,
                    response_serializer=pkg_dot_api_dot_queue__pb2.IdList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.AggregatedQueue', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AggregatedQueue(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def LeaseJobs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.AggregatedQueue/LeaseJobs',
            pkg_dot_api_dot_queue__pb2.LeaseRequest.SerializeToString,
            pkg_dot_api_dot_queue__pb2.JobLease.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RenewLease(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.AggregatedQueue/RenewLease',
            pkg_dot_api_dot_queue__pb2.RenewLeaseRequest.SerializeToString,
            pkg_dot_api_dot_queue__pb2.IdList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReturnLease(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.AggregatedQueue/ReturnLease',
            pkg_dot_api_dot_queue__pb2.ReturnLeaseRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReportDone(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.AggregatedQueue/ReportDone',
            pkg_dot_api_dot_queue__pb2.IdList.SerializeToString,
            pkg_dot_api_dot_queue__pb2.IdList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
