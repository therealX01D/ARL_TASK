# Self Driving Car model 
## Model Approach 
- CNN architecture of two layers ,
- each layer is of 3x3 kernel 1 stride both of them is followed by an maxpooling layer to extract more features and reduces dimensions of images.
- the first layer has an input of  1 channel (grey scale img) and output of 64 channels.
- the second layer has an input of 64 channels and output of 128
- An batch normalization is done on the outputs of those layers to make a more smooth learning and a fast one,
the input is then flatten then passed through a dense layer of 379392 nodes then passed to final 3 nodes layer 
## learning
- 10 epochs was choosen to run a model
- Mean squared error loss is choosen as the outputs is a continuous values vector of 3 * 1 (throttle,reverse,steering)  
- a learning rate of 0.01 is choosen as a suitable hyperparameter
- Adam optimizer is firstly used 
## After learning note
- the loss of the learning is found to be fluctuating between the minimum loss and maximum loss during learning this could be due to a 
hyperparameter in the adam optimizer dominating the momentum region (mainly used to speed up convergence often leading to overshooting)more than the rmsprop region (which leads to slowing down gradient descent)
- dropout should be employed and even introducting a regularization term 