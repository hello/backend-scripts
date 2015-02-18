# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audio_control.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='audio_control.proto',
  package='',
  serialized_pb='\n\x13\x61udio_control.proto\"\x92\x01\n\x16\x41udioClassifierMessage\x12\r\n\x05idata\x18\x01 \x03(\x11\x12\x12\n\nnumclasses\x18\x02 \x01(\x05\x12\x34\n\x04type\x18\x03 \x01(\x0e\x32&.AudioClassifierMessage.ClassifierType\"\x1f\n\x0e\x43lassifierType\x12\r\n\tLINEARSVM\x10\x00\"\x8a\x04\n\x0c\x41udioControl\x12\"\n\x1a\x61udio_min_energy_threshold\x18\x01 \x01(\x05\x12\x38\n0audio_num_feat_vecs_until_attempt_feature_upload\x18\x02 \x01(\x05\x12\x1e\n\x16\x61udio_feat_buffer_size\x18\x03 \x01(\x05\x12(\n audio_recording_period_in_frames\x18\x04 \x01(\x05\x12>\n\x14\x61udio_capture_action\x18\x08 \x01(\x0e\x32 .AudioControl.AudioCaptureAction\x12\x39\n\x18\x61udio_capture_classifier\x18\t \x01(\x0b\x32\x17.AudioClassifierMessage\x12\x32\n\x11\x61udio_capture_hmm\x18\n \x01(\x0b\x32\x17.AudioClassifierMessage\x12=\n\x13\x61udio_save_raw_data\x18\x0b \x01(\x0e\x32 .AudioControl.AudioCaptureAction\x12=\n\x13\x61udio_save_features\x18\x0c \x01(\x0e\x32 .AudioControl.AudioCaptureAction\"%\n\x12\x41udioCaptureAction\x12\x07\n\x03OFF\x10\x00\x12\x06\n\x02ON\x10\x01\x42\x30\n\x1a\x63om.hello.suripu.api.audioB\x12\x41udioControlProtos')



_AUDIOCLASSIFIERMESSAGE_CLASSIFIERTYPE = _descriptor.EnumDescriptor(
  name='ClassifierType',
  full_name='AudioClassifierMessage.ClassifierType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LINEARSVM', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=139,
  serialized_end=170,
)

_AUDIOCONTROL_AUDIOCAPTUREACTION = _descriptor.EnumDescriptor(
  name='AudioCaptureAction',
  full_name='AudioControl.AudioCaptureAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OFF', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ON', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=658,
  serialized_end=695,
)


_AUDIOCLASSIFIERMESSAGE = _descriptor.Descriptor(
  name='AudioClassifierMessage',
  full_name='AudioClassifierMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idata', full_name='AudioClassifierMessage.idata', index=0,
      number=1, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numclasses', full_name='AudioClassifierMessage.numclasses', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='AudioClassifierMessage.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AUDIOCLASSIFIERMESSAGE_CLASSIFIERTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=24,
  serialized_end=170,
)


_AUDIOCONTROL = _descriptor.Descriptor(
  name='AudioControl',
  full_name='AudioControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio_min_energy_threshold', full_name='AudioControl.audio_min_energy_threshold', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_num_feat_vecs_until_attempt_feature_upload', full_name='AudioControl.audio_num_feat_vecs_until_attempt_feature_upload', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_feat_buffer_size', full_name='AudioControl.audio_feat_buffer_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_recording_period_in_frames', full_name='AudioControl.audio_recording_period_in_frames', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_capture_action', full_name='AudioControl.audio_capture_action', index=4,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_capture_classifier', full_name='AudioControl.audio_capture_classifier', index=5,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_capture_hmm', full_name='AudioControl.audio_capture_hmm', index=6,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_save_raw_data', full_name='AudioControl.audio_save_raw_data', index=7,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_save_features', full_name='AudioControl.audio_save_features', index=8,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AUDIOCONTROL_AUDIOCAPTUREACTION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=173,
  serialized_end=695,
)

_AUDIOCLASSIFIERMESSAGE.fields_by_name['type'].enum_type = _AUDIOCLASSIFIERMESSAGE_CLASSIFIERTYPE
_AUDIOCLASSIFIERMESSAGE_CLASSIFIERTYPE.containing_type = _AUDIOCLASSIFIERMESSAGE;
_AUDIOCONTROL.fields_by_name['audio_capture_action'].enum_type = _AUDIOCONTROL_AUDIOCAPTUREACTION
_AUDIOCONTROL.fields_by_name['audio_capture_classifier'].message_type = _AUDIOCLASSIFIERMESSAGE
_AUDIOCONTROL.fields_by_name['audio_capture_hmm'].message_type = _AUDIOCLASSIFIERMESSAGE
_AUDIOCONTROL.fields_by_name['audio_save_raw_data'].enum_type = _AUDIOCONTROL_AUDIOCAPTUREACTION
_AUDIOCONTROL.fields_by_name['audio_save_features'].enum_type = _AUDIOCONTROL_AUDIOCAPTUREACTION
_AUDIOCONTROL_AUDIOCAPTUREACTION.containing_type = _AUDIOCONTROL;
DESCRIPTOR.message_types_by_name['AudioClassifierMessage'] = _AUDIOCLASSIFIERMESSAGE
DESCRIPTOR.message_types_by_name['AudioControl'] = _AUDIOCONTROL

class AudioClassifierMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUDIOCLASSIFIERMESSAGE

  # @@protoc_insertion_point(class_scope:AudioClassifierMessage)

class AudioControl(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUDIOCONTROL

  # @@protoc_insertion_point(class_scope:AudioControl)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\032com.hello.suripu.api.audioB\022AudioControlProtos')
# @@protoc_insertion_point(module_scope)