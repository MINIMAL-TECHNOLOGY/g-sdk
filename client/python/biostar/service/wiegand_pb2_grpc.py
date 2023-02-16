# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import wiegand_pb2 as wiegand__pb2


class WiegandStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetConfig = channel.unary_unary(
        '/wiegand.Wiegand/GetConfig',
        request_serializer=wiegand__pb2.GetConfigRequest.SerializeToString,
        response_deserializer=wiegand__pb2.GetConfigResponse.FromString,
        )
    self.SetConfig = channel.unary_unary(
        '/wiegand.Wiegand/SetConfig',
        request_serializer=wiegand__pb2.SetConfigRequest.SerializeToString,
        response_deserializer=wiegand__pb2.SetConfigResponse.FromString,
        )
    self.SetConfigMulti = channel.unary_unary(
        '/wiegand.Wiegand/SetConfigMulti',
        request_serializer=wiegand__pb2.SetConfigMultiRequest.SerializeToString,
        response_deserializer=wiegand__pb2.SetConfigMultiResponse.FromString,
        )


class WiegandServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
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


def add_WiegandServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=wiegand__pb2.GetConfigRequest.FromString,
          response_serializer=wiegand__pb2.GetConfigResponse.SerializeToString,
      ),
      'SetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfig,
          request_deserializer=wiegand__pb2.SetConfigRequest.FromString,
          response_serializer=wiegand__pb2.SetConfigResponse.SerializeToString,
      ),
      'SetConfigMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfigMulti,
          request_deserializer=wiegand__pb2.SetConfigMultiRequest.FromString,
          response_serializer=wiegand__pb2.SetConfigMultiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'wiegand.Wiegand', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
