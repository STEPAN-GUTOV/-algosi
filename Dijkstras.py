def errazeuglysymbols(s):
    return s.replace('\'', '').replace('[', '').replace(']', '')

class node():
    def __init__(self,name,  edges = {}):
        self.name = name
        self.edges = edges
        graph.append(self)
    def set_edges(self, edges = {}):
        self.edges = edges
    def __repr__(self):
        return str( str(self.name))
    def __str__(self):
        return str( str(self.name) + ': [' +errazeuglysymbols(str([i.name +' : ' + str(self.edges[i]) for i in self.edges])) + ']')

 
graph = []
kniga = node('kniga')
repl = node('repl')
poster = node('poster')
baroban = node('baroban')
bass = node('bass')
piano = node('piano')
kniga.set_edges({repl:5, poster:0})
repl.set_edges({bass:15, baroban:20})
poster.set_edges({bass:30, baroban:35})
bass.set_edges({piano:20})
baroban.set_edges({piano:10})

print(graph)
def Dijkstraalg(graph):
    def find_lowest_cost_node(costs, processed):
        lowest_cost_node = None
        lowest_cost = int('99999999999999')
        for i in costs:
            cost = costs[i]
            if cost < lowest_cost and i not in processed:
                lowest_cost = cost
                lowest_cost_node = i
        return lowest_cost_node
    parents = {}
    costs = {}
    processed = []
    sstart = graph[0]
    for i in sstart.edges:
        parents[i] = sstart
    for i in sstart.edges:
        costs[i] = sstart.edges[i]
    processed.append(sstart)
    node = find_lowest_cost_node(costs, processed)

    while node is not None:
        neighbors = node.edges

        for i in neighbors:

            if i not in costs:
                costs[i] = costs[node] + node.edges[i]
                parents[i] = node
            else:
                if costs[i] > costs[node] + node.edges[i]:

                    costs[i] = costs[node] + node.edges[i]
                    parents[i] = node

        node = find_lowest_cost_node(costs, processed)
        processed.append(node)
    way = []
    x = graph[-1]
    way.append(graph[-1])
    print(parents)
    while x != graph[0]:
        way.append(parents[x])
        x = parents[x]


   
    return(costs[graph[-1]], way[::-1])

print(Dijkstraalg(graph))
