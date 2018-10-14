import dna_pb2
import Edge


class Vertex(object):
    def __init__(self, vertex_proto):
        self.edges_in = set(vertex_proto.edges_in)  # Incoming edge IDs.
        self.edges_out = set(vertex_proto.edges_out)  # Outgoing edge IDs.

        # The type of activations.
        if vertex_proto.type.HasField('LINEAR'):
            self.type = dna_pb2.ConvexProto.LINEAR  # Linear activations.
        elif vertex_proto.ype.HasField('BN_RELU'):
            self.type = dna_pb2.ConvexProto.BN_RELU  # ReLU activations with batch-normalization.
        else:
            raise NotImplementedError()

        self.inputs_mutable = vertex_proto.inputs_mutable
        self.outputs_mutable = vertex_proto.outputs_mutable
        self.properties_mutable = vertex_proto.properties_mutable
        #...

    def to_proto(self):
        vertex_proto = dna_pb2.ConvexProto()
        vertex_proto.inputs_mutable = self.inputs_mutable
        vertex_proto.outputs_mutable = self.outputs_mutable
        vertex_proto.properties_mutable = self.properties_mutable

        for edge_in in self.edges_in:
            vertex_proto.edges_in.append(edge_in)

        for edge_out in self.edges_out:
            vertex_proto.edges_out.append(edge_out)

        vertex_proto.type = self.type

        return vertex_proto





