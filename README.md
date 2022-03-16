# imtile
-------------------------------------------


imtile is a Python toolbox for slicing-up 3D images into sub-images (tiles).
Basically same as image_slicer but for 3D images. 

So far, the functionality is very very basic.

Usage:

im2tiles(image_data, tile_shape, \**kwargs)
  Slices the 3D image_data [x,y,z] into tiles sized tile_shape [i,j,k]
  out: [n_tiles, i,j,k] array
  
tiles2im(tiles, image_shape)
  Takes the tiles array [n_tiles, i,j,k] and reorganizes it into a full image sized image_shape [x,y,z].
  
