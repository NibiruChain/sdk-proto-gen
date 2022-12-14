# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stablecoin/query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from stablecoin import params_pb2 as stablecoin_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16stablecoin/query.proto\x12\x14nibiru.stablecoin.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x17stablecoin/params.proto\"\x14\n\x12QueryParamsRequest\"I\n\x13QueryParamsResponse\x12\x32\n\x06params\x18\x01 \x01(\x0b\x32\x1c.nibiru.stablecoin.v1.ParamsB\x04\xc8\xde\x1f\x00\"\x1c\n\x1aQueryModuleAccountBalances\"\xa2\x01\n\"QueryModuleAccountBalancesResponse\x12|\n\x17module_account_balances\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB@\xf2\xde\x1f\x0cyaml:\"coins\"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"\x1a\n\x18QueryCirculatingSupplies\"\x80\x01\n QueryCirculatingSuppliesResponse\x12-\n\x04nibi\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12-\n\x04nusd\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"K\n\x14QueryGovToMintStable\x12\x33\n\ncollateral\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"L\n\x1cQueryGovToMintStableResponse\x12,\n\x03gov\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\xe5\x01\n\x12LiquidityRatioInfo\x12G\n\x0fliquidity_ratio\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x42\n\nupper_band\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x42\n\nlower_band\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\" \n\x1eQueryLiquidityRatioInfoRequest\"_\n\x1fQueryLiquidityRatioInfoResponse\x12<\n\x04info\x18\x01 \x01(\x0b\x32(.nibiru.stablecoin.v1.LiquidityRatioInfoB\x04\xc8\xde\x1f\x00\x32\xa9\x05\n\x05Query\x12\x80\x01\n\x06Params\x12(.nibiru.stablecoin.v1.QueryParamsRequest\x1a).nibiru.stablecoin.v1.QueryParamsResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/nibiru/stablecoin/params\x12\xb6\x01\n\x15ModuleAccountBalances\x12\x30.nibiru.stablecoin.v1.QueryModuleAccountBalances\x1a\x38.nibiru.stablecoin.v1.QueryModuleAccountBalancesResponse\"1\x82\xd3\xe4\x93\x02+\x12)/nibiru/stablecoin/module_account_balance\x12\xae\x01\n\x13\x43irculatingSupplies\x12..nibiru.stablecoin.v1.QueryCirculatingSupplies\x1a\x36.nibiru.stablecoin.v1.QueryCirculatingSuppliesResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/nibiru/stablecoin/circulating_supplies\x12\xb2\x01\n\x12LiquidityRatioInfo\x12\x34.nibiru.stablecoin.v1.QueryLiquidityRatioInfoRequest\x1a\x35.nibiru.stablecoin.v1.QueryLiquidityRatioInfoResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/nibiru/stablecoin/liquidity_ratio_infoB2Z0github.com/NibiruChain/nibiru/x/stablecoin/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stablecoin.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0github.com/NibiruChain/nibiru/x/stablecoin/types'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERYMODULEACCOUNTBALANCESRESPONSE.fields_by_name['module_account_balances']._options = None
  _QUERYMODULEACCOUNTBALANCESRESPONSE.fields_by_name['module_account_balances']._serialized_options = b'\362\336\037\014yaml:\"coins\"\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _QUERYCIRCULATINGSUPPLIESRESPONSE.fields_by_name['nibi']._options = None
  _QUERYCIRCULATINGSUPPLIESRESPONSE.fields_by_name['nibi']._serialized_options = b'\310\336\037\000'
  _QUERYCIRCULATINGSUPPLIESRESPONSE.fields_by_name['nusd']._options = None
  _QUERYCIRCULATINGSUPPLIESRESPONSE.fields_by_name['nusd']._serialized_options = b'\310\336\037\000'
  _QUERYGOVTOMINTSTABLE.fields_by_name['collateral']._options = None
  _QUERYGOVTOMINTSTABLE.fields_by_name['collateral']._serialized_options = b'\310\336\037\000'
  _QUERYGOVTOMINTSTABLERESPONSE.fields_by_name['gov']._options = None
  _QUERYGOVTOMINTSTABLERESPONSE.fields_by_name['gov']._serialized_options = b'\310\336\037\000'
  _LIQUIDITYRATIOINFO.fields_by_name['liquidity_ratio']._options = None
  _LIQUIDITYRATIOINFO.fields_by_name['liquidity_ratio']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _LIQUIDITYRATIOINFO.fields_by_name['upper_band']._options = None
  _LIQUIDITYRATIOINFO.fields_by_name['upper_band']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _LIQUIDITYRATIOINFO.fields_by_name['lower_band']._options = None
  _LIQUIDITYRATIOINFO.fields_by_name['lower_band']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _QUERYLIQUIDITYRATIOINFORESPONSE.fields_by_name['info']._options = None
  _QUERYLIQUIDITYRATIOINFORESPONSE.fields_by_name['info']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\033\022\031/nibiru/stablecoin/params'
  _QUERY.methods_by_name['ModuleAccountBalances']._options = None
  _QUERY.methods_by_name['ModuleAccountBalances']._serialized_options = b'\202\323\344\223\002+\022)/nibiru/stablecoin/module_account_balance'
  _QUERY.methods_by_name['CirculatingSupplies']._options = None
  _QUERY.methods_by_name['CirculatingSupplies']._serialized_options = b'\202\323\344\223\002)\022\'/nibiru/stablecoin/circulating_supplies'
  _QUERY.methods_by_name['LiquidityRatioInfo']._options = None
  _QUERY.methods_by_name['LiquidityRatioInfo']._serialized_options = b'\202\323\344\223\002)\022\'/nibiru/stablecoin/liquidity_ratio_info'
  _QUERYPARAMSREQUEST._serialized_start=201
  _QUERYPARAMSREQUEST._serialized_end=221
  _QUERYPARAMSRESPONSE._serialized_start=223
  _QUERYPARAMSRESPONSE._serialized_end=296
  _QUERYMODULEACCOUNTBALANCES._serialized_start=298
  _QUERYMODULEACCOUNTBALANCES._serialized_end=326
  _QUERYMODULEACCOUNTBALANCESRESPONSE._serialized_start=329
  _QUERYMODULEACCOUNTBALANCESRESPONSE._serialized_end=491
  _QUERYCIRCULATINGSUPPLIES._serialized_start=493
  _QUERYCIRCULATINGSUPPLIES._serialized_end=519
  _QUERYCIRCULATINGSUPPLIESRESPONSE._serialized_start=522
  _QUERYCIRCULATINGSUPPLIESRESPONSE._serialized_end=650
  _QUERYGOVTOMINTSTABLE._serialized_start=652
  _QUERYGOVTOMINTSTABLE._serialized_end=727
  _QUERYGOVTOMINTSTABLERESPONSE._serialized_start=729
  _QUERYGOVTOMINTSTABLERESPONSE._serialized_end=805
  _LIQUIDITYRATIOINFO._serialized_start=808
  _LIQUIDITYRATIOINFO._serialized_end=1037
  _QUERYLIQUIDITYRATIOINFOREQUEST._serialized_start=1039
  _QUERYLIQUIDITYRATIOINFOREQUEST._serialized_end=1071
  _QUERYLIQUIDITYRATIOINFORESPONSE._serialized_start=1073
  _QUERYLIQUIDITYRATIOINFORESPONSE._serialized_end=1168
  _QUERY._serialized_start=1171
  _QUERY._serialized_end=1852
# @@protoc_insertion_point(module_scope)
