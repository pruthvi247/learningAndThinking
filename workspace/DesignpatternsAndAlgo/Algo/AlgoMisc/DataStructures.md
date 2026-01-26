
![[Pasted image 20230816094209.png]]

## [Algorithms for  system design interview](https://www.youtube.com/watch?v=xbgzl2maQUU)

![[Pasted image 20230828092534.png]]

### [Consistent hashing](https://www.toptal.com/big-data/consistent-hashing)

Many well-known distributed systems use consistent hashing. For example, **Apache Cassandra** and **Amazon’s DynamoDB** use consistent hashing to distribute and replicate data efficiently across the cluster.

Similarly, the Content Delivery Networks(CDN) distribute contents evenly across the edge servers using consistent hashing.

In addition to this, Load Balancers use consistent hashing to distribute persistent connections across backend servers.

## Quadtree

A **quadtree** is a [tree data structure](https://en.wikipedia.org/wiki/Tree_data_structure "Tree data structure") in which each internal node has exactly four children. Quadtrees are the two-dimensional analog of [octrees](https://en.wikipedia.org/wiki/Octree "Octree") and are most often used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions.
![[Pasted image 20230828101804.png]]

## [Leaky bucket ](https://www.scaler.com/topics/leaky-bucket-algorithm/)
The **leaky bucket algorithm** is a method of congestion control where multiple packets are stored temporarily. These packets are sent to the network at a constant rate that is decided between the sender and the network. This algorithm is used to implement congestion control through traffic shaping in data networks.
![[Pasted image 20230828102024.png]]
![[Pasted image 20230828102408.png]]

- Consider that, each network interface has a leaky bucket.
- Now, when the sender wants to transmit packets, the packets are thrown into the bucket. These packets get accumulated in the bucket present at the network interface.
- If the bucket is full, the packets are discarded by the buckets and are lost.
- This bucket will leak at a constant rate. This means that the packets will be transmitted to the network at a constant rate. This constant rate is known as the Leak Rate or the Average Rate.
- In this way, bursty traffic is converted into smooth, fixed traffic by the leaky bucket.
- Queuing and releasing the packets at different intervals help in reducing network congestion and increasing overall performance.

This design can be simulated inside the host operating system, specifically in the transport and the network layer.

The leaky bucket algorithm can be implemented using a **FIFO** (First In First Out) **queue**. Packets that arrive first in the bucket should be transmitted first.

- A queue acts as a bucket or a buffer to hold the packets. This is implemented in the host operating system.
- Packets from the host are pushed into the queue as they arrive.
- At some intervals, the packets are sent to the network depending upon the leak rate. Generally, this interval is a clock tick. A clock tick is an interrupt generated from the physical clock to the processor.
- This leak rate is predetermined by the network. A network will guarantee some dedicated bandwidth for each host. This dedicated bandwidth can be used to set up this leak rate.
- If this queue is full, then the packets that arrive will be discarded.

## TRIE :
A `Trie`, (also known as a prefix tree) is a special type of tree used to store associative data structures

![[Pasted image 20230828103104.png]]
![[Pasted image 20230828103137.png]]

## [Bloom Filter](https://llimllib.github.io/bloomfilter-tutorial/):
A Bloom filter is a data structure designed to tell you, rapidly and memory-efficiently, whether an element is present in a set.

![[Pasted image 20230828111129.png]]
This makes it especially ideal when trying to search for items on expensive-to-access resources (such as over a network or disk): If I have a large on-disk database and I want to know if the key _foo_ exists in it, I can query the Bloom filter first, which will tell me with a certainty whether it potentially exists (and then the disk lookup can continue) or whether it does _not_ exist, and in this case I can forego the expensive disk lookup and simply send a negative reply up the stack.

While it’s possible to use other [data structures](https://redis.com/ebook/part-1-getting-started/chapter-1-getting-to-know-redis/1-2-what-redis-data-structures-look-like/) (such as a hash table) to perform this, Bloom filters are also especially useful in that they occupy very little space per element, typically counted in the number of _bits_ (not bytes!). There will exist a percentage of false positives (which is controllable), but for an initial test of whether a key exists in a set, they provide excellent speed and most importantly excellent space efficiency.

Bloom filters are used in a wide variety of applications such as ad serving – making sure a user doesn’t see an ad too often; likewise in content recommendation systems – ensuring recommendations don’t appear too often, in databases – quickly checking if an entry exists in a table before accessing it on disk, and so on.

`good read`: https://redis.com/blog/bloom-filter/


![[Pasted image 20230828111215.png]]

## Raft:

Raft is a distributed consensus algorithm. It was designed to be easily understood. It solves the 
problem of getting multiple servers to agree on a shared state even in the face of failures. The shared status is usually a data structure supported by a replicated log. We need the system to be fully operational as long as a majority of the servers are up.

The raft algorithm was developed primarily as an alternative to the Paxos consensus algorithm

Raft is built around the concept of a replicated log. When the leader receives a request, it first stores an entry for it in its durable local log. This local log is then replicated to all of the followers, or replicas. Once the majority of replicas confirm they have persisted with the log, the leader applies the entry and instructs the replicas to do the same. In the event of leader failure, a replica with the most up-to-date log becomes the leader.

Raft defines not only how the group makes a decision, but also the protocol for adding new members and removing members from the group. This feature makes Raft a natural fit for managing topology changes in distributed systems.
![[Pasted image 20230828112215.png]]
