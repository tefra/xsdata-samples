from ubl.models.common.ubl_common_aggregate_components_2_1 import Consignment
from ubl.models.common.ubl_common_aggregate_components_2_1 import Status
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportEquipment
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportExecutionPlanDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportHandlingUnit
from ubl.models.common.ubl_common_basic_components_2_1 import ConditionCode
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import StatusReason
from ubl.models.common.ubl_common_basic_components_2_1 import StatusReasonCode
from ubl.models.common.ubl_common_basic_components_2_1 import TransportExecutionStatusCode
from ubl.models.common.ubl_common_basic_components_2_1 import TransportationStatusTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.maindoc.ubl_transportation_status_2_1 import TransportationStatus
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = TransportationStatus(
    ublversion_id=UblversionId(
        value="2.1"
    ),
    id=Id(
        value="TS_1"
    ),
    issue_date=XmlDate(2011, 10, 6),
    issue_time=XmlTime(9, 29, 30, 0, 60),
    transportation_status_type_code=TransportationStatusTypeCode(
        value="All deviations"
    ),
    transport_execution_status_code=TransportExecutionStatusCode(
        value="35"
    ),
    consignment=[
        Consignment(
            id=Id(
                value="CON_1"
            ),
            transport_handling_unit=[
                TransportHandlingUnit(
                    id=Id(
                        value="CON_THU_1"
                    ),
                    transport_equipment=[
                        TransportEquipment(
                            id=Id(
                                value="CON_TE_1"
                            )
                        ),
                    ],
                    status=[
                        Status(
                            condition_code=ConditionCode(
                                value="4"
                            ),
                            status_reason_code=StatusReasonCode(
                                value="23"
                            ),
                            status_reason=[
                                StatusReason(
                                    value="Reefer container lost power - cargo of fish destroyed"
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        ),
    ],
    transport_execution_plan_document_reference=TransportExecutionPlanDocumentReference(
        id=Id(
            value="TEP_1"
        )
    )
)
