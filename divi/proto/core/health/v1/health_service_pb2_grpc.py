# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from divi.proto.core.health.v1 import health_service_pb2 as divi_dot_proto_dot_core_dot_health_dot_v1_dot_health__service__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in divi/proto/core/health/v1/health_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class HealthServiceStub(object):
    """HealthService is a service that implements health check.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Check = channel.unary_unary(
                '/divi.proto.core.health.v1.HealthService/Check',
                request_serializer=divi_dot_proto_dot_core_dot_health_dot_v1_dot_health__service__pb2.HealthCheckRequest.SerializeToString,
                response_deserializer=divi_dot_proto_dot_core_dot_health_dot_v1_dot_health__service__pb2.HealthCheckResponse.FromString,
                _registered_method=True)


class HealthServiceServicer(object):
    """HealthService is a service that implements health check.
    """

    def Check(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HealthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Check': grpc.unary_unary_rpc_method_handler(
                    servicer.Check,
                    request_deserializer=divi_dot_proto_dot_core_dot_health_dot_v1_dot_health__service__pb2.HealthCheckRequest.FromString,
                    response_serializer=divi_dot_proto_dot_core_dot_health_dot_v1_dot_health__service__pb2.HealthCheckResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'divi.proto.core.health.v1.HealthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('divi.proto.core.health.v1.HealthService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class HealthService(object):
    """HealthService is a service that implements health check.
    """

    @staticmethod
    def Check(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/divi.proto.core.health.v1.HealthService/Check',
            divi_dot_proto_dot_core_dot_health_dot_v1_dot_health__service__pb2.HealthCheckRequest.SerializeToString,
            divi_dot_proto_dot_core_dot_health_dot_v1_dot_health__service__pb2.HealthCheckResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
