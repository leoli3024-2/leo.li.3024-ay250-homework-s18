# HW06 - Homebrew Computer Vision

## Purpose:
Write a set of methods that takes as input one of given [images](https://www.dropbox.com/s/cst9awcjpp08k33/50_categories.tar.gz), and then computes real-numbered features as the return. Based on the feature set for each image, build a random forest classifier. Produce metrics on the estimated error rates using cross-validation. 

## Files:
* README.md
* hw_6-machine-learning-supervised.pdf
* Homebrew_Computer_Vision.ipynb
* features.pkl
  - serialized file for extracted features
* random_forest.pkl
  - not existed in this repo due to its too-large size for github
  - serialized file for trained Random Forest Classifier based on the extracted features
* random_guessing.pkl
  - not existed in this repo (though only ~4KB) but to keep consistency (ramdon_forest.pkl not existed)
  - serialized file for trained DummyClassifier based on the extracted features

## How to use the classifier?
Run function run_final_classifier then call this function with any set of images, all of which could be classified into the given 50 categories.

The given 50 categories are: airplanes, bat, bear, blimp, camel, comet, conch, cormorant, crab, dog, dolphin, duck, elephant, elk, frog, galaxy, giraffe, goat, goldfish, goose, garilla, helicopter, horse, hot-air-balloon, hummingbird, iguana, kangaroo, killer-whale, leopards, llama, mars, mussels, octopus, ostrich, owl, penguin, porcupine, raccoon, saturn, skunk, snail, snake, speed-boat, starfish, swan, teddy-bear, toad, triceratops, unicorn and zebra.