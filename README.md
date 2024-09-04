# SPOTIT.AI: Deepfake Detection Using MesoInception4

## Abstract
SPOTIT.AI is a sophisticated deepfake detection system leveraging the MesoInception4 model. This system is designed to identify manipulated videos and images with high accuracy. The project integrates with Django for application management and connects to the MyriadB server for data handling.

## 1. Introduction
Deepfake technology has advanced significantly, making it crucial to develop effective detection systems. SPOTIT.AI addresses this need by employing the MesoInception4 model, which utilizes advanced Convolutional Neural Networks (CNNs) to distinguish between genuine and manipulated content.

## 2. Features
- **Deepfake Detection**: Utilizes the MesoInception4 model to detect manipulated images and videos with high accuracy.
- **Integration with Django**: Enhances detection capabilities by incorporating additional features from Django.
- **MyriadB Server Connectivity**: Manages and stores data efficiently through integration with the MyriadB server.
- **User Interface**: Provides an easy-to-use interface via Django for interaction and analysis.
- **Real-Time Analysis**: Supports real-time analysis of images and videos for immediate detection results.

## 3. Methodology

### 3.1 Overview of SPOTIT.AI
SPOTIT.AI is designed to classify images as either real or deepfake. The system utilizes the MesoInception4 model to achieve high accuracy in detecting manipulated content.

### 3.2 Model Architecture

#### 3.2.1 Classifier Class
The base class handles common functionalities for deep learning models, including prediction, training, accuracy evaluation, and model weight management.

#### 3.2.2 Meso1
- **Purpose**: Feature extraction and classification.
- **Architecture**: Convolutional layers with batch normalization, max pooling, and dense layers with dropout for regularization.
- **Key Features**: Smaller convolutional kernels and max pooling to capture essential features.

#### 3.2.3 Meso4
- **Purpose**: Enhanced feature extraction.
- **Architecture**: Multiple convolutional layers with varying filter sizes, batch normalization, max pooling, and LeakyReLU activations.
- **Key Features**: Complex architecture for capturing intricate patterns.

#### 3.2.4 MesoInception4
- **Purpose**: Sophisticated feature extraction using Inception-like layers.
- **Architecture**: Incorporates multiple convolutional filters of different sizes and dilation rates within inception blocks.
- **Key Features**: Merges features from various convolutional operations, followed by batch normalization and pooling layers.

### 3.3 Training and Evaluation
- **Data Preprocessing**: Images are rescaled and divided into training and validation sets using `ImageDataGenerator`.
- **Training**: The `MesoInception4` model is trained with a checkpoint callback to save the best model based on validation loss.
- **Evaluation**: Metrics such as accuracy, confusion matrix, and F1 score are computed to assess performance.

## 4. Results

### 4.1 Training Details
- **Training Dataset**: 12,353 images
- **Validation Dataset**: 7,104 images
- **Epochs**: 8

### 4.2 Final Model Evaluation
- **Validation Loss**: 0.2387
- **Validation Accuracy**: 90.17%
- **Confusion Matrix**:

  |              | Predicted: Fake | Predicted: Real |
  |--------------|-----------------|-----------------|
  | Actual: Fake | 2,376           | 469             |
  | Actual: Real | 488             | 3,771           |

- **F1 Score**: 0.8874

The model achieved a validation accuracy of 90.17% and an F1 score of 0.8874, demonstrating its effectiveness in distinguishing between deepfakes and real images.

## 5. Conclusion
SPOTIT.AI effectively utilizes the MesoInception4 model to detect deepfakes with high accuracy. The system's sophisticated architecture and thorough evaluation ensure robust performance in real-world applications.

## 6. Installation
To set up SPOTIT.AI, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Hrishabh-V/SPOTIT.AI.git
   ```

2. Navigate to the project directory:
   ```bash
   cd sp
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Django server:
   ```bash
   python manage.py runserver
   ```

