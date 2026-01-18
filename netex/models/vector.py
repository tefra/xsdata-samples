from __future__ import annotations

from dataclasses import dataclass

from .vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class Vector(VectorType):
    class Meta:
        name = "vector"
        namespace = "http://www.opengis.net/gml/3.2"
