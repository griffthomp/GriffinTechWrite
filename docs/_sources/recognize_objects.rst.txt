Recognize Objects
=================

The `recognize_objects` function is a key feature of the AI Vision Library, enabling you to identify and classify known objects in images. This function is particularly useful for applications such as inventory management, quality control, and robotics, where recognizing specific objects is crucial.

**Function Signature**
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    recognize_objects(image, model, threshold=0.5, device='cpu')

**Parameters**:
- **image** (*ndarray*): The input image in which objects are to be recognized. This should be a NumPy array, typically read using OpenCV or similar libraries.
- **model** (*object*): The pre-trained model used for object recognition. This model should be loaded prior to calling the `recognize_objects` function.
- **threshold** (*float*, optional, default=0.5): The confidence threshold for recognizing objects. Objects with a recognition confidence lower than this threshold will be ignored.
- **device** (*str*, optional, default='cpu'): Specifies the device to run the recognition on. Options include `'cpu'`, `'cuda'`, or any specific GPU like `'cuda:0'`. Using CUDA enables GPU acceleration, significantly improving recognition speed.

**Return Value**:
- **recognized_objects** (*list of dicts*): A list of dictionaries, where each dictionary contains information about a recognized object. Each dictionary includes:
  - **bbox** (*tuple of (x_min, y_min, x_max, y_max)*): The bounding box coordinates of the recognized object.
  - **label** (*str*): The label or class name of the recognized object.
  - **confidence** (*float*): The confidence score of the recognition, indicating how likely it is that the recognized object belongs to the specified class.

**Example Usage**
~~~~~~~~~~~~~~~~~

Here's a basic example of how to use the `recognize_objects` function to recognize objects in an image:

.. code-block:: python

    from ai_vision_library import recognize_objects, load_model
    import cv2

    # Load an image using OpenCV
    image = cv2.imread('sample_image.jpg')

    # Load the pre-trained model
    model = load_model('my_model.h5')

    # Perform object recognition
    recognized_objects = recognize_objects(image, model, threshold=0.5, device='cuda')

    # Print out the recognized objects
    for obj in recognized_objects:
        print(f"Recognized {obj['label']} with confidence {obj['confidence']*100:.2f}% at {obj['bbox']}")

**Detailed Example: Displaying Recognized Objects with Bounding Boxes**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how to perform object recognition and visualize the results by drawing bounding boxes around recognized objects:

.. code-block:: python

    from ai_vision_library import recognize_objects, load_model
    import cv2

    # Load an image using OpenCV
    image = cv2.imread('sample_image.jpg')

    # Load the pre-trained model
    model = load_model('my_model.h5')

    # Perform object recognition
    recognized_objects = recognize_objects(image, model, threshold=0.5, device='cuda')

    # Draw bounding boxes on the image
    for obj in recognized_objects:
        x_min, y_min, x_max, y_max = obj['bbox']
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
        cv2.putText(image, f"{obj['label']} ({obj['confidence']*100:.1f}%)", 
                    (x_min, y_min-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Display the image with recognized objects
    cv2.imshow('Recognized Objects', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

**Advanced Usage: Custom Object Recognition Models**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use a custom model for object recognition, follow these steps:

1. **Train a Custom Model**: Train a model on your specific dataset using the `train_model` function.
2. **Load the Custom Model**: Load the trained model using `load_model`.
3. **Perform Recognition**: Use the `recognize_objects` function to recognize objects in new images.

.. code-block:: python

    # Example of using a custom model
    model = load_model('custom_model.h5')
    recognized_objects = recognize_objects(image, model, threshold=0.6, device='cuda')

**Optimization Tips**
~~~~~~~~~~~~~~~~~~~~~

- **Leverage Pre-trained Models**: If you don't have the resources to train a model from scratch, use pre-trained models and fine-tune them on your specific dataset.
- **Use High-Quality Images**: Recognition accuracy improves with higher quality images, so use images with good lighting and minimal noise.
- **Batch Processing**: For large-scale recognition tasks, consider processing images in batches to optimize performance.

**Common Errors and Troubleshooting**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Model Loading Errors**: Ensure the model file exists and is correctly loaded using the `load_model` function. Double-check the file path and format.
- **Low Confidence Scores**: If confidence scores are consistently low, consider retraining your model with more or better-quality data, or adjust the threshold.

**Conclusion**
~~~~~~~~~~~~~

The `recognize_objects` function is a powerful tool for identifying and classifying objects in images using the AI Vision Library. By understanding and utilizing its parameters and capabilities, you can integrate robust object recognition into your projects with ease.

For more advanced examples and use cases, be sure to explore the other sections of this documentation.
