# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: oracle/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from oracle.v1beta1 import oracle_pb2 as oracle_dot_v1beta1_dot_oracle__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1coracle/v1beta1/genesis.proto\x12\x15nibiru.oracle.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1boracle/v1beta1/oracle.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xbf\x04\n\x0cGenesisState\x12\x33\n\x06params\x18\x01 \x01(\x0b\x32\x1d.nibiru.oracle.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12I\n\x12\x66\x65\x65\x64\x65r_delegations\x18\x02 \x03(\x0b\x32\'.nibiru.oracle.v1beta1.FeederDelegationB\x04\xc8\xde\x1f\x00\x12\\\n\x0e\x65xchange_rates\x18\x03 \x03(\x0b\x32(.nibiru.oracle.v1beta1.ExchangeRateTupleB\x1a\xaa\xdf\x1f\x12\x45xchangeRateTuples\xc8\xde\x1f\x00\x12?\n\rmiss_counters\x18\x04 \x03(\x0b\x32\".nibiru.oracle.v1beta1.MissCounterB\x04\xc8\xde\x1f\x00\x12\x63\n aggregate_exchange_rate_prevotes\x18\x05 \x03(\x0b\x32\x33.nibiru.oracle.v1beta1.AggregateExchangeRatePrevoteB\x04\xc8\xde\x1f\x00\x12]\n\x1d\x61ggregate_exchange_rate_votes\x18\x06 \x03(\x0b\x32\x30.nibiru.oracle.v1beta1.AggregateExchangeRateVoteB\x04\xc8\xde\x1f\x00\x12\r\n\x05pairs\x18\x07 \x03(\t\x12=\n\x0cpair_rewards\x18\x08 \x03(\x0b\x32!.nibiru.oracle.v1beta1.PairRewardB\x04\xc8\xde\x1f\x00\"E\n\x10\x46\x65\x65\x64\x65rDelegation\x12\x16\n\x0e\x66\x65\x65\x64\x65r_address\x18\x01 \x01(\t\x12\x19\n\x11validator_address\x18\x02 \x01(\t\">\n\x0bMissCounter\x12\x19\n\x11validator_address\x18\x01 \x01(\t\x12\x14\n\x0cmiss_counter\x18\x02 \x01(\x04\x42.Z,github.com/NibiruChain/nibiru/x/oracle/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'oracle.v1beta1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/NibiruChain/nibiru/x/oracle/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['feeder_delegations']._options = None
  _GENESISSTATE.fields_by_name['feeder_delegations']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['exchange_rates']._options = None
  _GENESISSTATE.fields_by_name['exchange_rates']._serialized_options = b'\252\337\037\022ExchangeRateTuples\310\336\037\000'
  _GENESISSTATE.fields_by_name['miss_counters']._options = None
  _GENESISSTATE.fields_by_name['miss_counters']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['aggregate_exchange_rate_prevotes']._options = None
  _GENESISSTATE.fields_by_name['aggregate_exchange_rate_prevotes']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['aggregate_exchange_rate_votes']._options = None
  _GENESISSTATE.fields_by_name['aggregate_exchange_rate_votes']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['pair_rewards']._options = None
  _GENESISSTATE.fields_by_name['pair_rewards']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE._serialized_start=139
  _GENESISSTATE._serialized_end=714
  _FEEDERDELEGATION._serialized_start=716
  _FEEDERDELEGATION._serialized_end=785
  _MISSCOUNTER._serialized_start=787
  _MISSCOUNTER._serialized_end=849
# @@protoc_insertion_point(module_scope)
