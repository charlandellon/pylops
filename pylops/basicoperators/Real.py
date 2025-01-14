import numpy as np

from pylops import LinearOperator
from pylops.utils._internal import _value_or_list_like_to_tuple


class Real(LinearOperator):
    r"""Real operator.

    Return the real component of the input. The adjoint returns a complex
    number with the same real component as the input and zero imaginary
    component.

    Parameters
    ----------
    dims : :obj:`int` or :obj:`tuple`
        Number of samples for each dimension
    dtype : :obj:`str`, optional
        Type of elements in input array.
    name : :obj:`str`, optional
        .. versionadded:: 2.0.0

        Name of operator (to be used by :func:`pylops.utils.describe.describe`)

    Attributes
    ----------
    shape : :obj:`tuple`
        Operator shape
    explicit : :obj:`bool`
        Operator contains a matrix that can be solved explicitly (``True``) or
        not (``False``)

    Notes
    -----
    In forward mode:

    .. math::

        y_{i} = \Re\{x_{i}\} \quad \forall i=0,\ldots,N-1

    In adjoint mode:

    .. math::

        x_{i} = \Re\{y_{i}\} + 0i \quad \forall i=0,\ldots,N-1

    """

    def __init__(self, dims, dtype="complex128", name="R"):
        dims = _value_or_list_like_to_tuple(dims)
        super().__init__(
            dtype=np.dtype(dtype), dims=dims, dimsd=dims, clinear=False, name=name
        )
        self.rdtype = np.real(np.ones(1, self.dtype)).dtype

    def _matvec(self, x):
        return x.real.astype(self.rdtype)

    def _rmatvec(self, x):
        return (x.real + 0j).astype(self.dtype)
