
# Ethical hacking life cycle
1. Reconnaissance
2. Scanning and enumeration
3. Exploitation
4. Post-exploitation analysis
5. Reporting and remediation

## Reconnaissance
- Gathers information about the target
- Uses passive and active methods
- Exampels
	- Whois query reveals domain exposure

## Scanning and enumeration
- Identifies open ports, running services, and potential vulnerabilities
- Example
	- Nmap scan flags outdated SSh service

## Exploitation
- Attempts controlled exploitation of flaws
- Demonstrates real attack scenarios
- Example : 
	- SQL injection reveals insecure database queries
## Post-exploitation analysis
- Assesses the level of attacker access
- Evaluates internal movement or privilege gain
- Example :
	- Checks if low access can escalate to admin
## Reporting and remediation
- Compiles findings and business impact
- Recommends fixes and improvements
- Examples:
	- Reports suggests firewall rule updates and patches

# Hacker Types

## Black hat hackers
- Exploit systems illegally for personal gain
- Target vulnerabilities for financial benefit or sabotage
- Deploy malware, ransomeware, and phishing attacks
- Operates outside legal boundaries

## White hat hackers
- Work with explicit authorisation and legal  permissions
- Report vulnerabilities through proper channels
- Conduct ethical penetration testing and security assesments
- help improve organisational security posture

## Gray hat hackers
- Act without explicit authorization or permission
- Discover and sometimes publish vulnerabilities publicly
- Operate in ethical and legal gray areas
- Avoid malicious intent despite unauthorized access
## Red hat hackers
- Target and counter attack malicious hackers
	- Deploy offensive tactics against cybercriminals 
- Disrupt black hat operations using aggressive methods
- Act as digital vigilantes outside formal process

## Script kiddies
- Use pre-written tools without understanding mechanics
- Copy techniques from more skilled hackers
- Make basic mistakes during attack attempts
- Seek attention rather than specific technical goals

----------------
# Module-2

## Global cybersecurity regulations and frameworks

1. General Data Protection Regulation (GDPR) of the European Union
2. Network and Information Systems (NIS) Directive of the European Union
3. NIS2 Directive of the European Union, The NIS2 Directive, adopted in December 2022, builds on the NIS Directive.
4. Computer Fraud and Abuse Act (CFAA) - United states
5. California consumer privacy act (CCPA) - California , USA
6. Digital Personal Data Protection Act (DPDP) - India


## Legal preconditions for ethical hacking

|S.no|Requirement|Description|
|---|---|---|
|1|Explicit written consent|Before testing, you must obtain written authorization from the legitimate owner of the system or network. Courts do not recognize verbal or implied consent, leaving you vulnerable to prosecution without proper documentation.|
|2|Pre-test agreements|You need legal contracts that define your scope of work, including which systems you may test, what tools you will use, and how long the engagement will last. These agreements establish legal clarity and prevent boundary violations.|
|3|Responsible disclosure|You must report any discovered vulnerabilities through official, pre-agreed channels. You should never publicly disclose findings before the affected organization has an opportunity to fix the issue.|
|4|Jurisdictional compliance|You must understand laws that apply to your location and the locations of the systems or users involved. Laws regarding encryption, data sovereignty, and government systems vary by region.|

## Additional context

- Some jurisdictions, such as government networks and healthcare databases, make access to specific systems illegal regardless of purpose.
- Cloud-based systems create jurisdictional complications because data may exist in multiple regions with different legal rules.


### Review of legal risks

#### Exceeding scope of authorization
- Test only the systems listed in the signed agreement
- Request written approval before adding new systems
- Avoid actions that fall outside the approved scope
- Follow laws like the computer fraud and abuse acct(CFAA) and UK computer misuse Act
#### Lack of documentation
- Work under a signed agreement before testing
- Include system scope, test types, timelines, and contacts
- Avoid relying on verbal permissions
- Protect yourself with clear written documentation
#### Jurisdictional complexity and cross-border risks
- Check cybersecurity laws in server and user locations
- Follow data protection laws like the general data Protection Regulations (GDPR) and california consumer privacy act (CCPA)
- Recognise that public systems can still be protected
- Avoid testing across borders without formal consent

## Disclosure process
1. Confirm the vulnerability
2. Review legal boundaries
3. Identify the right contact
4. Report the vulnerability privately
5. Allow time for remediation
6. Make a responsible public disclosure

> `CVSS` - Common vulnerability scoring system


**Key sections of an effective security report are**:
- Executive summary
- Technical descriiption
- Reproduction steps
- Risk Assessments
- Recommendations
- 

# XSS - Cross-site scripting

## What are the types of XSS attacks?

There are three main types of XSS attacks. These are:

- [Reflected XSS](https://portswigger.net/web-security/cross-site-scripting#reflected-cross-site-scripting), where the malicious script comes from the current HTTP request.
- [Stored XSS](https://portswigger.net/web-security/cross-site-scripting#stored-cross-site-scripting), where the malicious script comes from the website's database.
- [DOM-based XSS](https://portswigger.net/web-security/cross-site-scripting#dom-based-cross-site-scripting), where the vulnerability exists in client-side code rather than server-side code.


This alphabetized glossary contains essential terms used in the Introduction to Ethical Hacking Principles course. Understanding these terms is crucial when working in the cybersecurity industry, participating in professional communities, and pursuing further certifications in ethical hacking.

|                                           |                                                                                                                                                                                                                                            |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Term**                                  | **Definition**                                                                                                                                                                                                                             |
| Access control                            | Access control consists of security measures that regulate user permissions for resources.                                                                                                                                                 |
| Black hat hacker                          | A black hat hacker is a malicious individual who breaches systems illegally for personal gain or harm.                                                                                                                                     |
| Blue teaming                              | Blue teaming involves defensive security operations aimed at protecting systems.                                                                                                                                                           |
| Bug bounty program                        | A bug bounty program is an organization initiative that rewards ethical hackers who responsibly identify and report security vulnerabilities.                                                                                              |
| California Consumer Privacy Act (CCPA)    | The California Consumer Privacy Act is a California law that enhances privacy rights and consumer protections.                                                                                                                             |
| Case study                                | A case study analyzes real-world cybersecurity incidents in-depth to illustrate best practices and lessons learned.                                                                                                                        |
| Code of conduct                           | A code of conduct consists of ethical guidelines that outline the expected professional behavior of ethical hackers, including explicit authorization, confidentiality, avoidance of disruption, legal compliance, and accurate reporting. |
| Computer Fraud and Abuse Act (CFAA)       | The Computer Fraud and Abuse Act is a U.S. federal law that criminalizes unauthorized access to computer systems.                                                                                                                          |
| Compliance                                | Compliance refers to the adherence to relevant laws, regulations, guidelines, and standards.                                                                                                                                               |
| Covering tracks                           | Covering tracks refers to actions taken by attackers to hide their intrusion and evade detection.                                                                                                                                          |
| Cyberterrorism                            | Cyberterrorism encompasses cyberattacks aimed at causing widespread disruption or fear.                                                                                                                                                    |
| Cyberthreat                               | A cyberthreat is any malicious attempt to damage, disrupt, or gain unauthorized access to digital infrastructure or services.                                                                                                              |
| Cybersecurity law                         | Cybersecurity law encompasses regulations and laws designed to protect systems, networks, and data from cyberthreats.                                                                                                                      |
| Dependency confusion                      | Dependency confusion is a supply chain attack that exploits the confusion between internal and external software package names.                                                                                                            |
| Encryption                                | Encryption involves converting data into secure code to prevent unauthorized access.                                                                                                                                                       |
| Ethical hacking                           | Ethical hacking is the authorized practice of penetrating systems to identify security weaknesses.                                                                                                                                         |
| Exploit                                   | An exploit is a method or software attackers use to exploit vulnerabilities.                                                                                                                                                               |
| Firewall                                  | A firewall is a network security system that monitors and filters traffic based on predefined rules.                                                                                                                                       |
| General Data Protection Regulation (GDPR) | The General Data Protection Regulation is an EU regulation that protects the privacy and security of personal data.                                                                                                                        |
| Grey hat hacker                           | A grey hat hacker is an individual who finds and discloses vulnerabilities without explicit permission but typically without malicious intent.                                                                                             |
| Hacker classification                     | Hacker classification refers to categories of hackers defined by intent, legality, and methods, such as white hat, black hat, and gray hat.                                                                                                |
| Hacker motivation                         | Hacker motivation refers to the reasons hackers engage in cyberactivities, such as financial gain, curiosity, political protest, espionage, or revenge.                                                                                    |
| Hacktivism                                | Hacktivism is hacking motivated by political or social causes.                                                                                                                                                                             |
| Information security                      | Information security protects digital and analog data from unauthorized access or modification.                                                                                                                                            |
| Insider threat                            | An insider threat refers to security risks from authorized users who exploit their access.                                                                                                                                                 |
| Intrusion detection system (IDS)          | An intrusion detection system consists of systems designed to detect unauthorized or anomalous network activities.                                                                                                                         |
| Intrusion prevention system (IPS)         | An intrusion prevention system is a security solution that detects and actively blocks threats.                                                                                                                                            |
| Legal boundaries                          | As defined by law, legal boundaries refer to the scope and limitations within which ethical hacking must operate.                                                                                                                          |
| Legal pitfalls                            | Legal pitfalls are risks of unintentionally breaking laws or regulations during cybersecurity activities.                                                                                                                                  |
| Malware                                   | Malware is malicious software created to disrupt, damage, or gain unauthorized system access.                                                                                                                                              |
| Nation-state hacking                      | Nation-state hacking refers to cyberoperations conducted or sponsored by governments, often for espionage or strategic advantage.                                                                                                          |
| Penetration testing                       | Penetration testing involves simulated cyberattacks conducted with authorization to test system security.                                                                                                                                  |
| Phishing                                  | Phishing involves fraudulent attempts to obtain sensitive personal information, typically via email.                                                                                                                                       |
| Ransomware                                | Ransomware is malware that encrypts victim data and demands payment to restore access.                                                                                                                                                     |
| Red teaming                               | Red teaming consists of simulated offensive attacks to evaluate organizational security defenses.                                                                                                                                          |
| Responsible disclosure                    | Responsible disclosure involves reporting vulnerabilities confidentially to affected organizations, allowing them time to remediate before public disclosure.                                                                              |
| Risk awareness                            | Risk awareness involves understanding cybersecurity risks and their implications.                                                                                                                                                          |
| Script kiddies                            | Script kiddies are inexperienced attackers who use pre-made hacking tools without deep technical knowledge.                                                                                                                                |
| Security report writing                   | Security report writing involves the preparation of detailed and actionable reports on security assessments and vulnerability findings.                                                                                                    |
| Security reporting                        | Security reporting encompasses the clear and effective documentation and communication of security vulnerabilities and findings.                                                                                                           |
| Social engineering                        | Social engineering involves manipulative tactics used to deceive individuals into revealing sensitive information.                                                                                                                         |
| Structured Query Language (SQL) injection | Structured Query Language injection is a cyberattack method where malicious SQL statements are inserted into entry fields to exploit database vulnerabilities.                                                                             |
| Two-factor authentication (2FA)           | Two-factor authentication is a security method that requires two verification forms to authenticate identity.                                                                                                                              |
| Vulnerability assessment                  | Vulnerability assessment is the process of systematically identifying and classifying security weaknesses.                                                                                                                                 |
| Vulnerability disclosure                  | Vulnerability disclosure involves reporting identified vulnerabilities with recommendations for remediation.                                                                                                                               |
| Weak authentication                       | Weak authentication refers to insufficient security measures that allow unauthorized access.                                                                                                                                               |
| White hat hacker                          | A white hat hacker is an ethical cybersecurity professional who identifies and addresses vulnerabilities legally and responsibly.                                                                                                          |
| Zero-day vulnerability                    | A zero-day vulnerability is a security flaw unknown to software creators during exploitation.                                                                                                                                              |