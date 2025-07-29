# SABTA

Sabta stands for Smart Ai Based Try-on Assistant

The way it works is by taking input of 2 images, image of the user and image of the cloth they are wanting to try on!

Then it processes the image of the cloth by going through a Cloth Segmentation process which uses Happyface Transformers (Pre-learnt Datasets) to segment the clothes from the given image into clear masks.

These masks are then copied into the dataset used by VITON-HD which is pre-made AI ML library that uses diffusion to virtually try on the clothes.

Finally, the result is generated and the user can see how the cloth looks on them!
