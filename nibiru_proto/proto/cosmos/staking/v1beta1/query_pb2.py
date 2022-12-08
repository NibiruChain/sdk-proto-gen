# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/staking/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"cosmos/staking/v1beta1/query.proto\x12\x16\x63osmos.staking.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a$cosmos/staking/v1beta1/staking.proto\"d\n\x16QueryValidatorsRequest\x12\x0e\n\x06status\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x93\x01\n\x17QueryValidatorsResponse\x12;\n\nvalidators\x18\x01 \x03(\x0b\x32!.cosmos.staking.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"/\n\x15QueryValidatorRequest\x12\x16\n\x0evalidator_addr\x18\x01 \x01(\t\"T\n\x16QueryValidatorResponse\x12:\n\tvalidator\x18\x01 \x01(\x0b\x32!.cosmos.staking.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00\"v\n QueryValidatorDelegationsRequest\x12\x16\n\x0evalidator_addr\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xc7\x01\n!QueryValidatorDelegationsResponse\x12\x65\n\x14\x64\x65legation_responses\x18\x01 \x03(\x0b\x32*.cosmos.staking.v1beta1.DelegationResponseB\x1b\xc8\xde\x1f\x00\xaa\xdf\x1f\x13\x44\x65legationResponses\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x7f\n)QueryValidatorUnbondingDelegationsRequest\x12\x16\n\x0evalidator_addr\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xb9\x01\n*QueryValidatorUnbondingDelegationsResponse\x12N\n\x13unbonding_responses\x18\x01 \x03(\x0b\x32+.cosmos.staking.v1beta1.UnbondingDelegationB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"R\n\x16QueryDelegationRequest\x12\x16\n\x0e\x64\x65legator_addr\x18\x01 \x01(\t\x12\x16\n\x0evalidator_addr\x18\x02 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"b\n\x17QueryDelegationResponse\x12G\n\x13\x64\x65legation_response\x18\x01 \x01(\x0b\x32*.cosmos.staking.v1beta1.DelegationResponse\"[\n\x1fQueryUnbondingDelegationRequest\x12\x16\n\x0e\x64\x65legator_addr\x18\x01 \x01(\t\x12\x16\n\x0evalidator_addr\x18\x02 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"e\n QueryUnbondingDelegationResponse\x12\x41\n\x06unbond\x18\x01 \x01(\x0b\x32+.cosmos.staking.v1beta1.UnbondingDelegationB\x04\xc8\xde\x1f\x00\"\x80\x01\n QueryDelegatorDelegationsRequest\x12\x16\n\x0e\x64\x65legator_addr\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xb0\x01\n!QueryDelegatorDelegationsResponse\x12N\n\x14\x64\x65legation_responses\x18\x01 \x03(\x0b\x32*.cosmos.staking.v1beta1.DelegationResponseB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x89\x01\n)QueryDelegatorUnbondingDelegationsRequest\x12\x16\n\x0e\x64\x65legator_addr\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xb9\x01\n*QueryDelegatorUnbondingDelegationsResponse\x12N\n\x13unbonding_responses\x18\x01 \x03(\x0b\x32+.cosmos.staking.v1beta1.UnbondingDelegationB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\xb1\x01\n\x19QueryRedelegationsRequest\x12\x16\n\x0e\x64\x65legator_addr\x18\x01 \x01(\t\x12\x1a\n\x12src_validator_addr\x18\x02 \x01(\t\x12\x1a\n\x12\x64st_validator_addr\x18\x03 \x01(\t\x12:\n\npagination\x18\x04 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xad\x01\n\x1aQueryRedelegationsResponse\x12R\n\x16redelegation_responses\x18\x01 \x03(\x0b\x32,.cosmos.staking.v1beta1.RedelegationResponseB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x7f\n\x1fQueryDelegatorValidatorsRequest\x12\x16\n\x0e\x64\x65legator_addr\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x9c\x01\n QueryDelegatorValidatorsResponse\x12;\n\nvalidators\x18\x01 \x03(\x0b\x32!.cosmos.staking.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"Z\n\x1eQueryDelegatorValidatorRequest\x12\x16\n\x0e\x64\x65legator_addr\x18\x01 \x01(\t\x12\x16\n\x0evalidator_addr\x18\x02 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"]\n\x1fQueryDelegatorValidatorResponse\x12:\n\tvalidator\x18\x01 \x01(\x0b\x32!.cosmos.staking.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00\",\n\x1aQueryHistoricalInfoRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03\"S\n\x1bQueryHistoricalInfoResponse\x12\x34\n\x04hist\x18\x01 \x01(\x0b\x32&.cosmos.staking.v1beta1.HistoricalInfo\"\x12\n\x10QueryPoolRequest\"E\n\x11QueryPoolResponse\x12\x30\n\x04pool\x18\x01 \x01(\x0b\x32\x1c.cosmos.staking.v1beta1.PoolB\x04\xc8\xde\x1f\x00\"\x14\n\x12QueryParamsRequest\"K\n\x13QueryParamsResponse\x12\x34\n\x06params\x18\x01 \x01(\x0b\x32\x1e.cosmos.staking.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x32\xea\x15\n\x05Query\x12\x99\x01\n\nValidators\x12..cosmos.staking.v1beta1.QueryValidatorsRequest\x1a/.cosmos.staking.v1beta1.QueryValidatorsResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/cosmos/staking/v1beta1/validators\x12\xa7\x01\n\tValidator\x12-.cosmos.staking.v1beta1.QueryValidatorRequest\x1a..cosmos.staking.v1beta1.QueryValidatorResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/cosmos/staking/v1beta1/validators/{validator_addr}\x12\xd4\x01\n\x14ValidatorDelegations\x12\x38.cosmos.staking.v1beta1.QueryValidatorDelegationsRequest\x1a\x39.cosmos.staking.v1beta1.QueryValidatorDelegationsResponse\"G\x82\xd3\xe4\x93\x02\x41\x12?/cosmos/staking/v1beta1/validators/{validator_addr}/delegations\x12\xf9\x01\n\x1dValidatorUnbondingDelegations\x12\x41.cosmos.staking.v1beta1.QueryValidatorUnbondingDelegationsRequest\x1a\x42.cosmos.staking.v1beta1.QueryValidatorUnbondingDelegationsResponse\"Q\x82\xd3\xe4\x93\x02K\x12I/cosmos/staking/v1beta1/validators/{validator_addr}/unbonding_delegations\x12\xc7\x01\n\nDelegation\x12..cosmos.staking.v1beta1.QueryDelegationRequest\x1a/.cosmos.staking.v1beta1.QueryDelegationResponse\"X\x82\xd3\xe4\x93\x02R\x12P/cosmos/staking/v1beta1/validators/{validator_addr}/delegations/{delegator_addr}\x12\xf7\x01\n\x13UnbondingDelegation\x12\x37.cosmos.staking.v1beta1.QueryUnbondingDelegationRequest\x1a\x38.cosmos.staking.v1beta1.QueryUnbondingDelegationResponse\"m\x82\xd3\xe4\x93\x02g\x12\x65/cosmos/staking/v1beta1/validators/{validator_addr}/delegations/{delegator_addr}/unbonding_delegation\x12\xc9\x01\n\x14\x44\x65legatorDelegations\x12\x38.cosmos.staking.v1beta1.QueryDelegatorDelegationsRequest\x1a\x39.cosmos.staking.v1beta1.QueryDelegatorDelegationsResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/cosmos/staking/v1beta1/delegations/{delegator_addr}\x12\xf9\x01\n\x1d\x44\x65legatorUnbondingDelegations\x12\x41.cosmos.staking.v1beta1.QueryDelegatorUnbondingDelegationsRequest\x1a\x42.cosmos.staking.v1beta1.QueryDelegatorUnbondingDelegationsResponse\"Q\x82\xd3\xe4\x93\x02K\x12I/cosmos/staking/v1beta1/delegators/{delegator_addr}/unbonding_delegations\x12\xc1\x01\n\rRedelegations\x12\x31.cosmos.staking.v1beta1.QueryRedelegationsRequest\x1a\x32.cosmos.staking.v1beta1.QueryRedelegationsResponse\"I\x82\xd3\xe4\x93\x02\x43\x12\x41/cosmos/staking/v1beta1/delegators/{delegator_addr}/redelegations\x12\xd0\x01\n\x13\x44\x65legatorValidators\x12\x37.cosmos.staking.v1beta1.QueryDelegatorValidatorsRequest\x1a\x38.cosmos.staking.v1beta1.QueryDelegatorValidatorsResponse\"F\x82\xd3\xe4\x93\x02@\x12>/cosmos/staking/v1beta1/delegators/{delegator_addr}/validators\x12\xde\x01\n\x12\x44\x65legatorValidator\x12\x36.cosmos.staking.v1beta1.QueryDelegatorValidatorRequest\x1a\x37.cosmos.staking.v1beta1.QueryDelegatorValidatorResponse\"W\x82\xd3\xe4\x93\x02Q\x12O/cosmos/staking/v1beta1/delegators/{delegator_addr}/validators/{validator_addr}\x12\xb3\x01\n\x0eHistoricalInfo\x12\x32.cosmos.staking.v1beta1.QueryHistoricalInfoRequest\x1a\x33.cosmos.staking.v1beta1.QueryHistoricalInfoResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/cosmos/staking/v1beta1/historical_info/{height}\x12\x81\x01\n\x04Pool\x12(.cosmos.staking.v1beta1.QueryPoolRequest\x1a).cosmos.staking.v1beta1.QueryPoolResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/cosmos/staking/v1beta1/pool\x12\x89\x01\n\x06Params\x12*.cosmos.staking.v1beta1.QueryParamsRequest\x1a+.cosmos.staking.v1beta1.QueryParamsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/cosmos/staking/v1beta1/paramsB.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.staking.v1beta1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
  _QUERYVALIDATORSRESPONSE.fields_by_name['validators']._options = None
  _QUERYVALIDATORSRESPONSE.fields_by_name['validators']._serialized_options = b'\310\336\037\000'
  _QUERYVALIDATORRESPONSE.fields_by_name['validator']._options = None
  _QUERYVALIDATORRESPONSE.fields_by_name['validator']._serialized_options = b'\310\336\037\000'
  _QUERYVALIDATORDELEGATIONSRESPONSE.fields_by_name['delegation_responses']._options = None
  _QUERYVALIDATORDELEGATIONSRESPONSE.fields_by_name['delegation_responses']._serialized_options = b'\310\336\037\000\252\337\037\023DelegationResponses'
  _QUERYVALIDATORUNBONDINGDELEGATIONSRESPONSE.fields_by_name['unbonding_responses']._options = None
  _QUERYVALIDATORUNBONDINGDELEGATIONSRESPONSE.fields_by_name['unbonding_responses']._serialized_options = b'\310\336\037\000'
  _QUERYDELEGATIONREQUEST._options = None
  _QUERYDELEGATIONREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYUNBONDINGDELEGATIONREQUEST._options = None
  _QUERYUNBONDINGDELEGATIONREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYUNBONDINGDELEGATIONRESPONSE.fields_by_name['unbond']._options = None
  _QUERYUNBONDINGDELEGATIONRESPONSE.fields_by_name['unbond']._serialized_options = b'\310\336\037\000'
  _QUERYDELEGATORDELEGATIONSREQUEST._options = None
  _QUERYDELEGATORDELEGATIONSREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYDELEGATORDELEGATIONSRESPONSE.fields_by_name['delegation_responses']._options = None
  _QUERYDELEGATORDELEGATIONSRESPONSE.fields_by_name['delegation_responses']._serialized_options = b'\310\336\037\000'
  _QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST._options = None
  _QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYDELEGATORUNBONDINGDELEGATIONSRESPONSE.fields_by_name['unbonding_responses']._options = None
  _QUERYDELEGATORUNBONDINGDELEGATIONSRESPONSE.fields_by_name['unbonding_responses']._serialized_options = b'\310\336\037\000'
  _QUERYREDELEGATIONSREQUEST._options = None
  _QUERYREDELEGATIONSREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYREDELEGATIONSRESPONSE.fields_by_name['redelegation_responses']._options = None
  _QUERYREDELEGATIONSRESPONSE.fields_by_name['redelegation_responses']._serialized_options = b'\310\336\037\000'
  _QUERYDELEGATORVALIDATORSREQUEST._options = None
  _QUERYDELEGATORVALIDATORSREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYDELEGATORVALIDATORSRESPONSE.fields_by_name['validators']._options = None
  _QUERYDELEGATORVALIDATORSRESPONSE.fields_by_name['validators']._serialized_options = b'\310\336\037\000'
  _QUERYDELEGATORVALIDATORREQUEST._options = None
  _QUERYDELEGATORVALIDATORREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYDELEGATORVALIDATORRESPONSE.fields_by_name['validator']._options = None
  _QUERYDELEGATORVALIDATORRESPONSE.fields_by_name['validator']._serialized_options = b'\310\336\037\000'
  _QUERYPOOLRESPONSE.fields_by_name['pool']._options = None
  _QUERYPOOLRESPONSE.fields_by_name['pool']._serialized_options = b'\310\336\037\000'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['Validators']._options = None
  _QUERY.methods_by_name['Validators']._serialized_options = b'\202\323\344\223\002$\022\"/cosmos/staking/v1beta1/validators'
  _QUERY.methods_by_name['Validator']._options = None
  _QUERY.methods_by_name['Validator']._serialized_options = b'\202\323\344\223\0025\0223/cosmos/staking/v1beta1/validators/{validator_addr}'
  _QUERY.methods_by_name['ValidatorDelegations']._options = None
  _QUERY.methods_by_name['ValidatorDelegations']._serialized_options = b'\202\323\344\223\002A\022?/cosmos/staking/v1beta1/validators/{validator_addr}/delegations'
  _QUERY.methods_by_name['ValidatorUnbondingDelegations']._options = None
  _QUERY.methods_by_name['ValidatorUnbondingDelegations']._serialized_options = b'\202\323\344\223\002K\022I/cosmos/staking/v1beta1/validators/{validator_addr}/unbonding_delegations'
  _QUERY.methods_by_name['Delegation']._options = None
  _QUERY.methods_by_name['Delegation']._serialized_options = b'\202\323\344\223\002R\022P/cosmos/staking/v1beta1/validators/{validator_addr}/delegations/{delegator_addr}'
  _QUERY.methods_by_name['UnbondingDelegation']._options = None
  _QUERY.methods_by_name['UnbondingDelegation']._serialized_options = b'\202\323\344\223\002g\022e/cosmos/staking/v1beta1/validators/{validator_addr}/delegations/{delegator_addr}/unbonding_delegation'
  _QUERY.methods_by_name['DelegatorDelegations']._options = None
  _QUERY.methods_by_name['DelegatorDelegations']._serialized_options = b'\202\323\344\223\0026\0224/cosmos/staking/v1beta1/delegations/{delegator_addr}'
  _QUERY.methods_by_name['DelegatorUnbondingDelegations']._options = None
  _QUERY.methods_by_name['DelegatorUnbondingDelegations']._serialized_options = b'\202\323\344\223\002K\022I/cosmos/staking/v1beta1/delegators/{delegator_addr}/unbonding_delegations'
  _QUERY.methods_by_name['Redelegations']._options = None
  _QUERY.methods_by_name['Redelegations']._serialized_options = b'\202\323\344\223\002C\022A/cosmos/staking/v1beta1/delegators/{delegator_addr}/redelegations'
  _QUERY.methods_by_name['DelegatorValidators']._options = None
  _QUERY.methods_by_name['DelegatorValidators']._serialized_options = b'\202\323\344\223\002@\022>/cosmos/staking/v1beta1/delegators/{delegator_addr}/validators'
  _QUERY.methods_by_name['DelegatorValidator']._options = None
  _QUERY.methods_by_name['DelegatorValidator']._serialized_options = b'\202\323\344\223\002Q\022O/cosmos/staking/v1beta1/delegators/{delegator_addr}/validators/{validator_addr}'
  _QUERY.methods_by_name['HistoricalInfo']._options = None
  _QUERY.methods_by_name['HistoricalInfo']._serialized_options = b'\202\323\344\223\0022\0220/cosmos/staking/v1beta1/historical_info/{height}'
  _QUERY.methods_by_name['Pool']._options = None
  _QUERY.methods_by_name['Pool']._serialized_options = b'\202\323\344\223\002\036\022\034/cosmos/staking/v1beta1/pool'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002 \022\036/cosmos/staking/v1beta1/params'
  _QUERYVALIDATORSREQUEST._serialized_start=196
  _QUERYVALIDATORSREQUEST._serialized_end=296
  _QUERYVALIDATORSRESPONSE._serialized_start=299
  _QUERYVALIDATORSRESPONSE._serialized_end=446
  _QUERYVALIDATORREQUEST._serialized_start=448
  _QUERYVALIDATORREQUEST._serialized_end=495
  _QUERYVALIDATORRESPONSE._serialized_start=497
  _QUERYVALIDATORRESPONSE._serialized_end=581
  _QUERYVALIDATORDELEGATIONSREQUEST._serialized_start=583
  _QUERYVALIDATORDELEGATIONSREQUEST._serialized_end=701
  _QUERYVALIDATORDELEGATIONSRESPONSE._serialized_start=704
  _QUERYVALIDATORDELEGATIONSRESPONSE._serialized_end=903
  _QUERYVALIDATORUNBONDINGDELEGATIONSREQUEST._serialized_start=905
  _QUERYVALIDATORUNBONDINGDELEGATIONSREQUEST._serialized_end=1032
  _QUERYVALIDATORUNBONDINGDELEGATIONSRESPONSE._serialized_start=1035
  _QUERYVALIDATORUNBONDINGDELEGATIONSRESPONSE._serialized_end=1220
  _QUERYDELEGATIONREQUEST._serialized_start=1222
  _QUERYDELEGATIONREQUEST._serialized_end=1304
  _QUERYDELEGATIONRESPONSE._serialized_start=1306
  _QUERYDELEGATIONRESPONSE._serialized_end=1404
  _QUERYUNBONDINGDELEGATIONREQUEST._serialized_start=1406
  _QUERYUNBONDINGDELEGATIONREQUEST._serialized_end=1497
  _QUERYUNBONDINGDELEGATIONRESPONSE._serialized_start=1499
  _QUERYUNBONDINGDELEGATIONRESPONSE._serialized_end=1600
  _QUERYDELEGATORDELEGATIONSREQUEST._serialized_start=1603
  _QUERYDELEGATORDELEGATIONSREQUEST._serialized_end=1731
  _QUERYDELEGATORDELEGATIONSRESPONSE._serialized_start=1734
  _QUERYDELEGATORDELEGATIONSRESPONSE._serialized_end=1910
  _QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST._serialized_start=1913
  _QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST._serialized_end=2050
  _QUERYDELEGATORUNBONDINGDELEGATIONSRESPONSE._serialized_start=2053
  _QUERYDELEGATORUNBONDINGDELEGATIONSRESPONSE._serialized_end=2238
  _QUERYREDELEGATIONSREQUEST._serialized_start=2241
  _QUERYREDELEGATIONSREQUEST._serialized_end=2418
  _QUERYREDELEGATIONSRESPONSE._serialized_start=2421
  _QUERYREDELEGATIONSRESPONSE._serialized_end=2594
  _QUERYDELEGATORVALIDATORSREQUEST._serialized_start=2596
  _QUERYDELEGATORVALIDATORSREQUEST._serialized_end=2723
  _QUERYDELEGATORVALIDATORSRESPONSE._serialized_start=2726
  _QUERYDELEGATORVALIDATORSRESPONSE._serialized_end=2882
  _QUERYDELEGATORVALIDATORREQUEST._serialized_start=2884
  _QUERYDELEGATORVALIDATORREQUEST._serialized_end=2974
  _QUERYDELEGATORVALIDATORRESPONSE._serialized_start=2976
  _QUERYDELEGATORVALIDATORRESPONSE._serialized_end=3069
  _QUERYHISTORICALINFOREQUEST._serialized_start=3071
  _QUERYHISTORICALINFOREQUEST._serialized_end=3115
  _QUERYHISTORICALINFORESPONSE._serialized_start=3117
  _QUERYHISTORICALINFORESPONSE._serialized_end=3200
  _QUERYPOOLREQUEST._serialized_start=3202
  _QUERYPOOLREQUEST._serialized_end=3220
  _QUERYPOOLRESPONSE._serialized_start=3222
  _QUERYPOOLRESPONSE._serialized_end=3291
  _QUERYPARAMSREQUEST._serialized_start=3293
  _QUERYPARAMSREQUEST._serialized_end=3313
  _QUERYPARAMSRESPONSE._serialized_start=3315
  _QUERYPARAMSRESPONSE._serialized_end=3390
  _QUERY._serialized_start=3393
  _QUERY._serialized_end=6187
# @@protoc_insertion_point(module_scope)
