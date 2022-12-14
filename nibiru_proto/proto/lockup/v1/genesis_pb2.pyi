"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import lockup.v1.lock_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the lockup module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCKS_FIELD_NUMBER: builtins.int
    @property
    def locks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[lockup.v1.lock_pb2.Lock]: ...
    def __init__(
        self,
        *,
        locks: collections.abc.Iterable[lockup.v1.lock_pb2.Lock] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locks", b"locks"]) -> None: ...

global___GenesisState = GenesisState
