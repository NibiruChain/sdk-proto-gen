"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
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

@typing_extensions.final
class MsgRemoveMargin(google.protobuf.message.Message):
    """-------------------------- RemoveMargin --------------------------

    MsgRemoveMargin: Msg to remove margin.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SENDER_FIELD_NUMBER: builtins.int
    TOKEN_PAIR_FIELD_NUMBER: builtins.int
    MARGIN_FIELD_NUMBER: builtins.int
    sender: builtins.str
    token_pair: builtins.str
    @property
    def margin(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(
        self,
        *,
        sender: builtins.str = ...,
        token_pair: builtins.str = ...,
        margin: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["margin", b"margin"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["margin", b"margin", "sender", b"sender", "token_pair", b"token_pair"]) -> None: ...

global___MsgRemoveMargin = MsgRemoveMargin

@typing_extensions.final
class MsgRemoveMarginResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MARGIN_OUT_FIELD_NUMBER: builtins.int
    FUNDING_PAYMENT_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    @property
    def margin_out(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """tokens transferred back to the trader"""
    funding_payment: builtins.str
    """the funding payment applied on this position interaction"""
    @property
    def position(self) -> perp.v1.state_pb2.Position:
        """The resulting position"""
    def __init__(
        self,
        *,
        margin_out: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
        funding_payment: builtins.str = ...,
        position: perp.v1.state_pb2.Position | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["margin_out", b"margin_out", "position", b"position"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["funding_payment", b"funding_payment", "margin_out", b"margin_out", "position", b"position"]) -> None: ...

global___MsgRemoveMarginResponse = MsgRemoveMarginResponse

@typing_extensions.final
class MsgAddMargin(google.protobuf.message.Message):
    """-------------------------- AddMargin --------------------------

    MsgAddMargin: Msg to remove margin.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SENDER_FIELD_NUMBER: builtins.int
    TOKEN_PAIR_FIELD_NUMBER: builtins.int
    MARGIN_FIELD_NUMBER: builtins.int
    sender: builtins.str
    token_pair: builtins.str
    @property
    def margin(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(
        self,
        *,
        sender: builtins.str = ...,
        token_pair: builtins.str = ...,
        margin: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["margin", b"margin"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["margin", b"margin", "sender", b"sender", "token_pair", b"token_pair"]) -> None: ...

global___MsgAddMargin = MsgAddMargin

@typing_extensions.final
class MsgAddMarginResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FUNDING_PAYMENT_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    funding_payment: builtins.str
    @property
    def position(self) -> perp.v1.state_pb2.Position: ...
    def __init__(
        self,
        *,
        funding_payment: builtins.str = ...,
        position: perp.v1.state_pb2.Position | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["position", b"position"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["funding_payment", b"funding_payment", "position", b"position"]) -> None: ...

global___MsgAddMarginResponse = MsgAddMarginResponse

@typing_extensions.final
class MsgLiquidate(google.protobuf.message.Message):
    """-------------------------- Liquidate --------------------------"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SENDER_FIELD_NUMBER: builtins.int
    TOKEN_PAIR_FIELD_NUMBER: builtins.int
    TRADER_FIELD_NUMBER: builtins.int
    sender: builtins.str
    """Sender is the liquidator address"""
    token_pair: builtins.str
    """TokenPair is the identifier for the position's virtual pool"""
    trader: builtins.str
    """Trader is the address of the owner of the position"""
    def __init__(
        self,
        *,
        sender: builtins.str = ...,
        token_pair: builtins.str = ...,
        trader: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["sender", b"sender", "token_pair", b"token_pair", "trader", b"trader"]) -> None: ...

global___MsgLiquidate = MsgLiquidate

@typing_extensions.final
class MsgLiquidateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEE_TO_LIQUIDATOR_FIELD_NUMBER: builtins.int
    FEE_TO_PERP_ECOSYSTEM_FUND_FIELD_NUMBER: builtins.int
    @property
    def fee_to_liquidator(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    @property
    def fee_to_perp_ecosystem_fund(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(
        self,
        *,
        fee_to_liquidator: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
        fee_to_perp_ecosystem_fund: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["fee_to_liquidator", b"fee_to_liquidator", "fee_to_perp_ecosystem_fund", b"fee_to_perp_ecosystem_fund"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["fee_to_liquidator", b"fee_to_liquidator", "fee_to_perp_ecosystem_fund", b"fee_to_perp_ecosystem_fund"]) -> None: ...

global___MsgLiquidateResponse = MsgLiquidateResponse

@typing_extensions.final
class MsgMultiLiquidate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class MultiLiquidation(google.protobuf.message.Message):
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

    SENDER_FIELD_NUMBER: builtins.int
    LIQUIDATIONS_FIELD_NUMBER: builtins.int
    sender: builtins.str
    @property
    def liquidations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MsgMultiLiquidate.MultiLiquidation]: ...
    def __init__(
        self,
        *,
        sender: builtins.str = ...,
        liquidations: collections.abc.Iterable[global___MsgMultiLiquidate.MultiLiquidation] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["liquidations", b"liquidations", "sender", b"sender"]) -> None: ...

global___MsgMultiLiquidate = MsgMultiLiquidate

@typing_extensions.final
class MsgMultiLiquidateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class MultiLiquidateResponse(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ERROR_FIELD_NUMBER: builtins.int
        LIQUIDATION_FIELD_NUMBER: builtins.int
        error: builtins.str
        @property
        def liquidation(self) -> global___MsgLiquidateResponse: ...
        def __init__(
            self,
            *,
            error: builtins.str = ...,
            liquidation: global___MsgLiquidateResponse | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["error", b"error", "liquidation", b"liquidation", "response", b"response"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["error", b"error", "liquidation", b"liquidation", "response", b"response"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["response", b"response"]) -> typing_extensions.Literal["error", "liquidation"] | None: ...

    LIQUIDATION_RESPONSES_FIELD_NUMBER: builtins.int
    @property
    def liquidation_responses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MsgMultiLiquidateResponse.MultiLiquidateResponse]: ...
    def __init__(
        self,
        *,
        liquidation_responses: collections.abc.Iterable[global___MsgMultiLiquidateResponse.MultiLiquidateResponse] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["liquidation_responses", b"liquidation_responses"]) -> None: ...

global___MsgMultiLiquidateResponse = MsgMultiLiquidateResponse

@typing_extensions.final
class MsgOpenPosition(google.protobuf.message.Message):
    """-------------------------- OpenPosition --------------------------"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SENDER_FIELD_NUMBER: builtins.int
    TOKEN_PAIR_FIELD_NUMBER: builtins.int
    SIDE_FIELD_NUMBER: builtins.int
    QUOTE_ASSET_AMOUNT_FIELD_NUMBER: builtins.int
    LEVERAGE_FIELD_NUMBER: builtins.int
    BASE_ASSET_AMOUNT_LIMIT_FIELD_NUMBER: builtins.int
    sender: builtins.str
    token_pair: builtins.str
    side: perp.v1.state_pb2.Side.ValueType
    quote_asset_amount: builtins.str
    leverage: builtins.str
    base_asset_amount_limit: builtins.str
    def __init__(
        self,
        *,
        sender: builtins.str = ...,
        token_pair: builtins.str = ...,
        side: perp.v1.state_pb2.Side.ValueType = ...,
        quote_asset_amount: builtins.str = ...,
        leverage: builtins.str = ...,
        base_asset_amount_limit: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_asset_amount_limit", b"base_asset_amount_limit", "leverage", b"leverage", "quote_asset_amount", b"quote_asset_amount", "sender", b"sender", "side", b"side", "token_pair", b"token_pair"]) -> None: ...

global___MsgOpenPosition = MsgOpenPosition

@typing_extensions.final
class MsgOpenPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_FIELD_NUMBER: builtins.int
    EXCHANGED_NOTIONAL_VALUE_FIELD_NUMBER: builtins.int
    EXCHANGED_POSITION_SIZE_FIELD_NUMBER: builtins.int
    FUNDING_PAYMENT_FIELD_NUMBER: builtins.int
    REALIZED_PNL_FIELD_NUMBER: builtins.int
    UNREALIZED_PNL_AFTER_FIELD_NUMBER: builtins.int
    MARGIN_TO_VAULT_FIELD_NUMBER: builtins.int
    POSITION_NOTIONAL_FIELD_NUMBER: builtins.int
    @property
    def position(self) -> perp.v1.state_pb2.Position: ...
    exchanged_notional_value: builtins.str
    """The amount of quote assets exchanged."""
    exchanged_position_size: builtins.str
    """The amount of base assets exchanged."""
    funding_payment: builtins.str
    """The funding payment applied on this position change, measured in quote units."""
    realized_pnl: builtins.str
    """The amount of PnL realized on this position changed, measured in quote units."""
    unrealized_pnl_after: builtins.str
    """The unrealized PnL in the position after the position change, measured in quote units."""
    margin_to_vault: builtins.str
    """The amount of margin the trader has to give to the vault.
    A negative value means the vault pays the trader.
    """
    position_notional: builtins.str
    """The position's notional value after the position change, measured in quote units."""
    def __init__(
        self,
        *,
        position: perp.v1.state_pb2.Position | None = ...,
        exchanged_notional_value: builtins.str = ...,
        exchanged_position_size: builtins.str = ...,
        funding_payment: builtins.str = ...,
        realized_pnl: builtins.str = ...,
        unrealized_pnl_after: builtins.str = ...,
        margin_to_vault: builtins.str = ...,
        position_notional: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["position", b"position"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["exchanged_notional_value", b"exchanged_notional_value", "exchanged_position_size", b"exchanged_position_size", "funding_payment", b"funding_payment", "margin_to_vault", b"margin_to_vault", "position", b"position", "position_notional", b"position_notional", "realized_pnl", b"realized_pnl", "unrealized_pnl_after", b"unrealized_pnl_after"]) -> None: ...

global___MsgOpenPositionResponse = MsgOpenPositionResponse

@typing_extensions.final
class MsgClosePosition(google.protobuf.message.Message):
    """-------------------------- ClosePosition --------------------------"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SENDER_FIELD_NUMBER: builtins.int
    TOKEN_PAIR_FIELD_NUMBER: builtins.int
    sender: builtins.str
    token_pair: builtins.str
    def __init__(
        self,
        *,
        sender: builtins.str = ...,
        token_pair: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["sender", b"sender", "token_pair", b"token_pair"]) -> None: ...

global___MsgClosePosition = MsgClosePosition

@typing_extensions.final
class MsgClosePositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXCHANGED_NOTIONAL_VALUE_FIELD_NUMBER: builtins.int
    EXCHANGED_POSITION_SIZE_FIELD_NUMBER: builtins.int
    FUNDING_PAYMENT_FIELD_NUMBER: builtins.int
    REALIZED_PNL_FIELD_NUMBER: builtins.int
    MARGIN_TO_TRADER_FIELD_NUMBER: builtins.int
    exchanged_notional_value: builtins.str
    """The amount of quote assets exchanged."""
    exchanged_position_size: builtins.str
    """The amount of base assets exchanged."""
    funding_payment: builtins.str
    """The funding payment applied on this position change, measured in quote units."""
    realized_pnl: builtins.str
    """The amount of PnL realized on this position changed, measured in quote units."""
    margin_to_trader: builtins.str
    """The amount of margin the trader receives after closing the position, from the vault.
    Should never be negative.
    """
    def __init__(
        self,
        *,
        exchanged_notional_value: builtins.str = ...,
        exchanged_position_size: builtins.str = ...,
        funding_payment: builtins.str = ...,
        realized_pnl: builtins.str = ...,
        margin_to_trader: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["exchanged_notional_value", b"exchanged_notional_value", "exchanged_position_size", b"exchanged_position_size", "funding_payment", b"funding_payment", "margin_to_trader", b"margin_to_trader", "realized_pnl", b"realized_pnl"]) -> None: ...

global___MsgClosePositionResponse = MsgClosePositionResponse

@typing_extensions.final
class MsgDonateToEcosystemFund(google.protobuf.message.Message):
    """-------------------------- DonateToEcosystemFund --------------------------"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SENDER_FIELD_NUMBER: builtins.int
    DONATION_FIELD_NUMBER: builtins.int
    sender: builtins.str
    @property
    def donation(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """donation to the EF"""
    def __init__(
        self,
        *,
        sender: builtins.str = ...,
        donation: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["donation", b"donation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["donation", b"donation", "sender", b"sender"]) -> None: ...

global___MsgDonateToEcosystemFund = MsgDonateToEcosystemFund

@typing_extensions.final
class MsgDonateToEcosystemFundResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgDonateToEcosystemFundResponse = MsgDonateToEcosystemFundResponse
