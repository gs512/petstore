# Docker : 
#  Start Kafka Server
docker-compose up -d
# verify that both the servers are listening
nc -z localhost 22181
nc -z localhost 29092
# check the verbose logs
docker-compose logs kafka | grep -i started

# open a cli on kafka container and run 
kafka-topics --create --partitions 4 --bootstrap-server kafka:29092 --topic test

kafka-console-consumer --from-beginning --bootstrap-server kafka:29092 --topic=test 
kafka-console-producer --broker-list kafka:29092 --topic=test 