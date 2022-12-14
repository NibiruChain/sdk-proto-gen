"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import common.common_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Params(google.protobuf.message.Message):
    """Params defines the parameters for the x/pricefeed module."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAIRS_FIELD_NUMBER: builtins.int
    TWAP_LOOKBACK_WINDOW_FIELD_NUMBER: builtins.int
    @property
    def pairs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common.common_pb2.AssetPair]:
        """Pairs is the list of valid trading pairs for the module.
        Add new trading pairs
        """
    @property
    def twap_lookback_window(self) -> google.protobuf.duration_pb2.Duration:
        """amount of time to look back for TWAP calculations"""
    def __init__(
        self,
        *,
        pairs: collections.abc.Iterable[common.common_pb2.AssetPair] | None = ...,
        twap_lookback_window: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["twap_lookback_window", b"twap_lookback_window"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pairs", b"pairs", "twap_lookback_window", b"twap_lookback_window"]) -> None: ...

global___Params = Params

@typing_extensions.final
class PriceSnapshot(google.protobuf.message.Message):
    """a snapshot of the pricefeed oracle's median price at a given point in time"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAIR_ID_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    TIMESTAMP_MS_FIELD_NUMBER: builtins.int
    pair_id: builtins.str
    """the token pair"""
    price: builtins.str
    """the median prices of all oracles"""
    timestamp_ms: builtins.int
    """milliseconds since unix epoch"""
    def __init__(
        self,
        *,
        pair_id: builtins.str = ...,
        price: builtins.str = ...,
        timestamp_ms: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pair_id", b"pair_id", "price", b"price", "timestamp_ms", b"timestamp_ms"]) -> None: ...

global___PriceSnapshot = PriceSnapshot

@typing_extensions.final
class OraclesMarshaler(google.protobuf.message.Message):
    """OraclesMarshaler is a codec.ProtoMarshaler for an oracles array in the
    OraclesState sdk.KVStore.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORACLES_FIELD_NUMBER: builtins.int
    @property
    def oracles(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    def __init__(
        self,
        *,
        oracles: collections.abc.Iterable[builtins.bytes] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["oracles", b"oracles"]) -> None: ...

global___OraclesMarshaler = OraclesMarshaler

@typing_extensions.final
class ActivePairMarshaler(google.protobuf.message.Message):
    """ActivePairMarshaler is a codec.ProtoMarshaler for the "IsActive" status of
    a pair in the ActivePairState sdk.KVStore.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IS_ACTIVE_FIELD_NUMBER: builtins.int
    is_active: builtins.bool
    def __init__(
        self,
        *,
        is_active: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["is_active", b"is_active"]) -> None: ...

global___ActivePairMarshaler = ActivePairMarshaler

@typing_extensions.final
class PostedPrice(google.protobuf.message.Message):
    """PostedPrice defines a price for an asset pair posted by a specific oracle."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAIR_ID_FIELD_NUMBER: builtins.int
    ORACLE_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    EXPIRY_FIELD_NUMBER: builtins.int
    pair_id: builtins.str
    oracle: builtins.str
    price: builtins.str
    @property
    def expiry(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        pair_id: builtins.str = ...,
        oracle: builtins.str = ...,
        price: builtins.str = ...,
        expiry: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["expiry", b"expiry"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["expiry", b"expiry", "oracle", b"oracle", "pair_id", b"pair_id", "price", b"price"]) -> None: ...

global___PostedPrice = PostedPrice

@typing_extensions.final
class CurrentPrice(google.protobuf.message.Message):
    """CurrentPrice defines the current price for an asset pair in the pricefeed
    module.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAIR_ID_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    pair_id: builtins.str
    price: builtins.str
    def __init__(
        self,
        *,
        pair_id: builtins.str = ...,
        price: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pair_id", b"pair_id", "price", b"price"]) -> None: ...

global___CurrentPrice = CurrentPrice

@typing_extensions.final
class CurrentTWAP(google.protobuf.message.Message):
    """CurrentTWAP states defines the numerator and denominator for the TWAP calculation"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAIR_ID_FIELD_NUMBER: builtins.int
    NUMERATOR_FIELD_NUMBER: builtins.int
    DENOMINATOR_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    pair_id: builtins.str
    numerator: builtins.str
    denominator: builtins.str
    price: builtins.str
    def __init__(
        self,
        *,
        pair_id: builtins.str = ...,
        numerator: builtins.str = ...,
        denominator: builtins.str = ...,
        price: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["denominator", b"denominator", "numerator", b"numerator", "pair_id", b"pair_id", "price", b"price"]) -> None: ...

global___CurrentTWAP = CurrentTWAP
