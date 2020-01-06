import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns

### DEFINE DATA ###
planets = sns.load_dataset('planets')


### MAKE THE GUI ###
root= tk.Tk()   

### Add Seaborn plot
figure1 = plt.Figure(figsize=(6,4), dpi=150)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
sns.catplot("year", data=planets, aspect=2,
                       kind="count", color='steelblue',ax=ax1)

# Set the step size of the x-axis
#ax1.set_xticks(ax1.get_xticks()[::12])
ax1.set_title('An Awesome Bar Plot')



root.mainloop()