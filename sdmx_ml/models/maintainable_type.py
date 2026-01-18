from dataclasses import dataclass, field

from sdmx_ml.models.maintainable_base_type import MaintainableBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class MaintainableType(MaintainableBaseType):
    """
    MaintainableType is an abstract base type for all maintainable objects.

    :ivar agency_id: The agencyID must be provided, and identifies the
        maintenance agency of the object.
    :ivar is_external_reference: The isExternalReference attribute, if
        true, indicates that the actual object is not defined the
        corresponding element, rather its full details are defined
        elsewhere - indicated by either the registryURL, the
        repositoryURL, or the structureURL. The purpose of this is so
        that each structure message does not have to redefine object
        that are already defined elsewhere. If the isExternalReference
        attribute is not set, then it is assumed to be false, and the
        object should contain the full definition of its contents. If
        more than one of the registryURL, the repositoryURL, and the
        structureURL are supplied, then the application processing the
        object can choose the method it finds best suited to retrieve
        the details of the object.
    :ivar service_url: The serviceURL attribute indicates the URL of an
        SDMX SOAP web service from which the details of the object can
        be retrieved. Note that this can be a registry or and SDMX
        structural metadata repository, as they both implement that same
        web service interface.
    :ivar structure_url: The structureURL attribute indicates the URL of
        a SDMX-ML structure message (in the same version as the source
        document) in which the externally referenced object is
        contained. Note that this may be a URL of an SDMX RESTful web
        service which will return the referenced object.
    """

    agency_id: str | None = field(
        default=None,
        metadata={
            "name": "agencyID",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_\-]*(\.[A-Za-z][A-Za-z0-9_\-]*)*",
        },
    )
    is_external_reference: bool = field(
        default=False,
        metadata={
            "name": "isExternalReference",
            "type": "Attribute",
        },
    )
    service_url: str | None = field(
        default=None,
        metadata={
            "name": "serviceURL",
            "type": "Attribute",
        },
    )
    structure_url: str | None = field(
        default=None,
        metadata={
            "name": "structureURL",
            "type": "Attribute",
        },
    )
