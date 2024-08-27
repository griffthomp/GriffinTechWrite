Sample Code and Tutorials
=========================

Welcome to the Sample Code and Tutorials section of the AI Vision Library documentation! This section is packed with practical examples, advanced tutorials, and best practices to help you master the library. Whether you're integrating AI vision into cutting-edge robotics or experimenting with new computer vision models, these examples will guide you every step of the way.

**Example 1: Real-Time Object Detection with Live Visualization**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, we'll walk through how to use the AI Vision Library to perform real-time object detection with live visualization. We'll leverage the power of GPU acceleration to detect objects at lightning speed and display the results in real-time.

**Code Example**

.. code-block:: python

    from ai_vision_library import detect_objects
    import cv2

    # Initialize video capture from the webcam
    video_capture = cv2.VideoCapture(0)  # Use 0 for the default camera

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        if not ret:
            print("Failed to capture image")
            break

        # Perform object detection on the frame
        detected_objects = detect_objects(frame, threshold=0.5, device='cuda')

        # Draw bounding boxes and labels on the frame
        for obj in detected_objects:
            x_min, y_min, x_max, y_max = obj['bbox']
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            cv2.putText(frame, f"{obj['label']} ({obj['confidence']*100:.1f}%)", 
                        (x_min, y_min-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Real-Time Object Detection', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close any OpenCV windows
    video_capture.release()
    cv2.destroyAllWindows()

**Expected Output**:

Running this code will open a window displaying the live camera feed with bounding boxes and labels around detected objects. The real-time performance, powered by CUDA, should allow for seamless interaction.

**Example 2: Training a Custom Object Recognition Model with Data Augmentation**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example covers how to train a custom object recognition model using your dataset, enhanced with data augmentation to improve generalization. We'll load the dataset, apply augmentation, configure training parameters, and save the trained model.

**Code Example**

.. code-block:: python

    from ai_vision_library import train_model
    from ai_vision_library.datasets import load_dataset, augment_data

    # Load and augment your dataset
    dataset = load_dataset('path_to_dataset')
    augmented_dataset = augment_data(dataset, flip=True, rotate=True, scale=True)

    # Configure training parameters
    architecture = 'resnet'
    epochs = 150
    batch_size = 64
    device = 'cuda'

    # Train the model with data augmentation
    model, logs = train_model(data=augmented_dataset, architecture=architecture, epochs=epochs, batch_size=batch_size, device=device)

    # Save the trained model
    model.save('my_augmented_model.h5')

    # Output training logs
    for epoch, metrics in logs.items():
        print(f"Epoch {epoch}: Loss = {metrics['loss']:.4f}, Accuracy = {metrics['accuracy']*100:.2f}%")

**Advanced Notes**:

- **Data Augmentation**: Applying transformations like flipping, rotating, and scaling to your dataset helps create a more robust model that generalizes better to unseen data.
- **Training Performance**: By increasing the batch size and using a powerful architecture like ResNet, we can leverage GPU acceleration to train complex models more efficiently.

**Example 3: Integrating with ROS for Autonomous Drone Navigation**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this advanced tutorial, we'll integrate the AI Vision Library with ROS to perform real-time object detection for autonomous drone navigation. The detected objects will be used to adjust the drone's flight path dynamically.

**Code Example**

.. code-block:: python

    import rospy
    from sensor_msgs.msg import Image
    from ai_vision_library import detect_objects
    from geometry_msgs.msg import Twist
    import cv2
    from cv_bridge import CvBridge

    # Initialize ROS node
    rospy.init_node('drone_vision_node')

    # Initialize publishers and subscribers
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    bridge = CvBridge()

    def image_callback(msg):
        # Convert the ROS image message to OpenCV format
        image = bridge.imgmsg_to_cv2(msg, "bgr8")

        # Perform object detection
        detected_objects = detect_objects(image, threshold=0.5, device='cuda')

        # Example logic: Adjust flight based on detected objects
        twist = Twist()
        for obj in detected_objects:
            if (obj['label'] == 'obstacle'):
                twist.linear.x = -0.5  # Move backward
            else:
                twist.linear.x = 0.5  # Move forward

            vel_pub.publish(twist)
            rospy.loginfo(f"Detected {obj['label']} with {obj['confidence']*100:.2f}% confidence")

    # Subscribe to the drone's camera feed
    image_sub = rospy.Subscriber('/drone/camera/image_raw', Image, image_callback)

    # Keep the node running
    rospy.spin()

**Expected Output**:

This script processes the drone's live camera feed in real-time, detecting obstacles and dynamically adjusting the drone's velocity to avoid collisions.

**Example 4: Video Analytics with Multi-Object Tracking**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here, we'll demonstrate how to process a video file for multi-object tracking, performing detection on each frame and tracking objects across the video.

**Code Example**

.. code-block:: python

    from ai_vision_library import detect_objects, track_objects
    import cv2

    # Load a video file
    video = cv2.VideoCapture('sample_video.mp4')

    # Initialize multi-object tracker
    tracker = track_objects()

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        # Perform object detection on the frame
        detected_objects = detect_objects(frame, threshold=0.5, device='cuda')

        # Update tracker with detected objects
        tracked_objects = tracker.update(detected_objects)

        # Draw bounding boxes and labels on the frame
        for obj in tracked_objects:
            x_min, y_min, x_max, y_max = obj['bbox']
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 255), 2)
            cv2.putText(frame, f"{obj['label']} ID:{obj['id']} ({obj['confidence']*100:.1f}%)", 
                        (x_min, y_min-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        # Display the resulting frame
        cv2.imshow('Video Analytics - Multi-Object Tracking', frame)

        # Save the processed frame to the output video
        out.write(frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release everything when the job is finished
    video.release()
    out.release()
    cv2.destroyAllWindows()

**Advanced Notes**:

- **Multi-Object Tracking**: This example introduces object tracking, allowing the AI Vision Library to not only detect but also track objects across video frames, maintaining consistent IDs.
- **Video Processing**: Ideal for security applications, autonomous vehicles, and advanced robotics, this example demonstrates how to handle video data efficiently.

**Performance Tips**:

- **Leverage GPU Acceleration**: Always use CUDA or other GPU acceleration options available to you for real-time performance, especially in high-throughput scenarios like video analytics.
- **Optimize Thresholds**: Fine-tune detection thresholds based on your specific application requirements to balance accuracy and processing speed.
- **Batch Processing**: For large-scale data processing, batch operations can significantly reduce overhead and improve efficiency.
