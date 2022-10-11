"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import tendermint.crypto.proof_pb2
import tendermint.types.validator_pb2
import tendermint.version.types_pb2
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _BlockIDFlag:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _BlockIDFlagEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_BlockIDFlag.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    BLOCK_ID_FLAG_UNKNOWN: _BlockIDFlag.ValueType  # 0
    BLOCK_ID_FLAG_ABSENT: _BlockIDFlag.ValueType  # 1
    BLOCK_ID_FLAG_COMMIT: _BlockIDFlag.ValueType  # 2
    BLOCK_ID_FLAG_NIL: _BlockIDFlag.ValueType  # 3

class BlockIDFlag(_BlockIDFlag, metaclass=_BlockIDFlagEnumTypeWrapper):
    """BlockIdFlag indicates which BlcokID the signature is for"""

BLOCK_ID_FLAG_UNKNOWN: BlockIDFlag.ValueType  # 0
BLOCK_ID_FLAG_ABSENT: BlockIDFlag.ValueType  # 1
BLOCK_ID_FLAG_COMMIT: BlockIDFlag.ValueType  # 2
BLOCK_ID_FLAG_NIL: BlockIDFlag.ValueType  # 3
global___BlockIDFlag = BlockIDFlag

class _SignedMsgType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SignedMsgTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SignedMsgType.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SIGNED_MSG_TYPE_UNKNOWN: _SignedMsgType.ValueType  # 0
    SIGNED_MSG_TYPE_PREVOTE: _SignedMsgType.ValueType  # 1
    """Votes"""
    SIGNED_MSG_TYPE_PRECOMMIT: _SignedMsgType.ValueType  # 2
    SIGNED_MSG_TYPE_PROPOSAL: _SignedMsgType.ValueType  # 32
    """Proposals"""

class SignedMsgType(_SignedMsgType, metaclass=_SignedMsgTypeEnumTypeWrapper):
    """SignedMsgType is a type of signed message in the consensus."""

SIGNED_MSG_TYPE_UNKNOWN: SignedMsgType.ValueType  # 0
SIGNED_MSG_TYPE_PREVOTE: SignedMsgType.ValueType  # 1
"""Votes"""
SIGNED_MSG_TYPE_PRECOMMIT: SignedMsgType.ValueType  # 2
SIGNED_MSG_TYPE_PROPOSAL: SignedMsgType.ValueType  # 32
"""Proposals"""
global___SignedMsgType = SignedMsgType

class PartSetHeader(google.protobuf.message.Message):
    """PartsetHeader"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOTAL_FIELD_NUMBER: builtins.int
    HASH_FIELD_NUMBER: builtins.int
    total: builtins.int
    hash: builtins.bytes
    def __init__(
        self,
        *,
        total: builtins.int = ...,
        hash: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["hash", b"hash", "total", b"total"]) -> None: ...

global___PartSetHeader = PartSetHeader

class Part(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INDEX_FIELD_NUMBER: builtins.int
    BYTES_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    index: builtins.int
    bytes: builtins.bytes
    @property
    def proof(self) -> tendermint.crypto.proof_pb2.Proof: ...
    def __init__(
        self,
        *,
        index: builtins.int = ...,
        bytes: builtins.bytes = ...,
        proof: tendermint.crypto.proof_pb2.Proof | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["proof", b"proof"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bytes", b"bytes", "index", b"index", "proof", b"proof"]) -> None: ...

global___Part = Part

class BlockID(google.protobuf.message.Message):
    """BlockID"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HASH_FIELD_NUMBER: builtins.int
    PART_SET_HEADER_FIELD_NUMBER: builtins.int
    hash: builtins.bytes
    @property
    def part_set_header(self) -> global___PartSetHeader: ...
    def __init__(
        self,
        *,
        hash: builtins.bytes = ...,
        part_set_header: global___PartSetHeader | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["part_set_header", b"part_set_header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["hash", b"hash", "part_set_header", b"part_set_header"]) -> None: ...

global___BlockID = BlockID

class Header(google.protobuf.message.Message):
    """--------------------------------

    Header defines the structure of a Tendermint block header.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VERSION_FIELD_NUMBER: builtins.int
    CHAIN_ID_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    LAST_BLOCK_ID_FIELD_NUMBER: builtins.int
    LAST_COMMIT_HASH_FIELD_NUMBER: builtins.int
    DATA_HASH_FIELD_NUMBER: builtins.int
    VALIDATORS_HASH_FIELD_NUMBER: builtins.int
    NEXT_VALIDATORS_HASH_FIELD_NUMBER: builtins.int
    CONSENSUS_HASH_FIELD_NUMBER: builtins.int
    APP_HASH_FIELD_NUMBER: builtins.int
    LAST_RESULTS_HASH_FIELD_NUMBER: builtins.int
    EVIDENCE_HASH_FIELD_NUMBER: builtins.int
    PROPOSER_ADDRESS_FIELD_NUMBER: builtins.int
    @property
    def version(self) -> tendermint.version.types_pb2.Consensus:
        """basic block info"""
    chain_id: builtins.str
    height: builtins.int
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def last_block_id(self) -> global___BlockID:
        """prev block info"""
    last_commit_hash: builtins.bytes
    """hashes of block data
    commit from validators from the last block
    """
    data_hash: builtins.bytes
    """transactions"""
    validators_hash: builtins.bytes
    """hashes from the app output from the prev block
    validators for the current block
    """
    next_validators_hash: builtins.bytes
    """validators for the next block"""
    consensus_hash: builtins.bytes
    """consensus params for current block"""
    app_hash: builtins.bytes
    """state after txs from the previous block"""
    last_results_hash: builtins.bytes
    """root hash of all results from the txs from the previous block"""
    evidence_hash: builtins.bytes
    """consensus info
    evidence included in the block
    """
    proposer_address: builtins.bytes
    """original proposer of the block"""
    def __init__(
        self,
        *,
        version: tendermint.version.types_pb2.Consensus | None = ...,
        chain_id: builtins.str = ...,
        height: builtins.int = ...,
        time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        last_block_id: global___BlockID | None = ...,
        last_commit_hash: builtins.bytes = ...,
        data_hash: builtins.bytes = ...,
        validators_hash: builtins.bytes = ...,
        next_validators_hash: builtins.bytes = ...,
        consensus_hash: builtins.bytes = ...,
        app_hash: builtins.bytes = ...,
        last_results_hash: builtins.bytes = ...,
        evidence_hash: builtins.bytes = ...,
        proposer_address: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["last_block_id", b"last_block_id", "time", b"time", "version", b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["app_hash", b"app_hash", "chain_id", b"chain_id", "consensus_hash", b"consensus_hash", "data_hash", b"data_hash", "evidence_hash", b"evidence_hash", "height", b"height", "last_block_id", b"last_block_id", "last_commit_hash", b"last_commit_hash", "last_results_hash", b"last_results_hash", "next_validators_hash", b"next_validators_hash", "proposer_address", b"proposer_address", "time", b"time", "validators_hash", b"validators_hash", "version", b"version"]) -> None: ...

global___Header = Header

class Data(google.protobuf.message.Message):
    """Data contains the set of transactions included in the block"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TXS_FIELD_NUMBER: builtins.int
    @property
    def txs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]:
        """Txs that will be applied by state @ block.Height+1.
        NOTE: not all txs here are valid.  We're just agreeing on the order first.
        This means that block.AppHash does not include these txs.
        """
    def __init__(
        self,
        *,
        txs: collections.abc.Iterable[builtins.bytes] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["txs", b"txs"]) -> None: ...

global___Data = Data

class Vote(google.protobuf.message.Message):
    """Vote represents a prevote, precommit, or commit vote from validators for
    consensus.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    BLOCK_ID_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    VALIDATOR_INDEX_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    type: global___SignedMsgType.ValueType
    height: builtins.int
    round: builtins.int
    @property
    def block_id(self) -> global___BlockID:
        """zero if vote is nil."""
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    validator_address: builtins.bytes
    validator_index: builtins.int
    signature: builtins.bytes
    def __init__(
        self,
        *,
        type: global___SignedMsgType.ValueType = ...,
        height: builtins.int = ...,
        round: builtins.int = ...,
        block_id: global___BlockID | None = ...,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        validator_address: builtins.bytes = ...,
        validator_index: builtins.int = ...,
        signature: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["block_id", b"block_id", "timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_id", b"block_id", "height", b"height", "round", b"round", "signature", b"signature", "timestamp", b"timestamp", "type", b"type", "validator_address", b"validator_address", "validator_index", b"validator_index"]) -> None: ...

global___Vote = Vote

class Commit(google.protobuf.message.Message):
    """Commit contains the evidence that a block was committed by a set of validators."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    BLOCK_ID_FIELD_NUMBER: builtins.int
    SIGNATURES_FIELD_NUMBER: builtins.int
    height: builtins.int
    round: builtins.int
    @property
    def block_id(self) -> global___BlockID: ...
    @property
    def signatures(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CommitSig]: ...
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        round: builtins.int = ...,
        block_id: global___BlockID | None = ...,
        signatures: collections.abc.Iterable[global___CommitSig] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["block_id", b"block_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_id", b"block_id", "height", b"height", "round", b"round", "signatures", b"signatures"]) -> None: ...

global___Commit = Commit

class CommitSig(google.protobuf.message.Message):
    """CommitSig is a part of the Vote included in a Commit."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BLOCK_ID_FLAG_FIELD_NUMBER: builtins.int
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    block_id_flag: global___BlockIDFlag.ValueType
    validator_address: builtins.bytes
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    signature: builtins.bytes
    def __init__(
        self,
        *,
        block_id_flag: global___BlockIDFlag.ValueType = ...,
        validator_address: builtins.bytes = ...,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        signature: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_id_flag", b"block_id_flag", "signature", b"signature", "timestamp", b"timestamp", "validator_address", b"validator_address"]) -> None: ...

global___CommitSig = CommitSig

class Proposal(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    POL_ROUND_FIELD_NUMBER: builtins.int
    BLOCK_ID_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    type: global___SignedMsgType.ValueType
    height: builtins.int
    round: builtins.int
    pol_round: builtins.int
    @property
    def block_id(self) -> global___BlockID: ...
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    signature: builtins.bytes
    def __init__(
        self,
        *,
        type: global___SignedMsgType.ValueType = ...,
        height: builtins.int = ...,
        round: builtins.int = ...,
        pol_round: builtins.int = ...,
        block_id: global___BlockID | None = ...,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        signature: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["block_id", b"block_id", "timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_id", b"block_id", "height", b"height", "pol_round", b"pol_round", "round", b"round", "signature", b"signature", "timestamp", b"timestamp", "type", b"type"]) -> None: ...

global___Proposal = Proposal

class SignedHeader(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEADER_FIELD_NUMBER: builtins.int
    COMMIT_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> global___Header: ...
    @property
    def commit(self) -> global___Commit: ...
    def __init__(
        self,
        *,
        header: global___Header | None = ...,
        commit: global___Commit | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["commit", b"commit", "header", b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["commit", b"commit", "header", b"header"]) -> None: ...

global___SignedHeader = SignedHeader

class LightBlock(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SIGNED_HEADER_FIELD_NUMBER: builtins.int
    VALIDATOR_SET_FIELD_NUMBER: builtins.int
    @property
    def signed_header(self) -> global___SignedHeader: ...
    @property
    def validator_set(self) -> tendermint.types.validator_pb2.ValidatorSet: ...
    def __init__(
        self,
        *,
        signed_header: global___SignedHeader | None = ...,
        validator_set: tendermint.types.validator_pb2.ValidatorSet | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["signed_header", b"signed_header", "validator_set", b"validator_set"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["signed_header", b"signed_header", "validator_set", b"validator_set"]) -> None: ...

global___LightBlock = LightBlock

class BlockMeta(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BLOCK_ID_FIELD_NUMBER: builtins.int
    BLOCK_SIZE_FIELD_NUMBER: builtins.int
    HEADER_FIELD_NUMBER: builtins.int
    NUM_TXS_FIELD_NUMBER: builtins.int
    @property
    def block_id(self) -> global___BlockID: ...
    block_size: builtins.int
    @property
    def header(self) -> global___Header: ...
    num_txs: builtins.int
    def __init__(
        self,
        *,
        block_id: global___BlockID | None = ...,
        block_size: builtins.int = ...,
        header: global___Header | None = ...,
        num_txs: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["block_id", b"block_id", "header", b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_id", b"block_id", "block_size", b"block_size", "header", b"header", "num_txs", b"num_txs"]) -> None: ...

global___BlockMeta = BlockMeta

class TxProof(google.protobuf.message.Message):
    """TxProof represents a Merkle proof of the presence of a transaction in the Merkle tree."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROOT_HASH_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    root_hash: builtins.bytes
    data: builtins.bytes
    @property
    def proof(self) -> tendermint.crypto.proof_pb2.Proof: ...
    def __init__(
        self,
        *,
        root_hash: builtins.bytes = ...,
        data: builtins.bytes = ...,
        proof: tendermint.crypto.proof_pb2.Proof | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["proof", b"proof"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data", "proof", b"proof", "root_hash", b"root_hash"]) -> None: ...

global___TxProof = TxProof
