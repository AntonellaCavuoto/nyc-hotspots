import copy
import random

from database.DAO import DAO
import networkx as nx
from geopy.distance import geodesic


class Model:
    def __init__(self):
        self._bestScore = 0
        self._bestPath = []
        self._graph = nx.Graph()
        #self._idMap = {}

    def getProvider(self):
        return DAO.getProvider()

    def getLocations(self, provider):
        return DAO.getNodes(provider)

    def buildGraph(self, provider, distanza):
        nodes = DAO.getNodes(provider)
        # self._idMap = {}
        # for n in nodes:
        #     self._idMap[n.OBJECTID] = n

        self._graph.add_nodes_from(nodes)

        edges = DAO.getEdges(provider)
        for edge in edges:
            loc1 = edge[0]
            loc2 = edge[1]
            distance = geodesic((loc1.n1Lat, loc1.n1Lang), (loc2.n1Lat, loc2.n1Lang)).km
            if distance < distanza:
                self._graph.add_edge(loc1.n1Loc, loc2.n1Loc, weight=distance)

        return self._graph.number_of_nodes(), self._graph.number_of_edges()


    def getVicini(self):
        numVicini = 0
        nodi = []
        for n in self._graph.nodes:
            vicini = list(nx.neighbors(self._graph, n))
            if len(vicini) >= numVicini:
                numVicini = len(vicini)

        for n in self._graph.nodes:
            vicini = list(nx.neighbors(self._graph, n))
            if len(vicini) == numVicini:
                nodi.append(n)

        return nodi, numVicini

    def getBestPath(self, target, stringa):
        self._bestPath = []
        self._bestScore = 0
        nodi, numVicini = self.getVicini()
        nodo = nodi[random.randint(0, len(nodi)-1)]

        parziale = [nodo]

        for n in list(nx.neighbors(self._graph, nodo)):
            if not stringa.lower() in n.lower():
                parziale.append(n)
                self._ricorsione(parziale, stringa, target)
                parziale.pop()

        return self._bestPath, self._bestScore, nodo

    def _ricorsione(self, parziale, stringa, target):
        if parziale[-1] == target and len(parziale) > self._bestScore:
            self._bestScore = len(parziale)
            self._bestPath = copy.deepcopy(parziale)
            return
        else:
            for n in list(nx.neighbors(self._graph, parziale[-1])):
                if n not in parziale:
                    if not stringa.lower() in n.lower():
                        parziale.append(n)
                        self._ricorsione(parziale, stringa, target)
                        parziale.pop()





