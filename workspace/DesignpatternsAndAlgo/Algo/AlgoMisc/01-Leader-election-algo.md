![[Pasted image 20260112112343.png]]
1. Bully Algorithm: Nodes have unique numeric IDs, and the one with the highest ID takes over as leader after notifying others.
    
2. Ring Algorithm: Nodes are arranged in a logical ring and pass messages containing their IDs. The highest ID node wins and becomes the leader.
    
3. Paxos Algorithm: A quorum-based consensus method where proposers suggest values, acceptors vote, and a learner recognizes the chosen leader.
    
4. Raft Algorithm: Nodes start as followers and become candidates if no leader is detected. The first to secure a majority of votes becomes the leader.
    
5. Zookeeper Atomic Broadcast: Uses ephemeral sequential znodes to elect the leader, ensuring that the lowest-numbered znode holder is the leader.