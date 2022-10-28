import matplotlib.pyplot as plt
import networkx as nx
import osmnx as ox

# get graphs of different infrastructure types, then combine
place = 'Manchester, UK'
G1 = ox.graph_from_place(place, custom_filter='["highway"~"primary|motorway|tertiary"]')
G2 = ox.graph_from_place(place, custom_filter='["waterway"~"canal"]')
G = nx.compose(G1, G2)

# get building footprints
fp = ox.geometries_from_place(place, tags = {"building": ['commercial','retail','residential','hotel','supermarket','cathedral'],
                                             "railway": ['light_rail','rail'],
                                             "leisure": ['park',"marina", 'nature_reserve'],
                                             "boundary": 'postal_code'}, buffer_dist=1000)

# plot highway edges in yellow, canal edges in blue
ec = ['y' if 'highway' in d else 'b' for _, _, _, d in G.edges(keys=True, data=True)]
fig, ax = ox.plot_graph(G, bgcolor='k', edge_color=ec,
                        node_size=0, edge_linewidth=0.5,
                        show=False, close=False)

# add footprints in 50% opacity white
fp.plot(ax=ax, color='w', alpha=0.5)
plt.show()