from __future__ import annotations

from dataclasses import dataclass

from ipxact.models.access_restrictions_type import AccessRestrictionsType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class AccessRestrictions(AccessRestrictionsType):
    """
    Access modes.
    """

    class Meta:
        name = "accessRestrictions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
