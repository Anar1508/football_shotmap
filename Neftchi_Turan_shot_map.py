#!/usr/bin/env python
# coding: utf-8

# In[108]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch
from matplotlib import font_manager
import matplotlib.image as mpimg


# In[99]:


shot_data = pd.read_csv('Downloads\\events (2).csv')
shot_data


# In[6]:


shot_data['result'] = ['Goal', 'Blocked', 'Blocked', 'Saved', 'Goal', 'Missed', 'Saved', 'Saved', 'Missed', 'Blocked', 'Missed'
                    , 'Blocked', 'Missed', 'Missed','Missed','Saved','Goal', 'Blocked', 'Blocked', 'Blocked', 'Missed','Blocked',
                    'Missed', 'Missed', 'Missed']
shot_data


# In[8]:


shot = shot_data.drop(columns = ['Player', 'Event', 'Mins', 'Secs', 'X2', 'Y2' ])
shot


# In[34]:


shot.loc[4, 'Y'] = 50.5
shot


# In[156]:


pitch = Pitch(pitch_type='statsbomb', line_color='#021c29', pitch_color='#e4d6a7', line_zorder=2)
fig, ax = pitch.draw()
fig.set_facecolor('#e4d6a7')

goal_shots = shot[shot['result'] == 'Goal']
ax.scatter(goal_shots['X'], goal_shots['Y'], color='red', label='Qol', edgecolors='black', zorder=6, s=100)

not_goal_shots = shot[shot['result'] != 'Goal']
ax.scatter(not_goal_shots['X'], not_goal_shots['Y'], color='#eaebed', label='Zərbə', edgecolors='black', zorder=6, s=100)

turan_logo = mpimg.imread('Downloads\\Turan_Tovuz_İK_loqo.png')  

x_position = 63 
y_position = 13 
width = 10      
height = -10      

plt.imshow(turan_logo, extent=[x_position, x_position + width, y_position, y_position + height])

neftci_logo = mpimg.imread('Downloads\\Нефтчи_Баку_logo.png')  

x_position = 47  
y_position = 13  
width = 10     
height = -12     

plt.imshow(neftci_logo, extent=[x_position, x_position + width, y_position, y_position + height])
    
font_dirs = ['\\Windows\\Fonts']
font_files = font_manager.findSystemFonts(fontpaths = font_dirs)
for font_file in font_files:
    font_manager.fontManager.addfont(font_file)
                                          
plt.rcParams['font.family'] = 'American Captain'
       
title_font = {'fontsize': 32, 'fontweight': 'bold', 'fontfamily': 'American Captain', 'color': '#021c29'}
plt.title('Neftçi Bakı 3 - 0 Turan Tovuz', fontdict = title_font, loc = 'center', x= 0.41 , y = 1, pad = 7)
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.03), ncol=2, facecolor = '#e4d6a7', edgecolor = '#e4d6a7')


###################

font_dirs = ['C:\\Users\\Lenovo\\AppData\\Local\\Microsoft\\Windows\\Fonts']
font_files = font_manager.findSystemFonts(fontpaths = font_dirs)
for font_file in font_files:
    font_manager.fontManager.addfont(font_file)
                                          
plt.rcParams['font.family'] = 'Arial'

plt.text(37, -1.5, 'Misli premyer liqası, 32-ci tur: 28.04.2024 ',color = '#503d2e', fontfamily='Arial',fontsize=12, ha='center',fontstyle='italic', fontweight = 'bold')

plt.savefig('Neftchi_Turant', dpi=300) 

plt.show()


# In[ ]:




