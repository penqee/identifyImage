# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: picture.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rpicture.proto\x12\x0fpicturetovector\"\x1d\n\x0cImageRequest\x12\r\n\x05image\x18\x01 \x01(\x0c\" \n\x0eVectorResponse\x12\x0e\n\x06vector\x18\x01 \x03(\x02\x32\x65\n\x11PictureConService\x12P\n\x0eGetImageVector\x12\x1d.picturetovector.ImageRequest\x1a\x1f.picturetovector.VectorResponseB\nZ\x08../protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'picture_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\010../proto'
  _globals['_IMAGEREQUEST']._serialized_start=34
  _globals['_IMAGEREQUEST']._serialized_end=63
  _globals['_VECTORRESPONSE']._serialized_start=65
  _globals['_VECTORRESPONSE']._serialized_end=97
  _globals['_PICTURECONSERVICE']._serialized_start=99
  _globals['_PICTURECONSERVICE']._serialized_end=200
# @@protoc_insertion_point(module_scope)
