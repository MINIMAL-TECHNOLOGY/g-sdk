# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import display_pb2 as display__pb2


class DisplayStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UpdateLanguagePack = channel.unary_unary(
        '/display.Display/UpdateLanguagePack',
        request_serializer=display__pb2.UpdateLanguagePackRequest.SerializeToString,
        response_deserializer=display__pb2.UpdateLanguagePackResponse.FromString,
        )
    self.UpdateLanguagePackMulti = channel.unary_unary(
        '/display.Display/UpdateLanguagePackMulti',
        request_serializer=display__pb2.UpdateLanguagePackMultiRequest.SerializeToString,
        response_deserializer=display__pb2.UpdateLanguagePackMultiResponse.FromString,
        )
    self.GetConfig = channel.unary_unary(
        '/display.Display/GetConfig',
        request_serializer=display__pb2.GetConfigRequest.SerializeToString,
        response_deserializer=display__pb2.GetConfigResponse.FromString,
        )
    self.SetConfig = channel.unary_unary(
        '/display.Display/SetConfig',
        request_serializer=display__pb2.SetConfigRequest.SerializeToString,
        response_deserializer=display__pb2.SetConfigResponse.FromString,
        )
    self.SetConfigMulti = channel.unary_unary(
        '/display.Display/SetConfigMulti',
        request_serializer=display__pb2.SetConfigMultiRequest.SerializeToString,
        response_deserializer=display__pb2.SetConfigMultiResponse.FromString,
        )


class DisplayServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def UpdateLanguagePack(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateLanguagePackMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetConfig(self, request, context):
    """
    rpc UpdateNotice(UpdateNoticeRequest) returns (UpdateNoticeResponse);
    rpc UpdateNoticeMulti(UpdateNoticeMultiRequest) returns (UpdateNoticeMultiResponse);

    rpc UpdateBackgroundImage(UpdateBackgroundImageRequest) returns (UpdateBackgroundImageResponse);
    rpc UpdateBackgroundImageMulti(UpdateBackgroundImageMultiRequest) returns (UpdateBackgroundImageMultiResponse);

    rpc UpdateSlideImages(UpdateSlideImagesRequest) returns (UpdateSlideImagesResponse);
    rpc UpdateSlideImagesMulti(UpdateSlideImagesMultiRequest) returns (UpdateSlideImagesMultiResponse);

    rpc UpdateSound(UpdateSoundRequest) returns (UpdateSoundResponse);
    rpc UpdateSoundMulti(UpdateSoundMultiRequest) returns (UpdateSoundMultiResponse); 

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetConfigMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DisplayServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UpdateLanguagePack': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateLanguagePack,
          request_deserializer=display__pb2.UpdateLanguagePackRequest.FromString,
          response_serializer=display__pb2.UpdateLanguagePackResponse.SerializeToString,
      ),
      'UpdateLanguagePackMulti': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateLanguagePackMulti,
          request_deserializer=display__pb2.UpdateLanguagePackMultiRequest.FromString,
          response_serializer=display__pb2.UpdateLanguagePackMultiResponse.SerializeToString,
      ),
      'GetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=display__pb2.GetConfigRequest.FromString,
          response_serializer=display__pb2.GetConfigResponse.SerializeToString,
      ),
      'SetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfig,
          request_deserializer=display__pb2.SetConfigRequest.FromString,
          response_serializer=display__pb2.SetConfigResponse.SerializeToString,
      ),
      'SetConfigMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfigMulti,
          request_deserializer=display__pb2.SetConfigMultiRequest.FromString,
          response_serializer=display__pb2.SetConfigMultiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'display.Display', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
