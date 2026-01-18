from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.agency_schemes_type import AgencySchemesType
from sdmx_ml.models.categorisations_type import CategorisationsType
from sdmx_ml.models.category_scheme_maps_type import CategorySchemeMapsType
from sdmx_ml.models.category_schemes_type import CategorySchemesType
from sdmx_ml.models.codelists_type import CodelistsType
from sdmx_ml.models.concept_scheme_maps_type import ConceptSchemeMapsType
from sdmx_ml.models.concept_schemes_type import ConceptSchemesType
from sdmx_ml.models.custom_type_schemes_type import CustomTypeSchemesType
from sdmx_ml.models.data_constraints_type import DataConstraintsType
from sdmx_ml.models.data_consumer_schemes_type import DataConsumerSchemesType
from sdmx_ml.models.data_provider_schemes_type import DataProviderSchemesType
from sdmx_ml.models.data_structures_type import DataStructuresType
from sdmx_ml.models.dataflows_type import DataflowsType
from sdmx_ml.models.geo_grid_codelists_type import GeoGridCodelistsType
from sdmx_ml.models.geographic_codelists_type import GeographicCodelistsType
from sdmx_ml.models.hierarchies_type import HierarchiesType
from sdmx_ml.models.hierarchy_associations_type import (
    HierarchyAssociationsType,
)
from sdmx_ml.models.metadata_constraints_type import MetadataConstraintsType
from sdmx_ml.models.metadata_provider_schemes_type import (
    MetadataProviderSchemesType,
)
from sdmx_ml.models.metadata_provision_agreements_type import (
    MetadataProvisionAgreementsType,
)
from sdmx_ml.models.metadata_structures_type import MetadataStructuresType
from sdmx_ml.models.metadataflows_type import MetadataflowsType
from sdmx_ml.models.name_personalisation_schemes_type import (
    NamePersonalisationSchemesType,
)
from sdmx_ml.models.organisation_scheme_maps_type import (
    OrganisationSchemeMapsType,
)
from sdmx_ml.models.organisation_unit_schemes_type import (
    OrganisationUnitSchemesType,
)
from sdmx_ml.models.processes_type import ProcessesType
from sdmx_ml.models.provision_agreements_type import ProvisionAgreementsType
from sdmx_ml.models.reporting_taxonomies_type import ReportingTaxonomiesType
from sdmx_ml.models.reporting_taxonomy_maps_type import (
    ReportingTaxonomyMapsType,
)
from sdmx_ml.models.representation_maps_type import RepresentationMapsType
from sdmx_ml.models.ruleset_schemes_type import RulesetSchemesType
from sdmx_ml.models.structure_maps_type import StructureMapsType
from sdmx_ml.models.transformation_schemes_type import (
    TransformationSchemesType,
)
from sdmx_ml.models.user_defined_operator_schemes_type import (
    UserDefinedOperatorSchemesType,
)
from sdmx_ml.models.value_lists_type import ValueListsType
from sdmx_ml.models.vtl_mapping_schemes_type import VtlMappingSchemesType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class StructuresType:
    """
    StructuresType describes the structure of the container for all
    structural metadata components.

    The structural components may be explicitly detailed, or referenced
    from an external structure document or registry service. Best practices
    dictate that, at a minimum, any structural component that is referenced
    by another structural component be included by reference.

    :ivar agency_schemes: AgencySchemes contains a collection of agency
        scheme descriptions. The agency schemes may be detailed in full,
        or referenced from an external structure document or registry
        service.
    :ivar categorisations: Categorisations contains a collection of
        structural object categorisations. This container may contain
        categorisations for many types of objects. The categorisations
        may be detailed in full, or referenced from an external
        structure document or registry service.
    :ivar category_scheme_maps: CategorySchemeMaps contains a collection
        of category scheme map descriptions. The category scheme maps
        may be detailed in full, or referenced from an external
        structure document or registry service.
    :ivar category_schemes: CategorySchemes contains a collection of
        category scheme descriptions. The category schemes may be
        detailed in full, or referenced from an external structure
        document or registry service.
    :ivar codelists: Codelists contains a collection of code list
        descriptions. The code lists may be detailed in full, or
        referenced from an external structure document or registry
        service.
    :ivar concept_scheme_maps: ConceptSchemeMaps contains a collection
        of concept scheme map descriptions. The concept scheme maps may
        be detailed in full, or referenced from an external structure
        document or registry service.
    :ivar concept_schemes: ConceptSchemes contains a collection of
        concept scheme descriptions. The concept schemes described are
        contained within schemes. The concepts may be detailed in full,
        or referenced from an external structure document or registry
        service.
    :ivar custom_type_schemes: CustomTypeSchemes contains a collection
        of custom type schemes. The scheme may be detailed in full, or
        referenced from an external structure document or registry
        service.
    :ivar data_constraints: DataConstraints contains a collection of
        data constraint descriptions. The constraints may be detailed in
        full, or referenced from an external structure document or
        registry service.
    :ivar data_consumer_schemes: DataConsumerSchemes contains a
        collection of data consumer scheme descriptions. The data
        consumer schemes may be detailed in full, or referenced from an
        external structure document or registry service.
    :ivar dataflows: Dataflows contains a collection of data flow
        descriptions. The data flows may be detailed in full, or
        referenced from an external structure document or registry
        service.
    :ivar data_provider_schemes: DataProviderSchemes contains a
        collection of data provider scheme descriptions. The data
        provider schemes may be detailed in full, or referenced from an
        external structure document or registry service.
    :ivar data_structures: DataStructures contains a collection of data
        structure definitions. The data structure definitions may be
        detailed in full, or referenced from an external structure
        document or registry service.
    :ivar geographic_codelists: GeographicCodelists contains a
        collection of geographi codelist descriptions. The codelists may
        be detailed in full, or referenced from an external structure
        document or registry service.
    :ivar geo_grid_codelists: GeoGridCodelists contains a collection of
        geographic grid codelist descriptions. The codelists may be
        detailed in full, or referenced from an external structure
        document or registry service.
    :ivar hierarchies: Hierarchies contains a collection of hierarchical
        code list descriptions. The hierarchical code lists may be
        detailed in full, or referenced from an external structure
        document or registry service.
    :ivar hierarchy_associations: HierarchyAssociations contains a
        collection of hierarchy associations. The associations may be
        detailed in full, or referenced from an external structure
        document or registry service.
    :ivar metadata_constraints: MetadataConstraints contains a
        collection of metadata constraint descriptions. The constraints
        may be detailed in full, or referenced from an external
        structure document or registry service.
    :ivar metadataflows: Metadataflows contains a collection of metadata
        flow descriptions. The metadata flows may be detailed in full,
        or referenced from an external structure document or registry
        service.
    :ivar metadata_provider_schemes: MetadataProviderSchemes contains a
        collection of metadata provider scheme descriptions. The
        meatadata provider schemes may be detailed in full, or
        referenced from an external structure document or registry
        service.
    :ivar metadata_provision_agreements: ProvisionAgreements contains a
        collection of provision agreements. The provision agreements may
        be detailed in full, or referenced from an external structure
        document or registry service.
    :ivar metadata_structures: MetadataStructures contains a collection
        of metadata structure definition descriptions. The metadata
        structure definitions may be detailed in full, or referenced
        from an external structure document or registry service.
    :ivar name_personalisation_schemes: NamePersonalisationSchemes
        contains a collection of name personalisation schemes. The
        scheme may be detailed in full, or referenced from an external
        structure document or registry service.
    :ivar organisation_scheme_maps: OrganisationSchemeMaps contains a
        collection of organisation scheme map descriptions. The
        organisation scheme maps may be detailed in full, or referenced
        from an external structure document or registry service.
    :ivar organisation_unit_schemes: OrganisationUnitSchemes contains a
        collection of organisation unit scheme descriptions. The
        organisation unit schemes may be detailed in full, or referenced
        from an external structure document or registry service.
    :ivar processes: Processes contains a collection of process
        descriptions. The processes may be detailed in full, or
        referenced from an external structure document or registry
        service.
    :ivar provision_agreements: ProvisionAgreements contains a
        collection of provision agreements. The provision agreements may
        be detailed in full, or referenced from an external structure
        document or registry service.
    :ivar reporting_taxonomies: ReportingTaxonomies contains a
        collection of reporting taxonomy descriptions. The reporting
        taxonomies may be detailed in full, or referenced from an
        external structure document or registry service.
    :ivar reporting_taxonomy_maps: ReportingTaxonomyMaps contains a
        collection of reporting taxonomy map descriptions. The reporting
        taxonomy maps may be detailed in full, or referenced from an
        external structure document or registry service.
    :ivar representation_maps: RepresentationMaps contains a collection
        of representation map descriptions. The representation maps may
        be detailed in full, or referenced from an external structure
        document or registry service.
    :ivar ruleset_schemes: RulesetSchemes contains a collection of
        ruleset schemes. The scheme may be detailed in full, or
        referenced from an external structure document or registry
        service.
    :ivar structure_maps: StructureMaps contains a collection of
        structure map descriptions. The structure maps may be detailed
        in full, or referenced from an external structure document or
        registry service.
    :ivar transformation_schemes: TransformationSchemes contains a
        collection of transformation schemes. The transformation schemes
        may be detailed in full, or referenced from an external
        structure document or registry service.
    :ivar user_defined_operator_schemes: UserDefinedOperatorSchemes
        contains a collection of user defined operator schemes. The
        scheme may be detailed in full, or referenced from an external
        structure document or registry service.
    :ivar value_lists: ValueLists contains a collection of value list
        descriptions. The value lists may be detailed in full, or
        referenced from an external structure document or registry
        service.
    :ivar vtl_mapping_schemes: VtlMappingSchemes contains a collection
        of VTL mapping schemes. The scheme may be detailed in full, or
        referenced from an external structure document or registry
        service.
    """

    agency_schemes: None | AgencySchemesType = field(
        default=None,
        metadata={
            "name": "AgencySchemes",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    categorisations: None | CategorisationsType = field(
        default=None,
        metadata={
            "name": "Categorisations",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    category_scheme_maps: None | CategorySchemeMapsType = field(
        default=None,
        metadata={
            "name": "CategorySchemeMaps",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    category_schemes: None | CategorySchemesType = field(
        default=None,
        metadata={
            "name": "CategorySchemes",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    codelists: None | CodelistsType = field(
        default=None,
        metadata={
            "name": "Codelists",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    concept_scheme_maps: None | ConceptSchemeMapsType = field(
        default=None,
        metadata={
            "name": "ConceptSchemeMaps",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    concept_schemes: None | ConceptSchemesType = field(
        default=None,
        metadata={
            "name": "ConceptSchemes",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    custom_type_schemes: None | CustomTypeSchemesType = field(
        default=None,
        metadata={
            "name": "CustomTypeSchemes",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    data_constraints: None | DataConstraintsType = field(
        default=None,
        metadata={
            "name": "DataConstraints",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    data_consumer_schemes: None | DataConsumerSchemesType = field(
        default=None,
        metadata={
            "name": "DataConsumerSchemes",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    dataflows: None | DataflowsType = field(
        default=None,
        metadata={
            "name": "Dataflows",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    data_provider_schemes: None | DataProviderSchemesType = field(
        default=None,
        metadata={
            "name": "DataProviderSchemes",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    data_structures: None | DataStructuresType = field(
        default=None,
        metadata={
            "name": "DataStructures",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    geographic_codelists: None | GeographicCodelistsType = field(
        default=None,
        metadata={
            "name": "GeographicCodelists",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    geo_grid_codelists: None | GeoGridCodelistsType = field(
        default=None,
        metadata={
            "name": "GeoGridCodelists",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    hierarchies: None | HierarchiesType = field(
        default=None,
        metadata={
            "name": "Hierarchies",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    hierarchy_associations: None | HierarchyAssociationsType = field(
        default=None,
        metadata={
            "name": "HierarchyAssociations",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    metadata_constraints: None | MetadataConstraintsType = field(
        default=None,
        metadata={
            "name": "MetadataConstraints",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    metadataflows: None | MetadataflowsType = field(
        default=None,
        metadata={
            "name": "Metadataflows",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    metadata_provider_schemes: None | MetadataProviderSchemesType = field(
        default=None,
        metadata={
            "name": "MetadataProviderSchemes",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    metadata_provision_agreements: None | MetadataProvisionAgreementsType = (
        field(
            default=None,
            metadata={
                "name": "MetadataProvisionAgreements",
                "type": "Element",
                "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            },
        )
    )
    metadata_structures: None | MetadataStructuresType = field(
        default=None,
        metadata={
            "name": "MetadataStructures",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    name_personalisation_schemes: None | NamePersonalisationSchemesType = (
        field(
            default=None,
            metadata={
                "name": "NamePersonalisationSchemes",
                "type": "Element",
                "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            },
        )
    )
    organisation_scheme_maps: None | OrganisationSchemeMapsType = field(
        default=None,
        metadata={
            "name": "OrganisationSchemeMaps",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    organisation_unit_schemes: None | OrganisationUnitSchemesType = field(
        default=None,
        metadata={
            "name": "OrganisationUnitSchemes",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    processes: None | ProcessesType = field(
        default=None,
        metadata={
            "name": "Processes",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    provision_agreements: None | ProvisionAgreementsType = field(
        default=None,
        metadata={
            "name": "ProvisionAgreements",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    reporting_taxonomies: None | ReportingTaxonomiesType = field(
        default=None,
        metadata={
            "name": "ReportingTaxonomies",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    reporting_taxonomy_maps: None | ReportingTaxonomyMapsType = field(
        default=None,
        metadata={
            "name": "ReportingTaxonomyMaps",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    representation_maps: None | RepresentationMapsType = field(
        default=None,
        metadata={
            "name": "RepresentationMaps",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    ruleset_schemes: None | RulesetSchemesType = field(
        default=None,
        metadata={
            "name": "RulesetSchemes",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    structure_maps: None | StructureMapsType = field(
        default=None,
        metadata={
            "name": "StructureMaps",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    transformation_schemes: None | TransformationSchemesType = field(
        default=None,
        metadata={
            "name": "TransformationSchemes",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    user_defined_operator_schemes: None | UserDefinedOperatorSchemesType = (
        field(
            default=None,
            metadata={
                "name": "UserDefinedOperatorSchemes",
                "type": "Element",
                "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            },
        )
    )
    value_lists: None | ValueListsType = field(
        default=None,
        metadata={
            "name": "ValueLists",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    vtl_mapping_schemes: None | VtlMappingSchemesType = field(
        default=None,
        metadata={
            "name": "VtlMappingSchemes",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
