#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 18:00:40 2021

@author: root
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from scipy import interp
from PIL import Image
import cv2
import os

def save_img(phase_imga,fileName):

    plt.imsave(fileName,disigmoidScaling(phase_imga, 20),dpi=600,  cmap='jet')
    
 
img_dir=os.listdir('../results/visualization/')
img_num=80
for  i in range(img_num):
     img_name=str(i)+'_ori.tiff'
     pred_name=str(i)+'_8_pred.tiff'
     img=Image.open('../results/visualization/'+img_name).convert('RGB')
     img=np.array(img)
     pred=Image.open('../results/visualization/'+pred_name).convert('L')
     pred = pred.resize((img.shape[1],img.shape[0]),Image.ANTIALIAS)
     
     heatmap=np.array(pred)

     heatmap=cv2.normalize( heatmap, None, alpha = 0, beta = 255, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_32F)
     heatmap = cv2.applyColorMap(np.uint8(heatmap), cv2.COLORMAP_JET)
     heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)
     heatmap = np.float32(heatmap)  /255 
     
     cam = heatmap + (img/255)
     cam = cam / np.max(cam)
     cm=np.uint8(255 * cam)
     
     save_name='../results/visualization/'+'ori_'+img_name
     img=img[22:874,17:1294]
     heatmap=heatmap[22:874,17:1294]
     cm=cm[22:874,17:1294]
  
     save_name1='../results/visualization/'+img_name
     plt.imsave(save_name1,img,dpi=600) 
     save_name2='../results/visualization/'+'map_'+img_name
     plt.imsave(save_name2,heatmap,dpi=600) 
     save_name3='../results/visualization/'+'cm_'+img_name
     plt.imsave(save_name3,cm,dpi=600) 
     print(save_name)
   
     
#     plt.imsave(save_name1,img,dpi=600,  cmap='jet')

#
#
#
#
#
#
#
#
#
#
