from Graph import Graph

def testing():
    gp = Graph()
    gp.insert_node('a')
    gp.insert_node('b')
    gp.insert_node('c')
    gp.insert_node('d')
    gp.insert_node('e')

    gp.insert_edge('a','b',10)
    gp.insert_edge('a','c',20)
    gp.insert_edge('c','d',5)
    gp.insert_edge('d','e',15)

    print(gp.test_dfs('a','e'))

testing()