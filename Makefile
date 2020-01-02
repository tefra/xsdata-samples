generate:
	xsdata xsd/travelport/air_v48_0/AirReqRsp.xsd --package samples.travelport.output.air_v48_0
	xsdata xsd/amadeus/Fare_MasterPricerTravelBoardSearch_15_3_1A.xsd --package samples.amadeus.output
	xsdata xsd/amadeus/Fare_MasterPricerTravelBoardSearchReply_15_3_1A.xsd --package samples.amadeus.output
	xsdata xsd/sabre/BargainFinderMaxRQ_v1-9-7.xsd --package samples.sabre.output
	xsdata xsd/sabre/BargainFinderMaxRS_v1-9-7.xsd --package samples.sabre.output

print:
	xsdata xsd/travelport/air_v48_0/AirReqRsp.xsd --package samples.travelport.output.air_v48_0 --print > ./samples/travelport/classes.txt
	xsdata xsd/amadeus/Fare_MasterPricerTravelBoardSearch_15_3_1A.xsd --package samples.amadeus.output --print > ./samples/amadeus/classes.txt
	xsdata xsd/sabre/BargainFinderMaxRQ_v1-9-7.xsd --package samples.sabre.output --print > ./samples/sabre/classes.txt
