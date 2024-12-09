from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class PowerDomainRef:
    """Power domain.

    It is the user’s responsibility to ensure it matches an existing
    power domain in UPF/CPF file.
    """

    class Meta:
        name = "powerDomainRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
