from skimage import transform, util, color, io
import numpy as np


def image_augmentation(image_file, target_shape=(240, 240, 3)):
    
    """Image Augmentation

    Returns:
        _type_: _description_
    """
    image = io.imread(image_file)
    # Rotation
    angle = np.random.uniform(low=-40, high=40)
    image = transform.rotate(image, angle)

    # Shift
    width_shift = np.random.uniform(low=-0.2, high=0.2)
    height_shift = np.random.uniform(low=-0.2, high=0.2)
    image = transform.warp(image, transform.AffineTransform(translation=(width_shift, height_shift)))

    # Shear
    shear_range = np.random.uniform(low=-0.2, high=0.2)
    image = transform.warp(image, transform.AffineTransform(shear=shear_range))

    # Zoom
    zoom_range = np.random.uniform(low=0.8, high=1.2)
    image = transform.rescale(image, zoom_range)

    # Horizontal Flip
    if np.random.choice([True, False]):
        image = np.fliplr(image)

    # Fill mode 'nearest' - scikit-image warp doesn't have a direct equivalent
    # You may choose to use skimage.util.random_noise or other transformations for filling
    
    augmented_image = (image * 255).astype(np.uint8)
    
    # Convert to RGB if the image is in grayscale with an alpha channel
    if augmented_image.shape[-1] == 2:
        augmented_image = color.gray2rgb(augmented_image[:, :, 0])
        
    # Convert to RGB if the image is in RGBA format
    if augmented_image.shape[-1] == 4:
        augmented_image = color.rgba2rgb(augmented_image)
        
     # Ensure the image has 3 channels (RGB)
    if augmented_image.shape[-1] != 3:
        augmented_image = np.stack([augmented_image[:, :, 0]] * 3, axis=-1)
        
    # Resize the image to the target shape
    augmented_image = transform.resize(augmented_image, target_shape, anti_aliasing=True)

    augmented_image = util.img_as_ubyte(augmented_image)
    
        
    
        
    #print(f"Augmented image shape: {augmented_image.shape}")
    #print(f"Augmented image data type: {augmented_image.dtype}")

        
    return augmented_image

