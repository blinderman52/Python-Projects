from pylab import *
from real_world_data import real_world_data

# === Main ===

n = 10

gdp, tags = real_world_data(n)

pie(gdp, labels=tags)
axis('equal')

title('GDP Rank from CIA World Fact Book')
show()