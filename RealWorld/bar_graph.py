from pylab import *
from real_world_data import real_world_data

# === Main ===

n = 5

gdp, labels = real_world_data(n)

bar(arange(n), gdp, align='center')
xticks(arange(n), labels, rotation=-10)

for i, val in enumerate(gdp):
    text(i, val/2, str(val), va='center', ha='center', color='yellow')

ylabel('$ in Billions')
xlabel('Country')
title('GDP Rank from CIA World Fact Book')
show()
