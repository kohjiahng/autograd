from backfuncs.backfunc import BackFunc

class FlattenBack(BackFunc):
    def __call__(self,tensor):
        assert len(tensor._parents) == 1, "FlattenBack called with > 1 parents"
        A, = tensor._parents
        A._add_grad(tensor.grad.reshape(A.shape))