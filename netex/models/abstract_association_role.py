from __future__ import annotations

from dataclasses import dataclass

from .association_role_type import AssociationRoleType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class AbstractAssociationRole(AssociationRoleType):
    class Meta:
        name = "abstractAssociationRole"
        namespace = "http://www.opengis.net/gml/3.2"
