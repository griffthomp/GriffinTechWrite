Detect Objects
==============

The `detect_objects` function is one of the core features of the AI Vision Library. It enables real-time object detection in images or video frames using state-of-the-art computer vision algorithms. This function is optimized for performance, supporting GPU acceleration for real-time applications.

**Function Signature**
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def detect_objects(image, threshold=0.5, device='cpu'):
        """
        Parameters:
        - image: ndarray
          The input image in which objects are to be detected. This should be a NumPy array, typically read using OpenCV or similar libraries.

        - threshold: float, optional, default: 0.5
          The confidence threshold for detecting objects. Objects with a detection confidence lower than this threshold will be ignored.

        - device: str, optional, default: cpu
          Specifies the device to run the detection on. Options include 'cpu', 'cuda', or any specific GPU like 'cuda:0'. Using CUDA enables GPU acceleration, significantly improving detection speed.

        Return Value:
        - detected_objects: list of dicts
          A list of dictionaries, where each dictionary contains information about a detected object. Each dictionary includes:
          - bbox: tuple of (x_min, y_min, x_max, y_max)
            The bounding box coordinates of the detected object.
          - label: str
            The label or class name of the detected object.
          - confidence: float
            The confidence score of the detection, indicating how likely it is that the detected object belongs to the specified class.
        """

**Example Usage**
~~~~~~~~~~~~~~~~~

Here's a basic example of how to use the `detect_objects` function to detect objects in an image:

.. code-block:: python

    from ai_vision_library import detect_objects
    import cv2

    # Load an image using OpenCV
    image = cv2.imread('sample_image.jpg')

    # Perform object detection
    detected_objects = detect_objects(image, threshold=0.5, device='cuda')

    # Print out the detected objects
    for obj in detected_objects:
        print(f"Detected {obj['label']} with confidence {obj['confidence']*100:.2f}% at {obj['bbox']}")

**Detailed Example: Displaying Detected Objects with Bounding Boxes**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how to perform object detection and visualize the results by drawing bounding boxes around detected objects:

.. code-block:: python

    from ai_vision_library import detect_objects
    import cv2

    # Load an image using OpenCV
    image = cv2.imread('sample_image.jpg')

    # Perform object detection
    detected_objects = detect_objects(image, threshold=0.5, device='cuda')

    # Draw bounding boxes on the image
    for obj in detected_objects:
        x_min, y_min, x_max, y_max = obj['bbox']
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        cv2.putText(image, f"{obj['label']} ({obj['confidence']*100:.1f}%)", 
                    (x_min, y_min-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the image with detected objects
    cv2.imshow('Detected Objects', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

**Advanced Usage: Optimizing Detection Performance**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To achieve the best performance, especially in real-time applications, consider the following tips:

- **Use GPU Acceleration**: Set `device='cuda'` to leverage GPU acceleration. This can significantly speed up detection, especially for high-resolution images or real-time video feeds.
- **Adjust the Threshold**: Fine-tune the `threshold` parameter depending on your application's tolerance for false positives. Lowering the threshold might detect more objects but at the risk of increasing false positives.
- **Batch Processing**: For scenarios where you need to process multiple images or frames in a video, consider batch processing to reduce overhead.

**Common Errors and Troubleshooting**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Image Loading Issues**: Ensure that the image is correctly loaded and is in the expected format (NumPy array). Use OpenCV's `cv2.imread()` to read images as `ndarray`.
- **Device Compatibility**: If CUDA is not installed or available on your machine, make sure to set `device='cpu'` to avoid runtime errors.

**Conclusion**
~~~~~~~~~~~~~

The `detect_objects` function is a powerful tool within the AI Vision Library, designed to handle a wide range of object detection tasks efficiently. By understanding and utilizing its parameters and capabilities, you can integrate robust object detection into your projects with ease.

For more advanced examples and use cases, be sure to explore the other sections of this documentation.

**What to Do Next:**
~~~~~~~~~~~~~~~~~~~~

1. **Create the `detect_objects.rst` File**:
   - Open your `source/` directory and create a file named `detect_objects.rst`.
   - Paste the entire content above into this file.

2. **Rebuild the Documentation**:
   - Navigate back to your project root and run the `make html` command to regenerate the documentation, now including the detailed `detect_objects` section.

3. **Review**:
   - Open the generated HTML file (`index.html` in the `build/html/` directory) to ensure that the `detect_objects` documentation is correctly formatted and comprehensive.
