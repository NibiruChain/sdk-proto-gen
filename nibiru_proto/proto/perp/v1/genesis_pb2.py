# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: perp/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from common import common_pb2 as common_dot_common__pb2
from perp.v1 import state_pb2 as perp_dot_v1_dot_state__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15perp/v1/genesis.proto\x12\x0enibiru.perp.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x13\x63ommon/common.proto\x1a\x13perp/v1/state.proto\"\xeb\x01\n\x0cGenesisState\x12,\n\x06params\x18\x01 \x01(\x0b\x32\x16.nibiru.perp.v1.ParamsB\x04\xc8\xde\x1f\x00\x12\x39\n\rpair_metadata\x18\x02 \x03(\x0b\x32\x1c.nibiru.perp.v1.PairMetadataB\x04\xc8\xde\x1f\x00\x12\x31\n\tpositions\x18\x03 \x03(\x0b\x32\x18.nibiru.perp.v1.PositionB\x04\xc8\xde\x1f\x00\x12?\n\x11prepaid_bad_debts\x18\x04 \x03(\x0b\x32\x1e.nibiru.perp.v1.PrepaidBadDebtB\x04\xc8\xde\x1f\x00\x42,Z*github.com/NibiruChain/nibiru/x/perp/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'perp.v1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z*github.com/NibiruChain/nibiru/x/perp/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['pair_metadata']._options = None
  _GENESISSTATE.fields_by_name['pair_metadata']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['positions']._options = None
  _GENESISSTATE.fields_by_name['positions']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['prepaid_bad_debts']._options = None
  _GENESISSTATE.fields_by_name['prepaid_bad_debts']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE._serialized_start=168
  _GENESISSTATE._serialized_end=403
# @@protoc_insertion_point(module_scope)
