from __future__ import annotations

from dataclasses import dataclass

from .complex_feature_projection_version_structure import (
    ComplexFeatureProjectionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplexFeatureProjection(ComplexFeatureProjectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
