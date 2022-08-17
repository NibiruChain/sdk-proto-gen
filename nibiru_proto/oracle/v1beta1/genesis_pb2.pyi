"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import oracle.v1beta1.oracle_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the oracle module's genesis state."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARAMS_FIELD_NUMBER: builtins.int
    FEEDER_DELEGATIONS_FIELD_NUMBER: builtins.int
    EXCHANGE_RATES_FIELD_NUMBER: builtins.int
    MISS_COUNTERS_FIELD_NUMBER: builtins.int
    AGGREGATE_EXCHANGE_RATE_PREVOTES_FIELD_NUMBER: builtins.int
    AGGREGATE_EXCHANGE_RATE_VOTES_FIELD_NUMBER: builtins.int
    TOBIN_TAXES_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> oracle.v1beta1.oracle_pb2.Params: ...
    @property
    def feeder_delegations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FeederDelegation]: ...
    @property
    def exchange_rates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[oracle.v1beta1.oracle_pb2.ExchangeRateTuple]: ...
    @property
    def miss_counters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MissCounter]: ...
    @property
    def aggregate_exchange_rate_prevotes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[oracle.v1beta1.oracle_pb2.AggregateExchangeRatePrevote]: ...
    @property
    def aggregate_exchange_rate_votes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[oracle.v1beta1.oracle_pb2.AggregateExchangeRateVote]: ...
    @property
    def tobin_taxes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TobinTax]: ...
    def __init__(self,
        *,
        params: typing.Optional[oracle.v1beta1.oracle_pb2.Params] = ...,
        feeder_delegations: typing.Optional[typing.Iterable[global___FeederDelegation]] = ...,
        exchange_rates: typing.Optional[typing.Iterable[oracle.v1beta1.oracle_pb2.ExchangeRateTuple]] = ...,
        miss_counters: typing.Optional[typing.Iterable[global___MissCounter]] = ...,
        aggregate_exchange_rate_prevotes: typing.Optional[typing.Iterable[oracle.v1beta1.oracle_pb2.AggregateExchangeRatePrevote]] = ...,
        aggregate_exchange_rate_votes: typing.Optional[typing.Iterable[oracle.v1beta1.oracle_pb2.AggregateExchangeRateVote]] = ...,
        tobin_taxes: typing.Optional[typing.Iterable[global___TobinTax]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params",b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["aggregate_exchange_rate_prevotes",b"aggregate_exchange_rate_prevotes","aggregate_exchange_rate_votes",b"aggregate_exchange_rate_votes","exchange_rates",b"exchange_rates","feeder_delegations",b"feeder_delegations","miss_counters",b"miss_counters","params",b"params","tobin_taxes",b"tobin_taxes"]) -> None: ...
global___GenesisState = GenesisState

class FeederDelegation(google.protobuf.message.Message):
    """FeederDelegation is the address for where oracle feeder authority are
    delegated to. By default this struct is only used at genesis to feed in
    default feeder addresses.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FEEDER_ADDRESS_FIELD_NUMBER: builtins.int
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    feeder_address: typing.Text
    validator_address: typing.Text
    def __init__(self,
        *,
        feeder_address: typing.Text = ...,
        validator_address: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["feeder_address",b"feeder_address","validator_address",b"validator_address"]) -> None: ...
global___FeederDelegation = FeederDelegation

class MissCounter(google.protobuf.message.Message):
    """MissCounter defines an miss counter and validator address pair used in
    oracle module's genesis state
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    MISS_COUNTER_FIELD_NUMBER: builtins.int
    validator_address: typing.Text
    miss_counter: builtins.int
    def __init__(self,
        *,
        validator_address: typing.Text = ...,
        miss_counter: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["miss_counter",b"miss_counter","validator_address",b"validator_address"]) -> None: ...
global___MissCounter = MissCounter

class TobinTax(google.protobuf.message.Message):
    """TobinTax defines a pair and tobin_tax pair used in
    oracle module's genesis state
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAIR_FIELD_NUMBER: builtins.int
    TOBIN_TAX_FIELD_NUMBER: builtins.int
    pair: typing.Text
    tobin_tax: typing.Text
    def __init__(self,
        *,
        pair: typing.Text = ...,
        tobin_tax: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pair",b"pair","tobin_tax",b"tobin_tax"]) -> None: ...
global___TobinTax = TobinTax
