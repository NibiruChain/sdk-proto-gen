# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lockup/v1/lock.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14lockup/v1/lock.proto\x12\x10nibiru.lockup.v1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xbf\x02\n\x04Lock\x12\x0f\n\x07lock_id\x18\x01 \x01(\x04\x12\x1f\n\x05owner\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"owner\"\x12^\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB1\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xea\xde\x1f\x12\x64uration,omitempty\xf2\xde\x1f\x0fyaml:\"duration\"\x12I\n\x08\x65nd_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x1b\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:\"end_time\"\x12Z\n\x05\x63oins\x18\x05 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsB.Z,github.com/NibiruChain/nibiru/x/lockup/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lockup.v1.lock_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/NibiruChain/nibiru/x/lockup/types'
  _LOCK.fields_by_name['owner']._options = None
  _LOCK.fields_by_name['owner']._serialized_options = b'\362\336\037\014yaml:\"owner\"'
  _LOCK.fields_by_name['duration']._options = None
  _LOCK.fields_by_name['duration']._serialized_options = b'\310\336\037\000\230\337\037\001\352\336\037\022duration,omitempty\362\336\037\017yaml:\"duration\"'
  _LOCK.fields_by_name['end_time']._options = None
  _LOCK.fields_by_name['end_time']._serialized_options = b'\220\337\037\001\310\336\037\000\362\336\037\017yaml:\"end_time\"'
  _LOCK.fields_by_name['coins']._options = None
  _LOCK.fields_by_name['coins']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _LOCK._serialized_start=162
  _LOCK._serialized_end=481
# @@protoc_insertion_point(module_scope)
