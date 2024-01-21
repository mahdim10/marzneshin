# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/proxyman/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_api.proto.common.net import address_pb2 as common_dot_net_dot_address__pb2
from xray_api.proto.common.net import port_pb2 as common_dot_net_dot_port__pb2
from xray_api.proto.transport.internet import config_pb2 as transport_dot_internet_dot_config__pb2
from xray_api.proto.common.serial import typed_message_pb2 as common_dot_serial_dot_typed__message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61pp/proxyman/config.proto\x12\x11xray.app.proxyman\x1a\x18\x63ommon/net/address.proto\x1a\x15\x63ommon/net/port.proto\x1a\x1ftransport/internet/config.proto\x1a!common/serial/typed_message.proto\"\x0f\n\rInboundConfig\"\x84\x03\n\x12\x41llocationStrategy\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32*.xray.app.proxyman.AllocationStrategy.Type\x12X\n\x0b\x63oncurrency\x18\x02 \x01(\x0b\x32\x43.xray.app.proxyman.AllocationStrategy.AllocationStrategyConcurrency\x12P\n\x07refresh\x18\x03 \x01(\x0b\x32?.xray.app.proxyman.AllocationStrategy.AllocationStrategyRefresh\x1a.\n\x1d\x41llocationStrategyConcurrency\x12\r\n\x05value\x18\x01 \x01(\r\x1a*\n\x19\x41llocationStrategyRefresh\x12\r\n\x05value\x18\x01 \x01(\r\",\n\x04Type\x12\n\n\x06\x41lways\x10\x00\x12\n\n\x06Random\x10\x01\x12\x0c\n\x08\x45xternal\x10\x02\"\x84\x01\n\x0eSniffingConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x1c\n\x14\x64\x65stination_override\x18\x02 \x03(\t\x12\x18\n\x10\x64omains_excluded\x18\x03 \x03(\t\x12\x15\n\rmetadata_only\x18\x04 \x01(\x08\x12\x12\n\nroute_only\x18\x05 \x01(\x08\"\x99\x03\n\x0eReceiverConfig\x12,\n\tport_list\x18\x01 \x01(\x0b\x32\x19.xray.common.net.PortList\x12+\n\x06listen\x18\x02 \x01(\x0b\x32\x1b.xray.common.net.IPOrDomain\x12\x42\n\x13\x61llocation_strategy\x18\x03 \x01(\x0b\x32%.xray.app.proxyman.AllocationStrategy\x12>\n\x0fstream_settings\x18\x04 \x01(\x0b\x32%.xray.transport.internet.StreamConfig\x12$\n\x1creceive_original_destination\x18\x05 \x01(\x08\x12>\n\x0f\x64omain_override\x18\x07 \x03(\x0e\x32!.xray.app.proxyman.KnownProtocolsB\x02\x18\x01\x12<\n\x11sniffing_settings\x18\x08 \x01(\x0b\x32!.xray.app.proxyman.SniffingConfigJ\x04\x08\x06\x10\x07\"\x9a\x01\n\x14InboundHandlerConfig\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12;\n\x11receiver_settings\x18\x02 \x01(\x0b\x32 .xray.common.serial.TypedMessage\x12\x38\n\x0eproxy_settings\x18\x03 \x01(\x0b\x32 .xray.common.serial.TypedMessage\"\x10\n\x0eOutboundConfig\"\xf9\x01\n\x0cSenderConfig\x12(\n\x03via\x18\x01 \x01(\x0b\x32\x1b.xray.common.net.IPOrDomain\x12>\n\x0fstream_settings\x18\x02 \x01(\x0b\x32%.xray.transport.internet.StreamConfig\x12<\n\x0eproxy_settings\x18\x03 \x01(\x0b\x32$.xray.transport.internet.ProxyConfig\x12\x41\n\x12multiplex_settings\x18\x04 \x01(\x0b\x32%.xray.app.proxyman.MultiplexingConfig\"l\n\x12MultiplexingConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x13\n\x0b\x63oncurrency\x18\x02 \x01(\x05\x12\x17\n\x0fxudpConcurrency\x18\x03 \x01(\x05\x12\x17\n\x0fxudpProxyUDP443\x18\x04 \x01(\t*#\n\x0eKnownProtocols\x12\x08\n\x04HTTP\x10\x00\x12\x07\n\x03TLS\x10\x01\x42U\n\x15\x63om.xray.app.proxymanP\x01Z&github.com/xtls/xray-core/app/proxyman\xaa\x02\x11Xray.App.Proxymanb\x06proto3')

_KNOWNPROTOCOLS = DESCRIPTOR.enum_types_by_name['KnownProtocols']
KnownProtocols = enum_type_wrapper.EnumTypeWrapper(_KNOWNPROTOCOLS)
HTTP = 0
TLS = 1


_INBOUNDCONFIG = DESCRIPTOR.message_types_by_name['InboundConfig']
_ALLOCATIONSTRATEGY = DESCRIPTOR.message_types_by_name['AllocationStrategy']
_ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYCONCURRENCY = _ALLOCATIONSTRATEGY.nested_types_by_name['AllocationStrategyConcurrency']
_ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYREFRESH = _ALLOCATIONSTRATEGY.nested_types_by_name['AllocationStrategyRefresh']
_SNIFFINGCONFIG = DESCRIPTOR.message_types_by_name['SniffingConfig']
_RECEIVERCONFIG = DESCRIPTOR.message_types_by_name['ReceiverConfig']
_INBOUNDHANDLERCONFIG = DESCRIPTOR.message_types_by_name['InboundHandlerConfig']
_OUTBOUNDCONFIG = DESCRIPTOR.message_types_by_name['OutboundConfig']
_SENDERCONFIG = DESCRIPTOR.message_types_by_name['SenderConfig']
_MULTIPLEXINGCONFIG = DESCRIPTOR.message_types_by_name['MultiplexingConfig']
_ALLOCATIONSTRATEGY_TYPE = _ALLOCATIONSTRATEGY.enum_types_by_name['Type']
InboundConfig = _reflection.GeneratedProtocolMessageType('InboundConfig', (_message.Message,), {
  'DESCRIPTOR' : _INBOUNDCONFIG,
  '__module__' : 'app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.xray_api.proto.app.proxyman.InboundConfig)
  })
_sym_db.RegisterMessage(InboundConfig)

AllocationStrategy = _reflection.GeneratedProtocolMessageType('AllocationStrategy', (_message.Message,), {

  'AllocationStrategyConcurrency' : _reflection.GeneratedProtocolMessageType('AllocationStrategyConcurrency', (_message.Message,), {
    'DESCRIPTOR' : _ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYCONCURRENCY,
    '__module__' : 'app.proxyman.config_pb2'
    # @@protoc_insertion_point(class_scope:xray.xray_api.proto.app.proxyman.AllocationStrategy.AllocationStrategyConcurrency)
    })
  ,

  'AllocationStrategyRefresh' : _reflection.GeneratedProtocolMessageType('AllocationStrategyRefresh', (_message.Message,), {
    'DESCRIPTOR' : _ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYREFRESH,
    '__module__' : 'app.proxyman.config_pb2'
    # @@protoc_insertion_point(class_scope:xray.xray_api.proto.app.proxyman.AllocationStrategy.AllocationStrategyRefresh)
    })
  ,
  'DESCRIPTOR' : _ALLOCATIONSTRATEGY,
  '__module__' : 'app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.xray_api.proto.app.proxyman.AllocationStrategy)
  })
_sym_db.RegisterMessage(AllocationStrategy)
_sym_db.RegisterMessage(AllocationStrategy.AllocationStrategyConcurrency)
_sym_db.RegisterMessage(AllocationStrategy.AllocationStrategyRefresh)

SniffingConfig = _reflection.GeneratedProtocolMessageType('SniffingConfig', (_message.Message,), {
  'DESCRIPTOR' : _SNIFFINGCONFIG,
  '__module__' : 'app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.xray_api.proto.app.proxyman.SniffingConfig)
  })
_sym_db.RegisterMessage(SniffingConfig)

ReceiverConfig = _reflection.GeneratedProtocolMessageType('ReceiverConfig', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVERCONFIG,
  '__module__' : 'app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.xray_api.proto.app.proxyman.ReceiverConfig)
  })
_sym_db.RegisterMessage(ReceiverConfig)

InboundHandlerConfig = _reflection.GeneratedProtocolMessageType('InboundHandlerConfig', (_message.Message,), {
  'DESCRIPTOR' : _INBOUNDHANDLERCONFIG,
  '__module__' : 'app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.xray_api.proto.app.proxyman.InboundHandlerConfig)
  })
_sym_db.RegisterMessage(InboundHandlerConfig)

OutboundConfig = _reflection.GeneratedProtocolMessageType('OutboundConfig', (_message.Message,), {
  'DESCRIPTOR' : _OUTBOUNDCONFIG,
  '__module__' : 'app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.xray_api.proto.app.proxyman.OutboundConfig)
  })
_sym_db.RegisterMessage(OutboundConfig)

SenderConfig = _reflection.GeneratedProtocolMessageType('SenderConfig', (_message.Message,), {
  'DESCRIPTOR' : _SENDERCONFIG,
  '__module__' : 'app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.xray_api.proto.app.proxyman.SenderConfig)
  })
_sym_db.RegisterMessage(SenderConfig)

MultiplexingConfig = _reflection.GeneratedProtocolMessageType('MultiplexingConfig', (_message.Message,), {
  'DESCRIPTOR' : _MULTIPLEXINGCONFIG,
  '__module__' : 'app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.xray_api.proto.app.proxyman.MultiplexingConfig)
  })
_sym_db.RegisterMessage(MultiplexingConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025com.xray.app.proxymanP\001Z&github.com/xtls/xray-core/app/proxyman\252\002\021Xray.App.Proxyman'
  _RECEIVERCONFIG.fields_by_name['domain_override']._options = None
  _RECEIVERCONFIG.fields_by_name['domain_override']._serialized_options = b'\030\001'
  _KNOWNPROTOCOLS._serialized_start=1657
  _KNOWNPROTOCOLS._serialized_end=1692
  _INBOUNDCONFIG._serialized_start=165
  _INBOUNDCONFIG._serialized_end=180
  _ALLOCATIONSTRATEGY._serialized_start=183
  _ALLOCATIONSTRATEGY._serialized_end=571
  _ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYCONCURRENCY._serialized_start=435
  _ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYCONCURRENCY._serialized_end=481
  _ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYREFRESH._serialized_start=483
  _ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYREFRESH._serialized_end=525
  _ALLOCATIONSTRATEGY_TYPE._serialized_start=527
  _ALLOCATIONSTRATEGY_TYPE._serialized_end=571
  _SNIFFINGCONFIG._serialized_start=574
  _SNIFFINGCONFIG._serialized_end=706
  _RECEIVERCONFIG._serialized_start=709
  _RECEIVERCONFIG._serialized_end=1118
  _INBOUNDHANDLERCONFIG._serialized_start=1121
  _INBOUNDHANDLERCONFIG._serialized_end=1275
  _OUTBOUNDCONFIG._serialized_start=1277
  _OUTBOUNDCONFIG._serialized_end=1293
  _SENDERCONFIG._serialized_start=1296
  _SENDERCONFIG._serialized_end=1545
  _MULTIPLEXINGCONFIG._serialized_start=1547
  _MULTIPLEXINGCONFIG._serialized_end=1655
# @@protoc_insertion_point(module_scope)
