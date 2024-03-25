from dataclasses import dataclass, field
from typing import Optional, Type, Union

from sdmx_ml.models.obs_dimensions_code_type import ObsDimensionsCodeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class PayloadStructureType:
    """PayloadStructureType is an abstract base type used to define the structural
    information for data or metadata sets.

    A reference to the structure is provided (either explicitly or
    through a reference to a structure usage).

    :ivar provision_agreement_or_structure_usage_or_structure:
    :ivar structure_id: The structureID attribute uniquely identifies
        the structure for the purpose of referencing it from the
        payload. This is only used in structure specific formats.
        Although it is required, it is only useful when more than one
        data set is present in the message.
    :ivar schema_url: The schemaURL attribute provides a location from
        which the structure specific schema can be located.
    :ivar namespace: The namespace attribute is used to provide the
        namespace for structure-specific formats. By communicating this
        information in the header, it is possible to generate the
        structure specific schema while processing the message.
    :ivar dimension_at_observation: The dimensionAtObservation is used
        to reference the dimension at the observation level for data
        messages. This can also be given the explicit value of
        "AllDimensions" which denotes that the cross sectional data is
        in the flat format.
    :ivar explicit_measures: The explicitMeasures indicates whether
        explicit measures are used in the cross sectional format. This
        is only applicable for the measure dimension as the dimension at
        the observation level or the flat structure.
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

    provision_agreement_or_structure_usage_or_structure: Optional[
        Union[
            "PayloadStructureType.ProvisionAgreement",
            "PayloadStructureType.StructureUsage",
            "PayloadStructureType.Structure",
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ProvisionAgreement",
                    "type": Type["PayloadStructureType.ProvisionAgreement"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
                },
                {
                    "name": "StructureUsage",
                    "type": Type["PayloadStructureType.StructureUsage"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
                },
                {
                    "name": "Structure",
                    "type": Type["PayloadStructureType.Structure"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
                },
            ),
        },
    )
    structure_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "structureID",
            "type": "Attribute",
            "required": True,
        },
    )
    schema_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaURL",
            "type": "Attribute",
        },
    )
    namespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dimension_at_observation: Optional[Union[str, ObsDimensionsCodeType]] = (
        field(
            default=None,
            metadata={
                "name": "dimensionAtObservation",
                "type": "Attribute",
                "pattern": r"[A-Za-z][A-Za-z0-9_\-]*",
            },
        )
    )
    explicit_measures: Optional[bool] = field(
        default=None,
        metadata={
            "name": "explicitMeasures",
            "type": "Attribute",
        },
    )
    service_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceURL",
            "type": "Attribute",
        },
    )
    structure_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "structureURL",
            "type": "Attribute",
        },
    )

    @dataclass(frozen=True)
    class ProvisionAgreement:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.registry\.ProvisionAgreement=.+",
            },
        )

    @dataclass(frozen=True)
    class StructureUsage:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.datastructure\.Dataflow=.+|.+\.metadatastructure\.Metadataflow=.+",
            },
        )

    @dataclass(frozen=True)
    class Structure:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.datastructure\.DataStructure=.+|.+\.metadatastructure\.MetadataStructure=.+",
            },
        )
