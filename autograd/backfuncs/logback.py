from autograd.backfuncs.backfunc import BackFunc
class LogBack(BackFunc):
    def __call__(self, tensor):
        assert len(tensor._parents) == 1, "LogBack called with > 1 parent"
        A, = tensor._parents
        A._add_grad(tensor.grad * (1 / A.asarray()))