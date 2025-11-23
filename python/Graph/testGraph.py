from Graph import Graph

# def testing():
#     gp = Graph()
#     gp.insert_node('a')
#     gp.insert_node('b')
#     gp.insert_node('c')
#     gp.insert_node('d')
#     gp.insert_node('e')

#     gp.insert_edge('a','b',10)
#     gp.insert_edge('a','c',20)
#     gp.insert_edge('c','d',5)
#     gp.insert_edge('d','e',15)

#     print(gp.test_dfs('a','e'))

# testing()

def testing():
    gp = Graph()

    # Insert nodes
    for i in range(10):
        gp.insert_node(str(i))

    # Insert edges based on your graph image
    gp.insert_edge('0', '1')
    gp.insert_edge('0', '2')

    gp.insert_edge('1', '2')
    gp.insert_edge('1', '3')
    gp.insert_edge('1', '4')

    gp.insert_edge('3', '5')

    gp.insert_edge('5', '6')
    gp.insert_edge('5', '7')
    gp.insert_edge('5', '8')

    gp.insert_edge('7', '8')
    gp.insert_edge('8', '9')

    # Run BFS from 0 to 9
    print(gp.bfs('0', '9')[::-1])

testing()
