# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: perp/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from perp.v1 import state_pb2 as perp_dot_v1_dot_state__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10perp/v1/tx.proto\x12\x0enibiru.perp.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x13perp/v1/state.proto\"f\n\x0fMsgRemoveMargin\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x12\n\ntoken_pair\x18\x02 \x01(\t\x12/\n\x06margin\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\xc3\x01\n\x17MsgRemoveMarginResponse\x12\x33\n\nmargin_out\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12G\n\x0f\x66unding_payment\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12*\n\x08position\x18\x03 \x01(\x0b\x32\x18.nibiru.perp.v1.Position\"c\n\x0cMsgAddMargin\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x12\n\ntoken_pair\x18\x02 \x01(\t\x12/\n\x06margin\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\x8b\x01\n\x14MsgAddMarginResponse\x12G\n\x0f\x66unding_payment\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12*\n\x08position\x18\x02 \x01(\x0b\x32\x18.nibiru.perp.v1.Position\"B\n\x0cMsgLiquidate\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x12\n\ntoken_pair\x18\x02 \x01(\t\x12\x0e\n\x06trader\x18\x03 \x01(\t\"\x97\x01\n\x14MsgLiquidateResponse\x12:\n\x11\x66\x65\x65_to_liquidator\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x43\n\x1a\x66\x65\x65_to_perp_ecosystem_fund\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\xa5\x01\n\x11MsgMultiLiquidate\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12H\n\x0cliquidations\x18\x02 \x03(\x0b\x32\x32.nibiru.perp.v1.MsgMultiLiquidate.MultiLiquidation\x1a\x36\n\x10MultiLiquidation\x12\x12\n\ntoken_pair\x18\x02 \x01(\t\x12\x0e\n\x06trader\x18\x03 \x01(\t\"\xf0\x01\n\x19MsgMultiLiquidateResponse\x12_\n\x15liquidation_responses\x18\x01 \x03(\x0b\x32@.nibiru.perp.v1.MsgMultiLiquidateResponse.MultiLiquidateResponse\x1ar\n\x16MultiLiquidateResponse\x12\x0f\n\x05\x65rror\x18\x01 \x01(\tH\x00\x12;\n\x0bliquidation\x18\x02 \x01(\x0b\x32$.nibiru.perp.v1.MsgLiquidateResponseH\x00\x42\n\n\x08response\"\xb8\x02\n\x0fMsgOpenPosition\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x12\n\ntoken_pair\x18\x02 \x01(\t\x12\"\n\x04side\x18\x03 \x01(\x0e\x32\x14.nibiru.perp.v1.Side\x12J\n\x12quote_asset_amount\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12@\n\x08leverage\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12O\n\x17\x62\x61se_asset_amount_limit\x18\x06 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\"\xd9\x04\n\x17MsgOpenPositionResponse\x12*\n\x08position\x18\x01 \x01(\x0b\x32\x18.nibiru.perp.v1.Position\x12P\n\x18\x65xchanged_notional_value\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12O\n\x17\x65xchanged_position_size\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12G\n\x0f\x66unding_payment\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x44\n\x0crealized_pnl\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12L\n\x14unrealized_pnl_after\x18\x06 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12G\n\x0fmargin_to_vault\x18\x07 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12I\n\x11position_notional\x18\x08 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"6\n\x10MsgClosePosition\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x12\n\ntoken_pair\x18\x02 \x01(\t\"\x96\x03\n\x18MsgClosePositionResponse\x12P\n\x18\x65xchanged_notional_value\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12O\n\x17\x65xchanged_position_size\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12G\n\x0f\x66unding_payment\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x44\n\x0crealized_pnl\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12H\n\x10margin_to_trader\x18\x07 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"p\n\x18MsgDonateToEcosystemFund\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x44\n\x08\x64onation\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x17\xf2\xde\x1f\x0fyaml:\"donation\"\xc8\xde\x1f\x00\"\"\n MsgDonateToEcosystemFundResponse2\x92\x07\n\x03Msg\x12|\n\x0cRemoveMargin\x12\x1f.nibiru.perp.v1.MsgRemoveMargin\x1a\'.nibiru.perp.v1.MsgRemoveMarginResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x1a/nibiru/perp/remove_margin\x12p\n\tAddMargin\x12\x1c.nibiru.perp.v1.MsgAddMargin\x1a$.nibiru.perp.v1.MsgAddMarginResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x17/nibiru/perp/add_margin\x12o\n\tLiquidate\x12\x1c.nibiru.perp.v1.MsgLiquidate\x1a$.nibiru.perp.v1.MsgLiquidateResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x16/nibiru/perp/liquidate\x12\x83\x01\n\x0eMultiLiquidate\x12!.nibiru.perp.v1.MsgMultiLiquidate\x1a).nibiru.perp.v1.MsgMultiLiquidateResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x1b/nibiru/perp/multiliquidate\x12|\n\x0cOpenPosition\x12\x1f.nibiru.perp.v1.MsgOpenPosition\x1a\'.nibiru.perp.v1.MsgOpenPositionResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x1a/nibiru/perp/open_position\x12\x80\x01\n\rClosePosition\x12 .nibiru.perp.v1.MsgClosePosition\x1a(.nibiru.perp.v1.MsgClosePositionResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x1b/nibiru/perp/close_position\x12\xa2\x01\n\x15\x44onateToEcosystemFund\x12(.nibiru.perp.v1.MsgDonateToEcosystemFund\x1a\x30.nibiru.perp.v1.MsgDonateToEcosystemFundResponse\"-\x82\xd3\xe4\x93\x02\'\"%/nibiru/perp/donate_to_ecosystem_fundB,Z*github.com/NibiruChain/nibiru/x/perp/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'perp.v1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z*github.com/NibiruChain/nibiru/x/perp/types'
  _MSGREMOVEMARGIN.fields_by_name['margin']._options = None
  _MSGREMOVEMARGIN.fields_by_name['margin']._serialized_options = b'\310\336\037\000'
  _MSGREMOVEMARGINRESPONSE.fields_by_name['margin_out']._options = None
  _MSGREMOVEMARGINRESPONSE.fields_by_name['margin_out']._serialized_options = b'\310\336\037\000'
  _MSGREMOVEMARGINRESPONSE.fields_by_name['funding_payment']._options = None
  _MSGREMOVEMARGINRESPONSE.fields_by_name['funding_payment']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGADDMARGIN.fields_by_name['margin']._options = None
  _MSGADDMARGIN.fields_by_name['margin']._serialized_options = b'\310\336\037\000'
  _MSGADDMARGINRESPONSE.fields_by_name['funding_payment']._options = None
  _MSGADDMARGINRESPONSE.fields_by_name['funding_payment']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGLIQUIDATERESPONSE.fields_by_name['fee_to_liquidator']._options = None
  _MSGLIQUIDATERESPONSE.fields_by_name['fee_to_liquidator']._serialized_options = b'\310\336\037\000'
  _MSGLIQUIDATERESPONSE.fields_by_name['fee_to_perp_ecosystem_fund']._options = None
  _MSGLIQUIDATERESPONSE.fields_by_name['fee_to_perp_ecosystem_fund']._serialized_options = b'\310\336\037\000'
  _MSGOPENPOSITION.fields_by_name['quote_asset_amount']._options = None
  _MSGOPENPOSITION.fields_by_name['quote_asset_amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _MSGOPENPOSITION.fields_by_name['leverage']._options = None
  _MSGOPENPOSITION.fields_by_name['leverage']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGOPENPOSITION.fields_by_name['base_asset_amount_limit']._options = None
  _MSGOPENPOSITION.fields_by_name['base_asset_amount_limit']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _MSGOPENPOSITIONRESPONSE.fields_by_name['exchanged_notional_value']._options = None
  _MSGOPENPOSITIONRESPONSE.fields_by_name['exchanged_notional_value']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGOPENPOSITIONRESPONSE.fields_by_name['exchanged_position_size']._options = None
  _MSGOPENPOSITIONRESPONSE.fields_by_name['exchanged_position_size']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGOPENPOSITIONRESPONSE.fields_by_name['funding_payment']._options = None
  _MSGOPENPOSITIONRESPONSE.fields_by_name['funding_payment']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGOPENPOSITIONRESPONSE.fields_by_name['realized_pnl']._options = None
  _MSGOPENPOSITIONRESPONSE.fields_by_name['realized_pnl']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGOPENPOSITIONRESPONSE.fields_by_name['unrealized_pnl_after']._options = None
  _MSGOPENPOSITIONRESPONSE.fields_by_name['unrealized_pnl_after']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGOPENPOSITIONRESPONSE.fields_by_name['margin_to_vault']._options = None
  _MSGOPENPOSITIONRESPONSE.fields_by_name['margin_to_vault']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGOPENPOSITIONRESPONSE.fields_by_name['position_notional']._options = None
  _MSGOPENPOSITIONRESPONSE.fields_by_name['position_notional']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['exchanged_notional_value']._options = None
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['exchanged_notional_value']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['exchanged_position_size']._options = None
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['exchanged_position_size']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['funding_payment']._options = None
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['funding_payment']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['realized_pnl']._options = None
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['realized_pnl']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['margin_to_trader']._options = None
  _MSGCLOSEPOSITIONRESPONSE.fields_by_name['margin_to_trader']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGDONATETOECOSYSTEMFUND.fields_by_name['donation']._options = None
  _MSGDONATETOECOSYSTEMFUND.fields_by_name['donation']._serialized_options = b'\362\336\037\017yaml:\"donation\"\310\336\037\000'
  _MSG.methods_by_name['RemoveMargin']._options = None
  _MSG.methods_by_name['RemoveMargin']._serialized_options = b'\202\323\344\223\002\034\"\032/nibiru/perp/remove_margin'
  _MSG.methods_by_name['AddMargin']._options = None
  _MSG.methods_by_name['AddMargin']._serialized_options = b'\202\323\344\223\002\031\"\027/nibiru/perp/add_margin'
  _MSG.methods_by_name['Liquidate']._options = None
  _MSG.methods_by_name['Liquidate']._serialized_options = b'\202\323\344\223\002\030\"\026/nibiru/perp/liquidate'
  _MSG.methods_by_name['MultiLiquidate']._options = None
  _MSG.methods_by_name['MultiLiquidate']._serialized_options = b'\202\323\344\223\002\035\"\033/nibiru/perp/multiliquidate'
  _MSG.methods_by_name['OpenPosition']._options = None
  _MSG.methods_by_name['OpenPosition']._serialized_options = b'\202\323\344\223\002\034\"\032/nibiru/perp/open_position'
  _MSG.methods_by_name['ClosePosition']._options = None
  _MSG.methods_by_name['ClosePosition']._serialized_options = b'\202\323\344\223\002\035\"\033/nibiru/perp/close_position'
  _MSG.methods_by_name['DonateToEcosystemFund']._options = None
  _MSG.methods_by_name['DonateToEcosystemFund']._serialized_options = b'\202\323\344\223\002\'\"%/nibiru/perp/donate_to_ecosystem_fund'
  _MSGREMOVEMARGIN._serialized_start=141
  _MSGREMOVEMARGIN._serialized_end=243
  _MSGREMOVEMARGINRESPONSE._serialized_start=246
  _MSGREMOVEMARGINRESPONSE._serialized_end=441
  _MSGADDMARGIN._serialized_start=443
  _MSGADDMARGIN._serialized_end=542
  _MSGADDMARGINRESPONSE._serialized_start=545
  _MSGADDMARGINRESPONSE._serialized_end=684
  _MSGLIQUIDATE._serialized_start=686
  _MSGLIQUIDATE._serialized_end=752
  _MSGLIQUIDATERESPONSE._serialized_start=755
  _MSGLIQUIDATERESPONSE._serialized_end=906
  _MSGMULTILIQUIDATE._serialized_start=909
  _MSGMULTILIQUIDATE._serialized_end=1074
  _MSGMULTILIQUIDATE_MULTILIQUIDATION._serialized_start=1020
  _MSGMULTILIQUIDATE_MULTILIQUIDATION._serialized_end=1074
  _MSGMULTILIQUIDATERESPONSE._serialized_start=1077
  _MSGMULTILIQUIDATERESPONSE._serialized_end=1317
  _MSGMULTILIQUIDATERESPONSE_MULTILIQUIDATERESPONSE._serialized_start=1203
  _MSGMULTILIQUIDATERESPONSE_MULTILIQUIDATERESPONSE._serialized_end=1317
  _MSGOPENPOSITION._serialized_start=1320
  _MSGOPENPOSITION._serialized_end=1632
  _MSGOPENPOSITIONRESPONSE._serialized_start=1635
  _MSGOPENPOSITIONRESPONSE._serialized_end=2236
  _MSGCLOSEPOSITION._serialized_start=2238
  _MSGCLOSEPOSITION._serialized_end=2292
  _MSGCLOSEPOSITIONRESPONSE._serialized_start=2295
  _MSGCLOSEPOSITIONRESPONSE._serialized_end=2701
  _MSGDONATETOECOSYSTEMFUND._serialized_start=2703
  _MSGDONATETOECOSYSTEMFUND._serialized_end=2815
  _MSGDONATETOECOSYSTEMFUNDRESPONSE._serialized_start=2817
  _MSGDONATETOECOSYSTEMFUNDRESPONSE._serialized_end=2851
  _MSG._serialized_start=2854
  _MSG._serialized_end=3768
# @@protoc_insertion_point(module_scope)
