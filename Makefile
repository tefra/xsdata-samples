generate:
	xsdata generate xsd/travelport/air_v48_0/AirReqRsp.xsd --package samples.travelport.output.air_v48_0
	xsdata generate xsd/amadeus/Fare_MasterPricerTravelBoardSearch_15_3_1A.xsd --package samples.amadeus.output
	xsdata generate xsd/sabre/BargainFinderMaxRQ_v1-9-7.xsd --package samples.sabre.output

print:
	xsdata generate xsd/travelport/air_v48_0/AirReqRsp.xsd --package samples.travelport.output.air_v48_0 --print > ./samples/travelport/classes.txt
	xsdata generate xsd/amadeus/Fare_MasterPricerTravelBoardSearch_15_3_1A.xsd --package samples.amadeus.output --print > ./samples/amadeus/classes.txt
	xsdata generate xsd/sabre/BargainFinderMaxRQ_v1-9-7.xsd --package samples.sabre.output --print > ./samples/sabre/classes.txt
