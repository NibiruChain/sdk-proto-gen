# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: oracle/v1beta1/oracle.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1boracle/v1beta1/oracle.proto\x12\x15nibiru.oracle.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xa1\x04\n\x06Params\x12+\n\x0bvote_period\x18\x01 \x01(\x04\x42\x16\xf2\xde\x1f\x12yaml:\"vote_period\"\x12_\n\x0evote_threshold\x18\x02 \x01(\tBG\xf2\xde\x1f\x15yaml:\"vote_threshold\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12Y\n\x0breward_band\x18\x03 \x01(\tBD\xf2\xde\x1f\x12yaml:\"reward_band\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\'\n\twhitelist\x18\x04 \x03(\tB\x14\xf2\xde\x1f\x10yaml:\"whitelist\"\x12_\n\x0eslash_fraction\x18\x05 \x01(\tBG\xf2\xde\x1f\x15yaml:\"slash_fraction\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12-\n\x0cslash_window\x18\x06 \x01(\x04\x42\x17\xf2\xde\x1f\x13yaml:\"slash_window\"\x12k\n\x14min_valid_per_window\x18\x07 \x01(\tBM\xf2\xde\x1f\x1byaml:\"min_valid_per_window\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00\"\x9b\x01\n\x1c\x41ggregateExchangeRatePrevote\x12\x1d\n\x04hash\x18\x01 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:\"hash\"\x12\x1f\n\x05voter\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"voter\"\x12-\n\x0csubmit_block\x18\x03 \x01(\x04\x42\x17\xf2\xde\x1f\x13yaml:\"submit_block\":\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"\xce\x01\n\x19\x41ggregateExchangeRateVote\x12\x81\x01\n\x14\x65xchange_rate_tuples\x18\x01 \x03(\x0b\x32(.nibiru.oracle.v1beta1.ExchangeRateTupleB9\xf2\xde\x1f\x1byaml:\"exchange_rate_tuples\"\xaa\xdf\x1f\x12\x45xchangeRateTuples\xc8\xde\x1f\x00\x12\x1f\n\x05voter\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"voter\":\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"\x9f\x01\n\x11\x45xchangeRateTuple\x12\x1d\n\x04pair\x18\x01 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:\"pair\"\x12]\n\rexchange_rate\x18\x02 \x01(\tBF\xf2\xde\x1f\x14yaml:\"exchange_rate\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"l\n\nPairReward\x12\x0c\n\x04pair\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x14\n\x0cvote_periods\x18\x03 \x01(\x04\x12.\n\x05\x63oins\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x42.Z,github.com/NibiruChain/nibiru/x/oracle/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'oracle.v1beta1.oracle_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/NibiruChain/nibiru/x/oracle/types'
  _PARAMS.fields_by_name['vote_period']._options = None
  _PARAMS.fields_by_name['vote_period']._serialized_options = b'\362\336\037\022yaml:\"vote_period\"'
  _PARAMS.fields_by_name['vote_threshold']._options = None
  _PARAMS.fields_by_name['vote_threshold']._serialized_options = b'\362\336\037\025yaml:\"vote_threshold\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _PARAMS.fields_by_name['reward_band']._options = None
  _PARAMS.fields_by_name['reward_band']._serialized_options = b'\362\336\037\022yaml:\"reward_band\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _PARAMS.fields_by_name['whitelist']._options = None
  _PARAMS.fields_by_name['whitelist']._serialized_options = b'\362\336\037\020yaml:\"whitelist\"'
  _PARAMS.fields_by_name['slash_fraction']._options = None
  _PARAMS.fields_by_name['slash_fraction']._serialized_options = b'\362\336\037\025yaml:\"slash_fraction\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _PARAMS.fields_by_name['slash_window']._options = None
  _PARAMS.fields_by_name['slash_window']._serialized_options = b'\362\336\037\023yaml:\"slash_window\"'
  _PARAMS.fields_by_name['min_valid_per_window']._options = None
  _PARAMS.fields_by_name['min_valid_per_window']._serialized_options = b'\362\336\037\033yaml:\"min_valid_per_window\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _PARAMS._options = None
  _PARAMS._serialized_options = b'\350\240\037\001\230\240\037\000'
  _AGGREGATEEXCHANGERATEPREVOTE.fields_by_name['hash']._options = None
  _AGGREGATEEXCHANGERATEPREVOTE.fields_by_name['hash']._serialized_options = b'\362\336\037\013yaml:\"hash\"'
  _AGGREGATEEXCHANGERATEPREVOTE.fields_by_name['voter']._options = None
  _AGGREGATEEXCHANGERATEPREVOTE.fields_by_name['voter']._serialized_options = b'\362\336\037\014yaml:\"voter\"'
  _AGGREGATEEXCHANGERATEPREVOTE.fields_by_name['submit_block']._options = None
  _AGGREGATEEXCHANGERATEPREVOTE.fields_by_name['submit_block']._serialized_options = b'\362\336\037\023yaml:\"submit_block\"'
  _AGGREGATEEXCHANGERATEPREVOTE._options = None
  _AGGREGATEEXCHANGERATEPREVOTE._serialized_options = b'\350\240\037\000\210\240\037\000\230\240\037\000'
  _AGGREGATEEXCHANGERATEVOTE.fields_by_name['exchange_rate_tuples']._options = None
  _AGGREGATEEXCHANGERATEVOTE.fields_by_name['exchange_rate_tuples']._serialized_options = b'\362\336\037\033yaml:\"exchange_rate_tuples\"\252\337\037\022ExchangeRateTuples\310\336\037\000'
  _AGGREGATEEXCHANGERATEVOTE.fields_by_name['voter']._options = None
  _AGGREGATEEXCHANGERATEVOTE.fields_by_name['voter']._serialized_options = b'\362\336\037\014yaml:\"voter\"'
  _AGGREGATEEXCHANGERATEVOTE._options = None
  _AGGREGATEEXCHANGERATEVOTE._serialized_options = b'\350\240\037\000\210\240\037\000\230\240\037\000'
  _EXCHANGERATETUPLE.fields_by_name['pair']._options = None
  _EXCHANGERATETUPLE.fields_by_name['pair']._serialized_options = b'\362\336\037\013yaml:\"pair\"'
  _EXCHANGERATETUPLE.fields_by_name['exchange_rate']._options = None
  _EXCHANGERATETUPLE.fields_by_name['exchange_rate']._serialized_options = b'\362\336\037\024yaml:\"exchange_rate\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _EXCHANGERATETUPLE._options = None
  _EXCHANGERATETUPLE._serialized_options = b'\350\240\037\000\210\240\037\000\230\240\037\000'
  _PAIRREWARD.fields_by_name['coins']._options = None
  _PAIRREWARD.fields_by_name['coins']._serialized_options = b'\310\336\037\000'
  _PARAMS._serialized_start=109
  _PARAMS._serialized_end=654
  _AGGREGATEEXCHANGERATEPREVOTE._serialized_start=657
  _AGGREGATEEXCHANGERATEPREVOTE._serialized_end=812
  _AGGREGATEEXCHANGERATEVOTE._serialized_start=815
  _AGGREGATEEXCHANGERATEVOTE._serialized_end=1021
  _EXCHANGERATETUPLE._serialized_start=1024
  _EXCHANGERATETUPLE._serialized_end=1183
  _PAIRREWARD._serialized_start=1185
  _PAIRREWARD._serialized_end=1293
# @@protoc_insertion_point(module_scope)
