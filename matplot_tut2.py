import numpy as np
from matplotlib import pyplot as plt

n_groups = 5

means_men = (20, 35, 30, 35, 27)
std_men = (2, 3, 4, 1, 2)

means_women = (-25, -32, -34, -20, -25)
std_women = (3, 5, 2, 3, 3)

fig, ax = plt.subplots()
score_max = max(max(means_men),max(means_women))
index = np.arange(n_groups)
score_index = np.arange(-score_max,score_max+5,5)

bar_width = 0.35

opacity = 0.8
error_config = {'ecolor': '0.3'}

#rects1 = ax.bar(index, means_men, bar_width,
 #               alpha=opacity, color='b',
  #              yerr=std_men, error_kw=error_config,
   #             label='Men')

#rects2 = ax.bar(index, means_women, bar_width,
 #               alpha=opacity, color='r',
  #              yerr=std_women, error_kw=error_config,
   #             label='Women')
   
rects1 = ax.barh(index, means_men, bar_width,
                alpha=opacity, color='b', error_kw=error_config,
                label='Men')

rects2 = ax.barh(index, means_women, bar_width,
                alpha=opacity, color='r', error_kw=error_config,
                label='Women')   

ax.set_xlabel('Group')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(score_index)
ax.set_yticks(index)
#ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
ax.legend()

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('zero')
#ax.gca().spines['left'].set_position((0,'data'))
#ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')

fig.tight_layout()
plt.show()