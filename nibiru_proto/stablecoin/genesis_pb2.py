# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stablecoin/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from stablecoin import params_pb2 as stablecoin_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18stablecoin/genesis.proto\x12\x14nibiru.stablecoin.v1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x17stablecoin/params.proto\"\xa4\x01\n\x0cGenesisState\x12\x32\n\x06params\x18\x01 \x01(\x0b\x32\x1c.nibiru.stablecoin.v1.ParamsB\x04\xc8\xde\x1f\x00\x12`\n\x16module_account_balance\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB%\xf2\xde\x1f\x1dyaml:\"module_account_balance\"\xc8\xde\x1f\x00\x42\x32Z0github.com/NibiruChain/nibiru/x/stablecoin/typesb\x06proto3')



_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'stablecoin.genesis_pb2'
  # @@protoc_insertion_point(class_scope:nibiru.stablecoin.v1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0github.com/NibiruChain/nibiru/x/stablecoin/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['module_account_balance']._options = None
  _GENESISSTATE.fields_by_name['module_account_balance']._serialized_options = b'\362\336\037\035yaml:\"module_account_balance\"\310\336\037\000'
  _GENESISSTATE._serialized_start=130
  _GENESISSTATE._serialized_end=294
# @@protoc_insertion_point(module_scope)
