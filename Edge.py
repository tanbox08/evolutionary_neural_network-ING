import dna_pb2

class Edge(object):

    def __init__(self, edge_proto):
        self.from_vertex = edge_proto.from_vertex  # Source vertex ID.
        self.to_vertex = edge_proto.to_vertex  # Destination vertex ID.

        if edge_proto.type.HasField('CONV'):
            self.type = dna_pb2.EdgeProto.CONV
            self.depth_factor = edge_proto.conv.depth_factor

            self.filter_half_width = edge_proto.conv.filter_half_width
            self.filter_half_height = edge_proto.conv.filter_half_height
            self.stride_scale = edge_proto.conv.stride_scale

        elif edge_proto.type.HasField('IDENTITY'):
            self.type = dna_pb2.EdgeProto.IDENTITY
        else:
            raise NotImplementedError()

        self.depth_precedence = edge_proto.depth_precedence
        self.scale_precedence = edge_proto.scale_precedence

    def to_proto(self):
        edge_proto = dna_pb2.EdgeProto()
        edge_proto.from_vertex = self.from_vertex
        edge_proto.to_vertex = self.to_vertex
        edge_proto.depth_precedence = self.depth_precedence
        edge_proto.scale_precedence = self.scale_precedence
        edge_proto.type = self.type
        if edge_proto.type.HasField('CONV'):
            edge_proto.conv.depth_factor = self.depth_factor
            edge_proto.conv.filter_half_width = self.filter_half_width
            edge_proto.conv.filter_half_height = self.filter_half_height
            edge_proto.conv.stride_scale = self.stride_scale


