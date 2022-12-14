"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.query.v1beta1.pagination_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class QueryEvidenceRequest(google.protobuf.message.Message):
    """QueryEvidenceRequest is the request type for the Query/Evidence RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EVIDENCE_HASH_FIELD_NUMBER: builtins.int
    evidence_hash: builtins.bytes
    """evidence_hash defines the hash of the requested evidence."""
    def __init__(
        self,
        *,
        evidence_hash: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["evidence_hash", b"evidence_hash"]) -> None: ...

global___QueryEvidenceRequest = QueryEvidenceRequest

@typing_extensions.final
class QueryEvidenceResponse(google.protobuf.message.Message):
    """QueryEvidenceResponse is the response type for the Query/Evidence RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EVIDENCE_FIELD_NUMBER: builtins.int
    @property
    def evidence(self) -> google.protobuf.any_pb2.Any:
        """evidence returns the requested evidence."""
    def __init__(
        self,
        *,
        evidence: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["evidence", b"evidence"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["evidence", b"evidence"]) -> None: ...

global___QueryEvidenceResponse = QueryEvidenceResponse

@typing_extensions.final
class QueryAllEvidenceRequest(google.protobuf.message.Message):
    """QueryEvidenceRequest is the request type for the Query/AllEvidence RPC
    method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest:
        """pagination defines an optional pagination for the request."""
    def __init__(
        self,
        *,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> None: ...

global___QueryAllEvidenceRequest = QueryAllEvidenceRequest

@typing_extensions.final
class QueryAllEvidenceResponse(google.protobuf.message.Message):
    """QueryAllEvidenceResponse is the response type for the Query/AllEvidence RPC
    method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EVIDENCE_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def evidence(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]:
        """evidence returns all evidences."""
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse:
        """pagination defines the pagination in the response."""
    def __init__(
        self,
        *,
        evidence: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["evidence", b"evidence", "pagination", b"pagination"]) -> None: ...

global___QueryAllEvidenceResponse = QueryAllEvidenceResponse
