"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.auth.v1beta1.auth_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the auth module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    ACCOUNTS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> cosmos.auth.v1beta1.auth_pb2.Params:
        """params defines all the paramaters of the module."""
    @property
    def accounts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]:
        """accounts are the accounts present at genesis."""
    def __init__(
        self,
        *,
        params: cosmos.auth.v1beta1.auth_pb2.Params | None = ...,
        accounts: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["accounts", b"accounts", "params", b"params"]) -> None: ...

global___GenesisState = GenesisState
