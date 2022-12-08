"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Since: cosmos-sdk 0.43"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class PubKey(google.protobuf.message.Message):
    """PubKey defines a secp256r1 ECDSA public key."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    key: builtins.bytes
    """Point on secp256r1 curve in a compressed representation as specified in section
    4.3.6 of ANSI X9.62: https://webstore.ansi.org/standards/ascx9/ansix9621998
    """
    def __init__(
        self,
        *,
        key: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key"]) -> None: ...

global___PubKey = PubKey

@typing_extensions.final
class PrivKey(google.protobuf.message.Message):
    """PrivKey defines a secp256r1 ECDSA private key."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SECRET_FIELD_NUMBER: builtins.int
    secret: builtins.bytes
    """secret number serialized using big-endian encoding"""
    def __init__(
        self,
        *,
        secret: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["secret", b"secret"]) -> None: ...

global___PrivKey = PrivKey
