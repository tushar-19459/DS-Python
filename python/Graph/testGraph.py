from Graph import Graph

def testing():
    gp = Graph()
    gp.insert_node('a')
    gp.insert_node('b')
    gp.insert_node('c')
    gp.insert_node('d')
    gp.insert_node('e')
    print(gp.get_count())

    print(gp._is_node_('a'))

    gp.insert_edge('a','b',10)
    gp.insert_edge('a','c',20)
    gp.insert_edge('c','d',5)
    gp.insert_edge('d','e',15)

    print(gp.get_edgeCost('e','d'))
    


testing()