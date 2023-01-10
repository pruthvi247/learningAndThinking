[source:](https://stiller.blog/2020/02/rabbitmq-vs-kafka-an-architects-dilemma-part-2/)

RabbitMQ is a **message broker**, while Apache Kafka is a **distributed streaming platform**.


#### TL;DR 

-   RabbitMQ is preferable when we need:
    1.  Advanced and flexible routing rules.
    2.  Message timing control (controlling either message expiry or message delay).
    3.  Advanced fault handling capabilities, in cases when consumers are more likely to fail to process messages (either temporarily or permanently).
    4.  Simpler consumer implementations.
-   Kafka is preferable when we require:
    1.  Strict message ordering.
    2.  Message retention for extended periods, including the possibility of replaying past messages.
    3.  The ability to reach a high scale when traditional solutions do not suffice.

1. RabbitMQ has built-in support for retry logic and dead-letter exchanges, while Kafka leaves such implementations in the hands of its users. 
2. Ordering of messages is taken care by kafka but we have to implement the logic for retry, where as ordering of message are partial for
			given scenario if one consumer fails process after reading the message, it is again put back to the message queue, kafka over comes this by having partitions to the topic and each partition can have a consumer
3. rabbitmq effectively allow consumers to specify the type of messages they are interested in receiving,Kafka, on the other hand, does not allow consumers to filter messages in a topic before polling them. A subscribed consumer receives all messages in a partition without exception.
4. **Rabbitmq** : If a consumer does not process it in due time, then it is automatically removed from the queue (and transferred to a dead-letter exchange.
	RabbitMQ supports delayed/scheduled messages via the use of a [plugin](https://github.com/rabbitmq/rabbitmq-delayed-message-exchange). When this plugin is enabled on a message exchange, a producer can send a message to RabbitMQ, and the producer can delay the time in which RabbitMQ routes this message to a consumer’s queue.
	**Kafka**: Kafka provides no support for such features. It writes messages to partitions as they arrive, where they are immediately available for consumers to consume. Also, Kafka provides no TTL mechanism for messages, although we could implement one at the application level. 
5. **RabbitMQ** evicts messages from storage as soon as consumers successfully consume them. This behavior cannot be modified. It is part of almost all message brokers’ design.
	**Kafka** persists all messages by design up to a configured timeout per topic. In regards to message retention, Kafka does not care regarding the consumption status of its consumers as it acts as a message log.

Questions to be considered:
1. How many times should we retry upon a message processing failure? 
2. How long should we wait between retries? 
3. How do we distinguish between transient and persistent failures?
4. what do we do when all retries fail, or we encounter a persistent failure?
5. Get the status of the message

Rabbit mq : 
**RabbitMQ** when a consumer is busy processing and retrying a specific message (even before returning it to the queue), other consumers can concurrently process the messages which follow it. Message processing as a whole is not stuck while a specific consumer retries a specific message. As a result, a message consumer can synchronously retry a message for as much as it wants without affecting the entire system.
![[Pasted image 20220509123508.png]]

**Kafka** does not provide any such mechanisms out of the box. With Kafka, it is up to us to provide and implement message retry mechanisms at the application level. Also, we should note that when a consumer is busy synchronously retrying a specific message, other messages from the same partition cannot be processed. We cannot reject and retry a specific message and commit a message that came after it since the consumer cannot change the message order. As you remember, the partition is merely an append-only log.
An application-level solution can commit failed messages to a “retry topic” and handle retries from there; however, we lose message ordering in this type of solution. [ref-uber engineering](https://eng.uber.com/reliable-reprocessing/)

##### Performance : 
Kafka is generally considered to have better performance than RabbitMQ. Kafka uses sequential disk I/O to boost performance. Its architecture using partitions means it scales better horizontally (scale-out) than RabbitMQ, which scales better vertically (scale-up).

##### ### Consumer Complexity:
- RabbitMQ uses a smart-broker & dumb-consumer approach.RabbitMQ’s structure also means that a queue’s consumer group can efficiently scale from just 1 consumer to multiple consumers when the load increases, without any changes to the system.
- ![[Pasted image 20220509124230.png]]
- Kafka, on the other hand, uses a dumb-broker & smart-consumer approach
- Kafka -  as the load increases, we can only scale the consumer group up to the point where the number of consumers is equal to the number of partitions in the topic.Above that, we need to configure Kafka to add additional partitions.However, as load decreases again – we cannot remove the partitions we already added, adding more to the work consumers need to make
- ![[Pasted image 20220509124334.png]]
- ![[Pasted image 20220509124425.png]]

