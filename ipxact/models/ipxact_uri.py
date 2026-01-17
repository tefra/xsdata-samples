from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class IpxactUri:
    """
    IP-XACT URI, like a standard xs:anyURI except that it can contain
    environment variables in the ${ } form, to be replaced by their value
    to provide the underlying URI.
    """

    class Meta:
        name = "ipxactURI"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
