
def main(g: list, s: int, e: int):
    """Computes fewest no. of edges from s to e using BFS

    Args:
        g (list): adjacency list (rows: nodes, cols: node that is connected to current node)
        s (int): starting vertex (starting from 1)
        e (int): vertex we want to reach (starting from 1)
    """
    cols = len(g[0])
    rows = len(g)
    queue = []

    distances = [float("inf")] * rows # we don't know the distances
    distances[s-1] = 0 # the distance from itself is 0

    mask = [0] * rows # initializing all nodes as unexplored
    mask[s-1] = 1 # mark s as explored

    queue.append(s)

    while len(queue) != 0:
        v = queue.pop(0) # removing first node of queue
        for edge in g[v-1][1:]:
            if edge == e:
                return distances[v-1] + 1
            elif mask[edge-1] == 0: # if unexplored
                queue.append(edge) # add edge to end of queue
                mask[edge-1] = 1 # mark as explored
                distances[edge-1] = distances[v-1] + 1 # the distance is 1+the node that discovered it

    


def to_graph(path: str):
    """Converts the txt file on given path to an adjacency list

    Args:
        path (str): path to txt file
    """
    with open(path, "r") as file:
        data = []
        for line in file:
            data.append([int(x) for x in line.strip().split()])
    return data




if __name__ == "__main__":
    graph = to_graph("data.txt")
    s = 1 # starting vertex
    e = 51 # ending vertex
    distance = main(graph, s, e)
    print(f"The shortest path from {s} to {e} is {distance}")