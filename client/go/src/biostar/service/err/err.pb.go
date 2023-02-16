// Code generated by protoc-gen-go. DO NOT EDIT.
// source: err.proto

package err

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	grpc "google.golang.org/grpc"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type ErrorResponse struct {
	DeviceID             uint32   `protobuf:"varint,1,opt,name=deviceID,proto3" json:"deviceID,omitempty"`
	Code                 int32    `protobuf:"varint,2,opt,name=code,proto3" json:"code,omitempty"`
	Msg                  string   `protobuf:"bytes,3,opt,name=msg,proto3" json:"msg,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ErrorResponse) Reset()         { *m = ErrorResponse{} }
func (m *ErrorResponse) String() string { return proto.CompactTextString(m) }
func (*ErrorResponse) ProtoMessage()    {}
func (*ErrorResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_b4a1db73bc95ee8c, []int{0}
}

func (m *ErrorResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ErrorResponse.Unmarshal(m, b)
}
func (m *ErrorResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ErrorResponse.Marshal(b, m, deterministic)
}
func (m *ErrorResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ErrorResponse.Merge(m, src)
}
func (m *ErrorResponse) XXX_Size() int {
	return xxx_messageInfo_ErrorResponse.Size(m)
}
func (m *ErrorResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_ErrorResponse.DiscardUnknown(m)
}

var xxx_messageInfo_ErrorResponse proto.InternalMessageInfo

func (m *ErrorResponse) GetDeviceID() uint32 {
	if m != nil {
		return m.DeviceID
	}
	return 0
}

func (m *ErrorResponse) GetCode() int32 {
	if m != nil {
		return m.Code
	}
	return 0
}

func (m *ErrorResponse) GetMsg() string {
	if m != nil {
		return m.Msg
	}
	return ""
}

func init() {
	proto.RegisterType((*ErrorResponse)(nil), "err.ErrorResponse")
}

func init() { proto.RegisterFile("err.proto", fileDescriptor_b4a1db73bc95ee8c) }

var fileDescriptor_b4a1db73bc95ee8c = []byte{
	// 165 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x3c, 0xce, 0x31, 0xcb, 0x82, 0x50,
	0x14, 0xc6, 0x71, 0xee, 0xeb, 0x6b, 0xe5, 0x01, 0x21, 0x6e, 0x10, 0xd2, 0x24, 0x4d, 0x4e, 0x57,
	0xa8, 0x6f, 0x10, 0x35, 0xb4, 0xd5, 0x1d, 0xdb, 0xf4, 0x7a, 0x08, 0x09, 0x3d, 0xf2, 0x1c, 0xeb,
	0xf3, 0x87, 0x0e, 0x6d, 0xff, 0x67, 0xf9, 0xf1, 0x50, 0xc2, 0x80, 0x1b, 0x20, 0xa3, 0xd8, 0x88,
	0x81, 0xfd, 0x9d, 0xd2, 0x0b, 0x20, 0xf0, 0xac, 0x83, 0xf4, 0xca, 0x76, 0x47, 0xab, 0x86, 0x3f,
	0x6d, 0xe0, 0xeb, 0x39, 0x33, 0xb9, 0x29, 0x52, 0xff, 0xdb, 0xd6, 0xd2, 0x7f, 0x90, 0x86, 0xb3,
	0xbf, 0xdc, 0x14, 0xb1, 0x9f, 0xdb, 0xae, 0x29, 0xea, 0xf4, 0x99, 0x45, 0xb9, 0x29, 0x12, 0x3f,
	0xe5, 0x61, 0x49, 0xf1, 0x4c, 0x9e, 0x4a, 0xda, 0x06, 0xe9, 0x9c, 0xbe, 0x07, 0x70, 0x57, 0xb5,
	0x7d, 0x70, 0xda, 0xbc, 0x1c, 0x03, 0x37, 0xf3, 0xd8, 0xd4, 0xad, 0xe8, 0x58, 0xa1, 0x54, 0xc6,
	0xa4, 0x97, 0x0c, 0xd4, 0x8b, 0xf9, 0xd8, 0xf1, 0x1b, 0x00, 0x00, 0xff, 0xff, 0x3f, 0xb4, 0x0e,
	0x8d, 0xa5, 0x00, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// ErrorClient is the client API for Error service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type ErrorClient interface {
}

type errorClient struct {
	cc *grpc.ClientConn
}

func NewErrorClient(cc *grpc.ClientConn) ErrorClient {
	return &errorClient{cc}
}

// ErrorServer is the server API for Error service.
type ErrorServer interface {
}

func RegisterErrorServer(s *grpc.Server, srv ErrorServer) {
	s.RegisterService(&_Error_serviceDesc, srv)
}

var _Error_serviceDesc = grpc.ServiceDesc{
	ServiceName: "err.Error",
	HandlerType: (*ErrorServer)(nil),
	Methods:     []grpc.MethodDesc{},
	Streams:     []grpc.StreamDesc{},
	Metadata:    "err.proto",
}
