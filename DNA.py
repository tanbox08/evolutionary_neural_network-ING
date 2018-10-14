import Vertex
import Edge
import dna_pb2


class DNA(object):
    def __init__(self, dna_proto):
        self.learning_rate = dna_proto.learning_rate

        self._vertices = {}  # String vertex ID to ‘Vertex‘ instance.
        for vertex_id in dna_proto.vertices:
            self._vertices[vertex_id] = Vertex(vertex_proto=dna_proto.vertices[vertex_id])       # attention?

        self._edges = {}  # String edge ID to ‘Edge‘ instance.
        for edge_id in dna_proto.edges:
            self._edges[edge_id] = Edge(edge_proto=dna_proto.edges[edge_id])
        # ...

    def to_proto(self):
        dna_proto = dna_pb2.DnaProto(learning_rate=self.learning_rate)

        for vertex_id, vertex in self._vertices.iteritems():
            dna_proto.vertices[vertex_id].CopyFrom(vertex.to_proto())

        for edge_id, edge in self._edges.iteritems():
            dna_proto.edges[edge_id].CopyFrom(edge.to_proto())

        # ...
        return dna_proto

    def add_edge(self, dna, from_vertex_id, to_vertex_id, edge_type, edge_id):
        edge = Edge(dna_pb2.EdgeProto(
            from_vertex=from_vertex_id, to_vertex=to_vertex_id, type=edge_type))
        self._edges[edge_id] = edge
        self._vertices[from_vertex_id].edges_out.add(edge_id)
        self._vertices[to_vertex_id].edges_in.add(edge_id)
        return edge



