# Integrating Threat Intelligence into After-Action Reports
## Learning objectives

1. Analyze the role of tactical and operational threat intelligence in enhancing after-action reports.
    
2. Evaluate threat intelligence integration tools and apply best practices to produce strategic after-action reports.
    

## Overview

In the evolving landscape of cybersecurity, post-incident analysis that lacks threat intelligence (TI) is no longer sufficient. Modern attacks are highly coordinated, often linked to broader campaigns, and executed by sophisticated adversaries using reusable tactics and tools. While technical logs and vulnerability scans tell what happened, **threat intelligence explains why and what to anticipate next.**

Effective integration of TI enables incident response teams to:

- Transition from reactive to **proactive defense**
- Identify **links to known threat actors**
- Understand **attack context, evolution, and likelihood of recurrence**
- Communicate risk to non-technical stakeholders with **narrative depth**

Incorporating TI into after-action reports (AARs) turns a basic forensic summary into a strategic asset for security operations, policy planning, and executive decision-making.

### Defining threat intelligence in context

TI is not just about indicators; it is structured information distilled from threat data to **aid decision-making**. Its value lies in providing **context**, **intent**, and **prediction**. TI is categorized across four tiers:

|Type|Focus|
|---|---|
|**Strategic**|Macro-level analysis of threat landscapes, geopolitical risks, and attacker goals.|
|**Operational**|Information about current campaigns, active infrastructure, and targeting patterns.|
|**Tactical**|Low-level indicators of compromise (IoCs) like hashes, domains, internet protocol addresses (IPs), and registry changes.|
|**Technical**|Detailed malware analysis, exploit mechanics, and payload construction.|

In AARs, **tactical and operational intelligence** are most directly usable. They support forensic analysis and help validate attacker behavior through:

- **Comparative IoC matching**
- **Attribution analysis**
- **Risk predictions**

### Enhancing the report with threat intelligence

TI enhances AARs in multiple dimensions:

- **Attribution**: Associating activity with a known adversary (for example, Advanced Persistent Threat 29 (APT29), Cl0p, or Lazarus Group).
- **Intent identification**: Determining whether the incident aimed at espionage, disruption, financial gain, or activism.
- **TTP correlation**: Mapping tactics, techniques, and procedures (tactic, technique, and procedure (TTPs) to Mitre Adversarial Tactics Techniques and Common Knowledge (MITRE ATT&CK) profiles for pattern analysis.
- **Risk forecasting**: Using campaign intelligence to anticipate similar attacks in other systems or regions.
- **Evidence validation**: Supporting technical findings with external threat data strengthens report defensibility.

Without TI, reports remain **tactically accurate but strategically blind**, failing to inform broader enterprise resilience efforts.

### Where to integrate TI in the report

To maximize its value, integrate TI into key AAR sections as follows:

|Report section|How to apply TI|
|---|---|
|**IoCs**|Enrich OpenVAS findings with matches from feeds like Malware Information Sharing Platform (MISP), AbuseIPDB, or VirusTotal.|
|**Attack vector**|Use MITRE ATT&CK to define specific methods (for example, T1190 for external application exploit).|
|**Attribution section**|Identify threat groups if their behavior matches, as supported by reports from IBM X-Force, CISA, etc.|
|**Recommendations**|Propose detection rules (for example, Yet Another Recursive Acronym (YARA) and Suricata signatures) or monitor adjustments based on observed TTPs.|
|**Lessons learned**|Compare against previous attacks-has the same vector been used before? What was missed?|

Visual tools like **MITRE ATT&CK Navigator** help plot TTPs for stakeholder presentations and pattern recognition.

### Case study – MOVEit transfer zero-day exploitation (2023)

In June 2023, attackers exploited a **zero-day vulnerability in MOVEit Transfer** (CVE-2023-34362) to perform **SQL injection and file upload attacks** across multiple sectors.

Organizations with strong TI capabilities were able to:

- Detect the threat using **shared IoCs**—uploaded .aspx files, specific attacker IP ranges, and known exploitation paths.
- Attribute the activity to the **Cl0p ransomware gang**, confirmed through pattern correlation and messaging artifacts.
- Preemptively patch and segment systems by acting on **TTP advisories** published by the Cybersecurity and Infrastructure Security Agency (**CISA)** and **Rapid7.**
- Generate after-action reports, including **timeline overlays**, **campaign mapping**, and **impact projections** based on affected industries.

The effectiveness of their response was enhanced by **using TI for detection, rapid containment, and executive awareness**.

### Best practices for using threat intelligence in AARs

To ensure threat intelligence adds value rather than noise:

- **Use reputable open and commercial sources**: MISP, IBM X-Force, Anomali, Recorded Future, CISA feeds.
- **Cross-reference TI with logs and OpenVAS output** to validate indicators or verify CVEs as exploited.
- **Visualize where possible**: Mapping TTPs on a timeline or using MITRE matrices improves readability.
- **Correlate with historical incidents**: Look for repeated use of similar IoCs or vectors to identify organizational blind spots.
- **Avoid speculative attribution**: Only assign threat groups when there is strong supporting evidence across multiple sources.

### Tools that support threat intelligence integration

|Tool|Use case|
|---|---|
|**OpenVAS (with updated feeds)**|Identifies CVEs and misconfigurations that TI can correlate against.|
|**Malware Information Sharing Platform (MISP)**|Open-source platform for sharing and correlating indicators.|
|**MITRE ATT&CK navigator**|Visualize attacker techniques and behaviors.|
|**VirusTotal / Hybrid analysis**|Analyze and verify file hashes or URLs.|
|**Security Information and Event Management (SIEM) platforms (for example, Splunk and QRadar)**|Correlate TI with internal alerts for detection validation.|
|**ThreatConnect, Anomali**|Commercial threat intelligence platforms (TIPs) offer structured campaign data and group behavior profiles.|

----------
![[Pasted image 20260125215448.png]]
![[Pasted image 20260125215524.png]]
## Overview

An incident report is more than a procedural log; it is a strategic communication and compliance tool that documents every critical detail of a cybersecurity event. When executed properly, the report enables organizations to capture the full scope of the incident, establish accountability, and initiate change. It serves as both **an analytical record** and a **compliance asset**, capable of informing internal security improvements and satisfying external regulatory requirements.

This reading explores the best practices that define a clear, comprehensive, and evidence-driven post-incident report (PIR), incorporating lessons learned from real-world examples and leveraging tools such as OpenVAS.

## Why high-quality reports matter

A well-written report does the following:

- **Supports investigations**: Serves as factual evidence for internal reviews, third-party audits, or legal proceedings.
- **Encodes institutional knowledge**: Becomes a referenceable artifact for future incident response, helping teams avoid repeating mistakes.
- **Improves cross-functional understanding**: Bridges technical findings with executive-level concerns to justify budgets, changes, or training.
- **Meets regulatory mandates**: Documents compliance with laws like the General Data Protection Regulation (GDPR) or standards like the International Organization for Standardization 27001 (ISO 27001), reducing liability exposure.

Poor documentation can lead to:

- Misunderstood risk exposure
- Delays in applying remediation
- Failure to meet audit requirements
- Reputational damage in post-breach communications

## Core structural elements of a professional report

Each PIR should follow a **structured and standardized layout**, ensuring team consistency and audit-readiness across sectors. Here's a breakdown:

|**Section**|**Purpose & expectations**|
|---|---|
|**Executive summary**|A concise, nontechnical summary intended for senior leadership. Includes incident scope, high-level impact, and status.|
|**Incident timeline**|Sequential listing of key events with timestamps (real or approximated). Supports response auditability.|
|**Impact assessment**|Details the affected systems, users, services, and data. Where possible, quantify exposure (for example, "personally identifiable information (PII) of 2,000 users").|
|**Root cause analysis**|Identifies both technical flaws (for example, common vulnerabilities and exposures (CVE) exploited) and procedural gaps (for example, delayed patching). Use root cause frameworks like 5 Whys or fishbone diagrams.|
|**Indicators of Compromise (IOCs)**|Include file hashes, domains, registry changes, malicious scripts, or unusual access patterns. Tie them to known threats when possible.|
|**Containment and Eradication**|Outline exact actions taken to isolate affected systems, remove malware, and stop attacker persistence.|
|**Remediation and recovery**|Describe follow-up actions like patch deployments, password resets, policy changes, and service restorations.|
|**Lessons learned**|Summarize what was missed, delayed, or successful, feeding into future training and planning.|
|**Recommendations**|Propose technical, procedural, and behavioral changes to prevent recurrence. Include timelines and owners.|
|**Appendices**|Attach logs, screenshots, open vulnerability assessment system (OpenVAS) scans, email threads, CVE references, and external advisories.|

Use consistent section headers across all internal reporting templates for alignment and auditability.

## Writing style and tone guidelines

To ensure clarity and professionalism:

- **Be factual**: Avoid conjecture. Use "evidence indicates…" instead of "it's likely that…"
- **Stay concise**: Avoid overly technical or verbose language, especially in executive summaries.
- **Support assertions**: Every finding must be linked to a log entry, OpenVAS output, or forensic evidence.
- **Remain neutral and blameless**: Focus on systems and processes, not individuals. Use objective phrasing:
    - "The admin forgot to update."
    - "The system lacked a recent patch due to process oversight."

For incidents involving potential attribution (for example, "suspected advanced persistent threat (APT) activity"), use conditional language and include threat intelligence references from credible sources.

## Report formatting and visualization tips

Visual clarity helps stakeholders process information efficiently. Best practices include:

- **Sectioned layouts**: Use bold headers and subheaders (for example, "Root Cause Analysis" and "IoCs").
- **Tables**: For comparing timelines, affected systems, CVEs, or action items.
- **Timelines**: Present events visually for better executive digestion.
- **Diagrams**: Use simple flowcharts or attack path visualizations to illustrate lateral movement or exploitation sequences.
- **Uniform fonts and spacing**: Maintain visual professionalism across all pages.

Tip: Use exportable formats (PDF/DOCX) that preserve visuals for sharing with external stakeholders.

## Case study insight: Uber 2022 breach report

In September 2022, Uber experienced a high-profile breach following a **Multi-Factor Authentication (MFA) fatigue attack**. The attacker leveraged repeated push notifications to trick an employee into approving a login.

Uber's **internal PIR** stood out because it:

- Included a detailed **timeline** of the attack progression
- Identified a **lack of endpoint detection and response (EDR)** on PowerShell execution
- Suggested **policy changes** such as adopting FIDO2 keys and restricting admin accounts
- Recommended **employee training enhancements** to cover social engineering resistance

This case demonstrates how actionable reports can catalyze real improvements in user access, tooling, and awareness.

## OpenVAS integration in post-incident reports

OpenVAS data should be strategically incorporated throughout the report to validate findings and remediation.

|**Use case**|**Example application**|
|---|---|
|Confirm exploited CVEs|Show that CVE-2022-26925 was present and known before exploitation.|
|Demonstrate missed vulnerabilities|Identify critical vulnerabilities flagged in earlier scans but left unresolved.|
|Validate remediation effectiveness|Include follow-up scan data showing CVE removal or severity reduction.|
|Enrich threat correlation|Link OpenVAS findings to tactics, techniques, and procedures (TTPs) using MITRE adversarial tactics, techniques, and common knowledge (MITRE ATT&CK) or external threat intelligence (TI) feeds.|

Example: A missed CVE that OpenVAS detected but was deprioritized due to low exploitability might later be found to match an attacker's path. That insight should be documented in the lessons learned and policy update sections.

## Regulatory compliance considerations

Incident reports often serve a dual role: operational record and **regulatory evidence**. To comply with frameworks like:

- **National Institute of Standards and Technology Special Publication 800-61 revision 2 (NIST 800- 61r2)**: Provide structured, timestamped evidence of detection, containment, and response phases.
- **GDPR Article 33**: If personal data is involved, ensure breach notifications are documented and timestamped.
- **International Organization for Standardization/International Electrotechnical Commission 27035 (ISO/IEC 27035)**: Show integration of incident findings into security improvement initiatives.
- **Payment Card Industry Data Security Standard (PCI-DSS)**: Log forensic activities, evidence handling, and cardholder data exposure.

Retain reports for a minimum of **3 to 7 years**, depending on jurisdiction and industry regulation.
------

# What to Include in an Incident Response Report

### Essential sections of a complete incident report

Each section of your report plays a specific role in telling the story of the incident—from detection to resolution and turning it into actionable knowledge.

|Section|What to include|
|---|---|
|**1. Executive summary**|Write a concise, plain-language summary for non-technical stakeholders. Briefly explain what happened, when and how it was discovered, the scale of the impact, and the current remediation status.|
|**2. Incident timeline**|Create a chronological sequence of key events, using real or simulated timestamps. Cover detection, initial investigation, containment efforts, remediation, and lessons learned. Present as a table or timeline chart.|
|**3. Systems affected**|List each impacted asset: include hostnames, IP addresses, exposed services (e.g., HTTP, SSH), user accounts, and system roles (e.g., DMZ web server, internal database).|
|**4. Root cause analysis**|Explain the underlying vulnerability or weakness that allowed the breach. Reference CVEs detected (e.g., CVE-2022-1388), scan data, and log evidence. Discuss if the issue was technical, procedural, or both.|
|**5. Indicators of compromise (IoCs)**|Provide technical artifacts linked to the attack-IP addresses, file hashes, registry entries, rogue processes, suspicious command executions. Use validated sources such as **VirusTotal**, **MITRE**, or **CISA**.|
|**6. Threat intelligence integration**|Correlate the observed behavior with known threat actor TTPs. Use MITRE ATT&CK techniques and campaigns reported by trusted sources to contextualize the attacker\'s actions and methods.|
|**7. Containment actions**|Describe specific actions taken to stop the threat: isolating hosts, killing processes, disabling services, revoking credentials, or blocking IP addresses. Document these in order of execution.|
|**8. Remediation steps**|Detail what was done to clean the environment and restore systems. Include patches applied, configuration hardening, re-imaging, and service restarts. Provide OpenVAS comparison screenshots if available.|
|**9. Lessons learned**|Reflect on security gaps exposed by the incident: Was patch management too slow? Were the logs incomplete? Did users fall for social engineering? Document operational weaknesses for future improvement.|
|**10. Recommendations**|Provide **clear, actionable, and measurable** steps to reduce future risk. Include both tactical (for example, "Apply all critical patches within 72 hours") and strategic (for example, "Implement quarterly credentialed scans").|
|**11. Appendices**|Include supporting evidence: scan reports, CVE references, screenshots, log files, command history, and annotated images showing attacker behavior or system states.|

### OpenVAS integration best practices

Your report should show that you've used OpenVAS **not just for scanning, but as a source of actionable intelligence**. Ensure you:

- Specify the **scan profile used** (for example, Full and Fast)
- Highlight **critical vulnerabilities (CVSS ≥ 7.0)** detected and explain how they relate to the breach
- Embed **screenshots** from the OpenVAS dashboard or exported reports
- Clarify if **credentialed scanning** was enabled and what additional vulnerabilities it uncovered
- Reference **before-and-after scan results** to demonstrate remediation impact

### Real-world reporting insight

Following the **MOVEit Transfer breach (CVE-2023-34362)**, numerous organizations submitted reports to CISA that included:

- Structured **timelines of attacker actions**
- Known **IoCs** from threat intelligence feeds (e.g., Cl0p ransomware activity)
- Root cause attributed to **third-party application weaknesses**
- Policy updates involving **SBOM adoption**, **segmentation improvements**, and **external attack surface audits**

Your report should reflect this level of clarity and strategic foresight.

### Best Practices: Do's and don'ts for professional reports

|Do|Don't|
|---|---|
|Write in a **formal, structured tone**|Use informal, speculative, or emotionally charged language|
|Support findings with **scan data and CVEs**|Make assumptions without backing them with data|
|Focus on **systems, vulnerabilities, and remediations**|Place blame on individuals|
|Use **visual aids** (diagrams, timelines, IoC tables) to aid understanding|Submit raw text without visual context|
|Provide **specific, measurable recommendations**|Use vague advice such as "improve security" or "increase awareness"|

### Submission readiness checklist

Before submitting your final incident report, verify that the following are present and complete:

|Requirement||
|---|---|
|Executive summary and incident timeline|✓|
|Interpretation of OpenVAS scan data|✓|
|Documentation and explanation of CVEs|✓|
|Mapping of IoCs to threat intelligence sources|✓|
|Description of containment and remediation actions|✓|
|Clear, specific, and actionable recommendations provided|✓|
|Proper structure, formatting, and inclusion of appendices|✓|