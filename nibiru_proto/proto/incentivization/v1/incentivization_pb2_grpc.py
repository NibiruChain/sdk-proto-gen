# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from incentivization.v1 import incentivization_pb2 as incentivization_dot_v1_dot_incentivization__pb2


class MsgStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateIncentivizationProgram = channel.unary_unary(
                '/nibiru.incentivization.v1.Msg/CreateIncentivizationProgram',
                request_serializer=incentivization_dot_v1_dot_incentivization__pb2.MsgCreateIncentivizationProgram.SerializeToString,
                response_deserializer=incentivization_dot_v1_dot_incentivization__pb2.MsgCreateIncentivizationProgramResponse.FromString,
                )
        self.FundIncentivizationProgram = channel.unary_unary(
                '/nibiru.incentivization.v1.Msg/FundIncentivizationProgram',
                request_serializer=incentivization_dot_v1_dot_incentivization__pb2.MsgFundIncentivizationProgram.SerializeToString,
                response_deserializer=incentivization_dot_v1_dot_incentivization__pb2.MsgFundIncentivizationProgramResponse.FromString,
                )


class MsgServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateIncentivizationProgram(self, request, context):
        """CreateIncentivizationProgram allows an entity to create an incentivization program for a liquidity pool.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FundIncentivizationProgram(self, request, context):
        """FundIncentivizationProgram allows an entity to fund an already existing incentivization program with more coins.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateIncentivizationProgram': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateIncentivizationProgram,
                    request_deserializer=incentivization_dot_v1_dot_incentivization__pb2.MsgCreateIncentivizationProgram.FromString,
                    response_serializer=incentivization_dot_v1_dot_incentivization__pb2.MsgCreateIncentivizationProgramResponse.SerializeToString,
            ),
            'FundIncentivizationProgram': grpc.unary_unary_rpc_method_handler(
                    servicer.FundIncentivizationProgram,
                    request_deserializer=incentivization_dot_v1_dot_incentivization__pb2.MsgFundIncentivizationProgram.FromString,
                    response_serializer=incentivization_dot_v1_dot_incentivization__pb2.MsgFundIncentivizationProgramResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nibiru.incentivization.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateIncentivizationProgram(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.incentivization.v1.Msg/CreateIncentivizationProgram',
            incentivization_dot_v1_dot_incentivization__pb2.MsgCreateIncentivizationProgram.SerializeToString,
            incentivization_dot_v1_dot_incentivization__pb2.MsgCreateIncentivizationProgramResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FundIncentivizationProgram(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.incentivization.v1.Msg/FundIncentivizationProgram',
            incentivization_dot_v1_dot_incentivization__pb2.MsgFundIncentivizationProgram.SerializeToString,
            incentivization_dot_v1_dot_incentivization__pb2.MsgFundIncentivizationProgramResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class QueryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.IncentivizationProgram = channel.unary_unary(
                '/nibiru.incentivization.v1.Query/IncentivizationProgram',
                request_serializer=incentivization_dot_v1_dot_incentivization__pb2.QueryIncentivizationProgramRequest.SerializeToString,
                response_deserializer=incentivization_dot_v1_dot_incentivization__pb2.QueryIncentivizationProgramResponse.FromString,
                )
        self.IncentivizationPrograms = channel.unary_unary(
                '/nibiru.incentivization.v1.Query/IncentivizationPrograms',
                request_serializer=incentivization_dot_v1_dot_incentivization__pb2.QueryIncentivizationProgramsRequest.SerializeToString,
                response_deserializer=incentivization_dot_v1_dot_incentivization__pb2.QueryIncentivizationProgramsResponse.FromString,
                )


class QueryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def IncentivizationProgram(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IncentivizationPrograms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'IncentivizationProgram': grpc.unary_unary_rpc_method_handler(
                    servicer.IncentivizationProgram,
                    request_deserializer=incentivization_dot_v1_dot_incentivization__pb2.QueryIncentivizationProgramRequest.FromString,
                    response_serializer=incentivization_dot_v1_dot_incentivization__pb2.QueryIncentivizationProgramResponse.SerializeToString,
            ),
            'IncentivizationPrograms': grpc.unary_unary_rpc_method_handler(
                    servicer.IncentivizationPrograms,
                    request_deserializer=incentivization_dot_v1_dot_incentivization__pb2.QueryIncentivizationProgramsRequest.FromString,
                    response_serializer=incentivization_dot_v1_dot_incentivization__pb2.QueryIncentivizationProgramsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nibiru.incentivization.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def IncentivizationProgram(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.incentivization.v1.Query/IncentivizationProgram',
            incentivization_dot_v1_dot_incentivization__pb2.QueryIncentivizationProgramRequest.SerializeToString,
            incentivization_dot_v1_dot_incentivization__pb2.QueryIncentivizationProgramResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IncentivizationPrograms(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nibiru.incentivization.v1.Query/IncentivizationPrograms',
            incentivization_dot_v1_dot_incentivization__pb2.QueryIncentivizationProgramsRequest.SerializeToString,
            incentivization_dot_v1_dot_incentivization__pb2.QueryIncentivizationProgramsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
