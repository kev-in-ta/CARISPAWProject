# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: carisPAWBuffers.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='carisPAWBuffers.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x63\x61risPAWBuffers.proto\"\xbd\x03\n\tframeUnit\x12\x12\n\ntime_stamp\x18\x01 \x01(\x02\x12%\n\nsensorType\x18\x02 \x01(\x0e\x32\x11.frameUnit.Sensor\x12\r\n\x05\x61\x63\x63_x\x18\x03 \x01(\x02\x12\r\n\x05\x61\x63\x63_y\x18\x04 \x01(\x02\x12\r\n\x05\x61\x63\x63_z\x18\x05 \x01(\x02\x12\x11\n\tangular_x\x18\x06 \x01(\x02\x12\x11\n\tangular_y\x18\x07 \x01(\x02\x12\x11\n\tangular_z\x18\x08 \x01(\x02\x12\r\n\x05mag_x\x18\t \x01(\x02\x12\r\n\x05mag_y\x18\n \x01(\x02\x12\r\n\x05mag_z\x18\x0b \x01(\x02\x12\x0f\n\x07heading\x18\x0c \x01(\x02\x12\r\n\x05pitch\x18\r \x01(\x02\x12\x0c\n\x04roll\x18\x0e \x01(\x02\x12\x16\n\x0eUSensorForward\x18\x0f \x01(\x02\x12\x17\n\x0fUSensorDownward\x18\x10 \x01(\x02\x12\x12\n\npiCamImage\x18\x11 \x01(\x0c\x12\x13\n\x0bimageHeight\x18\x12 \x01(\x05\x12\x12\n\nimageWidth\x18\x13 \x01(\x05\"F\n\x06Sensor\x12\t\n\x05IMU_9\x10\x00\x12\t\n\x05IMU_6\x10\x01\x12\x0c\n\x08USS_DOWN\x10\x02\x12\x0c\n\x08USS_FORW\x10\x03\x12\n\n\x06PI_CAM\x10\x04\"\x96\x01\n\twheelUnit\x12\x12\n\ntime_stamp\x18\x01 \x01(\x02\x12\x0f\n\x07isStamp\x18\x02 \x01(\x08\x12\r\n\x05\x61\x63\x63_x\x18\x03 \x01(\x02\x12\r\n\x05\x61\x63\x63_y\x18\x04 \x01(\x02\x12\r\n\x05\x61\x63\x63_z\x18\x05 \x01(\x02\x12\x11\n\tangular_x\x18\x06 \x01(\x02\x12\x11\n\tangular_y\x18\x07 \x01(\x02\x12\x11\n\tangular_z\x18\x08 \x01(\x02')
)



_FRAMEUNIT_SENSOR = _descriptor.EnumDescriptor(
  name='Sensor',
  full_name='frameUnit.Sensor',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IMU_9', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMU_6', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USS_DOWN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USS_FORW', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PI_CAM', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=401,
  serialized_end=471,
)
_sym_db.RegisterEnumDescriptor(_FRAMEUNIT_SENSOR)


_FRAMEUNIT = _descriptor.Descriptor(
  name='frameUnit',
  full_name='frameUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='frameUnit.time_stamp', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensorType', full_name='frameUnit.sensorType', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acc_x', full_name='frameUnit.acc_x', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acc_y', full_name='frameUnit.acc_y', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acc_z', full_name='frameUnit.acc_z', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_x', full_name='frameUnit.angular_x', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_y', full_name='frameUnit.angular_y', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_z', full_name='frameUnit.angular_z', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mag_x', full_name='frameUnit.mag_x', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mag_y', full_name='frameUnit.mag_y', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mag_z', full_name='frameUnit.mag_z', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading', full_name='frameUnit.heading', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='frameUnit.pitch', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roll', full_name='frameUnit.roll', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='USensorForward', full_name='frameUnit.USensorForward', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='USensorDownward', full_name='frameUnit.USensorDownward', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='piCamImage', full_name='frameUnit.piCamImage', index=16,
      number=17, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imageHeight', full_name='frameUnit.imageHeight', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imageWidth', full_name='frameUnit.imageWidth', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FRAMEUNIT_SENSOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=471,
)


_WHEELUNIT = _descriptor.Descriptor(
  name='wheelUnit',
  full_name='wheelUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='wheelUnit.time_stamp', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isStamp', full_name='wheelUnit.isStamp', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acc_x', full_name='wheelUnit.acc_x', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acc_y', full_name='wheelUnit.acc_y', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acc_z', full_name='wheelUnit.acc_z', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_x', full_name='wheelUnit.angular_x', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_y', full_name='wheelUnit.angular_y', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_z', full_name='wheelUnit.angular_z', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=474,
  serialized_end=624,
)

_FRAMEUNIT.fields_by_name['sensorType'].enum_type = _FRAMEUNIT_SENSOR
_FRAMEUNIT_SENSOR.containing_type = _FRAMEUNIT
DESCRIPTOR.message_types_by_name['frameUnit'] = _FRAMEUNIT
DESCRIPTOR.message_types_by_name['wheelUnit'] = _WHEELUNIT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

frameUnit = _reflection.GeneratedProtocolMessageType('frameUnit', (_message.Message,), dict(
  DESCRIPTOR = _FRAMEUNIT,
  __module__ = 'carisPAWBuffers_pb2'
  # @@protoc_insertion_point(class_scope:frameUnit)
  ))
_sym_db.RegisterMessage(frameUnit)

wheelUnit = _reflection.GeneratedProtocolMessageType('wheelUnit', (_message.Message,), dict(
  DESCRIPTOR = _WHEELUNIT,
  __module__ = 'carisPAWBuffers_pb2'
  # @@protoc_insertion_point(class_scope:wheelUnit)
  ))
_sym_db.RegisterMessage(wheelUnit)


# @@protoc_insertion_point(module_scope)
