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

---------
![[Pasted image 20260126133056.png]]
Here’s a quick tour of what actually happens:

1. The journey starts the moment you type “google. com” into the address bar.
    
2. The browser checks everywhere for a cached IP: Before touching the network, your browser looks through multiple cache layers, browser cache, OS cache, router cache, and even your ISP’s DNS cache.  
    A cache hit means an instant IP address. A miss kicks off the real journey.
    
3. Recursive DNS resolution begins: Your DNS resolver digs through the global DNS hierarchy:  
    - Root servers  
    - TLD servers (.com)  
    - Authoritative servers for google. com
    
4. A TCP connection is established: Your machine and Google’s server complete the classic TCP 3-way handshake:  
    - SYN → SYN/ACK → ACK  
    Only after the connection is stable does the browser move on. TLS handshake wraps everything in encryption. By the end of this handshake, a secure HTTPS tunnel is ready.
    
5. The actual HTTP request finally goes out: Google processes the request and streams back HTML, CSS, JavaScript, and all the assets needed to build the page.
    
6. The rendering pipeline kicks in:  
    Your browser parses HTML into a DOM tree, CSS into a CSSOM tree, merges them into the Render Tree, and then:  
    - Lays out elements  
    - Loads and executes JavaScript  
    - Repaints the screen  
      
    8. The page is fully loaded.  
    Over to you: What part of this journey was most surprising the first time you learned how browsers work?