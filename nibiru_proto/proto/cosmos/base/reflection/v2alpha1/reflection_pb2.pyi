"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Since: cosmos-sdk 0.43"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class AppDescriptor(google.protobuf.message.Message):
    """AppDescriptor describes a cosmos-sdk based application"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHN_FIELD_NUMBER: builtins.int
    CHAIN_FIELD_NUMBER: builtins.int
    CODEC_FIELD_NUMBER: builtins.int
    CONFIGURATION_FIELD_NUMBER: builtins.int
    QUERY_SERVICES_FIELD_NUMBER: builtins.int
    TX_FIELD_NUMBER: builtins.int
    @property
    def authn(self) -> global___AuthnDescriptor:
        """AuthnDescriptor provides information on how to authenticate transactions on the application
        NOTE: experimental and subject to change in future releases.
        """
    @property
    def chain(self) -> global___ChainDescriptor:
        """chain provides the chain descriptor"""
    @property
    def codec(self) -> global___CodecDescriptor:
        """codec provides metadata information regarding codec related types"""
    @property
    def configuration(self) -> global___ConfigurationDescriptor:
        """configuration provides metadata information regarding the sdk.Config type"""
    @property
    def query_services(self) -> global___QueryServicesDescriptor:
        """query_services provides metadata information regarding the available queriable endpoints"""
    @property
    def tx(self) -> global___TxDescriptor:
        """tx provides metadata information regarding how to send transactions to the given application"""
    def __init__(
        self,
        *,
        authn: global___AuthnDescriptor | None = ...,
        chain: global___ChainDescriptor | None = ...,
        codec: global___CodecDescriptor | None = ...,
        configuration: global___ConfigurationDescriptor | None = ...,
        query_services: global___QueryServicesDescriptor | None = ...,
        tx: global___TxDescriptor | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["authn", b"authn", "chain", b"chain", "codec", b"codec", "configuration", b"configuration", "query_services", b"query_services", "tx", b"tx"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["authn", b"authn", "chain", b"chain", "codec", b"codec", "configuration", b"configuration", "query_services", b"query_services", "tx", b"tx"]) -> None: ...

global___AppDescriptor = AppDescriptor

class TxDescriptor(google.protobuf.message.Message):
    """TxDescriptor describes the accepted transaction type"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FULLNAME_FIELD_NUMBER: builtins.int
    MSGS_FIELD_NUMBER: builtins.int
    fullname: builtins.str
    """fullname is the protobuf fullname of the raw transaction type (for instance the tx.Tx type)
    it is not meant to support polymorphism of transaction types, it is supposed to be used by
    reflection clients to understand if they can handle a specific transaction type in an application.
    """
    @property
    def msgs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MsgDescriptor]:
        """msgs lists the accepted application messages (sdk.Msg)"""
    def __init__(
        self,
        *,
        fullname: builtins.str = ...,
        msgs: collections.abc.Iterable[global___MsgDescriptor] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fullname", b"fullname", "msgs", b"msgs"]) -> None: ...

global___TxDescriptor = TxDescriptor

class AuthnDescriptor(google.protobuf.message.Message):
    """AuthnDescriptor provides information on how to sign transactions without relying
    on the online RPCs GetTxMetadata and CombineUnsignedTxAndSignatures
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SIGN_MODES_FIELD_NUMBER: builtins.int
    @property
    def sign_modes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SigningModeDescriptor]:
        """sign_modes defines the supported signature algorithm"""
    def __init__(
        self,
        *,
        sign_modes: collections.abc.Iterable[global___SigningModeDescriptor] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["sign_modes", b"sign_modes"]) -> None: ...

global___AuthnDescriptor = AuthnDescriptor

class SigningModeDescriptor(google.protobuf.message.Message):
    """SigningModeDescriptor provides information on a signing flow of the application
    NOTE(fdymylja): here we could go as far as providing an entire flow on how
    to sign a message given a SigningModeDescriptor, but it's better to think about
    this another time
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    NUMBER_FIELD_NUMBER: builtins.int
    AUTHN_INFO_PROVIDER_METHOD_FULLNAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """name defines the unique name of the signing mode"""
    number: builtins.int
    """number is the unique int32 identifier for the sign_mode enum"""
    authn_info_provider_method_fullname: builtins.str
    """authn_info_provider_method_fullname defines the fullname of the method to call to get
    the metadata required to authenticate using the provided sign_modes
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        number: builtins.int = ...,
        authn_info_provider_method_fullname: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["authn_info_provider_method_fullname", b"authn_info_provider_method_fullname", "name", b"name", "number", b"number"]) -> None: ...

global___SigningModeDescriptor = SigningModeDescriptor

class ChainDescriptor(google.protobuf.message.Message):
    """ChainDescriptor describes chain information of the application"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """id is the chain id"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id"]) -> None: ...

global___ChainDescriptor = ChainDescriptor

class CodecDescriptor(google.protobuf.message.Message):
    """CodecDescriptor describes the registered interfaces and provides metadata information on the types"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INTERFACES_FIELD_NUMBER: builtins.int
    @property
    def interfaces(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InterfaceDescriptor]:
        """interfaces is a list of the registerted interfaces descriptors"""
    def __init__(
        self,
        *,
        interfaces: collections.abc.Iterable[global___InterfaceDescriptor] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["interfaces", b"interfaces"]) -> None: ...

global___CodecDescriptor = CodecDescriptor

class InterfaceDescriptor(google.protobuf.message.Message):
    """InterfaceDescriptor describes the implementation of an interface"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FULLNAME_FIELD_NUMBER: builtins.int
    INTERFACE_ACCEPTING_MESSAGES_FIELD_NUMBER: builtins.int
    INTERFACE_IMPLEMENTERS_FIELD_NUMBER: builtins.int
    fullname: builtins.str
    """fullname is the name of the interface"""
    @property
    def interface_accepting_messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InterfaceAcceptingMessageDescriptor]:
        """interface_accepting_messages contains information regarding the proto messages which contain the interface as
        google.protobuf.Any field
        """
    @property
    def interface_implementers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InterfaceImplementerDescriptor]:
        """interface_implementers is a list of the descriptors of the interface implementers"""
    def __init__(
        self,
        *,
        fullname: builtins.str = ...,
        interface_accepting_messages: collections.abc.Iterable[global___InterfaceAcceptingMessageDescriptor] | None = ...,
        interface_implementers: collections.abc.Iterable[global___InterfaceImplementerDescriptor] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fullname", b"fullname", "interface_accepting_messages", b"interface_accepting_messages", "interface_implementers", b"interface_implementers"]) -> None: ...

global___InterfaceDescriptor = InterfaceDescriptor

class InterfaceImplementerDescriptor(google.protobuf.message.Message):
    """InterfaceImplementerDescriptor describes an interface implementer"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FULLNAME_FIELD_NUMBER: builtins.int
    TYPE_URL_FIELD_NUMBER: builtins.int
    fullname: builtins.str
    """fullname is the protobuf queryable name of the interface implementer"""
    type_url: builtins.str
    """type_url defines the type URL used when marshalling the type as any
    this is required so we can provide type safe google.protobuf.Any marshalling and
    unmarshalling, making sure that we don't accept just 'any' type
    in our interface fields
    """
    def __init__(
        self,
        *,
        fullname: builtins.str = ...,
        type_url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fullname", b"fullname", "type_url", b"type_url"]) -> None: ...

global___InterfaceImplementerDescriptor = InterfaceImplementerDescriptor

class InterfaceAcceptingMessageDescriptor(google.protobuf.message.Message):
    """InterfaceAcceptingMessageDescriptor describes a protobuf message which contains
    an interface represented as a google.protobuf.Any
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FULLNAME_FIELD_NUMBER: builtins.int
    FIELD_DESCRIPTOR_NAMES_FIELD_NUMBER: builtins.int
    fullname: builtins.str
    """fullname is the protobuf fullname of the type containing the interface"""
    @property
    def field_descriptor_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """field_descriptor_names is a list of the protobuf name (not fullname) of the field
        which contains the interface as google.protobuf.Any (the interface is the same, but
        it can be in multiple fields of the same proto message)
        """
    def __init__(
        self,
        *,
        fullname: builtins.str = ...,
        field_descriptor_names: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["field_descriptor_names", b"field_descriptor_names", "fullname", b"fullname"]) -> None: ...

global___InterfaceAcceptingMessageDescriptor = InterfaceAcceptingMessageDescriptor

class ConfigurationDescriptor(google.protobuf.message.Message):
    """ConfigurationDescriptor contains metadata information on the sdk.Config"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BECH32_ACCOUNT_ADDRESS_PREFIX_FIELD_NUMBER: builtins.int
    bech32_account_address_prefix: builtins.str
    """bech32_account_address_prefix is the account address prefix"""
    def __init__(
        self,
        *,
        bech32_account_address_prefix: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bech32_account_address_prefix", b"bech32_account_address_prefix"]) -> None: ...

global___ConfigurationDescriptor = ConfigurationDescriptor

class MsgDescriptor(google.protobuf.message.Message):
    """MsgDescriptor describes a cosmos-sdk message that can be delivered with a transaction"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MSG_TYPE_URL_FIELD_NUMBER: builtins.int
    msg_type_url: builtins.str
    """msg_type_url contains the TypeURL of a sdk.Msg."""
    def __init__(
        self,
        *,
        msg_type_url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["msg_type_url", b"msg_type_url"]) -> None: ...

global___MsgDescriptor = MsgDescriptor

class GetAuthnDescriptorRequest(google.protobuf.message.Message):
    """GetAuthnDescriptorRequest is the request used for the GetAuthnDescriptor RPC"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetAuthnDescriptorRequest = GetAuthnDescriptorRequest

class GetAuthnDescriptorResponse(google.protobuf.message.Message):
    """GetAuthnDescriptorResponse is the response returned by the GetAuthnDescriptor RPC"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTHN_FIELD_NUMBER: builtins.int
    @property
    def authn(self) -> global___AuthnDescriptor:
        """authn describes how to authenticate to the application when sending transactions"""
    def __init__(
        self,
        *,
        authn: global___AuthnDescriptor | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["authn", b"authn"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["authn", b"authn"]) -> None: ...

global___GetAuthnDescriptorResponse = GetAuthnDescriptorResponse

class GetChainDescriptorRequest(google.protobuf.message.Message):
    """GetChainDescriptorRequest is the request used for the GetChainDescriptor RPC"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetChainDescriptorRequest = GetChainDescriptorRequest

class GetChainDescriptorResponse(google.protobuf.message.Message):
    """GetChainDescriptorResponse is the response returned by the GetChainDescriptor RPC"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHAIN_FIELD_NUMBER: builtins.int
    @property
    def chain(self) -> global___ChainDescriptor:
        """chain describes application chain information"""
    def __init__(
        self,
        *,
        chain: global___ChainDescriptor | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["chain", b"chain"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["chain", b"chain"]) -> None: ...

global___GetChainDescriptorResponse = GetChainDescriptorResponse

class GetCodecDescriptorRequest(google.protobuf.message.Message):
    """GetCodecDescriptorRequest is the request used for the GetCodecDescriptor RPC"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetCodecDescriptorRequest = GetCodecDescriptorRequest

class GetCodecDescriptorResponse(google.protobuf.message.Message):
    """GetCodecDescriptorResponse is the response returned by the GetCodecDescriptor RPC"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODEC_FIELD_NUMBER: builtins.int
    @property
    def codec(self) -> global___CodecDescriptor:
        """codec describes the application codec such as registered interfaces and implementations"""
    def __init__(
        self,
        *,
        codec: global___CodecDescriptor | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["codec", b"codec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["codec", b"codec"]) -> None: ...

global___GetCodecDescriptorResponse = GetCodecDescriptorResponse

class GetConfigurationDescriptorRequest(google.protobuf.message.Message):
    """GetConfigurationDescriptorRequest is the request used for the GetConfigurationDescriptor RPC"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetConfigurationDescriptorRequest = GetConfigurationDescriptorRequest

class GetConfigurationDescriptorResponse(google.protobuf.message.Message):
    """GetConfigurationDescriptorResponse is the response returned by the GetConfigurationDescriptor RPC"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONFIG_FIELD_NUMBER: builtins.int
    @property
    def config(self) -> global___ConfigurationDescriptor:
        """config describes the application's sdk.Config"""
    def __init__(
        self,
        *,
        config: global___ConfigurationDescriptor | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config", b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config"]) -> None: ...

global___GetConfigurationDescriptorResponse = GetConfigurationDescriptorResponse

class GetQueryServicesDescriptorRequest(google.protobuf.message.Message):
    """GetQueryServicesDescriptorRequest is the request used for the GetQueryServicesDescriptor RPC"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetQueryServicesDescriptorRequest = GetQueryServicesDescriptorRequest

class GetQueryServicesDescriptorResponse(google.protobuf.message.Message):
    """GetQueryServicesDescriptorResponse is the response returned by the GetQueryServicesDescriptor RPC"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUERIES_FIELD_NUMBER: builtins.int
    @property
    def queries(self) -> global___QueryServicesDescriptor:
        """queries provides information on the available queryable services"""
    def __init__(
        self,
        *,
        queries: global___QueryServicesDescriptor | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["queries", b"queries"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["queries", b"queries"]) -> None: ...

global___GetQueryServicesDescriptorResponse = GetQueryServicesDescriptorResponse

class GetTxDescriptorRequest(google.protobuf.message.Message):
    """GetTxDescriptorRequest is the request used for the GetTxDescriptor RPC"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetTxDescriptorRequest = GetTxDescriptorRequest

class GetTxDescriptorResponse(google.protobuf.message.Message):
    """GetTxDescriptorResponse is the response returned by the GetTxDescriptor RPC"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TX_FIELD_NUMBER: builtins.int
    @property
    def tx(self) -> global___TxDescriptor:
        """tx provides information on msgs that can be forwarded to the application
        alongside the accepted transaction protobuf type
        """
    def __init__(
        self,
        *,
        tx: global___TxDescriptor | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tx", b"tx"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["tx", b"tx"]) -> None: ...

global___GetTxDescriptorResponse = GetTxDescriptorResponse

class QueryServicesDescriptor(google.protobuf.message.Message):
    """QueryServicesDescriptor contains the list of cosmos-sdk queriable services"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUERY_SERVICES_FIELD_NUMBER: builtins.int
    @property
    def query_services(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___QueryServiceDescriptor]:
        """query_services is a list of cosmos-sdk QueryServiceDescriptor"""
    def __init__(
        self,
        *,
        query_services: collections.abc.Iterable[global___QueryServiceDescriptor] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["query_services", b"query_services"]) -> None: ...

global___QueryServicesDescriptor = QueryServicesDescriptor

class QueryServiceDescriptor(google.protobuf.message.Message):
    """QueryServiceDescriptor describes a cosmos-sdk queryable service"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FULLNAME_FIELD_NUMBER: builtins.int
    IS_MODULE_FIELD_NUMBER: builtins.int
    METHODS_FIELD_NUMBER: builtins.int
    fullname: builtins.str
    """fullname is the protobuf fullname of the service descriptor"""
    is_module: builtins.bool
    """is_module describes if this service is actually exposed by an application's module"""
    @property
    def methods(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___QueryMethodDescriptor]:
        """methods provides a list of query service methods"""
    def __init__(
        self,
        *,
        fullname: builtins.str = ...,
        is_module: builtins.bool = ...,
        methods: collections.abc.Iterable[global___QueryMethodDescriptor] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fullname", b"fullname", "is_module", b"is_module", "methods", b"methods"]) -> None: ...

global___QueryServiceDescriptor = QueryServiceDescriptor

class QueryMethodDescriptor(google.protobuf.message.Message):
    """QueryMethodDescriptor describes a queryable method of a query service
    no other info is provided beside method name and tendermint queryable path
    because it would be redundant with the grpc reflection service
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    FULL_QUERY_PATH_FIELD_NUMBER: builtins.int
    name: builtins.str
    """name is the protobuf name (not fullname) of the method"""
    full_query_path: builtins.str
    """full_query_path is the path that can be used to query
    this method via tendermint abci.Query
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        full_query_path: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["full_query_path", b"full_query_path", "name", b"name"]) -> None: ...

global___QueryMethodDescriptor = QueryMethodDescriptor
