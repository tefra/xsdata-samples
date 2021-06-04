from dataclasses import dataclass
from netex.models.association_role_type import AssociationRoleType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractStrictAssociationRole(AssociationRoleType):
    class Meta:
        name = "abstractStrictAssociationRole"
        namespace = "http://www.opengis.net/gml/3.2"
