"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import perp.v1.state_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class QueryParamsRequest(google.protobuf.message.Message):
    """---------------------------------------- Params

    QueryParamsRequest is request type for the Query/Params RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryParamsRequest = QueryParamsRequest

class QueryParamsResponse(google.protobuf.message.Message):
    """QueryParamsResponse is response type for the Query/Params RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> perp.v1.state_pb2.Params:
        """params holds all the parameters of this module."""
    def __init__(
        self,
        *,
        params: perp.v1.state_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["params", b"params"]) -> None: ...

global___QueryParamsResponse = QueryParamsResponse

class QueryPositionsRequest(google.protobuf.message.Message):
    """---------------------------------------- Positions"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRADER_FIELD_NUMBER: builtins.int
    trader: builtins.str
    def __init__(
        self,
        *,
        trader: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["trader", b"trader"]) -> None: ...

global___QueryPositionsRequest = QueryPositionsRequest

class QueryPositionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITIONS_FIELD_NUMBER: builtins.int
    @property
    def positions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___QueryPositionResponse]: ...
    def __init__(
        self,
        *,
        positions: collections.abc.Iterable[global___QueryPositionResponse] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["positions", b"positions"]) -> None: ...

global___QueryPositionsResponse = QueryPositionsResponse

class QueryPositionRequest(google.protobuf.message.Message):
    """---------------------------------------- Position

    QueryPositionRequest is the request type for the position of the x/perp
    module account.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_PAIR_FIELD_NUMBER: builtins.int
    TRADER_FIELD_NUMBER: builtins.int
    token_pair: builtins.str
    trader: builtins.str
    def __init__(
        self,
        *,
        token_pair: builtins.str = ...,
        trader: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["token_pair", b"token_pair", "trader", b"trader"]) -> None: ...

global___QueryPositionRequest = QueryPositionRequest

class QueryPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_FIELD_NUMBER: builtins.int
    POSITION_NOTIONAL_FIELD_NUMBER: builtins.int
    UNREALIZED_PNL_FIELD_NUMBER: builtins.int
    MARGIN_RATIO_MARK_FIELD_NUMBER: builtins.int
    MARGIN_RATIO_INDEX_FIELD_NUMBER: builtins.int
    BLOCK_NUMBER_FIELD_NUMBER: builtins.int
    @property
    def position(self) -> perp.v1.state_pb2.Position:
        """The position as it exists in the blockchain state"""
    position_notional: builtins.str
    """The position's current notional value, if it were to be entirely closed (in
    margin units).
    """
    unrealized_pnl: builtins.str
    """The position's unrealized PnL."""
    margin_ratio_mark: builtins.str
    """margin ratio of the position based on the mark price, mark TWAP. The higher
    value of the possible margin ratios (TWAP and instantaneous) is taken to be
    'marginRatioMark'. Calculated from margin, unrealized PnL, and position
    notional.
    """
    margin_ratio_index: builtins.str
    """margin ratio of the position based on the index price. Calculated from
    margin, unrealized PnL, and position notional.
    """
    block_number: builtins.int
    """BlockNumber is current block number at the time of query."""
    def __init__(
        self,
        *,
        position: perp.v1.state_pb2.Position | None = ...,
        position_notional: builtins.str = ...,
        unrealized_pnl: builtins.str = ...,
        margin_ratio_mark: builtins.str = ...,
        margin_ratio_index: builtins.str = ...,
        block_number: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["position", b"position"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_number", b"block_number", "margin_ratio_index", b"margin_ratio_index", "margin_ratio_mark", b"margin_ratio_mark", "position", b"position", "position_notional", b"position_notional", "unrealized_pnl", b"unrealized_pnl"]) -> None: ...

global___QueryPositionResponse = QueryPositionResponse

class QueryFundingRatesRequest(google.protobuf.message.Message):
    """---------------------------------------- FundingPayments"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAIR_FIELD_NUMBER: builtins.int
    pair: builtins.str
    """the pair to query for"""
    def __init__(
        self,
        *,
        pair: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pair", b"pair"]) -> None: ...

global___QueryFundingRatesRequest = QueryFundingRatesRequest

class QueryFundingRatesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CUMULATIVE_FUNDING_RATES_FIELD_NUMBER: builtins.int
    @property
    def cumulative_funding_rates(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """a historical list of cumulative funding rates, with the most recent one
        last
        """
    def __init__(
        self,
        *,
        cumulative_funding_rates: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cumulative_funding_rates", b"cumulative_funding_rates"]) -> None: ...

global___QueryFundingRatesResponse = QueryFundingRatesResponse

class QueryMetricsRequest(google.protobuf.message.Message):
    """---------------------------------------- Metrics"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAIR_FIELD_NUMBER: builtins.int
    pair: builtins.str
    """the pair to query for"""
    def __init__(
        self,
        *,
        pair: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pair", b"pair"]) -> None: ...

global___QueryMetricsRequest = QueryMetricsRequest

class QueryMetricsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METRICS_FIELD_NUMBER: builtins.int
    @property
    def metrics(self) -> perp.v1.state_pb2.Metrics:
        """list of perp metrics"""
    def __init__(
        self,
        *,
        metrics: perp.v1.state_pb2.Metrics | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metrics", b"metrics"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["metrics", b"metrics"]) -> None: ...

global___QueryMetricsResponse = QueryMetricsResponse
