# kafka-python
 


## 1. Create kafka directory

```bash
mkdir kafka
cd kafka
```
## 2. Extract tag archive to kafka folder and skip the first main folder (--strip 1)

```bash
tar -xvzf ~/downloads/kafka.tgz --strip 1
```
## 3. Check your Java version and install it if missing

`java -version`

https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-20-04

```bash
sudo apt install default-jre -y
java -version

# to compile and run java-based apps install jdk

sudo apt install default-jdk -y
javac -version
```
# 4. Run services

At this moment, to run kafka server we need to run kafka service itself and zookeeper service. Both builds a kafka cluster. On every one machine, you can have many kafka servers/brokers. Zookeeper manages them.

What is Zookeeper? // Kafka will not want zookeeper anymore soon.

Zookeeper is a top-level software developed by Apache that acts as a centralized service and is used to maintain naming and configuration data and to provide flexible and robust synchronization within distributed systems. Zookeeper keeps track of status of the Kafka cluster nodes and it also keeps track of Kafka topics, partitions etc.

Zookeeper it self is allowing multiple clients to perform simultaneous reads and writes and acts as a shared configuration service within the system. The Zookeeper atomic broadcast (ZAB) protocol i s the brains of the whole system, making it possible for Zookeeper to act as an atomic broadcast system and issue orderly updates.

How does Zookeeper work?

The data within Zookeeper is divided across multiple collection of nodes and this is how it achieves its high availability and consistency. In case a node fails, Zookeeper can perform instant failover migration; e.g. if a leader node fails, a new one is selected in real-time by polling within an ensemble. A client connecting to the server can query a different node if the first one fails to respond.


The order below is required as kafka shell script requires zookeeper to be running.

## 1. Run Zookeeper service

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```
If everything is ok, then Zookeeper should listen on port 0.0.0.0/0.0.0.0:2181

## 2. Run Kafka service

Kafka might be launched by executing shell script from /bin folder. To do so, we need to execute the command below and pass config files for the script. See below:
```bash
bin/kafka-server-start.sh config/server.properties
```
if everything is ok, then kafka broker should listen on port 9092

```
[2021-04-23 22:36:20,272] INFO [broker-0-to-controller-send-thread]: Recorded new controller, from now on will use broker lin1dev1:9092
```

## Running multi-broker apache kafka cluster on a single node

https://www.michael-noll.com/blog/2013/03/13/running-a-multi-broker-apache-kafka-cluster-on-a-single-node/
