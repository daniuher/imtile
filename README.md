# imtile
-------------------------------------------


**imtile** is a Python toolbox for slicing-up 3D images into sub-images (tiles). Matrices into sub-matrices.
Furthermore, it can reconstruct the image back from the tiles.
Basically same as [image_slicer](https://github.com/samdobson/image_slicer) but for 3D images. 

So far, the functionality is very very basic and not tested much. There are some libraries available for this,
but I wanted something super simple and fast. This is it, just three functions altogether and it works in seconds.

Usage:

```
tiles = im2tiles(image_data, tile_shape, **kwargs)
```
  Slices the 3D image_data [x,y,z] into tiles sized tile_shape [i,j,k]
  out: [n_tiles, i,j,k] array

```
image = tiles2im(tiles, image_shape)
```  
  Takes the tiles array [n_tiles, i,j,k] and reorganizes it into a full image sized image_shape [x,y,z].
  
