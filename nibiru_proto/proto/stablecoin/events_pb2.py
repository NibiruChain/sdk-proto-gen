# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stablecoin/events.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17stablecoin/events.proto\x12\x14nibiru.stablecoin.v1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"X\n\rEventTransfer\x12-\n\x04\x63oin\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x0c\n\x04\x66rom\x18\x02 \x01(\t\x12\n\n\x02to\x18\x03 \x01(\t\"Q\n\x0f\x45ventMintStable\x12>\n\x06\x61mount\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\"Q\n\x0f\x45ventBurnStable\x12>\n\x06\x61mount\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\"O\n\rEventMintNIBI\x12>\n\x06\x61mount\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\"O\n\rEventBurnNIBI\x12>\n\x06\x61mount\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\"\xcf\x01\n\x14\x45ventRecollateralize\x12\x0e\n\x06\x63\x61ller\x18\x01 \x01(\t\x12\x30\n\x07in_coin\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x31\n\x08out_coin\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x42\n\ncoll_ratio\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\xc7\x01\n\x0c\x45ventBuyback\x12\x0e\n\x06\x63\x61ller\x18\x01 \x01(\t\x12\x30\n\x07in_coin\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x31\n\x08out_coin\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x42\n\ncoll_ratio\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x42\x32Z0github.com/NibiruChain/nibiru/x/stablecoin/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stablecoin.events_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0github.com/NibiruChain/nibiru/x/stablecoin/types'
  _EVENTTRANSFER.fields_by_name['coin']._options = None
  _EVENTTRANSFER.fields_by_name['coin']._serialized_options = b'\310\336\037\000'
  _EVENTMINTSTABLE.fields_by_name['amount']._options = None
  _EVENTMINTSTABLE.fields_by_name['amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _EVENTBURNSTABLE.fields_by_name['amount']._options = None
  _EVENTBURNSTABLE.fields_by_name['amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _EVENTMINTNIBI.fields_by_name['amount']._options = None
  _EVENTMINTNIBI.fields_by_name['amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _EVENTBURNNIBI.fields_by_name['amount']._options = None
  _EVENTBURNNIBI.fields_by_name['amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _EVENTRECOLLATERALIZE.fields_by_name['in_coin']._options = None
  _EVENTRECOLLATERALIZE.fields_by_name['in_coin']._serialized_options = b'\310\336\037\000'
  _EVENTRECOLLATERALIZE.fields_by_name['out_coin']._options = None
  _EVENTRECOLLATERALIZE.fields_by_name['out_coin']._serialized_options = b'\310\336\037\000'
  _EVENTRECOLLATERALIZE.fields_by_name['coll_ratio']._options = None
  _EVENTRECOLLATERALIZE.fields_by_name['coll_ratio']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _EVENTBUYBACK.fields_by_name['in_coin']._options = None
  _EVENTBUYBACK.fields_by_name['in_coin']._serialized_options = b'\310\336\037\000'
  _EVENTBUYBACK.fields_by_name['out_coin']._options = None
  _EVENTBUYBACK.fields_by_name['out_coin']._serialized_options = b'\310\336\037\000'
  _EVENTBUYBACK.fields_by_name['coll_ratio']._options = None
  _EVENTBUYBACK.fields_by_name['coll_ratio']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _EVENTTRANSFER._serialized_start=103
  _EVENTTRANSFER._serialized_end=191
  _EVENTMINTSTABLE._serialized_start=193
  _EVENTMINTSTABLE._serialized_end=274
  _EVENTBURNSTABLE._serialized_start=276
  _EVENTBURNSTABLE._serialized_end=357
  _EVENTMINTNIBI._serialized_start=359
  _EVENTMINTNIBI._serialized_end=438
  _EVENTBURNNIBI._serialized_start=440
  _EVENTBURNNIBI._serialized_end=519
  _EVENTRECOLLATERALIZE._serialized_start=522
  _EVENTRECOLLATERALIZE._serialized_end=729
  _EVENTBUYBACK._serialized_start=732
  _EVENTBUYBACK._serialized_end=931
# @@protoc_insertion_point(module_scope)
