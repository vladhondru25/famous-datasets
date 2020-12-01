# Fashion MNIST

The implementation of an adapted LeNet5 [1] and applied to the Fashion MNIST dataset in PyTorch. Two Tensorflow implementations were included, the difference being in the method of training the model (simpler version using Keras way with compile and fit, the other more advanced with GradientTape).

## How to run

The code is written as a Jupyer Notebook. It can pe run locally if [JupyterLab](https://jupyter.org/) in installed. In order to run it, just run the cells in their respective order. 
Note: Due to some issues ([see](https://github.com/dmlc/xgboost/issues/1715)), the Tensorflow notebooks contains the following block of code (uncomment if you got the same error):
<code>
    import os
    os.environ['KMP_DUPLICATE_LIB_OK']='True'
</code>

### Recommendation

If either JupyterLab is not installed on the machine or a faster training is desired, [Google Colab](https://colab.research.google.com/) can be used. It does provide free GPU for a limited amount of time, but more than sufficient to train the network.

## Features and results
The architecture of the network is mainly LeNet5, but batch normalisation layers were added after each convolutional layer, as well as dropout after all layers (including fully connected). The data is normalised with the mean and standard deviation of 0.5. The final accuracy using a random seed is 90.25%. Some predictions can be observed below:

![alt text](https://github.com/vladhondru25/famous-datasets/blob/master/./fashion-mnist/result.png?raw=true)


## References

[[1](http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf)] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. "Gradient-based learning applied to document recognition." Proceedings of the IEEE, 86(11):2278-2324, November 1998.
