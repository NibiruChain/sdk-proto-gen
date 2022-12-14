# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: perp/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from perp.v1 import state_pb2 as perp_dot_v1_dot_state__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13perp/v1/query.proto\x12\x0enibiru.perp.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x13perp/v1/state.proto\"\x14\n\x12QueryParamsRequest\"C\n\x13QueryParamsResponse\x12,\n\x06params\x18\x01 \x01(\x0b\x32\x16.nibiru.perp.v1.ParamsB\x04\xc8\xde\x1f\x00\"\'\n\x15QueryPositionsRequest\x12\x0e\n\x06trader\x18\x01 \x01(\t\"R\n\x16QueryPositionsResponse\x12\x38\n\tpositions\x18\x01 \x03(\x0b\x32%.nibiru.perp.v1.QueryPositionResponse\":\n\x14QueryPositionRequest\x12\x12\n\ntoken_pair\x18\x01 \x01(\t\x12\x0e\n\x06trader\x18\x02 \x01(\t\"\x83\x03\n\x15QueryPositionResponse\x12*\n\x08position\x18\x01 \x01(\x0b\x32\x18.nibiru.perp.v1.Position\x12I\n\x11position_notional\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x46\n\x0eunrealized_pnl\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12I\n\x11margin_ratio_mark\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12J\n\x12margin_ratio_index\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x14\n\x0c\x62lock_number\x18\x07 \x01(\x03\"5\n%QueryCumulativePremiumFractionRequest\x12\x0c\n\x04pair\x18\x01 \x01(\t\"\xe1\x01\n&QueryCumulativePremiumFractionResponse\x12S\n\x1b\x63umulative_premium_fraction\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x62\n*estimated_next_cumulative_premium_fraction\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"#\n\x13QueryMetricsRequest\x12\x0c\n\x04pair\x18\x01 \x01(\t\"F\n\x14QueryMetricsResponse\x12.\n\x07metrics\x18\x01 \x01(\x0b\x32\x17.nibiru.perp.v1.MetricsB\x04\xc8\xde\x1f\x00\x32\xa8\x05\n\x05Query\x12n\n\x06Params\x12\".nibiru.perp.v1.QueryParamsRequest\x1a#.nibiru.perp.v1.QueryParamsResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/nibiru/perp/params\x12{\n\rQueryPosition\x12$.nibiru.perp.v1.QueryPositionRequest\x1a%.nibiru.perp.v1.QueryPositionResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/nibiru/perp/position\x12\x7f\n\x0eQueryPositions\x12%.nibiru.perp.v1.QueryPositionsRequest\x1a&.nibiru.perp.v1.QueryPositionsResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/nibiru/perp/positions\x12\xbc\x01\n\x19\x43umulativePremiumFraction\x12\x35.nibiru.perp.v1.QueryCumulativePremiumFractionRequest\x1a\x36.nibiru.perp.v1.QueryCumulativePremiumFractionResponse\"0\x82\xd3\xe4\x93\x02*\x12(/nibiru/perp/cumulative_premium_fraction\x12r\n\x07Metrics\x12#.nibiru.perp.v1.QueryMetricsRequest\x1a$.nibiru.perp.v1.QueryMetricsResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/nibiru/perp/metricsB,Z*github.com/NibiruChain/nibiru/x/perp/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'perp.v1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z*github.com/NibiruChain/nibiru/x/perp/types'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERYPOSITIONRESPONSE.fields_by_name['position_notional']._options = None
  _QUERYPOSITIONRESPONSE.fields_by_name['position_notional']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _QUERYPOSITIONRESPONSE.fields_by_name['unrealized_pnl']._options = None
  _QUERYPOSITIONRESPONSE.fields_by_name['unrealized_pnl']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _QUERYPOSITIONRESPONSE.fields_by_name['margin_ratio_mark']._options = None
  _QUERYPOSITIONRESPONSE.fields_by_name['margin_ratio_mark']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _QUERYPOSITIONRESPONSE.fields_by_name['margin_ratio_index']._options = None
  _QUERYPOSITIONRESPONSE.fields_by_name['margin_ratio_index']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _QUERYCUMULATIVEPREMIUMFRACTIONRESPONSE.fields_by_name['cumulative_premium_fraction']._options = None
  _QUERYCUMULATIVEPREMIUMFRACTIONRESPONSE.fields_by_name['cumulative_premium_fraction']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _QUERYCUMULATIVEPREMIUMFRACTIONRESPONSE.fields_by_name['estimated_next_cumulative_premium_fraction']._options = None
  _QUERYCUMULATIVEPREMIUMFRACTIONRESPONSE.fields_by_name['estimated_next_cumulative_premium_fraction']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _QUERYMETRICSRESPONSE.fields_by_name['metrics']._options = None
  _QUERYMETRICSRESPONSE.fields_by_name['metrics']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\025\022\023/nibiru/perp/params'
  _QUERY.methods_by_name['QueryPosition']._options = None
  _QUERY.methods_by_name['QueryPosition']._serialized_options = b'\202\323\344\223\002\027\022\025/nibiru/perp/position'
  _QUERY.methods_by_name['QueryPositions']._options = None
  _QUERY.methods_by_name['QueryPositions']._serialized_options = b'\202\323\344\223\002\030\022\026/nibiru/perp/positions'
  _QUERY.methods_by_name['CumulativePremiumFraction']._options = None
  _QUERY.methods_by_name['CumulativePremiumFraction']._serialized_options = b'\202\323\344\223\002*\022(/nibiru/perp/cumulative_premium_fraction'
  _QUERY.methods_by_name['Metrics']._options = None
  _QUERY.methods_by_name['Metrics']._serialized_options = b'\202\323\344\223\002\026\022\024/nibiru/perp/metrics'
  _QUERYPARAMSREQUEST._serialized_start=112
  _QUERYPARAMSREQUEST._serialized_end=132
  _QUERYPARAMSRESPONSE._serialized_start=134
  _QUERYPARAMSRESPONSE._serialized_end=201
  _QUERYPOSITIONSREQUEST._serialized_start=203
  _QUERYPOSITIONSREQUEST._serialized_end=242
  _QUERYPOSITIONSRESPONSE._serialized_start=244
  _QUERYPOSITIONSRESPONSE._serialized_end=326
  _QUERYPOSITIONREQUEST._serialized_start=328
  _QUERYPOSITIONREQUEST._serialized_end=386
  _QUERYPOSITIONRESPONSE._serialized_start=389
  _QUERYPOSITIONRESPONSE._serialized_end=776
  _QUERYCUMULATIVEPREMIUMFRACTIONREQUEST._serialized_start=778
  _QUERYCUMULATIVEPREMIUMFRACTIONREQUEST._serialized_end=831
  _QUERYCUMULATIVEPREMIUMFRACTIONRESPONSE._serialized_start=834
  _QUERYCUMULATIVEPREMIUMFRACTIONRESPONSE._serialized_end=1059
  _QUERYMETRICSREQUEST._serialized_start=1061
  _QUERYMETRICSREQUEST._serialized_end=1096
  _QUERYMETRICSRESPONSE._serialized_start=1098
  _QUERYMETRICSRESPONSE._serialized_end=1168
  _QUERY._serialized_start=1171
  _QUERY._serialized_end=1851
# @@protoc_insertion_point(module_scope)
