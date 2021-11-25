from autograd.modules.module import Module
import autograd.tensor as tensor
class ReLU(Module):
    def __init__(self):
        pass

    def forward(self, X):
        return tensor.Tensor.scalarmax(X, 0)