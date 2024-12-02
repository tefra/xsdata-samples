from dataclasses import dataclass, field
from typing import ForwardRef, Union

from sdmx_ml.models.empty_type import EmptyType
from sdmx_ml.models.identifiable_object_event_type import (
    IdentifiableObjectEventType,
)
from sdmx_ml.models.versionable_object_event_type import (
    VersionableObjectEventType,
)
from sdmx_ml.models.wild_card_value_type import WildCardValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class StructuralRepositoryEventsType:
    """StructuralRepositoryEventsType details the structural events for the
    subscription.

    At least one maintenance agency must be specified, although it may
    be given a wildcard value (meaning the subscription is for the
    structural events of all agencies). This can also be a list of
    agencies to allow the subscription to subscribe the events of more
    than one agency. It should be noted that when doing so, all of the
    subsequent objects are assumed to apply to every agency in the list.
    The subscription is then refined by detailing the structural objects
    maintained by the agency for which the subscription should apply. It
    is possible to explicitly select all object events, all objects of
    given types, or to individually list out specific objects. Note that
    for any object, it is also possible to provide an explicit URN to
    reference a distinct object. In this case, the reference to
    maintenance agency described above is ignored. Although it is not
    required, if specific objects are being referenced by explicit URNs,
    it is good practice to list the agencies.

    :ivar agency_id: AgencyID specifies a maintenance agency for the
        object or objects indicated in the other fields. This can be
        either a specific ID, or a single wildcard character ("%"). A
        wild card character can be used to select all agencies, allowing
        a subscription to all events for particular object types. This
        can occur multiple times to list a of group of maintenance
        agencies, creating event subscriptions for all of the subsequent
        objects for each agency in the group. Note that if multiple
        agencies are supplied, then the wildcard character should not be
        used for any of them.
    :ivar choice:
    :ivar type_value: TYPE is a fixed attribute that is used to ensure
        only of each event selector may be provided, when it is
        referenced in a uniqueness constraint.
    """

    agency_id: tuple[Union[str, WildCardValueType], ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AgencyID",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "min_occurs": 1,
            "pattern": r"[A-Za-z0-9_@$\-]+(\.[A-Za-z0-9_@$\-]+)*",
        },
    )
    choice: tuple[
        Union[
            EmptyType,
            "StructuralRepositoryEventsType.AgencyScheme",
            "StructuralRepositoryEventsType.DataConsmerScheme",
            "StructuralRepositoryEventsType.DataProviderScheme",
            "StructuralRepositoryEventsType.OrganisationUnitScheme",
            "StructuralRepositoryEventsType.Dataflow",
            "StructuralRepositoryEventsType.Metadataflow",
            "StructuralRepositoryEventsType.CategoryScheme",
            IdentifiableObjectEventType,
            "StructuralRepositoryEventsType.Codelist",
            "StructuralRepositoryEventsType.HierarchicalCodelist",
            "StructuralRepositoryEventsType.ConceptScheme",
            "StructuralRepositoryEventsType.MetadataStructureDefinition",
            "StructuralRepositoryEventsType.KeyFamily",
            "StructuralRepositoryEventsType.StructureSet",
            "StructuralRepositoryEventsType.ReportingTaxonomy",
            "StructuralRepositoryEventsType.Process",
            "StructuralRepositoryEventsType.AttachmentConstraint",
            "StructuralRepositoryEventsType.ContentConstraint",
            "StructuralRepositoryEventsType.ProvisionAgreement",
            "StructuralRepositoryEventsType.TransformationScheme",
            "StructuralRepositoryEventsType.NameAliasScheme",
            "StructuralRepositoryEventsType.NamePersonalisationScheme",
            "StructuralRepositoryEventsType.RulesetScheme",
            "StructuralRepositoryEventsType.UserDefinedOperatorScheme",
        ],
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllEvents",
                    "type": EmptyType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "AgencyScheme",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.AgencyScheme"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "DataConsmerScheme",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.DataConsmerScheme"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "DataProviderScheme",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.DataProviderScheme"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "OrganisationUnitScheme",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.OrganisationUnitScheme"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "Dataflow",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.Dataflow"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "Metadataflow",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.Metadataflow"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "CategoryScheme",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.CategoryScheme"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "Categorisation",
                    "type": IdentifiableObjectEventType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "Codelist",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.Codelist"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "HierarchicalCodelist",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.HierarchicalCodelist"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "ConceptScheme",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.ConceptScheme"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "MetadataStructureDefinition",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.MetadataStructureDefinition"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "KeyFamily",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.KeyFamily"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "StructureSet",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.StructureSet"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "ReportingTaxonomy",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.ReportingTaxonomy"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "Process",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.Process"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "AttachmentConstraint",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.AttachmentConstraint"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "ContentConstraint",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.ContentConstraint"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "ProvisionAgreement",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.ProvisionAgreement"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "TransformationScheme",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.TransformationScheme"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "NameAliasScheme",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.NameAliasScheme"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "NamePersonalisationScheme",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.NamePersonalisationScheme"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "RulesetScheme",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.RulesetScheme"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "UserDefinedOperatorScheme",
                    "type": ForwardRef(
                        "StructuralRepositoryEventsType.UserDefinedOperatorScheme"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
            ),
        },
    )
    type_value: str = field(
        init=False,
        default="STRUCTURE",
        metadata={
            "name": "TYPE",
            "type": "Attribute",
        },
    )

    @dataclass(frozen=True)
    class AgencyScheme(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class DataConsmerScheme(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class DataProviderScheme(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class OrganisationUnitScheme(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class Dataflow(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class Metadataflow(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class CategoryScheme(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class Codelist(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class HierarchicalCodelist(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class ConceptScheme(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class MetadataStructureDefinition(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class KeyFamily(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class StructureSet(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class ReportingTaxonomy(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class Process(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class AttachmentConstraint(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class ContentConstraint(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class ProvisionAgreement(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class TransformationScheme(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class NameAliasScheme(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class NamePersonalisationScheme(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class RulesetScheme(VersionableObjectEventType):
        pass

    @dataclass(frozen=True)
    class UserDefinedOperatorScheme(VersionableObjectEventType):
        pass
