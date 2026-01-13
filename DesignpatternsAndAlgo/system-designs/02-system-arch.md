![[Pasted image 20260112112157.png]]

1. Load Balancing: Distributed incoming traffic across multiple servers to ensure no single node is overwhelmed.
    
2. Caching: Stores frequently accessed data in memory to reduce latency.
    
3. Content Delivery Network (CDN): Stores static assets across geographically distributed edge servers so users download content from the nearest location.
    
4. Message Queue: Decouples components by letting producers enqueue messages that consumers process asynchronously.
    
5. Publish-Subscribe: Enables multiple consumers to receive messages from a topic.
    
6. API Gateway: Acts as a single entry point for client requests, handling routing, authentication, rate limiting, and protocol translation.
    
7. Circuit Breaker: Monitors downstream service calls and stops attempts when failures exceed a threshold.
    
8. Service Discovery: Automatically tracks available service instances so components can locate and communicate with each other dynamically.
    
9. Sharding: Splits large datasets across multiple nodes based on a specific shard key.
    
10. Rate Limiting: Controls the number of requests a client can make in a given time window to protect services from overload.
    
11. Consistent Hashing: Distributes data across nodes in a way that minimizes reorganization when nodes join or leave.
    
12. Auto Scaling: Automatically adds or removes compute resources based on defined metrics.