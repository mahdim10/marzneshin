# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/dns/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_api.proto.common.net import destination_pb2 as common_dot_net_dot_destination__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16proxy/dns/config.proto\x12\x0exray.proxy.dns\x1a\x1c\x63ommon/net/destination.proto\"]\n\x06\x43onfig\x12)\n\x06server\x18\x01 \x01(\x0b\x32\x19.xray.common.net.Endpoint\x12\x12\n\nuser_level\x18\x02 \x01(\r\x12\x14\n\x0cnon_IP_query\x18\x03 \x01(\tBL\n\x12\x63om.xray.proxy.dnsP\x01Z#github.com/xtls/xray-core/proxy/dns\xaa\x02\x0eXray.Proxy.Dnsb\x06proto3')



_CONFIG = DESCRIPTOR.message_types_by_name['Config']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'proxy.dns.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.xray_api.proto.proxy.dns.Config)
  })
_sym_db.RegisterMessage(Config)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.xray.proxy.dnsP\001Z#github.com/xtls/xray-core/proxy/dns\252\002\016Xray.Proxy.Dns'
  _CONFIG._serialized_start=72
  _CONFIG._serialized_end=165
# @@protoc_insertion_point(module_scope)
