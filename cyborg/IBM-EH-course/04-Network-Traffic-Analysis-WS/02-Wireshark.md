`Wireshark` is a network traffic analyzer, or "sniffer", for Linux, macOS, *BSD and other Unix and Unix-like operating systems and for Windows. It uses Qt, a graphical user interface library, and libpcap and npcap as packet capture and filtering libraries.

The Wireshark distribution also comes with TShark, which is a line-oriented sniffer (similar to Sun's snoop or tcpdump) that uses the same dissection, capture-file reading and writing, and packet filtering code as Wireshark, and with editcap, which is a program to read capture files and write the packets from that capture file, possibly in a different capture file format, and with some packets possibly removed from the capture.

**Wireshark interface**

- `eth0` typically represents your wired (Ethernet) connection.
- `any` is a virtual interface that tells Wireshark to capture packets from all active network interfaces on your system simultaneously. It's a convenient way to capture traffic if you're unsure which specific interface carries the data you need or want a global view of all network activity.
- `Loopback:lo` is for traffic within your own Kali VM, not external network traffic.

## Comparison of Wireshark's features and their cybersecurity and ethical hacking applications

Below is a comparison of Wireshark's features and their cybersecurity and ethical hacking applications.

|Wireshark features|Cybersecurity|Ethical hacking|
|---|---|---|
|Passive packet capture|Used to monitor network traffic to find potential security threats and ensure compliance with security policies.|Used to see and analyze traffic patterns to discover vulnerabilities without interfering with the network.|
|Lua scripting for active probing|Allows sending probes for service discovery and performing specific security tests by analyzing network responses.|Enables crafting and sending packets to test for network vulnerabilities and simulate various attack scenarios.|
|Traffic analysis|Analyzes network traffic to detect anomalies, find trends, and understand network usage for security purposes.|Investigates captured traffic to uncover weaknesses and plan targeted penetration tests.|
|Basic vulnerability testing|Tests network resilience by sending specific malformed packets and analyzing the response to ensure robustness against attacks.|Creates and sends malformed packets to find and exploit network vulnerabilities.|
|Service discovery|Sends probes to discover and verify legitimate services on the network.|Uses probing techniques to identify and potentially exploit network services.|

----------

# Packet headers

In digital communication, data is transmitted across networks in the form of packets, small units containing both the actual data and essential control information in their headers. This guide explores the structure and function of packet headers in IPv4, IPv6, and UDP, highlighting key fields critical for routing, delivery, and error-checking. Identify and describe the primary components of IPv4 and IPv6 packet headers. It also compares key differences between IPv4 and IPv6 header structures and explains the purpose and function of header fields such as TTL, Protocol, and Fragment Offset. Finally, you will also be able to interpret how UDP header fields facilitate communication between applications.

## Introduction

Data travels across a network and is broken down into smaller units called packets. Each packet contains the actual data (the payload) and a header attached to the beginning. This header includes crucial information for network devices that route the packet correctly and ensure it is processed correctly at the receiving end.  
While different network protocols have slightly different header structures, some core fields are commonly found. We’ll focus on the most fundamental ones, often associated with the Internet Protocol (IP) and Transmission Control Protocol (TCP) or User Datagram Protocol (UDP), which form the backbone of much Internet communication.

### IPv4 Packet Header

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/9B-34Or8jJhXIIqmY5ExFg/Picture11.jpg)  

- **Version (4 bits)**: Because this format is for IPv4 packets, this will always be the number 4.
    
- **Header length (IHL) (4 bits):** Shows how long the IP header is (in 32-bit words). Think of it like an index for the packet's "addressing" information.
    
- **Type of service (ToS) (8 bits):** Helps routers know how vital the packet is (Quality of Service).
    
- **Total length (16 bits):** The total size of the entire IP packet (header plus all the data it’s carrying) in bytes.
    
- **Identification (16 bits):** If a packet is too big and must be split into fragments, this number helps put them back together in the correct order—all pieces of the same original packet share this ID.
    
- **IP flags (3 bits):** These are like little "yes/no" switches for fragmentation:
    
    - One bit is reserved (and usually set to 0).
    - "Don't Fragment" (DF) bit: If this is on, the packet shouldn't be split.
    - "More Fragments" (MF) bit: If this is on, it means this piece is part of a larger packet, and more pieces are coming (unless it's the very last piece).
- **Fragment offset (13 bits):** A split packet tells the receiver where this particular piece fits into the original, larger packet (measured in 8-byte units).
    
- **Time to live (TTL) (8 bits):** A counter that prevents packets from getting lost and circling the internet forever. Each time a packet passes through a router, this number usually goes down by one. If it hits zero, the packet is dropped.
    
- **Protocol (8 bits):** Tells the receiving computer what kind of data is inside the IP packet (that is, TCP has a value of 6, UDP has a value of 17).
    
- **Header checksum (16 bits):** A special number calculated from the header. The receiver recalculates this to check if the header got damaged or changed during its journey.
    
- **Source address (32 bits):** The 32-bit IP address of the computer that sent the packet.
    
- **Destination address (32 bits):** The 32-bit IP address of the computer the packet is going to.
    
- **IP options (Variable length):** An optional section for special instructions. Its length varies depending on the options used, and its presence increases the Header Length (IHL). It's not used very often.
    

### IPv6 packet header

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/b6LfIII-OJnhWlzmis1GnA/Picture12.jpg)

- **Version (4 bits):** This is the first field. It is always set to 6 (binary 0110) to indicate it's an IPv6 packet.
    
- **Traffic class (8 bits):** Such as the "Type of Service" field in IPv4, this field helps identify the packet's priority, which can be used for Quality of Service (QoS).
    
- **Flow label (20 bits):** This field can be used to mark sequences of packets from a specific source to a particular destination that requires the same special handling by IPv6 routers (for example, for a specific video call).
    
- **Payload length (16 bits):** This tells you the size of the data (the "payload") that the IPv6 packet is carrying, in bytes. It only includes the data, not the main IPv6 header (a fixed 40 bytes).
    
- **Next header (8 bits):** This field identifies the header type immediately following the current IPv6 header. It could be a transport layer protocol header (such as TCP (value 6) or UDP (value 17)) or an IPv6 "Extension Header" for special handling.
    
- **Hop limit (8 bits):** Just like the "Time to Live" (TTL) field in IPv4. It's a counter that is decreased by one for every router. If it reaches zero, the packet is discarded.
    
- **Source address (128 bits):** The 128-bit IPv6 address of the device that sent the packet (that is,`2001:0db8:85a3:0000:0000:8a2e:0370:7334`).
    
- **Destination address (128 bits):** The 128-bit IPv6 address of the device the packet is intended to reach.
    
    ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/svWawpb6AE1rPpxAt27LlA/Picture13.jpg)  
    
- **Source port (16 bits):**
    
    - This field tells the receiving device which application or process on the sending computer sent the UDP message.
    - This field is technically optional (it can be set to zero if not used by the sender), but it’s usually filled in for replies.
- **Destination port (16 bits):**
    
    - This tells the receiving computer which application or process on the destination computer the UDP message is intended for (for example, port 53 for DNS).
- **Length (16 bits):**
    
    - This field specifies the total length of the UDP datagram in bytes, which includes the 8-byte UDP header plus the actual data being carried.
    - The minimum value is 8 bytes (for a UDP packet with no data).
- **Checksum (16 bits):**
    
    - The checksum is used to check for errors in the UDP header and the UDP data.
    - Using the checksum is optional in IPv4 UDP (if unused, set to zero) but is generally mandatory in IPv6 UDP.

### Summary

In this reading, you learned that:

- Every packet that travels across a network includes a header, which contains control information necessary for routing and delivering the data correctly.
- IPv4 headers include fields such as version, header length, total length, time to live (TTL), and protocol type, each serving a specific function in packet delivery and management.
- Fragmentation fields in IPv4, such as identification, flags, and fragment offset, allow large packets to be split and reassembled during transmission.
- IPv6 simplifies header processing by using a fixed-length main header and replaces certain IPv4 fields with updated counterparts such as traffic class and flow label.
- The UDP header includes source and destination ports, which help identify the sending and receiving applications, as well as a checksum for error detection.
- Unlike TCP, UDP is connectionless and does not guarantee delivery, making it suitable for applications that prioritize speed over reliability, such as DNS or video streaming.
---------

# Basics of packet filtering

### Protocol type
- TCP (Connection-oriented traffic)
- UDP (Connectionless traffic)
- ICMP (Network diagnostics like ping)
- Routing or industrial control protocols


----------

# Creating and Troubleshooting Filter Configurations

Analyzing raw network traffic can be overwhelming without effective filtering techniques. Filters are essential for isolating the specific traffic you need to analyze. This reading will guide you through creating and troubleshooting filter configurations in these tools. It introduces the two primary types of filters—capture and display—and demonstrates how to create, apply, and troubleshoot them. You'll also learn how to isolate relevant traffic, avoid common filter mistakes, and use filtering tools to streamline network analysis.

### Understanding Filter Types in Network Analyzers

Network analysis tools generally use two main types of filters:

|Filter type|Purpose|When to use|Syntax|Where to apply|
|---|---|---|---|---|
|Capture filters|To select which packets are captured and written to disk before the capture starts. Packets that don't match the filter are typically discarded and are not part of the capture file.|On high-traffic networks, to reduce the capture file size, for long-duration captures, or when you know precisely what you're looking for beforehand.|Often uses Berkeley Packet Filter (BPF) syntax or a similar powerful, low-level filtering language. Syntax can vary slightly between tools.|Typically, it is in the capture configuration settings or setup screen before initiating a packet capture.|
|Display filters|To hide or show packets from an already captured file or live capture stream. They don't usually change the underlying saved capture file, only what's displayed in the tool's interface.|To explore captured data, iteratively refine your analysis, and when you need more complex or protocol-specific filtering based on deeply dissected fields.|Usually, a proprietary, rich, and extensive filter language specific to the analysis tool is designed for flexibility.|A dedicated filter input area or expression bar within the main interface of the analysis tool is applied to an active capture or a loaded capture file.|

Capture filters prevent non-matching data from being saved (sometimes, even processed by the capture engine). Display filters hide non-matching data from your current view in an existing capture. If you don't capture it with a capture filter, you generally cannot see it later with a display filter.

### Creating capture filters

1. Before starting a capture, look for a "capture filter" input field or section within the tool's capture options or interface configuration dialog.
2. Common syntax concepts and examples (often BPF-like):
    - Filtering by host IP: host 192.168.1.10 (traffic to or from this IP).
    - Filtering by network: net 192.168.1.0/24 (traffic to or from this network).
    - Filtering by port: port 80 (traffic using source or destination port 80).
    - Specifying direction: src host 192.168.1.10 (traffic _from_ this IP) or dst port 443 (traffic _to_ this port).
    - Filtering by protocol: tcp, udp, icmp.
3. Logical operators (common in many capture filter languages):
    - and (or &&): Both conditions must be true (i.e., host 192.168.1.10 and port 80).
    - or (or ||): Either condition can be true (for example, port 80 or port 443).
    - not (or !): Negates the condition (for example, not port 22).
    - Use parentheses () to group expressions for clarity and correct precedence: host 192.168.1.10 and (port 80 or port 443).
4. Most tools provide a way to save frequently used capture filters for easy recall.

### Creating display filters

1. Look for a prominent filter input bar or area in the main user interface, often labeled "Display filter," "Filter expression," or similar. Type your filter and apply it (for example, by pressing Enter).
2. Common syntax concepts and examples (syntax is tool-specific):
    - Tools often use a dot notation to access protocol fields (i.e., protocol.field_name).
    - Filtering by IP address: ip.address == 192.168.1.10 (conceptual; actual syntax varies).
    - Filtering by source/destination IP: ip.source == 192.168.1.10, ip.destination == 192.168.1.10.
    - Filtering by TCP/UDP port: tcp.port == 80, udp.port == 53.
    - Filtering by protocol name: http, dns (if the tool dissects these protocols).
    - Filtering on specific protocol fields: http.request.method == "GET" (to find HTTP GET requests).
    - Checking TCP flags: tcp.flags.synchronize == 1 and tcp.flags.acknowledgment == 0 (conceptual for a TCP SYN packet).
    - Searching for text within packets: frame contains "specific error message."
3. Comparison operators (syntax and keyword may vary):
    - == or eq (equal)
    - != or ne (not equal)
    - > or gt (greater than)
    - < or lt (less than)
    - >= or ge (greater than or equal to)
    - <= or le (less than or equal to)1
    - contains: Checks if a protocol or text field includes a specific substring.
    - matches: Often used for regular expression matching against a field.
4. Logical operators (syntax may vary, i.e., and/&&, or/||, not/!):
    - AND: Both conditions true.
    - OR: Either condition true.
    - NOT: Negates a condition.
    - Use parentheses () to group complex expressions.
5. Many tools allow you to select a field in the dissected packet details view, right-click (or use a context menu) to quickly apply that field's value as a filter, or prepare parts of a filter expression.
6. Look for buttons or menu options like "Expression…", "Filter Builder," or "Filter Assistant." These tools help you discover filterable protocol fields and construct syntactically correct expressions.
7. Most analysis tools offer features to save, name, and manage frequently used display filter expressions for quick access.

### Troubleshooting filter configurations

- **Syntax errors:**
    - Most tools will provide some indication of an invalid filter syntax, such as an error message, a change in color in the filter input area, or simply the filter not working.
    - Common errors include:
        - Using display filter syntax for capture filters, or vice-versa.
        - Using incorrect logical or comparison operators for the specific filter type.
        - Formatting issues, like missing quotes around string values where required by the tool.
- **Filter logic errors (Valid syntax, but not the expected results):**
    - You identified fewer packets than expected:
        - Try removing conditions one by one or using OR to broaden the scope.
        - Double-check IP addresses, port numbers, string values, and field names.
        - Verify that the traffic uses the protocol, port, or values you expect. Verify against raw packet details.
        - See if you selected the source where you meant destination, or vice-versa?
        - Check capitalization. Some filter languages or specific field comparisons might be case-sensitive.
    - You identified more packets than expected:
        - The filter may be too broad. Add more conditions using AND to make it more specific.
        - Verify that you used OR when you needed a wider match and AND for a narrower one.
- **No packets were captured:**
    - Are you capturing on the correct network interface (Ethernet, Wi-Fi, virtual, etc.)?
    - Is the tool capturing packets (check packet counters or status indicators)? Promiscuous mode settings might be relevant.
    - Check basic connectivity (cables, Wi-Fi association).
    - Does the analysis tool (or the user account running it) have the necessary operating system permissions to capture network traffic? It is often required.
    - Could local or network security software block the traffic or the capture process?
    - Is the traffic you are trying to filter for present on the network segment you are monitoring during the capture period?

### Tips for effective filtering

It's important to keep in mind some tips or best practices for effective filtering.

- Start broad, then narrow, especially with display filters.
- Know common protocols and ports
- Consult tool documentation
- Save useful filters

## Summary

In this reading, you learned that:

- Capture filters reduce data at the source. They are applied before packet capture begins and determine which packets are saved, helping manage file size and focus.
- Display filters refine what you see. When used after capture, they help you view specific traffic without altering the capture file.
- Syntax matters. Capture and display filters use different languages. Mixing their syntax is a common error that leads to non-functional filters.
- Start broad, then narrow. When troubleshooting or exploring unknown traffic, begin with general filters and add conditions to isolate specific patterns.
- Use logical and comparison operators carefully. Misusing AND, OR, NOT, or incorrect field references often leads to logic errors in filters.
- Troubleshooting requires multiple checks. Always verify the correct network interface, tool permissions, protocol expectations, and syntax when filters don't return expected results.

-----------
# Guide to Advanced Filtering Techniques in Wireshark

**Understanding display filter syntax**

Wireshark display filters use a flexible syntax that allows you to look deeper into packet details. Display filters use Wireshark's extensive protocol dissection capabilities, meaning that you can filter based on specific fields within various protocol headers. The general structure often involves the protocol name followed by a dot (.) and the particular field name (that is, http.request.method).

|Technique|Use case|Example|
|---|---|---|
|Filtering by specific protocol fields|This technique allows you to examine details within a particular protocol's header. It helps identify specific actions or characteristics of that protocol's communication.|The filter **http.request.method == "POST"** will show only HTTP packets, whereas the request method is "POST," which is often used to submit data.|
|Filtering by numeric field comparison|Analyze traffic based on numerical values within packet headers, such as size or sequence numbers, which helps identify large transfers or specific connection states.|The filter **tcp.seq == 100** displays TCP packets with a sequence number equal to 100.|
|Filtering by string field comparisons|Search for specific text within protocol fields like URLs or hostnames. It helps track particular web activity.|The filter **http.host contains "example.com"** and shows HTTP packets, whereas the "Host" header contains "example.com."|
|Filtering by Boolean flags|Identify packets based on the state of flags within protocol headers (commonly TCP), which helps understand connection establishment and termination.|The filter **tcp.flags.syn == 1 and tcp.flags.ack == 0** shows TCP SYN packets (connection initiation).|
|Using the "contains" operator|Check if a field includes a specific substring or byte pattern.|The filter **frame.contains "error"** will show all packets containing the ASCII string "error" in their raw data (Note: You'll want to use this example with caution on large captures).|
|Using the "matches" operator (regular expressions)|Perform advanced pattern matching on string fields.|The filter **http.user_agent matches** **"Mozilla**\/**5**\**.0.*****Firefox**\/**.*****"** finds HTTP packets with a User-Agent string indicating Firefox.|
|Combining filters with logical operators (and/or/not)|Create complex filters by combining multiple conditions.|The filter **(ip.src == 192.168.1.10 and tcp.port == 80)** or dns shows HTTP traffic from a specific IP or any DNS traffic.|
|Filtering by protocol or frame length|Analyze traffic based on packet size.|The filter **ip.len > 1500** displays IP packets larger than 1500 bytes.|
|Filtering by expert info|Analyze traffic based on warnings or errors.|The filter **expert.severity == "Error"** shows packets flagged as errors by Wireshark.|

---------
# Cybersecurity and Ethical Hacking Applications of Packet Capture
In cybersecurity and ethical hacking, packet capture (PCAP) is a vital technique for monitoring, analyzing, and securing network communications. This reading explores practical applications of packet capture in identifying threats, verifying controls, and conducting ethical hacking. You will gain insights into traffic filtering strategies for both defensive and offensive cybersecurity operations.

### Cybersecurity

|Application|Description|
|---|---|
|Initial Threat Detection (Filtering for Anomalies)|Capturing network traffic and immediately filtering for unusual protocols on standard ports (e.g., non-HTTP traffic on port 80) or traffic to/from unexpected IP addresses can help identify potential initial stages of an attack or unauthorized communication.|
|Targeted Evidence Collection (Filtering Specific Traffic)|During an incident response, capturing traffic and filtering for communication involving specific compromised systems (by IP address or MAC address) or known malicious actors (by IP address) allows for focused data collection relevant to the incident.|
|Verification of Security Controls (Filtering Policy Enforcement)|Capturing traffic and filtering for specific protocols or ports that firewalls or access control lists should block can be used to verify if these security controls are functioning as intended. For example, filtering for traffic on a blocked port to a specific server.|

### Ethical Hacking

|Application|Description|
|---|---|
|Reconnaissance (Passive Information Gathering through Filtering)|Capturing traffic on a target network (where authorized) and filtering for specific protocols like DNS or DHCP can reveal information about network infrastructure, server names, and IP address ranges without actively interacting with systems.|
|Identifying Attack Vectors (Filtering for Vulnerable Services)|During authorized penetration testing, capturing traffic and filtering for specific protocols or ports known to be associated with vulnerable services (e.g., older versions of SMB or unencrypted protocols) can help identify potential attack entry points.|

## Summary

In this reading, you have learned that:

- Packet capture is essential for threat detection – By monitoring network traffic and filtering anomalies such as unexpected protocols or IP addresses, security teams can identify early signs of cyberattacks.
- PCAP enables focused incident response – Filtering network data related to specific compromised systems or known threats helps gather targeted evidence during security investigations.
- Security controls can be verified through traffic analysis. Packet capture is a practical method for testing whether firewalls and access controls are correctly blocking prohibited traffic.
- Ethical hackers use passive reconnaissance – Authorized testers can filter captured DNS and DHCP traffic to map network infrastructure without actively probing systems.
- Vulnerabilities are revealed through protocol analysis – Filtering for outdated or unencrypted services helps ethical hackers identify potential points of entry during penetration testing.









































