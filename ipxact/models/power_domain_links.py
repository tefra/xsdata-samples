from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.string_expression import StringExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class PowerDomainLinks:
    """
    :ivar power_domain_link: A power domain link to one external power
        domain and one or more internal power domains.
    """

    class Meta:
        name = "powerDomainLinks"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    power_domain_link: list["PowerDomainLinks.PowerDomainLink"] = field(
        default_factory=list,
        metadata={
            "name": "powerDomainLink",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class PowerDomainLink:
        """
        :ivar external_power_domain_reference: Reference to a power
            domain defined on the top component.
        :ivar internal_power_domain_reference: Reference to a power
            domain defined on an instance
        :ivar id:
        """

        external_power_domain_reference: Optional[StringExpression] = field(
            default=None,
            metadata={
                "name": "externalPowerDomainReference",
                "type": "Element",
                "required": True,
            },
        )
        internal_power_domain_reference: list[
            "PowerDomainLinks.PowerDomainLink.InternalPowerDomainReference"
        ] = field(
            default_factory=list,
            metadata={
                "name": "internalPowerDomainReference",
                "type": "Element",
                "min_occurs": 1,
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )

        @dataclass
        class InternalPowerDomainReference:
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.w3.org/XML/1998/namespace",
                },
            )
