"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import common.common_pb2
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Direction:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DirectionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Direction.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DIRECTION_UNSPECIFIED: _Direction.ValueType  # 0
    ADD_TO_POOL: _Direction.ValueType  # 1
    REMOVE_FROM_POOL: _Direction.ValueType  # 2

class Direction(_Direction, metaclass=_DirectionEnumTypeWrapper): ...

DIRECTION_UNSPECIFIED: Direction.ValueType  # 0
ADD_TO_POOL: Direction.ValueType  # 1
REMOVE_FROM_POOL: Direction.ValueType  # 2
global___Direction = Direction

class _TwapCalcOption:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _TwapCalcOptionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TwapCalcOption.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    TWAP_CALC_OPTION_UNSPECIFIED: _TwapCalcOption.ValueType  # 0
    SPOT: _TwapCalcOption.ValueType  # 1
    """Spot price from quote asset reserve / base asset reserve"""
    QUOTE_ASSET_SWAP: _TwapCalcOption.ValueType  # 2
    """Swapping with quote assets, output denominated in base assets"""
    BASE_ASSET_SWAP: _TwapCalcOption.ValueType  # 3
    """Swapping with base assets, output denominated in quote assets"""

class TwapCalcOption(_TwapCalcOption, metaclass=_TwapCalcOptionEnumTypeWrapper):
    """Enumerates different options of calculating twap."""

TWAP_CALC_OPTION_UNSPECIFIED: TwapCalcOption.ValueType  # 0
SPOT: TwapCalcOption.ValueType  # 1
"""Spot price from quote asset reserve / base asset reserve"""
QUOTE_ASSET_SWAP: TwapCalcOption.ValueType  # 2
"""Swapping with quote assets, output denominated in base assets"""
BASE_ASSET_SWAP: TwapCalcOption.ValueType  # 3
"""Swapping with base assets, output denominated in quote assets"""
global___TwapCalcOption = TwapCalcOption

class Vpool(google.protobuf.message.Message):
    """A virtual pool used only for price discovery of perpetual futures contracts.
    No real liquidity exists in this pool.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAIR_FIELD_NUMBER: builtins.int
    BASE_ASSET_RESERVE_FIELD_NUMBER: builtins.int
    QUOTE_ASSET_RESERVE_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    @property
    def pair(self) -> common.common_pb2.AssetPair:
        """always BASE:QUOTE, e.g. BTC:NUSD or ETH:NUSD"""
    base_asset_reserve: builtins.str
    """base asset is the crypto asset, e.g. BTC or ETH"""
    quote_asset_reserve: builtins.str
    """quote asset is usually stablecoin, in our case NUSD"""
    @property
    def config(self) -> global___VpoolConfig: ...
    def __init__(
        self,
        *,
        pair: common.common_pb2.AssetPair | None = ...,
        base_asset_reserve: builtins.str = ...,
        quote_asset_reserve: builtins.str = ...,
        config: global___VpoolConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config", b"config", "pair", b"pair"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_asset_reserve", b"base_asset_reserve", "config", b"config", "pair", b"pair", "quote_asset_reserve", b"quote_asset_reserve"]) -> None: ...

global___Vpool = Vpool

class VpoolConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRADE_LIMIT_RATIO_FIELD_NUMBER: builtins.int
    FLUCTUATION_LIMIT_RATIO_FIELD_NUMBER: builtins.int
    MAX_ORACLE_SPREAD_RATIO_FIELD_NUMBER: builtins.int
    MAINTENANCE_MARGIN_RATIO_FIELD_NUMBER: builtins.int
    MAX_LEVERAGE_FIELD_NUMBER: builtins.int
    trade_limit_ratio: builtins.str
    """ratio applied to reserves in order not to over trade"""
    fluctuation_limit_ratio: builtins.str
    """percentage that a single open or close position can alter the reserve amounts"""
    max_oracle_spread_ratio: builtins.str
    """max_oracle_spread_ratio"""
    maintenance_margin_ratio: builtins.str
    """maintenance_margin_ratio"""
    max_leverage: builtins.str
    """max_leverage"""
    def __init__(
        self,
        *,
        trade_limit_ratio: builtins.str = ...,
        fluctuation_limit_ratio: builtins.str = ...,
        max_oracle_spread_ratio: builtins.str = ...,
        maintenance_margin_ratio: builtins.str = ...,
        max_leverage: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fluctuation_limit_ratio", b"fluctuation_limit_ratio", "maintenance_margin_ratio", b"maintenance_margin_ratio", "max_leverage", b"max_leverage", "max_oracle_spread_ratio", b"max_oracle_spread_ratio", "trade_limit_ratio", b"trade_limit_ratio"]) -> None: ...

global___VpoolConfig = VpoolConfig

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

class ReserveSnapshot(google.protobuf.message.Message):
    """a snapshot of the vpool's reserves at a given point in time"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAIR_FIELD_NUMBER: builtins.int
    BASE_ASSET_RESERVE_FIELD_NUMBER: builtins.int
    QUOTE_ASSET_RESERVE_FIELD_NUMBER: builtins.int
    TIMESTAMP_MS_FIELD_NUMBER: builtins.int
    @property
    def pair(self) -> common.common_pb2.AssetPair: ...
    base_asset_reserve: builtins.str
    quote_asset_reserve: builtins.str
    """quote asset is usually the margin asset, e.g. NUSD"""
    timestamp_ms: builtins.int
    """milliseconds since unix epoch"""
    def __init__(
        self,
        *,
        pair: common.common_pb2.AssetPair | None = ...,
        base_asset_reserve: builtins.str = ...,
        quote_asset_reserve: builtins.str = ...,
        timestamp_ms: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pair", b"pair"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_asset_reserve", b"base_asset_reserve", "pair", b"pair", "quote_asset_reserve", b"quote_asset_reserve", "timestamp_ms", b"timestamp_ms"]) -> None: ...

global___ReserveSnapshot = ReserveSnapshot

class PoolPrices(google.protobuf.message.Message):
    """PoolPrices is a simple structure that displays a snapshot of the mark and index
    prices for an asset. Empty strings for the indexPrice or twapMark fields 
    indicate that the price is currently unavailable.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAIR_FIELD_NUMBER: builtins.int
    MARK_PRICE_FIELD_NUMBER: builtins.int
    INDEX_PRICE_FIELD_NUMBER: builtins.int
    TWAP_MARK_FIELD_NUMBER: builtins.int
    SWAP_INVARIANT_FIELD_NUMBER: builtins.int
    BLOCK_NUMBER_FIELD_NUMBER: builtins.int
    pair: builtins.str
    """Pair identifier for the two assets. Always in format 'base:quote'"""
    mark_price: builtins.str
    """MarkPrice is the instantaneous price of the perp. 
    Equivalent to quoteAssetReserve / baseAssetReserve.
    """
    index_price: builtins.str
    """IndexPrice is the price of the "underlying" for the perp"""
    twap_mark: builtins.str
    """TwapMark is the time-weighted average (mark) price."""
    swap_invariant: builtins.str
    """SwapInvariant is the product of the reserves, commonly referred to as "k"."""
    block_number: builtins.int
    """The block number corresponding to each price"""
    def __init__(
        self,
        *,
        pair: builtins.str = ...,
        mark_price: builtins.str = ...,
        index_price: builtins.str = ...,
        twap_mark: builtins.str = ...,
        swap_invariant: builtins.str = ...,
        block_number: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_number", b"block_number", "index_price", b"index_price", "mark_price", b"mark_price", "pair", b"pair", "swap_invariant", b"swap_invariant", "twap_mark", b"twap_mark"]) -> None: ...

global___PoolPrices = PoolPrices
