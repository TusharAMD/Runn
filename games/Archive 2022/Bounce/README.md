# Bounce Gesture Control Game
Imagine you are working as a data scientist at a home electronics company which manufactures state of the art smart televisions. You want to develop a cool feature in the smart-TV that can recognise five different gestures performed by the user which will help users control the TV without using a remote.

The gestures are continuously monitored by the webcam mounted on the TV. Each gesture corresponds to a specific command.

## Features:
- Thumbs up: Increase the volume
- Thumbs down: Decrease the volume
- Left swipe: 'Jump' backwards 10 seconds
- Right swipe: 'Jump' forward 10 seconds
- Stop: Pause the movie
- Each video is a sequence of 30 frames (or images).

## Understanding the Dataset
The training data consists of a few hundred videos categorised into one of the five classes. Each video (typically 2-3 seconds long) is divided into a sequence of 30 frames(images). These videos have been recorded by various people performing one of the five gestures in front of a webcam - similar to what the smart TV will use.

Each row of the CSV file represents one video and contains three main pieces of information - the name of the subfolder containing the 30 images of the video, the name of the gesture and the numeric label (between 0-4) of the video.

Your task is to train a model on the 'train' folder which performs well on the 'val' folder as well (as usually done in ML projects). We have withheld the test folder for evaluation purposes - your final model's performance will be tested on the 'test' set.

To get started with the model building process, you first need to get the data on your persistent storage. In order to get the data on the persistent storage, perform the following steps in order.

Convolutions + RNN
The conv2D network will extract a feature vector for each image, and a sequence of these feature vectors is then fed to an RNN-based network. The output of the RNN is a regular softmax (for a classification problem such as this one).

3D Convolutional Network, or Conv3D
3D convolutions are a natural extension to the 2D convolutions you are already familiar with. Just like in 2D conv, you move the filter in two directions (x and y), in 3D conv, you move the filter in three directions (x, y and z). In this case, the input to a 3D conv is a video (which is a sequence of 30 RGB images). If we assume that the shape of each image is 100x100x3, for example, the video becomes a 4-D tensor of shape 100x100x3x30 which can be written as (100x100x30)x3 where 3 is the number of channels. Hence, deriving the analogy from 2-D convolutions where a 2-D kernel/filter (a square filter) is represented as (fxf)xc where f is filter size and c is the number of channels, a 3-D kernel/filter (a 'cubic' filter) is represented as (fxfxf)xc (here c = 3 since the input images have three channels). This cubic filter will now '3D-convolve' on each of the three channels of the (100x100x30) tensor.

As an example, let's calculate the output shape and the number of parameters in a Conv3D with an example of a video having 7 frames. Each image is an RGB image of dimension 100x100x3. Here, the number of channels is 3.

The input (video) is then 7 images stacked on top of each other, so the shape of the input is (100x100x7)x3, i.e (length x width x number of images) x number of channels. Now, let's use a 3-D filter of size 2x2x2. This is represented as (2x2x2)x3 since the filter has the same number of channels as the input (exactly like in 2D convs).

## Understanding Generators
Now that you understand the two types of architectures to experiment with, let's discuss how to set up the data ingestion pipeline. As you already know, in most deep learning projects you need to feed data to the model in batches. This is done using the concept of generators.

Creating data generators is probably the most important part of building a training pipeline. Although libraries such as Keras provide builtin generator functionalities, they are often restricted in scope and you have to write your own generators from scratch. For example, in this problem, you need to feed batches of videos, not images. Similarly, in an entirely different problem such as 'music generation,' you may need to write generators which can create batches of audio files.


## Procedure:
number of images to be taken per video/sequence
cropping the images
resizing the images
normalizing the images
Goals of this Project
In this project, you will build a model to recognise 5 hand gestures. You need to accomplish the following in the project:

## Generator: 
The generator should be able to take a batch of videos as input without any error. Steps like cropping, resizing and normalization should be performed successfully.

## Model:
Develop a model that is able to train without any errors which will be judged on the total number of parameters (as the inference(prediction) time should be less) and the accuracy achieved.
