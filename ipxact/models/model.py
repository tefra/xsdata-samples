from __future__ import annotations

from dataclasses import dataclass

from ipxact.models.model_type import ModelType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Model(ModelType):
    """
    Model information.
    """

    class Meta:
        name = "model"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
