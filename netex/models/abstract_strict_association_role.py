from __future__ import annotations

from dataclasses import dataclass

from .association_role_type import AssociationRoleType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class AbstractStrictAssociationRole(AssociationRoleType):
    class Meta:
        name = "abstractStrictAssociationRole"
        namespace = "http://www.opengis.net/gml/3.2"
