import networkx as nx
import matplotlib.pyplot as plt
import time

class Graph:
    def __init__(self, v):
        self.V = v
        self.adjList = [[] for _ in range(v)]

    def addEdge(self, v, w):
        self.adjList[v].append(w)
        self.adjList[w].append(v)  

    def greedyColoring(self):
        start_time = time.time()  
        
        result = [-1] * self.V
        result[0] = 0  

        available = [True] * self.V

        for u in range(1, self.V):
            for i in self.adjList[u]:
                if result[i] != -1:
                    available[result[i]] = False

            cr = 0
            while not available[cr]:
                cr += 1

            result[u] = cr

            available = [True] * self.V

        maxColor = max(result) + 1

        G = nx.Graph()

        for v in range(self.V):
            for w in self.adjList[v]:
                G.add_edge(v, w)

        plt.title('Colored Graph')
        pos = nx.spring_layout(G)
        nx.draw(G, pos, node_color=result, cmap=plt.cm.tab10, with_labels=True)
        plt.show()

        print("Minimum number of colors required:", maxColor)
        print("Node colorings:")
        for i in range(self.V):
            print("Node", i, "-> Color", result[i]+1)

        end_time = time.time() 
        print("Runtime:", end_time - start_time, "seconds")  

if __name__ == "__main__":
    file_path = r"Path 5"
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            V, E = map(int, lines[0].split())  
            graph = Graph(V)

            for line in lines[1:]:  
                src, dest = map(int, line.split())
                graph.addEdge(src, dest)

            print("Dataset:", V, "nodes,", E, "edges")
            graph.greedyColoring()
            print()

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred:", e)
