## Exploit module structure in Metasploit

Each Metasploit exploit module includes:

- **Name and description:** CVE reference and summary
- **Targets:** Operating systems or software versions affected
- **Payload compatibility:** List of usable payloads
- **Options:** RHOSTS, RPORT, USERNAME, etc.
- **Check function:** Some modules include a check function to verify vulnerability before exploiting

## **Understanding payloads in Metasploit**

After successfully exploiting a vulnerability, you need a way to interact with the compromised system. This is where payloads come into play. The following section breaks down how Metasploit organizes and implements payloads to maximize your effectiveness during security assessments.

**Payloads serve as the executable code that runs on target systems after successful exploitation.** The Metasploit framework employs a modular payload architecture that maximizes flexibility and effectiveness across different attack scenarios.

## **Payload architecture**

Metasploit organizes payloads into three distinct categories:

- **Singles** function as self-contained payloads that perform specific actions independently. These lightweight options work well for creating backdoors, adding system users, or executing simple commands when space constraints limit payload size.
    
- **Stagers** establish communication channels between the attacker and the target system. These lightweight payloads download and execute larger, more functional payloads while using standard ports like HTTP or HTTPS to evade detection.
    
- **Stages** provide the full-featured functionality delivered by stagers. These powerful components offer comprehensive system access, file operations, and advanced capabilities like keylogging or webcam access.```
## Types of exploits

|Exploit type|Command|Explanation|
|---|---|---|
|**Remote exploit**|1. 1<br><br>1. `exploit/windows/smb/ms17_010_eternalblue`<br><br>Copied!Wrap Toggled!|Targets services over the network|
|**Local exploit**|1. 1<br><br>1. `exploit/linux/local/dirty_cow`<br><br>Copied!Wrap Toggled!|Used post-access to escalate privileges|
|**Client-side exploit**|1. 1<br><br>1. `exploit/windows/browser/ms12_063_ie_execcommand_uaf`<br><br>Copied!Wrap Toggled!|Used in phishing attacks and requires user interaction|
|**Web exploit**|1. 1<br><br>1. `exploit/multi/http/apache_path_traversal`<br><br>Copied!Wrap Toggled!|Targets web servers and apps like Apache|

----------------------------
