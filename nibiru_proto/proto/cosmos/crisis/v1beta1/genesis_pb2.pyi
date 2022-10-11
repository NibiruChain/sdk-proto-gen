"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the crisis module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONSTANT_FEE_FIELD_NUMBER: builtins.int
    @property
    def constant_fee(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """constant_fee is the fee used to verify the invariant in the crisis
        module.
        """
    def __init__(
        self,
        *,
        constant_fee: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["constant_fee", b"constant_fee"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["constant_fee", b"constant_fee"]) -> None: ...

global___GenesisState = GenesisState
