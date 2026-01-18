from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.domain_type_def import DomainTypeDef

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class DomainTypeDefs:
    """
    The group of domain type definitions.
    """

    class Meta:
        name = "domainTypeDefs"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    domain_type_def: list[DomainTypeDef] = field(
        default_factory=list,
        metadata={
            "name": "domainTypeDef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
