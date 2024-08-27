Train Model
===========

The `train_model` function is a key feature of the AI Vision Library, allowing you to train custom object recognition models on your dataset. This function supports various neural network architectures and provides options for fine-tuning pre-trained models or training from scratch.

**Function Signature**
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    train_model(data, architecture='resnet', epochs=100, batch_size=32, learning_rate=0.001, device='cpu')

**Parameters**
~~~~~~~~~~~~~~

- **data**: Dataset  
  The dataset used for training the model. This should be an instance of a dataset class that provides images and labels for training.

- **architecture**: str, optional, default: 'resnet'  
  The neural network architecture to be used for training. Supported architectures include 'resnet', 'vgg', 'mobilenet', and more.

- **epochs**: int, optional, default: 100  
  The number of training epochs. An epoch refers to one complete pass through the entire training dataset.

- **batch_size**: int, optional, default: 32  
  The number of samples per batch of computation. Larger batch sizes can improve training speed at the cost of memory usage.

- **learning_rate**: float, optional, default: 0.001  
  The learning rate controls how much to change the model in response to the estimated error each time the model weights are updated.

- **device**: str, optional, default: 'cpu'  
  Specifies the device to run the training on. Options include 'cpu', 'cuda', or any specific GPU like 'cuda:0'. Using CUDA enables GPU acceleration, significantly improving training speed.

**Return Value**
~~~~~~~~~~~~~~~

- **model**: object  
  The trained model instance, which can be used for inference or further fine-tuning.

- **logs**: dict  
  A dictionary containing training logs, including metrics such as loss and accuracy for each epoch.

**Example Usage**
~~~~~~~~~~~~~~~~~

Here's a basic example of how to use the `train_model` function to train a model on a dataset:

.. code-block:: python

    from ai_vision_library import train_model, load_dataset

    # Load a custom dataset
    dataset = load_dataset('path_to_dataset')

    # Train the model using the ResNet architecture
    model, logs = train_model(data=dataset, architecture='resnet', epochs=50, batch_size=64, device='cuda')

    # Save the trained model
    model.save('my_custom_model.h5')

    # Print training logs
    for epoch, metrics in logs.items():
        print(f"Epoch {epoch}: Loss = {metrics['loss']:.4f}, Accuracy = {metrics['accuracy']*100:.2f}%")

**Detailed Example: Fine-Tuning a Pre-Trained Model**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how to fine-tune a pre-trained model on your dataset. Fine-tuning is particularly useful when you have a limited dataset and want to leverage the knowledge of a model trained on a larger dataset.

.. code-block:: python

    from ai_vision_library import train_model, load_dataset, load_pretrained_model

    # Load a custom dataset
    dataset = load_dataset('path_to_dataset')

    # Load a pre-trained model (e.g., ResNet trained on ImageNet)
    pretrained_model = load_pretrained_model('resnet', pretrained=True)

    # Fine-tune the pre-trained model on your dataset
    model, logs = train_model(data=dataset, architecture='resnet', epochs=30, batch_size=32, learning_rate=0.0001, device='cuda')

    # Save the fine-tuned model
    model.save('fine_tuned_model.h5')

    # Print training logs
    for epoch, metrics in logs.items():
        print(f"Epoch {epoch}: Loss = {metrics['loss']:.4f}, Accuracy = {metrics['accuracy']*100:.2f}%")

**Advanced Usage: Customizing the Training Process**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To fully customize the training process, you can adjust additional parameters such as learning rate, batch size, and number of epochs:

- **Learning Rate**: Adjust the `learning_rate` parameter based on your specific dataset and model architecture. A lower learning rate may lead to slower but more stable convergence, while a higher learning rate can speed up training but may cause instability.

.. code-block:: python

    model, logs = train_model(data=dataset, architecture='resnet', epochs=100, batch_size=16, learning_rate=0.0005, device='cuda')

- **Batch Size**: Experiment with different batch sizes to balance training speed and memory usage. Larger batch sizes can improve GPU utilization but may require more memory.

.. code-block:: python

    model, logs = train_model(data=dataset, batch_size=128, device='cuda')

- **Epochs**: The number of epochs should be chosen based on the complexity of your model and the size of your dataset. More epochs may improve accuracy, but can also lead to overfitting.

.. code-block:: python

    model, logs = train_model(data=dataset, epochs=200, device='cuda')

**Optimization Tips**
~~~~~~~~~~~~~~~~~~~~~

- **Use Data Augmentation**: Augment your training data to improve model generalization. This can include techniques like flipping, rotating, or scaling images.

.. code-block:: python

    augmented_dataset = augment_data(dataset, flip=True, rotate=True, scale=True)
    model, logs = train_model(data=augmented_dataset, architecture='vgg', epochs=50, device='cuda')

- **Monitor Training**: Regularly monitor training metrics, such as loss and accuracy, to ensure that the model is learning effectively. Consider using early stopping to prevent overfitting.

.. code-block:: python

    if logs[epoch]['loss'] > previous_loss:
        print("Warning: Loss is increasing, consider stopping early.")

**Common Errors and Troubleshooting**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Out of Memory Errors**: If you encounter out-of-memory errors, reduce the batch size or use a smaller model architecture.
- **Slow Convergence**: If training is slow or the model is not converging, try adjusting the learning rate or increasing the number of epochs.
- **Overfitting**: If the model performs well on the training data but poorly on validation data, consider using techniques like data augmentation, dropout, or early stopping.

**Conclusion**
~~~~~~~~~~~~~~

The `train_model` function provides a flexible and powerful way to train custom object recognition models with the AI Vision Library. By understanding and leveraging its parameters, you can create models tailored to your specific application needs.

For more advanced examples and use cases, be sure to explore the other sections of this documentation.
