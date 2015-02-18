# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sync_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import audio_control_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sync_response.proto',
  package='',
  serialized_pb='\n\x13sync_response.proto\x1a\x13\x61udio_control.proto\"\x8b\r\n\x0cSyncResponse\x12\x14\n\x0cupload_cycle\x18\x01 \x01(\x05\x12\x12\n\nsync_cycle\x18\x02 \x01(\x05\x12\x15\n\racc_scan_cyle\x18\x03 \x01(\x05\x12\x1d\n\x15\x61\x63\x63_sampling_interval\x18\x04 \x01(\x05\x12 \n\x18\x64\x65vice_sampling_interval\x18\x05 \x01(\x05\x12\"\n\x05\x61larm\x18\x06 \x01(\x0b\x32\x13.SyncResponse.Alarm\x12\x33\n\x0epairing_action\x18\x07 \x01(\x0b\x32\x1b.SyncResponse.PairingAction\x12-\n\x0bwhite_noise\x18\x08 \x01(\x0b\x32\x18.SyncResponse.WhiteNoise\x12/\n\x0c\x66lash_action\x18\t \x01(\x0b\x32\x19.SyncResponse.FlashAction\x12\x14\n\x0creset_device\x18\n \x01(\x08\x12\x35\n\x0froom_conditions\x18\x0c \x01(\x0e\x32\x1c.SyncResponse.RoomConditions\x12)\n\x05\x66iles\x18\r \x03(\x0b\x32\x1a.SyncResponse.FileDownload\x12\x1b\n\x13reset_to_factory_fw\x18\x0e \x01(\x08\x12$\n\raudio_control\x18\x0f \x01(\x0b\x32\r.AudioControl\x12\x11\n\tunix_time\x18\x10 \x01(\r\x12+\n\nled_action\x18\x11 \x01(\x0b\x32\x17.SyncResponse.LEDAction\x12\x0b\n\x03mac\x18\x12 \x01(\x0c\x12\x12\n\nbatch_size\x18\x13 \x01(\x05\x1a\x85\x02\n\x0c\x46ileDownload\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x1c\n\x14\x63opy_to_serial_flash\x18\x04 \x01(\x08\x12\x1f\n\x17reset_network_processor\x18\x05 \x01(\x08\x12#\n\x1breset_application_processor\x18\x06 \x01(\x08\x12\x1d\n\x15serial_flash_filename\x18\x07 \x01(\t\x12\x19\n\x11serial_flash_path\x18\x08 \x01(\t\x12\x18\n\x10sd_card_filename\x18\x03 \x01(\t\x12\x14\n\x0csd_card_path\x18\t \x01(\t\x12\x0c\n\x04sha1\x18\n \x01(\x0c\x1a\x8e\x01\n\x05\x41larm\x12\x12\n\nstart_time\x18\x01 \x01(\r\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\r\x12\x16\n\x0bringtone_id\x18\x03 \x01(\x05:\x01\x31\x12&\n\x1ering_offset_from_now_in_second\x18\x04 \x01(\x05\x12\x1f\n\x17ring_duration_in_second\x18\x05 \x01(\x05\x1aw\n\rPairingAction\x12\x0c\n\x04ssid\x18\x01 \x01(\t\x12\x34\n\x04type\x18\x02 \x01(\x0e\x32&.SyncResponse.PairingAction.ActionType\"\"\n\nActionType\x12\x08\n\x04PAIR\x10\x00\x12\n\n\x06UNPAIR\x10\x01\x1a\x44\n\nWhiteNoise\x12\x12\n\nstart_time\x18\x01 \x01(\x05\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\x05\x12\x10\n\x08sound_id\x18\x03 \x01(\x05\x1a\x95\x01\n\x0b\x46lashAction\x12\x0b\n\x03red\x18\x01 \x01(\x05\x12\r\n\x05green\x18\x02 \x01(\x05\x12\x0c\n\x04\x62lue\x18\x03 \x01(\x05\x12\x1a\n\x12\x64\x65lay_milliseconds\x18\x04 \x01(\x05\x12\x0f\n\x07\x66\x61\x64\x65_in\x18\x05 \x01(\x08\x12\x10\n\x08\x66\x61\x64\x65_out\x18\x06 \x01(\x08\x12\x0e\n\x06rotate\x18\x07 \x01(\x08\x12\r\n\x05\x61lpha\x18\x08 \x01(\x05\x1a\xfe\x01\n\tLEDAction\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32%.SyncResponse.LEDAction.LEDActionType\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\r\n\x05\x63olor\x18\x03 \x01(\r\x12\x11\n\talt_color\x18\x04 \x01(\r\x12\x18\n\x10\x64uration_seconds\x18\x06 \x01(\x05\"s\n\rLEDActionType\x12\n\n\x06\x46\x41\x44\x45IO\x10\x00\x12\x08\n\x04GLOW\x10\x01\x12\t\n\x05THROB\x10\x02\x12\n\n\x06PULSAR\x10\x03\x12\n\n\x06\x44OUBLE\x10\x04\x12\t\n\x05SIREN\x10\x05\x12\n\n\x06TRIPPY\x10\x06\x12\t\n\x05PARTY\x10\x07\x12\x07\n\x03URL\x10\x08\"3\n\x0eRoomConditions\x12\t\n\x05IDEAL\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05\x41LERT\x10\x03\x42+\n\x1b\x63om.hello.suripu.api.outputB\x0cOutputProtos')



_SYNCRESPONSE_PAIRINGACTION_ACTIONTYPE = _descriptor.EnumDescriptor(
  name='ActionType',
  full_name='SyncResponse.PairingAction.ActionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PAIR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNPAIR', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1154,
  serialized_end=1188,
)

_SYNCRESPONSE_LEDACTION_LEDACTIONTYPE = _descriptor.EnumDescriptor(
  name='LEDActionType',
  full_name='SyncResponse.LEDAction.LEDActionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FADEIO', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLOW', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THROB', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PULSAR', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIREN', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRIPPY', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTY', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1552,
  serialized_end=1667,
)

_SYNCRESPONSE_ROOMCONDITIONS = _descriptor.EnumDescriptor(
  name='RoomConditions',
  full_name='SyncResponse.RoomConditions',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IDEAL', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALERT', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1669,
  serialized_end=1720,
)


_SYNCRESPONSE_FILEDOWNLOAD = _descriptor.Descriptor(
  name='FileDownload',
  full_name='SyncResponse.FileDownload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='SyncResponse.FileDownload.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='SyncResponse.FileDownload.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='copy_to_serial_flash', full_name='SyncResponse.FileDownload.copy_to_serial_flash', index=2,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reset_network_processor', full_name='SyncResponse.FileDownload.reset_network_processor', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reset_application_processor', full_name='SyncResponse.FileDownload.reset_application_processor', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serial_flash_filename', full_name='SyncResponse.FileDownload.serial_flash_filename', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serial_flash_path', full_name='SyncResponse.FileDownload.serial_flash_path', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sd_card_filename', full_name='SyncResponse.FileDownload.sd_card_filename', index=7,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sd_card_path', full_name='SyncResponse.FileDownload.sd_card_path', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sha1', full_name='SyncResponse.FileDownload.sha1', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  serialized_start=661,
  serialized_end=922,
)

_SYNCRESPONSE_ALARM = _descriptor.Descriptor(
  name='Alarm',
  full_name='SyncResponse.Alarm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='SyncResponse.Alarm.start_time', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='SyncResponse.Alarm.end_time', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ringtone_id', full_name='SyncResponse.Alarm.ringtone_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ring_offset_from_now_in_second', full_name='SyncResponse.Alarm.ring_offset_from_now_in_second', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ring_duration_in_second', full_name='SyncResponse.Alarm.ring_duration_in_second', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=925,
  serialized_end=1067,
)

_SYNCRESPONSE_PAIRINGACTION = _descriptor.Descriptor(
  name='PairingAction',
  full_name='SyncResponse.PairingAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ssid', full_name='SyncResponse.PairingAction.ssid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='SyncResponse.PairingAction.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SYNCRESPONSE_PAIRINGACTION_ACTIONTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1069,
  serialized_end=1188,
)

_SYNCRESPONSE_WHITENOISE = _descriptor.Descriptor(
  name='WhiteNoise',
  full_name='SyncResponse.WhiteNoise',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='SyncResponse.WhiteNoise.start_time', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='SyncResponse.WhiteNoise.end_time', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sound_id', full_name='SyncResponse.WhiteNoise.sound_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=1190,
  serialized_end=1258,
)

_SYNCRESPONSE_FLASHACTION = _descriptor.Descriptor(
  name='FlashAction',
  full_name='SyncResponse.FlashAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='red', full_name='SyncResponse.FlashAction.red', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='green', full_name='SyncResponse.FlashAction.green', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blue', full_name='SyncResponse.FlashAction.blue', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delay_milliseconds', full_name='SyncResponse.FlashAction.delay_milliseconds', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fade_in', full_name='SyncResponse.FlashAction.fade_in', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fade_out', full_name='SyncResponse.FlashAction.fade_out', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rotate', full_name='SyncResponse.FlashAction.rotate', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alpha', full_name='SyncResponse.FlashAction.alpha', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=1261,
  serialized_end=1410,
)

_SYNCRESPONSE_LEDACTION = _descriptor.Descriptor(
  name='LEDAction',
  full_name='SyncResponse.LEDAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='SyncResponse.LEDAction.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='SyncResponse.LEDAction.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='color', full_name='SyncResponse.LEDAction.color', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alt_color', full_name='SyncResponse.LEDAction.alt_color', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration_seconds', full_name='SyncResponse.LEDAction.duration_seconds', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SYNCRESPONSE_LEDACTION_LEDACTIONTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1413,
  serialized_end=1667,
)

_SYNCRESPONSE = _descriptor.Descriptor(
  name='SyncResponse',
  full_name='SyncResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='upload_cycle', full_name='SyncResponse.upload_cycle', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sync_cycle', full_name='SyncResponse.sync_cycle', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acc_scan_cyle', full_name='SyncResponse.acc_scan_cyle', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acc_sampling_interval', full_name='SyncResponse.acc_sampling_interval', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_sampling_interval', full_name='SyncResponse.device_sampling_interval', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alarm', full_name='SyncResponse.alarm', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pairing_action', full_name='SyncResponse.pairing_action', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='white_noise', full_name='SyncResponse.white_noise', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flash_action', full_name='SyncResponse.flash_action', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reset_device', full_name='SyncResponse.reset_device', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='room_conditions', full_name='SyncResponse.room_conditions', index=10,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='files', full_name='SyncResponse.files', index=11,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reset_to_factory_fw', full_name='SyncResponse.reset_to_factory_fw', index=12,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_control', full_name='SyncResponse.audio_control', index=13,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unix_time', full_name='SyncResponse.unix_time', index=14,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='led_action', full_name='SyncResponse.led_action', index=15,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mac', full_name='SyncResponse.mac', index=16,
      number=18, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='SyncResponse.batch_size', index=17,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SYNCRESPONSE_FILEDOWNLOAD, _SYNCRESPONSE_ALARM, _SYNCRESPONSE_PAIRINGACTION, _SYNCRESPONSE_WHITENOISE, _SYNCRESPONSE_FLASHACTION, _SYNCRESPONSE_LEDACTION, ],
  enum_types=[
    _SYNCRESPONSE_ROOMCONDITIONS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=45,
  serialized_end=1720,
)

_SYNCRESPONSE_FILEDOWNLOAD.containing_type = _SYNCRESPONSE;
_SYNCRESPONSE_ALARM.containing_type = _SYNCRESPONSE;
_SYNCRESPONSE_PAIRINGACTION.fields_by_name['type'].enum_type = _SYNCRESPONSE_PAIRINGACTION_ACTIONTYPE
_SYNCRESPONSE_PAIRINGACTION.containing_type = _SYNCRESPONSE;
_SYNCRESPONSE_PAIRINGACTION_ACTIONTYPE.containing_type = _SYNCRESPONSE_PAIRINGACTION;
_SYNCRESPONSE_WHITENOISE.containing_type = _SYNCRESPONSE;
_SYNCRESPONSE_FLASHACTION.containing_type = _SYNCRESPONSE;
_SYNCRESPONSE_LEDACTION.fields_by_name['type'].enum_type = _SYNCRESPONSE_LEDACTION_LEDACTIONTYPE
_SYNCRESPONSE_LEDACTION.containing_type = _SYNCRESPONSE;
_SYNCRESPONSE_LEDACTION_LEDACTIONTYPE.containing_type = _SYNCRESPONSE_LEDACTION;
_SYNCRESPONSE.fields_by_name['alarm'].message_type = _SYNCRESPONSE_ALARM
_SYNCRESPONSE.fields_by_name['pairing_action'].message_type = _SYNCRESPONSE_PAIRINGACTION
_SYNCRESPONSE.fields_by_name['white_noise'].message_type = _SYNCRESPONSE_WHITENOISE
_SYNCRESPONSE.fields_by_name['flash_action'].message_type = _SYNCRESPONSE_FLASHACTION
_SYNCRESPONSE.fields_by_name['room_conditions'].enum_type = _SYNCRESPONSE_ROOMCONDITIONS
_SYNCRESPONSE.fields_by_name['files'].message_type = _SYNCRESPONSE_FILEDOWNLOAD
_SYNCRESPONSE.fields_by_name['audio_control'].message_type = audio_control_pb2._AUDIOCONTROL
_SYNCRESPONSE.fields_by_name['led_action'].message_type = _SYNCRESPONSE_LEDACTION
_SYNCRESPONSE_ROOMCONDITIONS.containing_type = _SYNCRESPONSE;
DESCRIPTOR.message_types_by_name['SyncResponse'] = _SYNCRESPONSE

class SyncResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class FileDownload(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SYNCRESPONSE_FILEDOWNLOAD

    # @@protoc_insertion_point(class_scope:SyncResponse.FileDownload)

  class Alarm(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SYNCRESPONSE_ALARM

    # @@protoc_insertion_point(class_scope:SyncResponse.Alarm)

  class PairingAction(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SYNCRESPONSE_PAIRINGACTION

    # @@protoc_insertion_point(class_scope:SyncResponse.PairingAction)

  class WhiteNoise(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SYNCRESPONSE_WHITENOISE

    # @@protoc_insertion_point(class_scope:SyncResponse.WhiteNoise)

  class FlashAction(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SYNCRESPONSE_FLASHACTION

    # @@protoc_insertion_point(class_scope:SyncResponse.FlashAction)

  class LEDAction(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SYNCRESPONSE_LEDACTION

    # @@protoc_insertion_point(class_scope:SyncResponse.LEDAction)
  DESCRIPTOR = _SYNCRESPONSE

  # @@protoc_insertion_point(class_scope:SyncResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\033com.hello.suripu.api.outputB\014OutputProtos')
# @@protoc_insertion_point(module_scope)
