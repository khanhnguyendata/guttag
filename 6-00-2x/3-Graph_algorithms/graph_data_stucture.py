class Node:
    """
    Represent a graph node
    """
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """
        Return the name of the node
        :return: name of node (str)
        """
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return str(self.name)


class Edge:
    def __init__(self, source, destination):
        """
        Store source node and destination node object as attribute to edge object
        :param source: source node object
        :param destination: destination node object
        """
        self.source = source
        self.destination = destination

    def get_source(self):
        """
        Return the source node of the edge
        :return: source node of edge (str)
        """
        return self.source

    def get_destination(self):
        """
        Return the destination node of the edge
        :return: destination node of the edge (str)
        """
        return self.destination

    def __str__(self):
        return f'{self.source.get_name()} -> {self.destination.get_name()}'


class Graph:
    def __init__(self):
        self.edges = {}
        self.nodes = []
        self.node_names = [node.get_name() for node in self.nodes]

    def add_node(self, node):
        """
        Add a node to a graph
        :param node: Node class object
        :return: edges attribute updated with node name as key, and blank list as list of destinations to that node
        """
        if node.get_name() in self.node_names:
            error = 'Node already exists in graph'
            raise ValueError(error)
        else:
            self.edges[node] = []
            self.nodes.append(node)
            self.node_names.append(node.get_name())

    def add_edge(self, edge):
        """
        Add an edge to a graph when nodes after nodes have been added
        :param edge: Edge class object
        :return: update the source node in edge with the destination node in edge
        """
        source = edge.get_source()  # return Node object
        destination = edge.get_destination()  # return Node object
        if source not in self.nodes or destination not in self.nodes:
            error = 'Node does not exist in graph yet. Please add node before adding edge.'
            raise ValueError(error)
        else:
            self.edges[source].append(destination)

    def get_destination(self, node):
        """
        Get destination nodes of a node in the graph
        :return: a node object in the graph
        """
        return self.edges[node]

    def __str__(self):
        display = ''
        for source, destinations in self.edges.items():
            for destination in destinations:
                display += f'{source.get_name()} -> {destination.get_name()}\n'

        return display[:-1]


def path_display(path):
    """
    Display a path with the nodes inside it
    :param path: path containing nodes going from left to right
    :return: str displaying node 1 -> node 2 -> ... -> node n
    """
    display = ''
    for index, node in enumerate(path):
        display += f'{node}'
        if index < len(path) - 1:
            display += ' -> '

    return display


def dfs(graph, start, end, path, shortest):
    """
    Find the shortest path between 2 nodes in a graph using depth-first search
    :param graph: Graph object with all nodes and edges added
    :param start: starting Node object
    :param end: ending Node object
    :param path: current path
    :param shortest: current shortest path
    :return: shorted path (in list of Node objects) from start node to end node
    """
    path = path + [start]

    if start == end:
        return path

    destinations = graph.get_destination(start)
    for destination in destinations:
        if destination in path:
            return shortest
        elif (not shortest) or len(path) < len(shortest):
            shortest = dfs(graph, destination, end, path, shortest)

    return shortest


def main():
    graph = Graph()
    nodes = []

    # Build node list
    for num in range(6):
        nodes.append(Node(num))

    # Add nodes from node list to graph
    for node in nodes:
        graph.add_node(node)

    # Add edges
    edge_vertices = [(0, 1), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5), (0, 2), (1, 0), (3, 1), (4, 0)]
    for source, destination in edge_vertices:
        graph.add_edge(Edge(Node(source), Node(destination)))

    # Find shortest path using depth-first search
    dfs_result = dfs(graph, Node(0), Node(5), [], [])
    print(path_display(dfs_result))


if __name__ == '__main__':
    main()