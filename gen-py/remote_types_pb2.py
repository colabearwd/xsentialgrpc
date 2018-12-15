# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remote_types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='remote_types.proto',
  package='remote',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12remote_types.proto\x12\x06remote\"P\n\x04\x43url\x12\x11\n\ttargeturl\x18\x01 \x01(\t\x12\x11\n\tipversion\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x05\x12\x11\n\tserialnum\x18\x04 \x01(\x05\"\x88\x02\n\x07\x43urlRes\x12\x14\n\x0c\x63urlhttpcode\x18\x01 \x01(\t\x12\x17\n\x0f\x63urlhttpconnect\x18\x02 \x01(\t\x12\x1a\n\x12\x63urltimenameloopup\x18\x03 \x01(\t\x12\x18\n\x10\x63urltimeredirect\x18\x04 \x01(\t\x12\x1b\n\x13\x63urltimepretransfer\x18\x05 \x01(\t\x12\x17\n\x0f\x63urltimeconnect\x18\x06 \x01(\t\x12\x1d\n\x15\x63urltimestarttransfer\x18\x07 \x01(\t\x12\x15\n\rcurltimetotal\x18\x08 \x01(\t\x12\x19\n\x11\x63urlspeeddownload\x18\t \x01(\t\x12\x11\n\tserialnum\x18\n \x01(\x05\"t\n\x04Ping\x12\x11\n\ttargeturl\x18\x01 \x01(\t\x12\x11\n\tipversion\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x05\x12\x13\n\x0bpackagesize\x18\x04 \x01(\x05\x12\r\n\x05\x63ount\x18\x05 \x01(\x05\x12\x11\n\tserialnum\x18\x06 \x01(\x05\"T\n\x07PingRes\x12\x10\n\x08lossrate\x18\x01 \x01(\x05\x12\x0f\n\x07maxtime\x18\x02 \x01(\x05\x12\x13\n\x0b\x61veragetime\x18\x03 \x01(\x05\x12\x11\n\tserialnum\x18\x04 \x01(\x05\"$\n\x0e\x41\x64\x64\x43urlRequest\x12\x12\n\nrequestnum\x18\x01 \x01(\x05\"+\n\rAddCurlResult\x12\x1a\n\x04\x63url\x18\x01 \x01(\x0b\x32\x0c.remote.Curl\"2\n\x0e\x43urlResRequest\x12 \n\x07\x63urlres\x18\x01 \x01(\x0b\x32\x0f.remote.CurlRes\" \n\rCurlResResult\x12\x0f\n\x07results\x18\x01 \x01(\x05\"$\n\x0e\x41\x64\x64PingRequest\x12\x12\n\nrequestnum\x18\x01 \x01(\x05\"+\n\rAddPingResult\x12\x1a\n\x04ping\x18\x01 \x01(\x0b\x32\x0c.remote.Ping\"2\n\x0ePingResRequest\x12 \n\x07pingres\x18\x01 \x01(\x0b\x32\x0f.remote.PingRes\" \n\rPingResResult\x12\x0f\n\x07results\x18\x01 \x01(\x05\x62\x06proto3')
)




_CURL = _descriptor.Descriptor(
  name='Curl',
  full_name='remote.Curl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targeturl', full_name='remote.Curl.targeturl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipversion', full_name='remote.Curl.ipversion', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='remote.Curl.timeout', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialnum', full_name='remote.Curl.serialnum', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=110,
)


_CURLRES = _descriptor.Descriptor(
  name='CurlRes',
  full_name='remote.CurlRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='curlhttpcode', full_name='remote.CurlRes.curlhttpcode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curlhttpconnect', full_name='remote.CurlRes.curlhttpconnect', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curltimenameloopup', full_name='remote.CurlRes.curltimenameloopup', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curltimeredirect', full_name='remote.CurlRes.curltimeredirect', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curltimepretransfer', full_name='remote.CurlRes.curltimepretransfer', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curltimeconnect', full_name='remote.CurlRes.curltimeconnect', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curltimestarttransfer', full_name='remote.CurlRes.curltimestarttransfer', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curltimetotal', full_name='remote.CurlRes.curltimetotal', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curlspeeddownload', full_name='remote.CurlRes.curlspeeddownload', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialnum', full_name='remote.CurlRes.serialnum', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=377,
)


_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='remote.Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targeturl', full_name='remote.Ping.targeturl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipversion', full_name='remote.Ping.ipversion', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='remote.Ping.timeout', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packagesize', full_name='remote.Ping.packagesize', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='remote.Ping.count', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialnum', full_name='remote.Ping.serialnum', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=379,
  serialized_end=495,
)


_PINGRES = _descriptor.Descriptor(
  name='PingRes',
  full_name='remote.PingRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lossrate', full_name='remote.PingRes.lossrate', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxtime', full_name='remote.PingRes.maxtime', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='averagetime', full_name='remote.PingRes.averagetime', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialnum', full_name='remote.PingRes.serialnum', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=497,
  serialized_end=581,
)


_ADDCURLREQUEST = _descriptor.Descriptor(
  name='AddCurlRequest',
  full_name='remote.AddCurlRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestnum', full_name='remote.AddCurlRequest.requestnum', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=583,
  serialized_end=619,
)


_ADDCURLRESULT = _descriptor.Descriptor(
  name='AddCurlResult',
  full_name='remote.AddCurlResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='curl', full_name='remote.AddCurlResult.curl', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=621,
  serialized_end=664,
)


_CURLRESREQUEST = _descriptor.Descriptor(
  name='CurlResRequest',
  full_name='remote.CurlResRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='curlres', full_name='remote.CurlResRequest.curlres', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=666,
  serialized_end=716,
)


_CURLRESRESULT = _descriptor.Descriptor(
  name='CurlResResult',
  full_name='remote.CurlResResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='remote.CurlResResult.results', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=718,
  serialized_end=750,
)


_ADDPINGREQUEST = _descriptor.Descriptor(
  name='AddPingRequest',
  full_name='remote.AddPingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestnum', full_name='remote.AddPingRequest.requestnum', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=752,
  serialized_end=788,
)


_ADDPINGRESULT = _descriptor.Descriptor(
  name='AddPingResult',
  full_name='remote.AddPingResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ping', full_name='remote.AddPingResult.ping', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=790,
  serialized_end=833,
)


_PINGRESREQUEST = _descriptor.Descriptor(
  name='PingResRequest',
  full_name='remote.PingResRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pingres', full_name='remote.PingResRequest.pingres', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=835,
  serialized_end=885,
)


_PINGRESRESULT = _descriptor.Descriptor(
  name='PingResResult',
  full_name='remote.PingResResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='remote.PingResResult.results', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=887,
  serialized_end=919,
)

_ADDCURLRESULT.fields_by_name['curl'].message_type = _CURL
_CURLRESREQUEST.fields_by_name['curlres'].message_type = _CURLRES
_ADDPINGRESULT.fields_by_name['ping'].message_type = _PING
_PINGRESREQUEST.fields_by_name['pingres'].message_type = _PINGRES
DESCRIPTOR.message_types_by_name['Curl'] = _CURL
DESCRIPTOR.message_types_by_name['CurlRes'] = _CURLRES
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['PingRes'] = _PINGRES
DESCRIPTOR.message_types_by_name['AddCurlRequest'] = _ADDCURLREQUEST
DESCRIPTOR.message_types_by_name['AddCurlResult'] = _ADDCURLRESULT
DESCRIPTOR.message_types_by_name['CurlResRequest'] = _CURLRESREQUEST
DESCRIPTOR.message_types_by_name['CurlResResult'] = _CURLRESRESULT
DESCRIPTOR.message_types_by_name['AddPingRequest'] = _ADDPINGREQUEST
DESCRIPTOR.message_types_by_name['AddPingResult'] = _ADDPINGRESULT
DESCRIPTOR.message_types_by_name['PingResRequest'] = _PINGRESREQUEST
DESCRIPTOR.message_types_by_name['PingResResult'] = _PINGRESRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Curl = _reflection.GeneratedProtocolMessageType('Curl', (_message.Message,), dict(
  DESCRIPTOR = _CURL,
  __module__ = 'remote_types_pb2'
  # @@protoc_insertion_point(class_scope:remote.Curl)
  ))
_sym_db.RegisterMessage(Curl)

CurlRes = _reflection.GeneratedProtocolMessageType('CurlRes', (_message.Message,), dict(
  DESCRIPTOR = _CURLRES,
  __module__ = 'remote_types_pb2'
  # @@protoc_insertion_point(class_scope:remote.CurlRes)
  ))
_sym_db.RegisterMessage(CurlRes)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), dict(
  DESCRIPTOR = _PING,
  __module__ = 'remote_types_pb2'
  # @@protoc_insertion_point(class_scope:remote.Ping)
  ))
_sym_db.RegisterMessage(Ping)

PingRes = _reflection.GeneratedProtocolMessageType('PingRes', (_message.Message,), dict(
  DESCRIPTOR = _PINGRES,
  __module__ = 'remote_types_pb2'
  # @@protoc_insertion_point(class_scope:remote.PingRes)
  ))
_sym_db.RegisterMessage(PingRes)

AddCurlRequest = _reflection.GeneratedProtocolMessageType('AddCurlRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDCURLREQUEST,
  __module__ = 'remote_types_pb2'
  # @@protoc_insertion_point(class_scope:remote.AddCurlRequest)
  ))
_sym_db.RegisterMessage(AddCurlRequest)

AddCurlResult = _reflection.GeneratedProtocolMessageType('AddCurlResult', (_message.Message,), dict(
  DESCRIPTOR = _ADDCURLRESULT,
  __module__ = 'remote_types_pb2'
  # @@protoc_insertion_point(class_scope:remote.AddCurlResult)
  ))
_sym_db.RegisterMessage(AddCurlResult)

CurlResRequest = _reflection.GeneratedProtocolMessageType('CurlResRequest', (_message.Message,), dict(
  DESCRIPTOR = _CURLRESREQUEST,
  __module__ = 'remote_types_pb2'
  # @@protoc_insertion_point(class_scope:remote.CurlResRequest)
  ))
_sym_db.RegisterMessage(CurlResRequest)

CurlResResult = _reflection.GeneratedProtocolMessageType('CurlResResult', (_message.Message,), dict(
  DESCRIPTOR = _CURLRESRESULT,
  __module__ = 'remote_types_pb2'
  # @@protoc_insertion_point(class_scope:remote.CurlResResult)
  ))
_sym_db.RegisterMessage(CurlResResult)

AddPingRequest = _reflection.GeneratedProtocolMessageType('AddPingRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDPINGREQUEST,
  __module__ = 'remote_types_pb2'
  # @@protoc_insertion_point(class_scope:remote.AddPingRequest)
  ))
_sym_db.RegisterMessage(AddPingRequest)

AddPingResult = _reflection.GeneratedProtocolMessageType('AddPingResult', (_message.Message,), dict(
  DESCRIPTOR = _ADDPINGRESULT,
  __module__ = 'remote_types_pb2'
  # @@protoc_insertion_point(class_scope:remote.AddPingResult)
  ))
_sym_db.RegisterMessage(AddPingResult)

PingResRequest = _reflection.GeneratedProtocolMessageType('PingResRequest', (_message.Message,), dict(
  DESCRIPTOR = _PINGRESREQUEST,
  __module__ = 'remote_types_pb2'
  # @@protoc_insertion_point(class_scope:remote.PingResRequest)
  ))
_sym_db.RegisterMessage(PingResRequest)

PingResResult = _reflection.GeneratedProtocolMessageType('PingResResult', (_message.Message,), dict(
  DESCRIPTOR = _PINGRESRESULT,
  __module__ = 'remote_types_pb2'
  # @@protoc_insertion_point(class_scope:remote.PingResResult)
  ))
_sym_db.RegisterMessage(PingResResult)


# @@protoc_insertion_point(module_scope)