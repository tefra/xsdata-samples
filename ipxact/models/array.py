from dataclasses import dataclass, field

from ipxact.models.dim import Dim
from ipxact.models.stride import Stride

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Array:
    """
    :ivar dim: Dimensions a memory-map element array, the semantics for
        dim elements are the same as the C language standard for the
        layout of memory in multidimensional arrays.
    :ivar stride:
    """

    class Meta:
        name = "array"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    dim: list[Dim] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    stride: Stride | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
