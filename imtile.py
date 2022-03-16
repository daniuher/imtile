#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:19:44 2022

@author: g10060008
"""
import numpy as np


def getTileCoords(im_shape, tile_shape):
    
    """
    tileCoords = getTileCoords(im, tile_shape)
    
    This function returns the coordinates (i.e. indices) for each 3D tile 
    extracted from the 3D image.
    
    im        ... [x,y,z] the full image data
    tile_shape  ... (i,j,k) tuple i.e. (10,10,10) will results in tiles 10x10x10  
    """    
       
    """ method 2 """
    x_inds = np.arange(0,im_shape[0]+1, tile_shape[0])
    y_inds = np.arange(0,im_shape[1]+1, tile_shape[1])
    z_inds = np.arange(0,im_shape[2]+1, tile_shape[2])
    tile_indices = list()
    
    for i in range(len(x_inds)-1):
        # print(str(i))
        for j in range(len(y_inds)-1):
            for k in range(len(z_inds)-1):
                tile_indices.append([x_inds[i:i+2], y_inds[j:j+2], z_inds[k:k+2]])    
    
  
    return tile_indices


def im2tiles(im, tile_shape, expand_final_dim='False'):
    
    """
    tiles = im2tiles(image, tile_shape)
    
    This function takes a 3D image and splits it into sub-images, i.e. tiles
    
    out:
    ----
    tiles       ... [n_tiles, (tile_shape)] all the tiles extracted from the image    
    
    
    in:
    ---    
    image       ... [x,y,z] image data
    tile_shape  ... (i,j,k) tuple i.e. (10,10,10) will results in tiles 10x10x10  
    (optional) expand_final_dim ... expands the final tiles output by one dimension
                                    at the end. This is for input into CNNs
    """
    
    c = 0
    alongXs = np.array_split(im, im.shape[0]/tile_shape[0], axis=0)   
    
    for alongX in alongXs:
        alongYs = np.array_split(alongX, im.shape[1]/tile_shape[1], axis=1)
        
        
        for alongY in alongYs:
            alongZs = np.array_split(alongY, im.shape[2]/tile_shape[2], axis=2)    
            
            
            if c == 0:
                tiles = np.concatenate([alongZs])          
                c = 1
            else:
                tiles = np.concatenate([tiles, alongZs])
               
    if expand_final_dim == 'True':  
        return np.expand_dims(tiles, axis=-1)  
    else: 
        return tiles
    
    
    
def tiles2im(tiles, im_shape):
  
    """
    im = tiles2im(tiles, im_shape)
    
    This function is the reverse for the im2tiles function. The tiles are 
    arranged back into a 3D image.
    
    out:
    ----
    im        ... [im_shape] image reconstructed from the tiles    
    
    
    in:
    ---
    tiles     ... list of the tiles [n_tiles, tile_shape_x, tile_shape_y, tile_shape_z]
    im_shape  ... (i,j,k) tuple with the dimensions of the output image
    
    """
    
    if len(tiles.shape) == 5:
        tiles = np.squeeze(tiles, axis=-1)
    
    im = np.zeros(im_shape)
    
    # print("Getting tile coordinates ...")
    tile_indices = getTileCoords(im_shape, tiles[0,:,:,:].shape)
    
    # print("Reconstructing full image ...")
    for i in range(tiles.shape[0]):
        im[tile_indices[i][0][0]:tile_indices[i][0][1],   
           tile_indices[i][1][0]:tile_indices[i][1][1],
           tile_indices[i][2][0]:tile_indices[i][2][1]] = tiles[i,:,:,:]
            
                
    return im            