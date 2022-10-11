"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import cosmos.distribution.v1beta1.tx_pb2
import grpc

class MsgStub:
    """Msg defines the distribution Msg service."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    SetWithdrawAddress: grpc.UnaryUnaryMultiCallable[
        cosmos.distribution.v1beta1.tx_pb2.MsgSetWithdrawAddress,
        cosmos.distribution.v1beta1.tx_pb2.MsgSetWithdrawAddressResponse,
    ]
    """SetWithdrawAddress defines a method to change the withdraw address
    for a delegator (or validator self-delegation).
    """
    WithdrawDelegatorReward: grpc.UnaryUnaryMultiCallable[
        cosmos.distribution.v1beta1.tx_pb2.MsgWithdrawDelegatorReward,
        cosmos.distribution.v1beta1.tx_pb2.MsgWithdrawDelegatorRewardResponse,
    ]
    """WithdrawDelegatorReward defines a method to withdraw rewards of delegator
    from a single validator.
    """
    WithdrawValidatorCommission: grpc.UnaryUnaryMultiCallable[
        cosmos.distribution.v1beta1.tx_pb2.MsgWithdrawValidatorCommission,
        cosmos.distribution.v1beta1.tx_pb2.MsgWithdrawValidatorCommissionResponse,
    ]
    """WithdrawValidatorCommission defines a method to withdraw the
    full commission to the validator address.
    """
    FundCommunityPool: grpc.UnaryUnaryMultiCallable[
        cosmos.distribution.v1beta1.tx_pb2.MsgFundCommunityPool,
        cosmos.distribution.v1beta1.tx_pb2.MsgFundCommunityPoolResponse,
    ]
    """FundCommunityPool defines a method to allow an account to directly
    fund the community pool.
    """

class MsgServicer(metaclass=abc.ABCMeta):
    """Msg defines the distribution Msg service."""

    @abc.abstractmethod
    def SetWithdrawAddress(
        self,
        request: cosmos.distribution.v1beta1.tx_pb2.MsgSetWithdrawAddress,
        context: grpc.ServicerContext,
    ) -> cosmos.distribution.v1beta1.tx_pb2.MsgSetWithdrawAddressResponse:
        """SetWithdrawAddress defines a method to change the withdraw address
        for a delegator (or validator self-delegation).
        """
    @abc.abstractmethod
    def WithdrawDelegatorReward(
        self,
        request: cosmos.distribution.v1beta1.tx_pb2.MsgWithdrawDelegatorReward,
        context: grpc.ServicerContext,
    ) -> cosmos.distribution.v1beta1.tx_pb2.MsgWithdrawDelegatorRewardResponse:
        """WithdrawDelegatorReward defines a method to withdraw rewards of delegator
        from a single validator.
        """
    @abc.abstractmethod
    def WithdrawValidatorCommission(
        self,
        request: cosmos.distribution.v1beta1.tx_pb2.MsgWithdrawValidatorCommission,
        context: grpc.ServicerContext,
    ) -> cosmos.distribution.v1beta1.tx_pb2.MsgWithdrawValidatorCommissionResponse:
        """WithdrawValidatorCommission defines a method to withdraw the
        full commission to the validator address.
        """
    @abc.abstractmethod
    def FundCommunityPool(
        self,
        request: cosmos.distribution.v1beta1.tx_pb2.MsgFundCommunityPool,
        context: grpc.ServicerContext,
    ) -> cosmos.distribution.v1beta1.tx_pb2.MsgFundCommunityPoolResponse:
        """FundCommunityPool defines a method to allow an account to directly
        fund the community pool.
        """

def add_MsgServicer_to_server(servicer: MsgServicer, server: grpc.Server) -> None: ...
