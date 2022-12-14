"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PoolType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PoolTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PoolType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    BALANCER: _PoolType.ValueType  # 0
    STABLESWAP: _PoolType.ValueType  # 1

class PoolType(_PoolType, metaclass=_PoolTypeEnumTypeWrapper):
    """- `balancer`: Balancer are pools defined by the equation xy=k, extended by the weighs introduced by Balancer.
    - `stableswap`: Stableswap pools are defined by a combination of constant-product and constant-sum pool
    """

BALANCER: PoolType.ValueType  # 0
STABLESWAP: PoolType.ValueType  # 1
global___PoolType = PoolType

@typing_extensions.final
class PoolParams(google.protobuf.message.Message):
    """Configuration parameters for the pool."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SWAP_FEE_FIELD_NUMBER: builtins.int
    EXIT_FEE_FIELD_NUMBER: builtins.int
    A_FIELD_NUMBER: builtins.int
    POOL_TYPE_FIELD_NUMBER: builtins.int
    swap_fee: builtins.str
    exit_fee: builtins.str
    A: builtins.str
    """Amplification Parameter (A): Larger value of A make the curve better resemble a straight 
    line in the center (when pool is near balance).  Highly volatile assets should use a lower value, while assets that 
    are closer together may be best with a higher value.
    This is only used if the pool_type is set to 1 (stableswap)
    """
    pool_type: global___PoolType.ValueType
    def __init__(
        self,
        *,
        swap_fee: builtins.str = ...,
        exit_fee: builtins.str = ...,
        A: builtins.str = ...,
        pool_type: global___PoolType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["A", b"A", "exit_fee", b"exit_fee", "pool_type", b"pool_type", "swap_fee", b"swap_fee"]) -> None: ...

global___PoolParams = PoolParams

@typing_extensions.final
class PoolAsset(google.protobuf.message.Message):
    """Which assets the pool contains."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_FIELD_NUMBER: builtins.int
    WEIGHT_FIELD_NUMBER: builtins.int
    @property
    def token(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """Coins we are talking about,
        the denomination must be unique amongst all PoolAssets for this pool.
        """
    weight: builtins.str
    """Weight that is not normalized. This weight must be less than 2^50"""
    def __init__(
        self,
        *,
        token: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
        weight: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["token", b"token"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["token", b"token", "weight", b"weight"]) -> None: ...

global___PoolAsset = PoolAsset

@typing_extensions.final
class Pool(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    POOL_PARAMS_FIELD_NUMBER: builtins.int
    POOL_ASSETS_FIELD_NUMBER: builtins.int
    TOTAL_WEIGHT_FIELD_NUMBER: builtins.int
    TOTAL_SHARES_FIELD_NUMBER: builtins.int
    id: builtins.int
    """The pool id."""
    address: builtins.str
    """The pool account address."""
    @property
    def pool_params(self) -> global___PoolParams:
        """Fees and other pool-specific parameters."""
    @property
    def pool_assets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PoolAsset]:
        """These are assumed to be sorted by denomiation.
        They contain the pool asset and the information about the weight
        """
    total_weight: builtins.str
    """sum of all non-normalized pool weights"""
    @property
    def total_shares(self) -> cosmos.base.v1beta1.coin_pb2.Coin:
        """sum of all LP tokens sent out"""
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        address: builtins.str = ...,
        pool_params: global___PoolParams | None = ...,
        pool_assets: collections.abc.Iterable[global___PoolAsset] | None = ...,
        total_weight: builtins.str = ...,
        total_shares: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pool_params", b"pool_params", "total_shares", b"total_shares"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address", "id", b"id", "pool_assets", b"pool_assets", "pool_params", b"pool_params", "total_shares", b"total_shares", "total_weight", b"total_weight"]) -> None: ...

global___Pool = Pool
