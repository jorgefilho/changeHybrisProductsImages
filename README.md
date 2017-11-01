# Change Hybris Products Images

This Project was inspired of a script created by @natanaelpantoja to facilitate the replacement of product images in Hybris with new images. According to that script,  I created this project to modify easily all products images using the new images collection. It use a SAP Hybris Commerce Accelerator Recipe to get all products imagens as reference and another folder with new images to substitute. The process is very simple.

## Important Information

- To have a good quality in this process the source images must be a good resolution. i recommended at least 1200px X 1200px.
- You must have the following programs installed and configured in your machine:
  - [Image Magick](http://www.imagemagick.org/script/download.php) 
  - [Python](https://www.python.org/downloads/)
  
## Directory Structure
  * sourceImages: Directory where must contain the new images with high resolution
  * generatedImages: The new directory structure with all new products images to be replaced in the products images folder in Hybris 
  
## How do use

1. First of all, get the project
```
$ git clone https://github.com/jorgefilho/changeHybrisProductsImages.git
```
2. Enter in the folder project
```
$ cd changeHybrisProductsImages
```
3. Execute the following command line
```
$ python changeIt.py  ${HYBRIS_INSTALATION}\bin\ext-data\electronicsstore\resources\electronicsstore\import\sampledata\productCatalogs\electronicsProductCatalog\images\30Wx30H'
```
  **The argument should be changed according to your necessity**
