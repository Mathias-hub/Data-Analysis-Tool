import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns

### DEFINE DATA ###
planets = sns.load_dataset('planets')

###### MAKE THE GUI ######

### DEFINE MAIN GUI CANVAS WINDOW ###
root= tk.Tk()   
root.title("Data Analysis Tool")
root.geometry('1000x500')

### Add Seaborn plot
figure1 = plt.Figure(figsize=(6,4), dpi=50)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(fill=tk.X)
g = sns.catplot("year", data=planets, aspect=2,
                       kind="count", color='steelblue',ax=ax1)
#g.set_xticklabels(step=5)
ax1.set_title('An Awesome Bar Plot')

### Add Some info stuff
figure2 = plt.Figure(figsize=(6,4), dpi=100)
ax2 = figure2.add_subplot(111)
bar2 = FigureCanvasTkAgg(figure2, root)
bar2.get_tk_widget().pack(fill=tk.X)
planets.plot(kind='line', legend=True, ax=ax2)

ax1.set_title('An Awesome Bar Plot')

#g.set_ylabels('Number of Planets Discovered')

root.mainloop()