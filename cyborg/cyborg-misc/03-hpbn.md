[source-book](https://hpbn.co/)

_Latency_
The time from the source sending a packet to the destination receiving it

_Bandwidth_
Maximum throughput of a logical or physical communication path

> Network data rates are typically measured in bits per second (bps), whereas data rates for non-network equipment are typically shown in bytes per second (Bps). This is a common source of confusion, pay close attention to the units.
	For example, to put a 10 megabyte (MB) file "on the wire" over a 1Mbps link, we will need 80 seconds. 10MB is equal to 80Mb because there are 8 bits for every byte!


>Content delivery network (CDN) services provide many benefits, but chief among them is the simple observation that distributing the content around the globe, and serving that content from a nearby location to the client, enables us to significantly reduce the propagation time of all the data packets.
	We may not be able to make the packets travel faster, but we can reduce the distance by strategically positioning our servers closer to the users! Leveraging a CDN to serve your data can offer significant performance benefits.

`traceroute google.com`
On Unix platforms the tool can be run from the command line via `traceroute`, and on Windows it is known as `tracert`.

Proportional Rate Reduction (PRR) is a new algorithm specified by RFC 6937, whose goal is to improve the speed of recovery when a packet is lost. How much better is it? According to measurements done at Google, where the new algorithm was developed, it provides a 3–10% reduction in average latency for connections with packet loss.

PRR is now the default congestion-avoidance algorithm in Linux 3.2+ kernels — another good reason to upgrade your servers!


For Linux users, `ss` is a useful power tool to inspect various statistics for open sockets. From the command line, run `ss --options --extended --memory --processes --info` to see the current peers and their respective connection settings.

## UDP

UDP is a simple, stateless protocol, suitable for bootstrapping other application protocols on top: virtually all of the protocol design decisions are left to the application above it. However, before you run away to implement your own protocol to replace TCP, you should think carefully about complications such as UDP interaction with the many layers of deployed middleboxes (NAT traversal), as well as general network protocol design best practices. Without careful engineering and planning, it is not uncommon to start with a bright idea for a new protocol but end up with a poorly implemented version of TCP. The algorithms and the state machines in TCP have been honed and improved over decades and have taken into account dozens of mechanisms that are anything but easy to replicate well.

No guarantee of message delivery
	No acknowledgments, retransmissions, or timeouts

No guarantee of order of delivery
	No packet sequence numbers, no reordering, no head-of-line blocking

No connection state tracking
	No connection establishment or teardown state machines

No congestion control
	No built-in client or network feedback mechanisms


`NAT:` NAT translates private IP address to public IP addresses,allowing us to map private ip address to public ip addresses,it helps in network security

### TCP vs UDP

They're different ways to send information on a network. TCP has built in checks to make sure all the data gets there in the correct order, but that means it takes longer to since all those checks take more time. UDP just sends all the data but doesn't check to make sure it all arrived. It's a lot faster, but less reliable.

---

TCP looks kinda like:

PC1: I want to send you some data. It will be in 12 packets, each 256 bytes long.

PC2: I am ready to receive packet 1 of 12.

PC1: I am sending packet 1 of 12, it is 256 bytes long.

PC2: I have received packet 1 of 12, it was 256 bytes long. I am ready to receive packet 2 of 12.

PC1: I am sending packet 2 of 12, it is 256 bytes long.

PD2: I have received packet 2 of 12, but it was only 183 bytes long. Please resend.

PC1: I am sending packet 2 of 12, it is 256 bytes long.

PC2: I have received packet 2 of 12, it was 256 bytes long. I am ready to receive packet 3 of 12.

... And so on

---

UDP looks kinda like:

PC1: I want to send you some data. It will be in 12 packets, each 256 bytes long.

PC2: I am ready to receive 12 packets, each 256 bytes long.

PC1: I am sending packet 1 of 12.

PC1: I am sending packet 2 of 12.

PC1: I am sending packet 3 of 12.

PC1: I am sending packet 4 of 12.

... And so on

# TLS
When the SSL protocol was standardized by the IETF, it was renamed to Transport Layer Security (TLS). Many use the TLS and SSL names interchangeably, but technically, they are different, since each describes a different version of the protocol.

The SSL protocol was originally developed at Netscape to enable ecommerce transaction security on the Web, which required encryption to protect customers’ personal data, as well as authentication and integrity guarantees to ensure a safe transaction. To achieve this, the SSL protocol was implemented at the application layer, directly on top of TCP ([Figure 4-1](https://hpbn.co/transport-layer-security-tls/#ssl-layer)), enabling protocols above it (HTTP, email, instant messaging, and many others) to operate unchanged while providing communication security when communicating across the network.

![Figure 4-1. Transport Layer Security (TLS)](https://hpbn.co/assets/diagrams/9873c7441be06e0b53a006aac442696c.svg)

TLS was designed to operate on top of a reliable transport protocol such as TCP. However, it has also been adapted to run over datagram protocols such as UDP. The Datagram Transport Layer Security (DTLS) protocol, defined in RFC 6347, is based on the TLS protocol and is able to provide similar security guarantees while preserving the datagram delivery model.

_Encryption_
A mechanism to obfuscate what is sent from one host to another.

_Authentication_
A mechanism to verify the validity of provided identification material.

_Integrity_
A mechanism to detect message tampering and forgery.


More info on TLS hand shake : [practical Networking](https://www.youtube.com/watch?v=ZkL10eoG1PY)


>Internet Engineering Task Force (IETF)


## TLS Handshake

Before the client and the server can begin exchanging application data over TLS, the encrypted tunnel must be negotiated: the client and the server must agree on the version of the TLS protocol, choose the ciphersuite, and verify certificates if necessary. Unfortunately, each of these steps requires new packet roundtrips ([Figure 4-2](https://hpbn.co/transport-layer-security-tls/#tls-handshake-protocol)) between the client and the server, which adds startup latency to all TLS connections.


![Figure 4-2. TLS handshake protocol](https://hpbn.co/assets/diagrams/b83b75dbbf5b7e4be31c8000f91fc1a8.svg)
![[Pasted image 20260614203715.png]]

`0 ms`

TLS runs over a reliable transport (TCP), which means that we must first complete the TCP three-way handshake, which takes one full roundtrip.

`56 ms`

With the TCP connection in place, the client sends a number of specifications in plain text, such as the version of the TLS protocol it is running, the list of supported ciphersuites, and other TLS options it may want to use.

`84 ms`

The server picks the TLS protocol version for further communication, decides on a ciphersuite from the list provided by the client, attaches its certificate, and sends the response back to the client. Optionally, the server can also send a request for the client’s certificate and parameters for other TLS extensions.

`112 ms`

Assuming both sides are able to negotiate a common version and cipher, and the client is happy with the certificate provided by the server, the client initiates either the RSA or the Diffie-Hellman key exchange, which is used to establish the symmetric key for the ensuing session.

`140 ms`

The server processes the key exchange parameters sent by the client, checks message integrity by verifying the MAC, and returns an encrypted `Finished` message back to the client.

`168 ms`

The client decrypts the message with the negotiated symmetric key, verifies the MAC, and if all is well, then the tunnel is established and application data can now be sent.

As the above exchange illustrates, new TLS connections require two roundtrips for a "full handshake"—that’s the bad news. However, in practice, optimized deployments can do much better and deliver a consistent 1-RTT TLS handshake:

- False Start is a TLS protocol extension that allows the client and server to start transmitting encrypted application data when the handshake is only partially complete—i.e., once `ChangeCipherSpec` and `Finished` messages are sent, but without waiting for the other side to do the same. This optimization reduces handshake overhead for new TLS connections to one roundtrip; see [Enable TLS False Start](https://hpbn.co/transport-layer-security-tls/#enable-tls-false-start).
    
- If the client has previously communicated with the server, an "abbreviated handshake" can be used, which requires one roundtrip and also allows the client and server to reduce the CPU overhead by reusing the previously negotiated parameters for the secure session; see [TLS Session Resumption](https://hpbn.co/transport-layer-security-tls/#tls-session-resumption).
    

The combination of both of the above optimizations allows us to deliver a consistent 1-RTT TLS handshake for new and returning visitors, plus computational savings for sessions that can be resumed based on previously negotiated session parameters. Make sure to take advantage of these optimizations in your deployments.

> One of the design goals for [TLS 1.3](https://hpbn.co/tls13-spec) is to reduce the latency overhead for setting up the secure connection: 1-RTT for new, and 0-RTT for resumed sessions!


>An RSA handshake is ==the legacy method used in TLS/SSL to negotiate a secure connection between a client and a server==. It relies on asymmetric encryption—the server's RSA public and private keys—to securely share a "pre-master secret," which both sides then use to create the symmetric session keys for encrypted data transfer
>	By contrast, the Diffie-Hellman key exchange allows the client and server to negotiate a shared secret without explicitly communicating it in the handshake: the server’s private key is used to sign and verify the handshake, but the established symmetric key never leaves the client or server and cannot be intercepted by a passive attacker even if they have access to the private key.


#### Performance of Public vs. Symmetric Key Cryptography

Public-key cryptography is used only during initial setup of the TLS tunnel: the certificates are authenticated and the key exchange algorithm is executed.

Symmetric key cryptography, which uses the established symmetric key is then used for all further communication between the client and the server within the session. This is done, in large part, to improve performance—public key cryptography is much more computationally expensive. To illustrate the difference, if you have OpenSSL installed on your computer, you can run the following tests:

- `$> openssl speed ecdh`
    
- `$> openssl speed aes`
    

Note that the units between the two tests are not directly comparable: the Elliptic Curve Diffie-Hellman (ECDH) test provides a summary table of operations per second for different key sizes, while AES performance is measured in bytes per second. Nonetheless, it should be easy to see that the ECDH operations are much more computationally expensive.

The exact performance numbers vary significantly based on used hardware, number of cores, TLS version, server configuration, and other factors. Don’t fall for an outdated benchmark! Always run the performance tests on your own hardware and refer to [Reduce Computational Costs](https://hpbn.co/transport-layer-security-tls/#reduce-computational-costs) for additional context.

> The command `openssl speed ecdh` is ==a benchmark tool used to **test the performance of Elliptic Curve Diffie-Hellman (ECDH) key exchange algorithms** on your computer's CPU==

### Server Name Indication (SNI)

An encrypted TLS tunnel can be established between any two TCP peers: the client only needs to know the IP address of the other peer to make the connection and perform the TLS handshake. However, what if the server wants to host multiple independent sites, each with its own TLS certificate, on the same IP address — how does that work? Trick question; it doesn’t.

To address the preceding problem, the Server Name Indication (SNI) extension was introduced to the TLS protocol, which allows the client to indicate the hostname the client is attempting to connect to as part of the TLS handshake. In turn, the server is able to inspect the SNI hostname sent in the `ClientHello` message, select the appropriate certificate, and complete the TLS handshake for the desired host.

### Application Layer Protocol Negotiation (ALPN)

to use port 443, which is reserved for secure HTTPS sessions running over TLS. The use of an end-to-end encrypted tunnel obfuscates the data from intermediate proxies and enables a quick and reliable way to deploy new application protocols. However, we still need another mechanism to negotiate the protocol that will be used within the TLS session.

Application Layer Protocol Negotiation (ALPN), as the name implies, is a TLS extension that addresses the need. It extends the TLS handshake ([Figure 4-2](https://hpbn.co/transport-layer-security-tls/#tls-handshake-protocol)) and allows the peers to negotiate protocols without additional roundtrips. Specifically, the process is as follows:

- The client appends a new `ProtocolNameList` field, containing the list of supported application protocols, into the `ClientHello` message.
    
- The server inspects the `ProtocolNameList` field and returns a `ProtocolName` field indicating the selected protocol as part of the `ServerHello` message.
    

The server may respond with only a single protocol name, and if it does not support any that the client requests, then it may choose to abort the connection. As a result, once the TLS handshake is finished, both the secure tunnel is established, and the client and server are in agreement as to which application protocol will be used; the client and server can immediately begin exchanging messages via the negotiated protocol.

### Session Identifiers

The first Session Identifiers (RFC 5246) resumption mechanism was introduced in SSL 2.0, which allowed the server to create and send a 32-byte session identifier as part of its `ServerHello` message during the full TLS negotiation we saw earlier. With the session ID in place, both the client and server can store the previously negotiated session parameters—keyed by session ID—and reuse them for a subsequent session.

Specifically, the client can include the session ID in the `ClientHello` message to indicate to the server that it still remembers the negotiated cipher suite and keys from previous handshake and is able to reuse them. In turn, if the server is able to find the session parameters associated with the advertised ID in its cache, then an abbreviated handshake ([Figure 4-3](https://hpbn.co/transport-layer-security-tls/#tls-resumed)) can take place. Otherwise, a full new session negotiation is required, which will generate a new session ID.

![Figure 4-3. Abbreviated TLS handshake protocol](https://hpbn.co/assets/diagrams/6cb3c673b9ae40cfbd2a88ffa02bfc66.svg)
Leveraging session identifiers allows us to remove a full roundtrip, as well as the overhead of public key cryptography, which is used to negotiate the shared secret key. This allows a secure connection to be established quickly and with no loss of security, since we are reusing the previously negotiated session data.

However, one of the practical limitations of the Session Identifiers mechanism is the requirement for the server to create and maintain a session cache for every client. This results in several problems on the server, which may see tens of thousands or even millions of unique connections every day: consumed memory for every open TLS connection, a requirement for a session ID cache and eviction policies, and nontrivial deployment challenges for popular sites with many servers, which should, ideally, use a shared TLS session cache for best performance.

None of the preceding problems are impossible to solve, and many high-traffic sites are using session identifiers successfully today. But for any multi-server deployment, session identifiers will require some careful thinking and systems architecture to ensure a well operating session cache.

## Chain of Trust and Certificate Authorities

Authentication is an integral part of establishing every TLS connection. After all, it is possible to carry out a conversation over an encrypted tunnel with any peer, including an attacker, and unless we can be sure that the host we are speaking to is the one we trust, then all the encryption work could be for nothing. To understand how we can verify the peer’s identity, let’s examine a simple authentication workflow between Alice and Bob:

- Both Alice and Bob generate their own public and private keys.
    
- Both Alice and Bob hide their respective private keys.
    
- Alice shares her public key with Bob, and Bob shares his with Alice.
    
- Alice generates a new message for Bob and signs it with her private key.
    
- Bob uses Alice’s public key to verify the provided message signature.
    

Trust is a key component of the preceding exchange. Specifically, public key encryption allows us to use the public key of the sender to verify that the message was signed with the right private key, but the decision to approve the sender is still one that is based on trust. In the exchange just shown, Alice and Bob could have exchanged their public keys when they met in person, and because they know each other well, they are certain that their exchange was not compromised by an impostor—perhaps they even verified their identities through another, secret (physical) handshake they had established earlier!

Next, Alice receives a message from Charlie, whom she has never met, but who claims to be a friend of Bob’s. In fact, to prove that he is friends with Bob, Charlie asked Bob to sign his own public key with Bob’s private key and attached this signature with his message ([Figure 4-4](https://hpbn.co/transport-layer-security-tls/#cot)). In this case, Alice first checks Bob’s signature of Charlie’s key. She knows Bob’s public key and is thus able to verify that Bob did indeed sign Charlie’s key. Because she trusts Bob’s decision to verify Charlie, she accepts the message and performs a similar integrity check on Charlie’s message to ensure that it is, indeed, from Charlie.

![Figure 4-4. Chain of trust for Alice, Bob, and Charlie](https://hpbn.co/assets/diagrams/ea8e7fb6c96bce4a62ab11458890ad2a.svg)

Figure 4-4. Chain of trust for Alice, Bob, and Charlie

What we have just done is established a chain of trust: Alice trusts Bob, Bob trusts Charlie, and by transitive trust, Alice decides to trust Charlie. As long as nobody in the chain is compromised, this allows us to build and grow the list of trusted parties.

Authentication on the Web and in your browser follows the exact same process as shown. Which means that at this point you should be asking: whom does your browser trust, and whom do you trust when you use the browser? There are at least three answers to this question:

Manually specified certificates

Every browser and operating system provides a mechanism for you to manually import any certificate you trust. How you obtain the certificate and verify its integrity is completely up to you.

Certificate authorities

A certificate authority (CA) is a trusted third party that is trusted by both the subject (owner) of the certificate and the party relying upon the certificate.

The browser and the operating system

Every operating system and most browsers ship with a list of well-known certificate authorities. Thus, you also trust the vendors of this software to provide and maintain a list of trusted parties.

In practice, it would be impractical to store and manually verify each and every key for every website (although you can, if you are so inclined). Hence, the most common solution is to use certificate authorities (CAs) to do this job for us ([Figure 4-5](https://hpbn.co/transport-layer-security-tls/#ca-cot)): the browser specifies which CAs to trust (root CAs), and the burden is then on the CAs to verify each site they sign, and to audit and verify that these certificates are not misused or compromised. If the security of any site with the CA’s certificate is breached, then it is also the responsibility of that CA to revoke the compromised certificate.

![Figure 4-5. CA signing of digital certificates](https://hpbn.co/assets/diagrams/bb75b8bd469ce5b703b76abb7042e978.svg)

Figure 4-5. CA signing of digital certificates

## TLS Record Protocol

Not unlike the IP or TCP layers below it, all data exchanged within a TLS session is also framed using a well-defined protocol ([Figure 4-8](https://hpbn.co/transport-layer-security-tls/#tls-record-diagram)). The TLS Record protocol is responsible for identifying different types of messages (handshake, alert, or data via the "Content Type" field), as well as securing and verifying the integrity of each message.

![Figure 4-8. TLS record structure](https://hpbn.co/assets/diagrams/4603275cd98c93aeb8c46b1b1afa0ba6.svg)

Figure 4-8. TLS record structure

A typical workflow for delivering application data is as follows:

- Record protocol receives application data.
    
- Received data is divided into blocks: maximum of 214 bytes, or 16 KB per record.
    
- Message authentication code (MAC) or HMAC is added to each record.
    
- Data within each record is encrypted using the negotiated cipher.
    

Once these steps are complete, the encrypted data is passed down to the TCP layer for transport. On the receiving end, the same workflow, but in reverse, is applied by the peer: decrypt record using negotiated cipher, verify MAC, extract and deliver the data to the application above it.

The good news is that all the work just shown is handled by the TLS layer itself and is completely transparent to most applications. However, the record protocol does introduce a few important implications that we need to be aware of:

- Maximum TLS record size is 16 KB
    
- Each record contains a 5-byte header, a MAC (up to 20 bytes for SSLv3, TLS 1.0, TLS 1.1, and up to 32 bytes for TLS 1.2), and padding if a block cipher is used.
    
- To decrypt and verify the record, the entire record must be available.
    

Picking the right record size for your application, if you have the ability to do so, can be an important optimization. Small records incur a larger CPU and byte overhead due to record framing and MAC verification, whereas large records will have to be delivered and reassembled by the TCP layer before they can be processed by the TLS layer and delivered to your application—skip ahead to [Optimize TLS Record Size](https://hpbn.co/transport-layer-security-tls/#optimize-tls-record-size) for full details.

> If the TCP connection has been idle, and even if Slow-Start Restart is disabled on the server, the best strategy is to decrease the record size when sending a new burst of data: the conditions may have changed since last transmission, and our goal is to minimize the probability of buffering at the application layer due to lost packets, reordering, and retransmissions.


### Performance Checklist

As application developers we are shielded from most of the complexity of the TLS protocol—the client and server do most of the hard work on our behalf. However, as we saw in this chapter, this does not mean that we can ignore the performance aspects of delivering our applications over TLS. Tuning our servers to enable critical TLS optimizations and configuring our applications to enable the client to take advantage of such features pays high dividends: faster handshakes, reduced latency, better security guarantees, and more.

With that in mind, a short checklist to put on the agenda:

- Get best performance from TCP; see [Optimizing for TCP](https://hpbn.co/building-blocks-of-tcp/#optimizing-for-tcp).
    
- Upgrade TLS libraries to latest release, and (re)build servers against them.
    
- Enable and configure session caching and stateless resumption.
    
- Monitor your session caching hit rates and adjust configuration accordingly.
    
- Configure forward secrecy ciphers to enable TLS False Start.
    
- Terminate TLS sessions closer to the user to minimize roundtrip latencies.
    
- Use dynamic TLS record sizing to optimize latency and throughput.
    
- Audit and optimize the size of your certificate chain.
    
- Configure OCSP stapling.
    
- Configure HSTS and HPKP.
    
- Configure CSP policies.
    
- Enable HTTP/2; see [HTTP/2](https://hpbn.co/http2/).
    

Finally, to verify and test your configuration, you can use an online service, such as the [Qualys SSL Server Test](https://hpbn.co/qualys) to scan your public server for common configuration and security flaws. Additionally, you should familiarize yourself with the `openssl` command-line interface, which will help you inspect the entire handshake and configuration of your server locally.

![[Pasted image 20260615191543.png]]


The parsing of the HTML document is what constructs the Document Object Model (DOM). In parallel, there is an oft-forgotten cousin, the CSS Object Model (CSSOM), which is constructed from the specified stylesheet rules and resources. The two are then combined to create the "render tree," at which point the browser has enough information to perform a layout and paint something to the screen. So far, so good.

However, this is where we must, unfortunately, introduce our favorite friend and foe: JavaScript. Script execution can issue a synchronous `doc.write` and block DOM parsing and construction. Similarly, scripts can query for a computed style of any object, which means that JavaScript can also block on CSS. Consequently, the construction of DOM and CSSOM objects is frequently intertwined: DOM construction cannot proceed until JavaScript is executed, and JavaScript execution cannot proceed until CSSOM is available.


![Figure 10-7. User-specific performance timers exposed by Navigation Timing](https://hpbn.co/assets/diagrams/54af0f14aaabe6664274d81d60e38d40.svg)
`fig: Navigation timing`

As of early 2013, Navigation Timing is supported by IE9+, Chrome 6+, and Firefox 7+ across desktop and mobile platforms. The notable omissions are the Safari and Opera browsers. For the latest status, see [caniuse.com/nav-timing](http://caniuse.com/nav-timing).

For a deep dive into how these and other networking optimizations are implemented in Google Chrome, see [High Performance Networking in Google Chrome](https://hpbn.co/chrome-networking).

**Browser Optimizations**
1. `<link rel="dns-prefetch" href="//hostname_to_resolve.com"> [](https://hpbn.co/primer-on-web-performance/#dns)`
2. `<link rel="subresource"  href="/javascript/myapp.js"> [](https://hpbn.co/primer-on-web-performance/#subresource)`
3. `<link rel="prefetch"     href="/images/big.jpeg"> [](https://hpbn.co/primer-on-web-performance/#prefetch)`
4. `<link rel="prerender"    href="//example.org/next_page.html">`
-------
1. Pre-resolve specified hostname.[](https://hpbn.co/primer-on-web-performance/#subresource-co)
2. Prefetch critical resource found later on this page. [](https://hpbn.co/primer-on-web-performance/#prefetch-co)
3. Prefetch resource for this or future navigation.[](https://hpbn.co/primer-on-web-performance/#prerender-co)
4. Prerender specified page in anticipation of next user destination.
Each of these is a hint for a speculative optimization. The browser does not guarantee that it will act on it, but it may use the hint to optimize its loading strategy. Unfortunately, not all browsers support all hints ([Table 10-2](https://hpbn.co/primer-on-web-performance/#speculative-hints)), but if they don’t, then the hint is treated as a no-op and is harmless; make use of each of the techniques just shown where possible.
-----------
# HTTP2
HTTP/2 does not modify the application semantics of HTTP in any way. All the core concepts, such as HTTP methods, status codes, URIs, and header fields, remain in place. Instead, HTTP/2 modifies how the data is formatted (framed) and transported between the client and server, both of whom manage the entire process, and hides all the complexity from our applications within the new framing layer. As a result, all existing applications can be delivered without modification. That’s the good news.

>#### Why not HTTP/1.2?
	To achieve the performance goals set by the HTTP Working Group, HTTP/2 introduces a new binary framing layer that is not backward compatible with previous HTTP/1.x servers and clients—hence the major protocol version increment to HTTP/2.
	That said, unless you are implementing a web server (or a custom client) by working with raw TCP sockets, then you won’t see any difference: all the new, low-level framing is performed by the client and server on your behalf. The only observable differences will be improved performance and availability of new capabilities like request prioritization, flow control, and server push!

At the core of all performance enhancements of HTTP/2 is the new _binary framing layer_ ([Figure 12-1](https://hpbn.co/http2/#http2-framing-layer)), which dictates how the HTTP messages are encapsulated and transferred between the client and server.

![Figure 12-1. HTTP/2 binary framing layer](https://hpbn.co/assets/diagrams/ae09920e853bee0b21be83f8e770ba01.svg)

You will need some tooling to inspect the low-level HTTP/2 frame exchange. Your favorite hex viewer is, of course, an option. Or, for a more human-friendly representation, you can use a tool like Wireshark, which understands the HTTP/2 protocol and can capture, decode, and analyze the exchange.

Wireshark decodes and displays the frame fields in the same order as encoded on the wire

# Optimizing Application Delivery
while we cannot make the bits travel any faster, it is crucial that we apply all the possible optimizations at the transport and application layers to eliminate unnecessary roundtrips, requests, and minimize the distance traveled by each packet—i.e., position the servers closer to the client.

Moving up the stack from the physical layer, we must ensure that each and every server is configured to use the latest TCP and TLS best practices. Optimizing the underlying protocols ensures that each client can get the best performance—high throughput and low latency—when communicating with the server:

- [Optimizing for TCP](https://hpbn.co/building-blocks-of-tcp/#optimizing-for-tcp)
- [Optimizing for TLS](https://hpbn.co/transport-layer-security-tls/#optimizing-for-tls)
    
Finally, we arrive at the application layer. By all accounts and measures, HTTP is an incredibly successful protocol. After all, it is the common language between billions of clients and servers, enabling the modern Web. However, it is also an imperfect protocol, which means that we must take special care in how we architect our applications:

- We must work around the limitations of HTTP/1.x.
- We must leverage new performance capabilities of HTTP/2.
- We must be vigilant about applying the evergeen performance best practices.

## Evergreen Performance Best Practices

Regardless of the type of network or the type or version of the networking protocols in use, all applications should always seek to eliminate or reduce unnecessary network latency and minimize the number of transferred bytes. These two simple rules are the foundation for all of the evergreen performance best practices:

_Reduce DNS lookups_

Every hostname resolution requires a network roundtrip, imposing latency on the request and blocking the request while the lookup is in progress.

_Reuse TCP connections_

Leverage connection keepalive whenever possible to eliminate the TCP handshake and slow-start latency overhead; see [Slow-Start](https://hpbn.co/building-blocks-of-tcp/#slow-start).

_Minimize number of HTTP redirects_

HTTP redirects impose high latency overhead—e.g., a single redirect to a different origin can result in DNS, TCP, TLS, and request-response roundtrips that can add hundreds to thousands of milliseconds of delay. The optimal number of redirects is zero.

_Reduce roundtrip times_

Locating servers closer to the user improves protocol performance by reducing roundtrip times (e.g., faster TCP and TLS handshakes), and improves the transfer throughput of static and dynamic content; see [Uncached Origin Fetch](https://hpbn.co/transport-layer-security-tls/#uncached-origin-fetch).

_Eliminate unnecessary resources_

No request is faster than a request not made. Be vigilant about auditing and removing unnecessary resources.

By this point, all of these recommendations should require no explanation: latency is the bottleneck, and the fastest byte is a byte not sent. However, HTTP provides some additional mechanisms, such as caching and compression, as well as its set of version-specific performance quirks:


_Cache resources on the client_

Application resources should be cached to avoid re-requesting the same bytes each time the resources are required.For hands-on advice on optimizing your caching strategy, see the ["HTTP caching" section on Google’s Web Fundamentals](https://hpbn.co/wf-caching).

_Compress assets during transfer_

Application resources should be transferred with the minimum number of bytes: always apply the best compression method for each transferred asset.

_Eliminate unnecessary request bytes_

Reducing the transferred HTTP header data (e.g., HTTP cookies) can save entire roundtrips of network latency.

_Parallelize request and response processing_

Request and response queuing latency, both on the client and server, often goes unnoticed, but contributes significant and unnecessary latency delays.

_Apply protocol-specific optimizations_

HTTP/1.x offers limited parallelism, which requires that we bundle resources, split delivery across domains, and more. By contrast, HTTP/2 performs best when a single connection is used, and HTTP/1.x specific optimizations are removed.

Images account for over half of the transferred bytes of an average page, which makes them a high-value optimization target: the simple choice of an optimal image format can yield dramatically improved compression ratios; lossy compression methods can reduce transfer sizes by orders of magnitude; sizing the image to its display width will reduce both the transfer and memory footprints (see [Calculating Image Memory Requirements](https://hpbn.co/http1x/#calculating-image-memory-requirements)) on the client. Invest into tools and automation to optimize image delivery on your site.

For hands-on advice on reducing the transfer size of text, image, webfont, and other resources, see the ["Optimizing Content Efficiency" section on Google’s Web Fundamentals](https://hpbn.co/wf-compression).


- In HTTP/1.x, all HTTP headers, including cookies, are transferred uncompressed on each request.
    
- In HTTP/2, headers are compressed with HPACK, but at a minimum the cookie value is transferred on the first request, which will affect the performance of your initial page load.
Cookie size should be monitored judiciously: transfer the minimum amount of required data, such as a secure session token, and leverage a shared session cache on the server to look up other metadata. And even better, eliminate cookies entirely wherever possible—chances are, you do not need client-specific metadata when requesting static assets, such as images, scripts, and stylesheets.

### Parallelize Request and Response Processing

To achieve the fastest response times within your application, all resource requests should be dispatched as soon as possible. However, another important point to consider is how these requests will be processed on the server. After all, if all of our requests are then serially queued by the server, then we are once again incurring unnecessary latency. Here’s how to get the best performance:

- Reuse TCP connections by optimizing connection keepalive timeouts.
    
- Use multiple HTTP/1.1 connections where necessary for parallel downloads.
    
- Upgrade to HTTP/2 to enable multiplexing and best performance.
    
- Allocate sufficient server resources to process requests in parallel.

Identifying the sources of unnecessary client and server latency is both an art and science: examine the client resource waterfall (see [Analyzing the Resource Waterfall](https://hpbn.co/primer-on-web-performance/#analyzing-the-resource-waterfall)), as well as your server logs. Common pitfalls often include the following:


_Leverage HTTP pipelining_

If your application controls both the client and the server, then pipelining can help eliminate unnecessary network latency; see [HTTP Pipelining](https://hpbn.co/http1x/#http-pipelining).

_Apply domain sharding_

If your application performance is limited by the default six connections per origin limit, consider splitting resources across multiple origins; see [Domain Sharding](https://hpbn.co/http1x/#domain-sharding).

_Bundle resources to reduce HTTP requests_

Techniques such as concatenation and spriting can both help minimize the protocol overhead and deliver pipelining-like performance benefits; see [Concatenation and Spriting](https://hpbn.co/http1x/#concatenation-and-spriting).

_Inline small resources_

Consider embedding small resources directly into the parent document to minimize the number of requests; see [Resource Inlining](https://hpbn.co/http1x/#resource-inlining).

> Best practices of optimisation in **http1.x** may not be the best practice in **http2**

**Eliminate Domain Sharding**
HTTP/2 achieves the best performance by multiplexing requests over the same TCP connection, which enables effective request and response prioritization, flow control, and header compression. As a result, the optimal number of connections is exactly one and domain sharding is an anti-pattern.

HTTP/2 also provides a TLS connection-coalescing mechanism that allows the client to coalesce requests from different origins and dispatch them over the same connection when the following conditions are satisfied:

- The origins are covered by the same TLS certificate—e.g., a wildcard certificate, or a certificate with matching "Subject Alternative Names."
    
- The origins resolve to the same server IP address.

**Minimize Concatenation and Image Spriting**
Bundling multiple assets into a single response was a critical optimization for HTTP/1.x where limited parallelism and high protocol overhead typically outweighed all other concerns—see [Concatenation and Spriting](https://hpbn.co/http1x/#concatenation-and-spriting). However, with HTTP/2, multiplexing is no longer an issue, and header compression dramatically reduces the metadata overhead of each HTTP request. As a result, we need to reconsider the use of concatenation and spriting in light of its new pros and cons

**Eliminate Roundtrips with Server Push**

Server push is a powerful new feature of HTTP/2 that enables the server to send multiple responses for a single client request. That said, recall that the use of resource inlining (e.g., embedding an image into an HTML document via a data URI) is, in fact, a form of application-layer server push. As such, while this is not an entirely new capability for web developers, the use of HTTP/2 server push offers many performance benefits over inlining: pushed resources can be cached individually, reused across pages, canceled by the client, and more—see [Server Push](https://hpbn.co/http2/#server-push).

If the client does not support, or disables the use of server push, it will initiate the request for the same resource on its own—i.e., server push is a safe and transparent latency optimization.

With HTTP/2 the client places a lot of trust on the server. To get the best performance, an HTTP/2 client has to be "optimistic": it annotates requests with priority information (see [Stream Prioritization](https://hpbn.co/http2/#stream-prioritization)) and dispatches them to the server as soon as possible


There is no one best protocol or API. Every nontrivial application will require a mix of different transports based on a variety of requirements: interaction with the browser cache, protocol overhead, message latency, reliability, type of data transfer, and more. Some protocols may offer low-latency delivery (e.g., Server-Sent Events, WebSocket), but may not meet other critical criteria, such as the ability to leverage the browser cache or support efficient binary transfers in all cases.

![[Pasted image 20260616065416.png]]

_webRTC_ is a peer-to-peer delivery model offers a significant departure from XHR, SSE, and WebSocket protocols.

# XMLHttpRequest

XMLHttpRequest (XHR) is a browser-level API that enables the client to script data transfers via JavaScript. XHR made its first debut in Internet Explorer 5, became one of the key technologies behind the Asynchronous JavaScript and XML (AJAX) revolution, and is now a fundamental building block of nearly every modern web application

Prior to XHR, the web page had to be refreshed to send or fetch any state updates between the client and server. With XHR, this workflow could be done asynchronously and under full control of the application JavaScript code. XHR is what enabled us to make the leap from building pages to building interactive web applications in the browser.

However, the power of XHR is not only that it enabled asynchronous communication within the browser, but also that it made it simple. XHR is an application API provided by the browser, which is to say that the browser automatically takes care of all the low-level connection management, protocol negotiation, formatting of HTTP requests, and much more:

- The browser manages connection establishment, pooling, and termination.
- The browser determines the best HTTP(S) transport (HTTP/1.0, 1.1, 2).
- The browser handles HTTP caching, redirects, and content-type negotiation.
- The browser enforces security, authentication, and privacy constraints.

**Cross-Origin Resource Sharing (CORS)**

XHR is a browser-level API that automatically handles myriad low-level details such as caching, handling redirects, content negotiation, authentication, and much more. This serves a dual purpose. First, it makes the application APIs much easier to work with, allowing us to focus on the business logic. But, second, it allows the browser to sandbox and enforce a set of security and policy constraints on the application code.

The XHR interface enforces strict HTTP semantics on each request: the application supplies the data and URL, and the browser formats the request and handles the full lifecycle of each connection. Similarly, while the XHR API allows the application to add custom HTTP headers (via the `setRequestHeader()` method), there are a number of protected headers that are off-limits to application code:

- Accept-Charset, Accept-Encoding, Access-Control-*
- Host, Upgrade, Connection, Referer, Origin
- Cookie, Sec-*, Proxy-*, and a dozen others…

The browser will refuse to override any of the unsafe headers, which guarantees that the application cannot impersonate a fake user-agent, user, or the origin from where the request is being made. In fact, protecting the origin header is especially important, as it is the key piece of the "same-origin policy" applied to all XHR requests.

early versions of XHR were restricted to same-origin requests only, where the requesting origin had to match the origin of the requested resource: an XHR initiated from _example.com_ could request another resource only from the same _example.com_ origin. Alternatively, if the same origin precondition failed, then the browser would simply refuse to initiate the XHR request and raise an error.

However, while necessary, the same-origin policy also places severe restrictions on the usefulness of XHR: what if the server wants to offer a resource to a script running in a different origin? That’s where "Cross-Origin Resource Sharing" (CORS) comes in! CORS provides a secure opt-in mechanism for client-side cross-origin requests

The opt-in authentication mechanism for the CORS request is handled at a lower layer: when the request is made, the browser automatically appends the protected _Origin_ HTTP header, which advertises the origin from where the request is being made. In turn, the remote server is then able to examine the _Origin_ header and decide if it should allow the request by returning an _Access-Control-Allow-Origin_ header in its response

`Note`:
If the third-party server is not CORS aware, then the client request will fail, as the client always verifies the presence of the opt-in header. As a special case, CORS also allows the server to return a wildcard (`Access-Control-Allow-Origin: *`) to indicate that it allows access from any origin. However, think twice before enabling this policy!

With that, we are all done, right? Turns out, not quite, as CORS takes a number of additional security precautions to ensure that the server is CORS aware:

- CORS requests omit user credentials such as cookies and HTTP authentication.
    
- The client is limited to issuing "simple cross-origin requests," which restricts both the allowed methods (GET, POST, HEAD) and access to HTTP headers that can be sent and read by the XHR.
    

To enable cookies and HTTP authentication, the client must set an extra property (`withCredentials`) on the XHR object when making the request, and the server must also respond with an appropriate header (_Access-Control-Allow-Credentials_) to indicate that it is knowingly allowing the application to include private user data. Similarly, if the client needs to write or read custom HTTP headers or wants to use a "non-simple method" for the request, then it must first ask for permission from the third-party server by issuing a preflight request
```
<= Preflight response
HTTP/1.1 200 OK [](https://hpbn.co/xmlhttprequest/#pre-response)
Access-Control-Allow-Origin: http://example.com
Access-Control-Allow-Methods: GET, POST, PUT
Access-Control-Allow-Headers: My-Custom-Header
```
>To estimate the amount of transferred data, the server must provide a content length in its response: we can’t estimate progress of chunked transfers, since by definition, the total size of the response is unknown.
	Also, XHR requests do not have a default timeout, which means that a request can be "in progress" indefinitely. As a best practice, always set a meaningful timeout for your application and handle the error!

_Lack of streaming support as a first-class use case for XHR is a well-recognized limitation, and there is work in progress to address the problem_

While XHR may not meet the criteria, we do have other transports that are optimized for the streaming use case: Server-Sent Events offers a convenient API for streaming text-based data from server to client, and WebSocket offers efficient, bidirectional streaming for both binary and text-based data.

## XHR Use Cases and Performance

XMLHttpRequest is what enabled us to make the leap from building pages to building interactive web applications in the browser. First, it enabled asynchronous communication within the browser, but just as importantly, it also made the process simple. Dispatching and controlling a scripted HTTP request takes just a few lines of JavaScript code, and the browser handles all the rest:

- Browser formats the HTTP request and parses the response.
- Browser enforces relevant security (same-origin) policies.
- Browser handles content negotiation (e.g., gzip).
- Browser handles request and response caching.
- Browser handles authentication, redirects, and more…
    

As such, XHR is a versatile and a high-performance transport for any transfers that follow the HTTP request-response cycle. Need to fetch a resource that requires authentication, should be compressed while in transfer, and should be cached for future lookups? The browser takes care of all of this and more, allowing us to focus on the application logic!

However, XHR also has its limitations. As we saw, streaming has never been an official use case in the XHR standard, and the support is limited: streaming with XHR is neither efficient nor convenient. Different browsers have different behaviors, and efficient binary streaming is impossible. In short, XHR is not a good fit for streaming.

Similarly, there is no one best strategy for delivering real-time updates with XHR. Periodic polling incurs high overhead and message latency delays. Long-polling delivers low latency but still has the same per-message overhead; each message is its own HTTP request. To have both low latency and low overhead, we need XHR streaming!

As a result, while XHR is a popular mechanism for "real-time" delivery, it may not be the best-performing transport for the job. Modern browsers support both simpler and more efficient options, such as Server-Sent Events and WebSocket. Hence, unless you have a specific reason why XHR polling is required, use them.
# Server-Sent Events (SSE)

Server-Sent Events enables efficient server-to-client streaming of text-based event data—e.g., real-time notifications or updates generated on the server. To meet this goal, SSE introduces two components: a new EventSource interface in the browser, which allows the client to receive push notifications from the server as DOM events, and the "event stream" data format, which is used to deliver the individual updates.

The combination of the EventSource API in the browser and the well-defined event stream data format is what makes SSE both an efficient and an indispensable tool for handling real-time data in the browser:

- Low latency delivery via a single, long-lived connection
- Efficient browser message parsing with no unbounded buffers
- Automatic tracking of last seen message and auto reconnect
- Client message notifications as DOM events
Under the hood, SSE provides an efficient, cross-browser implementation of XHR streaming; the actual delivery of the messages is done over a single, long-lived HTTP connection. However, unlike dealing XHR streaming on our own, the browser handles all the connection management and message parsing, allowing our applications to focus on the business logic! In short, SSE makes working with real-time data simple and efficient. Let’s take a look under the hood.

in addition to automatic event parsing, SSE provides built-in support for reestablishing dropped connections, as well as recovery of messages the client may have missed while disconnected. By default, if the connection is dropped, then the browser will automatically reestablish the connection. The SSE specification recommends a 2–3 second delay, which is a common default for most browsers, but the server can also set a custom interval at any point by sending a `retry` command to the client.

Similarly, the server can also associate an arbitrary ID string with each message. The browser automatically remembers the last seen ID and will automatically append a "Last-Event-ID" HTTP header with the remembered value when issuing a reconnect request.

**SSE Streaming over TLS**

SSE provides a simple and convenient real-time transport on top of a regular HTTP connection, which makes it simple to deploy on the server and to polyfill on the client. However, existing network middleware, such as proxy servers and firewalls, which are not SSE aware, may still cause problems: intermediaries may choose to buffer the event-stream data, which will translate to increased latency or an outright broken SSE connection.

As a result, if you experience this or similar problems, you may want to consider delivering an SSE event-stream over a TLS connection; see [Proxies, Intermediaries, TLS, and New Protocols on the Web](https://hpbn.co/transport-layer-security-tls/#proxies-intermediaries-tls-and-new-protocols-on-the-web).


# Websocket
WebSocket enables bidirectional, message-oriented streaming of text and binary data between client and server. It is the closest API to a raw network socket in the browser. Except a WebSocket connection is also much more than a network socket, as the browser abstracts all the complexity behind a simple API and provides a number of additional services:

- Connection negotiation and same-origin policy enforcement
- Interoperability with existing HTTP infrastructure
- Message-oriented communication and efficient message framing
- Subprotocol negotiation and extensibility

>WebSocket is a set of multiple standards: the WebSocket API is defined by the W3C, and the WebSocket protocol (RFC 6455) and its extensions are defined by the HyBi Working Group (IETF).

In this [article](https://medium.com/data-science/deep-dive-into-websockets-and-their-role-in-client-server-communication-aac387e10cb6), we’ll explore how WebSockets fit into the bigger picture of client‑server communication. We’ll discuss what they do well, where they fall short, and — yes — how to design a real‑time messaging app.

## Client-server communication

At its core, client-server communication is the exchange of data between two entities: a client and a server.

The client requests for data, and the server processes these requests and returns a response. These roles are not exclusive — services can act as both a client and a server simultaneously, depending on the context.

Before diving into the details of WebSockets, let’s take a step back and explore the bigger picture of client-server communication methods.

### 1. Short polling

Short polling is the simplest, most familiar approach.

The client repeatedly sends HTTP requests to the server at regular intervals (e.g., every few seconds) to check for new data. Each request is independent and one-directional (client → server).

This method is easy to set up but can waste resources if the server rarely has fresh data. Use it for less time‑sensitive applications where occasional polling is sufficient.

### 2. Long polling

Long polling is an improvement over short polling, designed to reduce the number of unnecessary requests. Instead of the server immediately responding to a client request, the server **keeps the connection open** until new data is available. Once the server has data, it sends the response, and the client immediately establishes a new connection.

Long polling is also **stateless** and **one-directional** (client → server).

A typical example is a ride‑hailing app, where the client waits for a match or booking update.

### 3. Webhooks

Webhooks flip the script by making the server the initiator. The server sends **HTTP POST** requests to a client-defined endpoint whenever specific events occur.

Each request is **independent** and does not rely on a persistent connection. Webhooks are also **one-directional** (server to client).

Webhooks are widely used for asynchronous notifications, especially when integrating with third-party services. For example, payment systems use webhooks to notify clients when the status of a transaction changes.

### 4. Server-Sent Events (SSE)

SSEs are a **native HTTP-based event streaming protocol** that allows servers to push real-time updates to clients over a single, **persistent connection**.

SSE works using the `EventSource` API, making it simple to implement in modern web applications. It is **one-directional** (server to client) and ideal for situations where the client only needs to receive updates.

SSE is well-suited for applications like trading platforms or live sports updates, where the server pushes data like stock prices or scores in real time. The client does not need to send data back to the server in these scenarios.

### But what about two-way communication?

All the methods above focus on one‑directional flow. For true two‑way, real‑time exchanges, we need a different approach. That’s where WebSockets shine.

Let’s dive in.

## How do WebSockets work?

WebSockets enable **real-time, bidirectional communication**, making them perfect for applications like chat apps, live notifications, and online gaming. Unlike the traditional HTTP request-response model, WebSockets create a **persistent** connection, where both client and server can send messages independently without waiting for a request.

> The connection begins as a regular HTTP request and is upgraded to a WebSocket connection through a handshake.

[image-source](https://www.youtube.com/watch?v=G0_e02DdH7I)

![[Pasted image 20260616074219.png]]
Once established, it uses a single TCP connection, operating on the same ports as HTTP (80 and 443). Messages sent over WebSockets are small and lightweight, making them efficient for low-latency, high-interactivity use cases.

WebSocket connections follow a specific URI format: `ws://` for regular connections and `wss://` for secure, encrypted connections.

**What’s a handshake?**

A handshake is the process of **initialising a connection** between two systems. For WebSockets, it begins with an HTTP GET request from the client, asking for a protocol upgrade. This ensures compatibility with HTTP infrastructure before transitioning to a persistent WebSocket connection.

1. **Client sends a request, with headers that look like:**
```
GET /chat HTTP/1.1  
Host: server.example.com  
Upgrade: websocket  
Connection: Upgrade  
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==  
Origin: http://example.com  
Sec-WebSocket-Protocol: chat, superchat  
Sec-WebSocket-Version: 13
```


- `Upgrade` — signals the request to switch the protocol
- `Sec-WebSocket-Key` — Randomly generated, base64 encoded string used for handshake verification
- `Sec-WebSocket-Protocol` (optional) — Lists subprotocols the client supports, allowing the server to pick one.

**2. Server responds to resquest**

If the server supports WebSockets and agrees to the upgrade, it responds with a **101 Switching Protocols** status. Example headers:
```
HTTP/1.1 101 Switching Protocols  
Upgrade: websocket  
Connection: Upgrade  
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=  
Sec-WebSocket-Protocol: chat
```


- `Sec-WebSocket-Accept` — Base64 encoded hash of the client’s `Sec-WebSocket-Key` and a GUID. This ensures the handshake is secure and valid.

**3. Handshake validation**

With the `101 Switching Protocols` response, the WebSocket connection is successfully established and both client and server can start exchanging messages in real time.

This connection will remain open till it is explicitly closed by either party.

If any code other than `101` is returned, the client has to end the connection and the WebSocket handshake will fail.

**Trade off**
**Not optimised for streaming audio and video data**

WebSocket messages are designed for sending **small, structured messages.** To stream large media data, a technology like WebRTC is better suited for these scenarios.

**WebSockets are stateful, hence horizontally scaling is not trivial**

WebSockets are **stateful**, meaning the server must maintain an active connection for every client. This makes horizontal scaling more complex compared to stateless HTTP, where any server can handle a client request without maintaining persistent state.

### Request and Response Streaming

WebSocket is the only transport that allows bidirectional communication over the same TCP connection ([Figure 17-2](https://hpbn.co/websocket/#transport-flow)): the client and server can exchange messages at will. As a result, WebSocket provides low latency delivery of text and binary application data in both directions.
![[Pasted image 20260616074427.png]]

- XHR is optimized for "transactional" request-response communication: the client sends the full, well-formed HTTP request to the server, and the server responds with a full response. There is no support for request streaming, and until the Streams API is available, no reliable cross-browser response streaming API.
    
- SSE enables efficient, low-latency server-to-client streaming of text-based data: the client initiates the SSE connection, and the server uses the event source protocol to stream updates to the client. The client can’t send any data to the server after the initial handshake.
# WEBRTC

UDP offers no promises on reliability or order of the data, and delivers each packet to the application the moment it arrives. In effect, it is a thin wrapper around the best-effort delivery model offered by the IP layer of our network stacks.

WebRTC uses UDP at the transport layer: latency and timeliness are critical. With that, we can just fire off our audio, video, and application UDP packets, and we are good to go, right? Well, not quite. We also need mechanisms to traverse the many layers of NATs and firewalls, negotiate the parameters for each stream, provide encryption of user data, implement congestion and flow control, and more!

UDP is the foundation for real-time communication in the browser, but to meet all the requirements of WebRTC, the browser also needs a large supporting cast ([Figure 18-3](https://hpbn.co/webrtc/#webrtc-stack)) of protocols and services above it.
![[Pasted image 20260617155859.png]]

- ICE: Interactive Connectivity Establishment (RFC 5245)
    - STUN: Session Traversal Utilities for NAT (RFC 5389)
    - TURN: Traversal Using Relays around NAT (RFC 5766)
- SDP: Session Description Protocol (RFC 4566)
- DTLS: Datagram Transport Layer Security (RFC 6347)
- SCTP: Stream Control Transport Protocol (RFC 4960)
- SRTP: Secure Real-Time Transport Protocol (RFC 3711)

ICE, STUN, and TURN are necessary to establish and maintain a peer-to-peer connection over UDP. DTLS is used to secure all data transfers between peers; encryption is a mandatory feature of WebRTC. Finally, SCTP and SRTP are the application protocols used to multiplex the different streams, provide congestion and flow control, and provide partially reliable delivery and other additional services on top of UDP.

![Figure 18-13. Audio and video delivery via SRTP over UDP](https://hpbn.co/assets/diagrams/b7877f7c09eee79e8dfd7847e0a5930f.svg)
