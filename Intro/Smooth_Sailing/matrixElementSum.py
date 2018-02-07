#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 17:01:23 2018

@author: alexpm94
"""

def matrixElementsSum(matrix):
    noZ=0 #stands for non zero elments
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]==0:
                try:
                    if not matrix[row+1][col]==0:
                        matrix[row+1][col]=0
                except IndexError:
                    pass
            else:
                noZ+=matrix[row][col]
    return noZ

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
print(matrixElementsSum(matrix))