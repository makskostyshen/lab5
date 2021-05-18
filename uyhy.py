import math

lis1 = [1, 3, 4, 5]
lis2 = [1, 3, 2, 4]

n = 4
rad = 4
angle = 2*math.pi/n

x = [rad*math.sin(i*angle) for i in range(n)]
y = [rad*math.cos(i*angle) for i in range(n)]

zip((list(zip(x, y))))



print(list(zip(lis1, lis2)))



#n = 8
#rad = 4
#angle = 2*math.pi/n

#x = [rad*math.sin(i*angle) for i in range(n)]
#y = [rad*math.cos(i*angle) for i in range(n)]

#lay = dict(zip(g, (list(zip(x, y)))))
#nx.draw(g, lay)



#gg = nx.petersen_graph()
#nx.draw(gg)
#my_layout = zip(g.nodes, [1, 3, 2, 3, 4])

#gg = nx.petersen_graph()
#lay = nx.shell_layout(g, nlist=[range(5,10), range(0,5)], rotate=0)
#plt.axes().set_aspect('equal', adjustable='datalim')
#nx.draw(gg, pos=lay, with_labels=True, font_weight='bold', font_color='white')


#nx.draw_shell(g)



