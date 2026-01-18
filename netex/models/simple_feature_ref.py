from __future__ import annotations

from dataclasses import dataclass

from .simple_feature_ref_structure import SimpleFeatureRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SimpleFeatureRef(SimpleFeatureRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
