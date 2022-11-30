"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ConfigRequest(google.protobuf.message.Message):
    """ConfigRequest defines the request structure for the Config gRPC query."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ConfigRequest = ConfigRequest

class ConfigResponse(google.protobuf.message.Message):
    """ConfigResponse defines the response structure for the Config gRPC query."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MINIMUM_GAS_PRICE_FIELD_NUMBER: builtins.int
    minimum_gas_price: builtins.str
    def __init__(
        self,
        *,
        minimum_gas_price: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["minimum_gas_price", b"minimum_gas_price"]) -> None: ...

global___ConfigResponse = ConfigResponse
