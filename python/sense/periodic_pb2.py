# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: periodic.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='periodic.proto',
  package='',
  serialized_pb=_b('\n\x0eperiodic.proto\"\x90\x03\n\rperiodic_data\x12\x11\n\tunix_time\x18\x01 \x01(\x05\x12\r\n\x05light\x18\x02 \x01(\x05\x12\x13\n\x0btemperature\x18\x03 \x01(\x05\x12\x10\n\x08humidity\x18\x04 \x01(\x05\x12\x0c\n\x04\x64ust\x18\x05 \x01(\x05\x12\x19\n\x11light_variability\x18\x08 \x01(\x05\x12\x16\n\x0elight_tonality\x18\t \x01(\x05\x12\x18\n\x10\x64ust_variability\x18\r \x01(\x05\x12\x10\n\x08\x64ust_max\x18\x0e \x01(\x05\x12\x10\n\x08\x64ust_min\x18\x0f \x01(\x05\x12\x12\n\nwave_count\x18\x10 \x01(\x05\x12\x12\n\nhold_count\x18\x11 \x01(\x05\x12\x1e\n\x16\x61udio_num_disturbances\x18\x12 \x01(\x05\x12(\n audio_peak_disturbance_energy_db\x18\x13 \x01(\x05\x12\'\n\x1f\x61udio_peak_background_energy_db\x18\x14 \x01(\x05\x12\x1c\n\x14\x61udio_peak_energy_db\x18\x15 \x01(\x05\"\x98\x03\n\x15\x62\x61tched_periodic_data\x12\x1c\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x0e.periodic_data\x12\x11\n\tdevice_id\x18\x02 \x02(\t\x12\x18\n\x10\x66irmware_version\x18\x03 \x02(\x05\x12\x18\n\x10uptime_in_second\x18\x04 \x01(\x05\x12\x16\n\x0e\x63onnected_ssid\x18\x07 \x01(\t\x12\x15\n\rring_time_ack\x18\t \x01(\t\x12\x36\n\x04scan\x18\n \x03(\x0b\x32(.batched_periodic_data.wifi_access_point\x12\x19\n\x11messages_in_queue\x18\x0b \x01(\x05\x1a\x97\x01\n\x11wifi_access_point\x12\x0c\n\x04ssid\x18\x01 \x01(\t\x12\x0c\n\x04rssi\x18\x02 \x01(\x05\x12\x45\n\x07\x61ntenna\x18\x03 \x01(\x0e\x32\x34.batched_periodic_data.wifi_access_point.AntennaType\"\x1f\n\x0b\x41ntennaType\x12\x07\n\x03IFA\x10\x01\x12\x07\n\x03PCB\x10\x02\x42-\n\x1a\x63om.hello.suripu.api.inputB\x0f\x44\x61taInputProtos')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_BATCHED_PERIODIC_DATA_WIFI_ACCESS_POINT_ANTENNATYPE = _descriptor.EnumDescriptor(
  name='AntennaType',
  full_name='batched_periodic_data.wifi_access_point.AntennaType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IFA', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PCB', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=799,
  serialized_end=830,
)
_sym_db.RegisterEnumDescriptor(_BATCHED_PERIODIC_DATA_WIFI_ACCESS_POINT_ANTENNATYPE)


_PERIODIC_DATA = _descriptor.Descriptor(
  name='periodic_data',
  full_name='periodic_data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unix_time', full_name='periodic_data.unix_time', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='light', full_name='periodic_data.light', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='periodic_data.temperature', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='humidity', full_name='periodic_data.humidity', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dust', full_name='periodic_data.dust', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='light_variability', full_name='periodic_data.light_variability', index=5,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='light_tonality', full_name='periodic_data.light_tonality', index=6,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dust_variability', full_name='periodic_data.dust_variability', index=7,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dust_max', full_name='periodic_data.dust_max', index=8,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dust_min', full_name='periodic_data.dust_min', index=9,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wave_count', full_name='periodic_data.wave_count', index=10,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hold_count', full_name='periodic_data.hold_count', index=11,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_num_disturbances', full_name='periodic_data.audio_num_disturbances', index=12,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_peak_disturbance_energy_db', full_name='periodic_data.audio_peak_disturbance_energy_db', index=13,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_peak_background_energy_db', full_name='periodic_data.audio_peak_background_energy_db', index=14,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_peak_energy_db', full_name='periodic_data.audio_peak_energy_db', index=15,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=419,
)


_BATCHED_PERIODIC_DATA_WIFI_ACCESS_POINT = _descriptor.Descriptor(
  name='wifi_access_point',
  full_name='batched_periodic_data.wifi_access_point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ssid', full_name='batched_periodic_data.wifi_access_point.ssid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='batched_periodic_data.wifi_access_point.rssi', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='antenna', full_name='batched_periodic_data.wifi_access_point.antenna', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BATCHED_PERIODIC_DATA_WIFI_ACCESS_POINT_ANTENNATYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=679,
  serialized_end=830,
)

_BATCHED_PERIODIC_DATA = _descriptor.Descriptor(
  name='batched_periodic_data',
  full_name='batched_periodic_data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='batched_periodic_data.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='batched_periodic_data.device_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firmware_version', full_name='batched_periodic_data.firmware_version', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uptime_in_second', full_name='batched_periodic_data.uptime_in_second', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connected_ssid', full_name='batched_periodic_data.connected_ssid', index=4,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ring_time_ack', full_name='batched_periodic_data.ring_time_ack', index=5,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scan', full_name='batched_periodic_data.scan', index=6,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='messages_in_queue', full_name='batched_periodic_data.messages_in_queue', index=7,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BATCHED_PERIODIC_DATA_WIFI_ACCESS_POINT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=422,
  serialized_end=830,
)

_BATCHED_PERIODIC_DATA_WIFI_ACCESS_POINT.fields_by_name['antenna'].enum_type = _BATCHED_PERIODIC_DATA_WIFI_ACCESS_POINT_ANTENNATYPE
_BATCHED_PERIODIC_DATA_WIFI_ACCESS_POINT.containing_type = _BATCHED_PERIODIC_DATA
_BATCHED_PERIODIC_DATA_WIFI_ACCESS_POINT_ANTENNATYPE.containing_type = _BATCHED_PERIODIC_DATA_WIFI_ACCESS_POINT
_BATCHED_PERIODIC_DATA.fields_by_name['data'].message_type = _PERIODIC_DATA
_BATCHED_PERIODIC_DATA.fields_by_name['scan'].message_type = _BATCHED_PERIODIC_DATA_WIFI_ACCESS_POINT
DESCRIPTOR.message_types_by_name['periodic_data'] = _PERIODIC_DATA
DESCRIPTOR.message_types_by_name['batched_periodic_data'] = _BATCHED_PERIODIC_DATA

periodic_data = _reflection.GeneratedProtocolMessageType('periodic_data', (_message.Message,), dict(
  DESCRIPTOR = _PERIODIC_DATA,
  __module__ = 'periodic_pb2'
  # @@protoc_insertion_point(class_scope:periodic_data)
  ))
_sym_db.RegisterMessage(periodic_data)

batched_periodic_data = _reflection.GeneratedProtocolMessageType('batched_periodic_data', (_message.Message,), dict(

  wifi_access_point = _reflection.GeneratedProtocolMessageType('wifi_access_point', (_message.Message,), dict(
    DESCRIPTOR = _BATCHED_PERIODIC_DATA_WIFI_ACCESS_POINT,
    __module__ = 'periodic_pb2'
    # @@protoc_insertion_point(class_scope:batched_periodic_data.wifi_access_point)
    ))
  ,
  DESCRIPTOR = _BATCHED_PERIODIC_DATA,
  __module__ = 'periodic_pb2'
  # @@protoc_insertion_point(class_scope:batched_periodic_data)
  ))
_sym_db.RegisterMessage(batched_periodic_data)
_sym_db.RegisterMessage(batched_periodic_data.wifi_access_point)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.hello.suripu.api.inputB\017DataInputProtos'))
# @@protoc_insertion_point(module_scope)
