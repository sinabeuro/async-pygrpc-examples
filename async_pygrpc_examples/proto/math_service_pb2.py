# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: math_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='math_service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12math_service.proto\"!\n\x10GetSquareRequest\x12\r\n\x05input\x18\x01 \x01(\x05\"#\n\x11GetSquareResponse\x12\x0e\n\x06output\x18\x01 \x01(\x05\x32:\n\x04Math\x12\x32\n\tGetSquare\x12\x11.GetSquareRequest\x1a\x12.GetSquareResponseb\x06proto3'
)




_GETSQUAREREQUEST = _descriptor.Descriptor(
  name='GetSquareRequest',
  full_name='GetSquareRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='GetSquareRequest.input', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=55,
)


_GETSQUARERESPONSE = _descriptor.Descriptor(
  name='GetSquareResponse',
  full_name='GetSquareResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='output', full_name='GetSquareResponse.output', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=92,
)

DESCRIPTOR.message_types_by_name['GetSquareRequest'] = _GETSQUAREREQUEST
DESCRIPTOR.message_types_by_name['GetSquareResponse'] = _GETSQUARERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetSquareRequest = _reflection.GeneratedProtocolMessageType('GetSquareRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSQUAREREQUEST,
  '__module__' : 'math_service_pb2'
  # @@protoc_insertion_point(class_scope:GetSquareRequest)
  })
_sym_db.RegisterMessage(GetSquareRequest)

GetSquareResponse = _reflection.GeneratedProtocolMessageType('GetSquareResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSQUARERESPONSE,
  '__module__' : 'math_service_pb2'
  # @@protoc_insertion_point(class_scope:GetSquareResponse)
  })
_sym_db.RegisterMessage(GetSquareResponse)



_MATH = _descriptor.ServiceDescriptor(
  name='Math',
  full_name='Math',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=94,
  serialized_end=152,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSquare',
    full_name='Math.GetSquare',
    index=0,
    containing_service=None,
    input_type=_GETSQUAREREQUEST,
    output_type=_GETSQUARERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MATH)

DESCRIPTOR.services_by_name['Math'] = _MATH

# @@protoc_insertion_point(module_scope)