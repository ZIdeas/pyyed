import pyyed

g = pyyed.Graph()

n0 = g.add_node("node0", label = "my node")

group1 = g.add_group("main1", label = "My group")
n11 = group1.add_node("node11")
group12 = group1.add_group("sub12")
n121 = group12.add_node("node121")
group122 = group12.add_group("sub122")


g.add_edge('node11', 'node0', label="EDGE!", width="3.0", color="#0000FF",
           arrowhead="dash", arrowfoot="standard", line_type="line")

g.add_edge('main1', 'node0', label="EDGE!", width="3.0", color="#0000FF",
           arrowhead="dash", arrowfoot="standard", line_type="line")



g.write_graph('test.2.graphml')

f = open('test.2.graphml')

with f as f1:
    print(f1.read())
