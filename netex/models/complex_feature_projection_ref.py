from __future__ import annotations

from dataclasses import dataclass

from .complex_feature_projection_ref_structure import (
    ComplexFeatureProjectionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplexFeatureProjectionRef(ComplexFeatureProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
