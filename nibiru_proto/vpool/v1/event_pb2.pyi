"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ReserveSnapshotSavedEvent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAIR_FIELD_NUMBER: builtins.int
    QUOTE_RESERVE_FIELD_NUMBER: builtins.int
    BASE_RESERVE_FIELD_NUMBER: builtins.int
    pair: typing.Text
    quote_reserve: typing.Text
    base_reserve: typing.Text
    def __init__(self,
        *,
        pair: typing.Text = ...,
        quote_reserve: typing.Text = ...,
        base_reserve: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_reserve",b"base_reserve","pair",b"pair","quote_reserve",b"quote_reserve"]) -> None: ...
global___ReserveSnapshotSavedEvent = ReserveSnapshotSavedEvent

class SwapQuoteForBaseEvent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAIR_FIELD_NUMBER: builtins.int
    QUOTE_AMOUNT_FIELD_NUMBER: builtins.int
    BASE_AMOUNT_FIELD_NUMBER: builtins.int
    pair: typing.Text
    quote_amount: typing.Text
    base_amount: typing.Text
    def __init__(self,
        *,
        pair: typing.Text = ...,
        quote_amount: typing.Text = ...,
        base_amount: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_amount",b"base_amount","pair",b"pair","quote_amount",b"quote_amount"]) -> None: ...
global___SwapQuoteForBaseEvent = SwapQuoteForBaseEvent

class SwapBaseForQuoteEvent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAIR_FIELD_NUMBER: builtins.int
    QUOTE_AMOUNT_FIELD_NUMBER: builtins.int
    BASE_AMOUNT_FIELD_NUMBER: builtins.int
    pair: typing.Text
    quote_amount: typing.Text
    base_amount: typing.Text
    def __init__(self,
        *,
        pair: typing.Text = ...,
        quote_amount: typing.Text = ...,
        base_amount: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_amount",b"base_amount","pair",b"pair","quote_amount",b"quote_amount"]) -> None: ...
global___SwapBaseForQuoteEvent = SwapBaseForQuoteEvent

class MarkPriceChanged(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAIR_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    pair: typing.Text
    price: typing.Text
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        pair: typing.Text = ...,
        price: typing.Text = ...,
        timestamp: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp",b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pair",b"pair","price",b"price","timestamp",b"timestamp"]) -> None: ...
global___MarkPriceChanged = MarkPriceChanged
