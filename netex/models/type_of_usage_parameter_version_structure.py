from __future__ import annotations

from dataclasses import dataclass

from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfUsageParameterVersionStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfUsageParameter_VersionStructure"
