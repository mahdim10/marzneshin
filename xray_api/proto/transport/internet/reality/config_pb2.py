# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/reality/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'transport/internet/reality/config.proto\x12\x1fxray.transport.internet.reality\"\xb9\x02\n\x06\x43onfig\x12\x0c\n\x04show\x18\x01 \x01(\x08\x12\x0c\n\x04\x64\x65st\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0c\n\x04xver\x18\x04 \x01(\x04\x12\x14\n\x0cserver_names\x18\x05 \x03(\t\x12\x13\n\x0bprivate_key\x18\x06 \x01(\x0c\x12\x16\n\x0emin_client_ver\x18\x07 \x01(\x0c\x12\x16\n\x0emax_client_ver\x18\x08 \x01(\x0c\x12\x15\n\rmax_time_diff\x18\t \x01(\x04\x12\x11\n\tshort_ids\x18\n \x03(\x0c\x12\x13\n\x0b\x46ingerprint\x18\x15 \x01(\t\x12\x13\n\x0bserver_name\x18\x16 \x01(\t\x12\x12\n\npublic_key\x18\x17 \x01(\x0c\x12\x10\n\x08short_id\x18\x18 \x01(\x0c\x12\x10\n\x08spider_x\x18\x19 \x01(\t\x12\x10\n\x08spider_y\x18\x1a \x03(\x03\x42\x7f\n#com.xray.transport.internet.realityP\x01Z4github.com/xtls/xray-core/transport/internet/reality\xaa\x02\x1fXray.Transport.Internet.Realityb\x06proto3')



_CONFIG = DESCRIPTOR.message_types_by_name['Config']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'transport.internet.reality.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.xray_api.proto.transport.internet.reality.Config)
  })
_sym_db.RegisterMessage(Config)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.xray.transport.internet.realityP\001Z4github.com/xtls/xray-core/transport/internet/reality\252\002\037Xray.Transport.Internet.Reality'
  _CONFIG._serialized_start=77
  _CONFIG._serialized_end=390
# @@protoc_insertion_point(module_scope)
