# Cryptography: A Comprehensive, Ground-Up Study Guide
*A self-contained learning document covering the foundations, mathematical mechanics, protocols, and modern standards of secure communication.*

---

## Table of Contents
1. [Fundamental Concepts of Cryptology](#1-fundamental-concepts-of-cryptology)
2. [Symmetric Cryptography: Foundational Mechanics](#2-symmetric-cryptography-foundational-mechanics)
3. [The Advanced Encryption Standard (AES)](#3-the-advanced-encryption-standard-aes)
4. [Symmetric Modes of Operation & Stream Ciphers](#4-symmetric-modes-of-operation--stream-ciphers)
5. [Cryptographic Hash Functions & Integrity](#5-cryptographic-hash-functions--integrity)
6. [Passwords & Key Derivation Protocols](#6-passwords--key-derivation-protocols)
7. [Asymmetric Cryptography: The RSA Cryptosystem](#7-asymmetric-cryptography-the-rsa-cryptosystem)
8. [Digital Signatures & Hybrid Systems](#8-digital-signatures--hybrid-systems)
9. [Key Exchange & Perfect Forward Secrecy](#9-key-exchange--perfect-forward-secrecy)
10. [Modern Horizons: Elliptic Curve Cryptography (ECC) & Security Equivalences](#10-modern-horizons-elliptic-curve-cryptography-ecc--security-equivalences)

---

## 1. Fundamental Concepts of Cryptology

To master secure communications, one must first grasp the core terminology and historical context that shaped modern cryptographic engineering.

### Core Terminology
Every discipline has its precise language. In secure systems, we draw distinct boundaries between these core terms:

*   **Cryptography**: The practice of writing secret messages such that only authorized parties can read them [1]. It involves designing algorithms and protocols to enforce confidentiality, integrity, and authenticity.
*   **Cryptanalysis**: The science of analyzing secret messages—often using statistical, algebraic, or brute-force tools—to uncover hidden patterns and intercept messages without authorized credentials [1].
*   **Cryptology**: The overarching academic and practical discipline that unites both **cryptography** and **cryptanalysis** [1].
*   **Steganography**: The practice of writing messages such that no one else notices that a communication is even taking place [1]. Unlike cryptography, which renders a message unreadable, steganography hides the message in plain sight (e.g., in invisible ink, or embedded in image pixels).
*   **Encoding**: The representation of data using a defined set of characters to enable reliable digital transmission or storage (e.g., Base64, Base32, UTF-8, ASCII) [1]. **Encoding is not cryptography** because it does not attempt to hide information; it is completely public and lacks a secret key [1].

### Classical Substitution: The Caesar Cipher
The **Caesar Cipher** is one of the earliest known substitution ciphers [2]. In a substitution cipher, each character of the plaintext is systematically replaced by another character.

#### Plain English Explanation
To encrypt a message, you shift every letter down the alphabet by a fixed number of positions (known as the shift key, $k$). For instance, with a shift key of $3$, 'A' becomes 'D', 'B' becomes 'E', and 'Z' wraps around to become 'C'.

#### Mathematical Form
To represent this mathematically, we assign each letter of the alphabet an integer value from $0$ to $25$ ($A=0, B=1, \dots, Z=25$). The encryption and decryption operations are:

$$	ext{Encrypt}(P) = (P + k) \pmod{26}$$

$$	ext{Decrypt}(C) = (C - k) \pmod{26}$$

Where:
*   $P$ is the integer representing the plaintext letter.
*   $C$ is the integer representing the ciphertext letter.
*   $k$ is the secret shift key ($0 \le k \le 25$).
*   $\pmod{26}$ ensures that the shifting wraps around the 26-letter English alphabet.

> **Deep Dive: Frequency Analysis & CyberChef**
> In a classroom or lab environment, a common exercise is to take a block of text (such as the Wikipedia plot summary of your favorite movie) and encrypt it using the Caesar Cipher via the open-source web tool *CyberChef* [2]. 
> While simple to implement, the Caesar Cipher is entirely insecure. Because it is a **monoalphabetic substitution cipher** (each plaintext letter always maps to the same ciphertext letter), it completely preserves the underlying statistical properties of the language. 
> In any natural language, certain letters appear with highly predictable frequencies. For example, in English, the letter **E** is the most common, followed by **T**, **A**, and **O**. A cryptanalyst can perform **frequency analysis** on the ciphertext, identify the most frequent characters, match them to the language's natural distribution, and instantly solve the key $k$ [2].

---

### Classical Transposition: The Railfence Cipher
In contrast to substitution ciphers, a **transposition cipher** does not replace characters. Instead, it "deplaces" (reorders or shuffles) them [2].

#### The Railfence & The Scytale
The **Railfence Cipher** is based on ancient Greek military technology called the **scytale** [2]. 

*   **Scytale Diagram Description**: Visualize a wooden rod of a specific diameter. A strip of leather or parchment is wrapped tightly around it. The sender writes the message horizontally along the length of the rod. When the strip is unwound, the letters appear completely scrambled and disconnected. To read the message, the recipient must wrap the strip around a wooden rod of the exact same diameter. Here, the "diameter of the rod" acts as the secret key.

---

### Key Design Principles
As cryptography transitioned from a classical art into a modern mathematical science, two foundational guidelines emerged:

#### 1. Kerckhoffs's Principle
Standardized by Auguste Kerckhoffs in the 19th century, this principle states:
> *The security of a cryptosystem should solely depend on the secrecy of the key, but never on the secrecy of the algorithms [2].*

This is the bedrock of modern open security standards. Keeping algorithms secret (known as "security through obscurity") is fragile because algorithms can be reverse-engineered, leaked by insiders, or broken through cryptanalysis. Open algorithms allow for public peer review, hardening the system against flaws.

#### 2. Shannon's Principles for Secure Ciphers
In 1949, mathematician Claude Shannon defined two primary mechanisms to obstruct cryptanalysis:
*   **Confusion**: Obscuring the relationship between the secret key and the ciphertext [3]. This ensures that knowing the ciphertext gives no mathematical clues about the key. Modern systems achieve confusion using non-linear **substitution** steps (e.g., S-Boxes).
*   **Diffusion**: Spreading the statistical structure of the plaintext over the entire ciphertext [3]. If a single bit of the plaintext changes, diffusion ensures that approximately half of the ciphertext bits change randomly. Modern systems achieve diffusion using **transposition** or mixing steps.

---

### Key Takeaways
*   **Cryptology** includes cryptography (writing secrets) and cryptanalysis (breaking secrets) [1]. Steganography hides the existence of the message [1].
*   **Caesar ciphers** substitute characters using modular arithmetic but are trivial to break via **frequency analysis** [2].
*   **Transposition ciphers** (like the Greek **scytale**) rearrange characters instead of replacing them [2].
*   **Kerckhoffs's Principle** mandates that algorithm designs remain public; only the key must be secret [2].
*   **Confusion** hides the key; **Diffusion** hides plaintext structure [3].

---

### Quick Check
1.  **Question**: Why is Base64 encoding not considered a form of cryptography?
    *   *Answer*: Encoding represents data in a specific character set for digital compatibility, but it uses no secret key and provides no confidentiality [1]. Anyone can decode Base64 instantly.
2.  **Question**: If you encrypt the word "CAB" using a Caesar cipher with key $k=5$, what is the ciphertext?
    *   *Answer*: Assignment: $C=2, A=0, B=1$. 
        *   $C 	o (2 + 5) \pmod{26} = 7 	o \mathbf{H}$
        *   $A 	o (0 + 5) \pmod{26} = 5 	o \mathbf{F}$
        *   $B 	o (1 + 5) \pmod{26} = 6 	o \mathbf{G}$
        *   Ciphertext: **HFG**.

---

## 2. Symmetric Cryptography: Foundational Mechanics

Symmetric encryption forms the workhorse of high-speed data protection. Let us explore its core components, mathematical operations, and the historic transition from DES to AES.

### Motivation & Basic Concept
Symmetric key encryption is primarily used to secure communications over an untrusted channel or protect files stored in untrusted storage [5]. 

```
Plaintext (M) ---> [ Encrypt using Key K ] ---> Ciphertext (C) ---> [ Decrypt using Key K ] ---> Plaintext (M)
```
*Symmetric Cryptography Diagram: The exact same key ($K$) is shared between both endpoints to lock and unlock the message.*

The system is defined by three algorithms [5, 6]:
1.  **Key Generation (KeyGen)**: Generates a strong key used for both encryption and decryption [5, 6].
2.  **Encrypt (Enc)**: Given the secret key and a plaintext, outputs a ciphertext [5, 6].
3.  **Decrypt (Dec)**: Given the secret key and a ciphertext, outputs the original plaintext [5, 6].

---

### Block Ciphers
A **block cipher** is a stateless, deterministic symmetric cipher that encrypts data in fixed-sized chunks called "blocks" [6].

*   **Plaintext block ($M$)**: Bit size of $n$ [6].
*   **Ciphertext block ($C$)**: Bit size of $n$ [6].
*   **Secret Key ($K$)**: Bit size of $s$ [6].
*   **Stateless**: The cipher does not remember past blocks; encrypting the same block $M$ under the same key $K$ will always output the exact same block $C$ [6].

---

### The Binary Engine: Exclusive OR (XOR)
At the lowest physical layer of computer chips, symmetric encryption relies heavily on the **exclusive OR (XOR)** boolean binary operation [6].

#### Plain English Explanation
The XOR operation compares two input bits. If the bits are different, the output is $1$. If the bits are the same, the output is $0$ [6].

#### Truth Table and Properties
Let $\oplus$ denote XOR:

| Input $x$ | Input $y$ | Output $s = x \oplus y$ |
| :---: | :---: | :---: |
| 0 | 0 | **0** |
| 0 | 1 | **1** |
| 1 | 0 | **1** |
| 1 | 1 | **0** [6] |

XOR has two critical properties that make it perfect for cryptography:
1.  **Self-Inverse**: $x \oplus y \oplus y = x$. This means XORing a bit with the same value twice restores the original value, making it extremely easy to apply during encryption and remove during decryption [6, 17].
2.  **Uniform Distribution**: If input $y$ is a truly random bit, then $x \oplus y$ will be a perfectly random bit, regardless of the value of $x$.

#### Mathematical Example
Let us compute the XOR of two byte matrices in binary [6]:
*   $A = 1001\ 1110$ [6]
*   $B = 0111\ 0001$ [6]
*   $A \oplus B = C$:
    ```
      1 0 0 1   1 1 1 0  (A)
    + 0 1 1 1   0 0 0 1  (B)
    -------------------
    = 1 1 1 0   1 1 1 1  (C) [6]
    ```
*   **To Decrypt (Retrieve A from C and B)**:
    ```
      1 1 1 0   1 1 1 1  (C)
    + 0 1 1 1   0 0 0 1  (B)
    -------------------
    = 1 0 0 1   1 1 1 0  (A) [6]
    ```
*   **To Retrieve B from C and A**:
    ```
      1 1 1 0   1 1 1 1  (C)
    + 1 0 0 1   1 1 1 0  (A)
    -------------------
    = 0 1 1 1   0 0 0 1  (B) [6]
    ```

> **Deep Dive: XOR Hardware Gate Implementation**
> In silicon, XOR gates are typically built using standard **NAND gates** [6]. 
> A NAND gate outputs $0$ only if both inputs are $1$. To construct an XOR gate ($A \oplus B$), four NAND gates are connected as follows:
> 1. Gate 1 receives inputs $A$ and $B$. Output is $N_1 = 	ext{NAND}(A, B)$.
> 2. Gate 2 receives inputs $A$ and $N_1$. Output is $N_2 = 	ext{NAND}(A, N_1)$.
> 3. Gate 3 receives inputs $B$ and $N_1$. Output is $N_3 = 	ext{NAND}(B, N_1)$.
> 4. Gate 4 receives inputs $N_2$ and $N_3$. Output is the final XOR result: $S = 	ext{NAND}(N_2, N_3)$.

---

### The Data Encryption Standard (DES)
Standardized in **1977** by the National Bureau of Standards (now NIST), DES was the first globally accepted commercial encryption standard [6].

*   **Key Size**: 56 bits (extremely small by modern standards) [6].
*   **Block Size**: 64 bits [7].
*   **Structure**: **Feistel Network** [7].

#### Feistel Network Encryption Diagram Description
The 64-bit plaintext block is processed sequentially as follows [7]:
1.  An **Initial Permutation (IP)** shuffles the 64 bits [7].
2.  The block is split into two 32-bit halves: Left ($L$) and Right ($R$) [7].
3.  The block passes through **16 Rounds** [7]. In each round $i$:
    *   $L_i = R_{i-1}$
    *   $R_i = L_{i-1} \oplus F(R_{i-1}, K_i)$, where $F$ is a round function and $K_i$ is a unique 48-bit round key derived from the master key [7].
4.  After the 16th round, the halves are recombined, and a **Final Permutation (Inverse IP)** is applied to produce the 64-bit ciphertext [7].

#### Decryption
To decrypt, the exact same structure is run in reverse [7]. The ciphertext is passed through the Feistel network, but the round keys are applied in reverse order (from $K_{16}$ down to $K_1$) [7]. This symmetry makes Feistel networks highly efficient to implement in hardware [7].

#### Other Feistel Ciphers
Several notable modern symmetric algorithms are based on Feistel Networks, including **Blowfish**, **Twofish**, **Mars**, and **RC6** [7, 8].

#### Why DES is Obsolete (Too Weak)
The 56-bit key space of DES yields only $2^{56} pprox 7.2 	imes 10^{16}$ possible keys. This key space is too small to resist modern brute-force attacks [8].
*   **Deep Crack (1998)**: Built by the Electronic Frontier Foundation (EFF) for \$250,000, this machine featured 29 custom circuit boards containing 64 **ASICs** (Application-Specific Integrated Circuits—highly customized computer chips) [8]. It brute-forced a DES key in just **9 days** [8].
*   **COPACOBANA (2006)**: Built using 120 **FPGAs** (Field Programmable Gate Arrays—reprogrammable hardware chips) for only \$10,000, this system brute-forced the entire DES key space in **6.4 days** [8].

---

### Key Takeaways
*   Symmetric encryption uses a single shared secret key for encryption and decryption [5, 6].
*   **Block ciphers** process fixed $n$-bit blocks of data statelessly [6].
*   **XOR ($\oplus$)** is a self-inverse boolean operation ($	ext{XOR}(x, y, y) = x$) that serves as the hardware foundation of ciphers [6, 17].
*   **DES** was a Feistel network cipher with 16 rounds, a 64-bit block size, and a 56-bit key size [6, 7].
*   DES is thoroughly broken. Custom hardware like ASICs and FPGAs can brute-force 56-bit keys in days [8].

---

### Quick Check
1.  **Question**: What is the difference between an ASIC and an FPGA?
    *   *Answer*: An ASIC is a custom-manufactured chip optimized permanently for one task. An FPGA is a programmable chip that can be reconfigured dynamically via software [8].
2.  **Question**: If a Feistel network cipher round function $F$ is incredibly complex and mathematically non-invertible, how is decryption still possible?
    *   *Answer*: The Feistel structure does not require $F$ to be invertible. During decryption, we compute $F(R_{i-1}, K_i)$ and XOR it with the left side, naturally canceling out the encryption XOR due to the self-inverse property of the XOR operation ($x \oplus y \oplus y = x$).

---

## 3. The Advanced Encryption Standard (AES)

As DES became obsolete, the cryptographic community required a secure, highly efficient successor. This led to the standardization of the Advanced Encryption Standard (AES) in 2001 [8].

### High-Level Overview & Rijndael Competition
In 1997, NIST announced a competition to select a replacement for DES. The winning algorithm, selected in **2001**, was **Rijndael** (designed by Belgian cryptographers Vincent Rijmen and Joan Daemen) [8].

#### AES Competition Requirements [9]
*   **Block Size**: Must natively support 128-bit blocks [9].
*   **Key Sizes**: Must natively support at least 128-bit, 192-bit, and 256-bit keys [9].
*   **Security**: Must be resistant to all known cryptanalytic and mathematical attacks [9].
*   **Efficiency**: Must execute rapidly on resource-constrained 8-bit systems (like smart cards), 32-bit microcontrollers, and high-performance CPUs [9].
*   **Flexibility & Simplicity**: Must be clean to implement with minimal memory footprints [9].

#### Evaluation Criteria [10]
Candidates were evaluated on:
1.  **Security**: Mathematical proof of resistance to differential, linear, and algebraic cryptanalysis [10].
2.  **Performance**: Execution speed on a wide array of CPU architectures [10].
3.  **Efficiency**: Memory usage, code size, and low power consumption [10].
4.  **Complexity**: Simplicity of the design to minimize bugs and side-channel vulnerabilities [10].

---

### Step-by-Step Round Transformations
Unlike DES, AES is **not** a Feistel network. It is a **Substitution-Permutation Network (SPN)**. It operates on the entire 128-bit block in parallel, representing the data as a $4 	imes 4$ matrix of bytes [12].

```
Plaintext State ---> AddRoundKey() ---> [ Rounds 1 to 9: SubBytes() -> ShiftRows() -> MixColumns() -> AddRoundKey() ] ---> [ Round 10 (Final): SubBytes() -> ShiftRows() -> AddRoundKey() ] ---> Ciphertext State
```
*AES-128 Encryption Pipeline: Highlighting the 10 rounds of SPN operations and the omission of MixColumns() in the final round [11].*

#### AES Round Counts
*   **AES-128**: 10 Rounds (requires 11 round keys) [11, 12].
*   **AES-192**: 12 Rounds (requires 13 round keys).
*   **AES-256**: 14 Rounds (requires 15 round keys).

Each standard encryption round consists of four distinct algebraic operations [10]:

#### 1. Key Expansion (KDF)
Before encryption starts, the master key is expanded to generate one 128-bit key per round (plus an initial key applied before Round 1) [10, 12].
*   **AES-128 Key Expansion Matrix representation [12]**: The original key is loaded directly. A key expansion routine generates unique $4 	imes 4$ byte keys for each sequential round [12].

#### 2. SubBytes() - S-Box Substitution
This is the only non-linear step in AES, providing the necessary **confusion** to thwart mathematical attacks [3, 10].
*   **Operation**: Every byte in the state matrix is replaced with a corresponding byte from a static lookup table called the **S-Box** [14].
*   **S-Box Lookup Mechanics [14]**: To substitute a byte like `0x49` (hexadecimal), we use the first nibble (`4`) to locate the row, and the second nibble (`9`) to locate the column in the S-Box table. The intersection reveals the substituted value `0x3b` [14].
*   An **Inverse S-Box** is used to reverse this step during decryption [14].

#### 3. ShiftRows() - Row Transposition
This step provides **diffusion** by shifting bytes horizontally across the matrix rows [3, 10, 15].
*   **Row 0**: No shift [15].
*   **Row 1**: Shifted/rotated left by 1 byte [15].
*   **Row 2**: Shifted/rotated left by 2 bytes [15].
*   **Row 3**: Shifted/rotated left by 3 bytes [15].
*   Decryption simply shifts the rows in the opposite direction (right) [15].

#### 4. MixColumns() - Column Mixing
This step provides massive **diffusion** vertically down the matrix columns [3, 10, 15].
*   **Operation**: Each of the 4 columns in the state matrix is treated as a vector and multiplied by a fixed mathematical matrix over a **Galois Finite Field $GF(2^8)$** [15, 16].
*   **GF(2^8) Matrix Multiplication [16]**:
    
    $$egin{pmatrix} s'_{0,c} \ s'_{1,c} \ s'_{2,c} \ s'_{3,c} \end{pmatrix} = egin{pmatrix} 2 & 3 & 1 & 1 \ 1 & 2 & 3 & 1 \ 1 & 1 & 2 & 3 \ 3 & 1 & 1 & 2 \end{pmatrix} egin{pmatrix} s_{0,c} \ s_{1,c} \ s_{2,c} \ s_{3,c} \end{pmatrix}$$
    
    This ensures that changing a single byte in a column will completely change all four bytes of that column after the multiplication [16].
*   To reverse this during decryption, we multiply by the **Inverse Matrix** [16]:
    
    $$egin{pmatrix} E & B & D & 9 \ 9 & E & B & D \ D & 9 & E & B \ B & D & 9 & E \end{pmatrix}$$ [16]

#### 5. AddRoundKey()
*   **Operation**: The current state is XORed bitwise with the specific $4 	imes 4$ round key generated during Key Expansion [10, 16]. Because XOR is a self-inverse operation, repeating `AddRoundKey()` with the same key during decryption cancels out the encryption round key [17].

> **The Final Round Exception**: In the final round of AES (e.g., Round 10 in AES-128), the **MixColumns()** step is entirely omitted [11]. This makes the encryption and decryption architectures symmetric and prevents the cipher from wasting computation on a mixing step that would be immediately exposed after the final key addition.

---

### Step-by-Step Worked Matrix Example
Let us trace the physical state matrix transformation for the first round of AES-128 [13].

#### Input Data
*   **128-bit key in hex**: `0x0123456789abcdef0123456789abcdef` [12]
*   **Plaintext**: `"Hello World!!!!!"` $	o$ Hex: `0x48656c6c6f20576f726c642121212121` [13]

#### Step 1: Initialize the State Matrix
The plaintext hex bytes are loaded column-by-column into a $4 	imes 4$ state matrix [13]:

$$egin{pmatrix} 48 & 6f & 72 & 21 \ 65 & 20 & 6c & 21 \ 6c & 57 & 64 & 21 \ 6c & 6f & 21 & 21 \end{pmatrix}$$ [13]

#### Step 2: Initial AddRoundKey()
We XOR the initial state matrix with the original key (`0x0123456789abcdef...`) [12, 13]:

$$egin{pmatrix} 48 \oplus 01 & 6f \oplus 89 & 72 \oplus 01 & 21 \oplus 89 \ 65 \oplus 23 & 20 \oplus ab & 6c \oplus 23 & 21 \oplus ab \ 6c \oplus 45 & 57 \oplus cd & 64 \oplus 45 & 21 \oplus cd \ 6c \oplus 67 & 6f \oplus ef & 21 \oplus 67 & 21 \oplus ef \end{pmatrix} = egin{pmatrix} 49 & e6 & 73 & a8 \ 46 & 8b & 4f & a8 \ 29 & 9a & 21 & ec \ 0b & 80 & 46 & ce \end{pmatrix}$$ [13]

*Note: The intermediate state matrix matches the XOR output values in slide 13 [13].*

#### Step 3: SubBytes()
Using the standard S-Box lookup table, every byte is substituted. E.g., `49` becomes `3b` [14]:

$$	ext{SubBytes}egin{pmatrix} 49 & e6 & 73 & a8 \ 46 & 8b & 4f & a8 \ 29 & 9a & 21 & ec \ 0b & 80 & 46 & ce \end{pmatrix} = egin{pmatrix} 3b & 8e & 8f & c2 \ 5a & 3d & 84 & 7e \ a5 & b8 & fd & ce \ 2b & cd & 5a & 8b \end{pmatrix}$$ [14]

#### Step 4: ShiftRows()
We rotate the rows left [15]:
*   Row 0: no shift (`3b 8e 8f c2` $	o$ `3b 8e 8f c2`) [15]
*   Row 1: shift left 1 (`5a 3d 84 7e` $	o$ `3d 84 7e 5a`) [15]
*   Row 2: shift left 2 (`a5 b8 fd ce` $	o$ `fd ce a5 b8`) [15]
*   Row 3: shift left 3 (`2b cd 5a 8b` $	o$ `8b 2b cd 5a`) [15]

$$	ext{ShiftRows}egin{pmatrix} 3b & 8e & 8f & c2 \ 5a & 3d & 84 & 7e \ a5 & b8 & fd & ce \ 2b & cd & 5a & 8b \end{pmatrix} = egin{pmatrix} 3b & 8e & 8f & c2 \ 3d & 84 & 7e & 5a \ fd & ce & a5 & b8 \ 8b & 2b & cd & 5a \end{pmatrix}$$ [15]

#### Step 5: MixColumns()
Multiplying each column by the fixed matrix over $GF(2^8)$ mixes the byte vectors. 
For column 1 (`[3b, 3d, fd, 8b]^T`), the result is `[47, d6, 61, 80]^T` [16]:

$$	ext{MixColumns}egin{pmatrix} 3b & 8e & 8f & c2 \ 3d & 84 & 7e & 5a \ fd & ce & a5 & b8 \ 8b & 2b & cd & 5a \end{pmatrix} = egin{pmatrix} 47 & 75 & ef & 93 \ d6 & ff & 4a & ff \ 61 & f0 & ec & 1d \ 80 & 95 & d0 & 0b \end{pmatrix}$$ [16]

#### Step 6: AddRoundKey() for Round 1
XOR the state with the Round 1 Key (`62 eb ea 63 9e 35 16 bd 9a 57 12 df c0 2f 48 a7`) [12, 17]:

$$egin{pmatrix} 47 \oplus 62 & 75 \oplus eb & ef \oplus ea & 93 \oplus 63 \ d6 \oplus 9e & ff \oplus 35 & 4a \oplus 16 & ff \oplus bd \ 61 \oplus 9a & f0 \oplus 57 & ec \oplus 12 & 1d \oplus df \ 80 \oplus c0 & 95 \oplus 2f & d0 \oplus 48 & 0b \oplus a7 \end{pmatrix} = egin{pmatrix} 25 & 9e & 05 & f0 \ 48 & ca & 5c & 42 \ fb & a7 & fe & c2 \ 40 & ba & 98 & ac \end{pmatrix}$$ [17]

This is the final state matrix after Round 1 [17]. This 4-step round sequence is repeated 9 more times to compute the final ciphertext of AES-128 [17].

---

### Key Takeaways
*   AES was standardized in 2001 after the Rijndael cipher won a multi-year NIST competition [8].
*   AES operates on a $4 	imes 4$ byte state matrix with block sizes of 128 bits and key sizes of 128, 192, or 256 bits [9, 12].
*   The standard rounds use four steps: **SubBytes** (confusion lookup) [14], **ShiftRows** (horizontal diffusion transposition) [15], **MixColumns** (vertical $GF(2^8)$ algebraic diffusion) [15, 16], and **AddRoundKey** (XORing round keys) [10, 16].
*   The final round of AES omits the MixColumns step [11].

---

### Quick Check
1.  **Question**: Why does AES-256 require more rounds (14) than AES-128 (10)?
    *   *Answer*: The larger 256-bit key size requires a longer mathematical key expansion sequence. More rounds are necessary to ensure that the higher security margin offered by the longer key is fully propagated to prevent advanced cryptanalytic shortcuts.
2.  **Question**: Can a single bit error in a plaintext block affect the entire block of ciphertext?
    *   *Answer*: Yes, absolutely. Due to the massive diffusion provided by the combination of `ShiftRows()` and `MixColumns()`, a single bit change in the plaintext cascades rapidly, completely scrambling approximately half of the bits in the output ciphertext block after just a few rounds.

---

## 4. Symmetric Modes of Operation & Stream Ciphers

In production systems, files and streams are always larger than a single block cipher block. To encrypt arbitrarily sized datasets, we must use secure modes of operation or stream ciphers.

### Block Cipher Modes of Operation

#### 1. Electronic Codebook (ECB) Mode (The "Bad" Idea)
ECB is the most straightforward, but highly insecure, mode of operation [17]. It simply splits the plaintext $D$ into $n$-bit blocks and encrypts each block independently using the block cipher with the same key [17].

$$	ext{Encrypt}(P_i) = E_K(P_i) = C_i$$

$$	ext{Decrypt}(C_i) = D_K(C_i) = P_i$$

##### Why ECB is Insecure
*   **Dictionary Attacks**: Because the encryption is purely deterministic and stateless, identical plaintext blocks always result in identical ciphertext blocks [18].
*   **Vulnerability to Manipulation**: Attackers who intercept the transmission can easily delete blocks, double blocks, inject false blocks, or modify the block ordering without triggering any decryption errors [18].

```
Original Image (Tux) ---> ECB Encryption ---> Ciphertext Image (Still reveals Tux silhouette)
```
*Visualizing the ECB Mode Failure: An image of Tux the penguin encrypted in ECB mode preserves Tux's distinct shape because identical blocks of pixel colors are mapped to identical ciphertext values, completely leaking the structure of the data.*

---

#### 2. Cipher Block Chaining (CBC) Mode
To fix the leakage of structural patterns in ECB, CBC introduces feedback by chaining blocks together [19].

##### Encryption Formula
Before a plaintext block is encrypted, it is XORed with the previous ciphertext block [19]. An **Initialization Vector (IV)** is used to seed the first block:

$$C_i = E_K(P_i \oplus C_{i-1}), \quad C_0 = IV$$

##### Decryption Formula
During decryption, the ciphertext block is decrypted first, and then XORed with the *previous* ciphertext block to recover the plaintext [19]:

$$P_i = D_K(C_i) \oplus C_{i-1}, \quad C_0 = IV$$

##### CBC Diagram Descriptions
*   **CBC Encryption Flow**: Plaintext block $P_1$ is XORed with $C_0$ ($IV$). The result is passed into the block cipher encryption engine to output ciphertext block $C_1$. Next, $P_2$ is XORed with $C_1$ and passed to the encryption engine to output $C_2$. This chaining occurs serially.
*   **CBC Decryption Flow**: Ciphertext block $C_1$ is passed to the decryption engine. The output is XORed with $C_0$ ($IV$) to recover plaintext block $P_1$. Simultaneously, $C_2$ is passed to the decryption engine, and the output is XORed with $C_1$ to recover $P_2$. Because decryption only relies on the current and previous ciphertext blocks, decryption can be processed in parallel.

##### The Salt/Initialization Vector Rule
To prevent dictionary attacks, every unique encryption session must use a fresh, random, and unique **Initialization Vector (IV)**.

---

### Stream Ciphers
While block ciphers operate on large chunks of data, a **stream cipher** encrypts data bit-by-bit or byte-by-byte continuously [19, 20].

#### The One-Time Pad (OTP)
The theoretical ideal behind all stream ciphers is the **One-Time Pad** [19]. It encrypts plaintext by XORing it bitwise with a completely random key.
The One-Time Pad is mathematically **unbreakable** (it achieves perfect secrecy) if and only if these four strict conditions are met [19]:
1.  The key is never re-used (in whole or in part) [19].
2.  The key is kept completely secret [19].
3.  The key is at least as long as the plaintext [19].
4.  The key is truly random [19].

If these conditions are met, an attacker intercepts nothing but random noise. Even if they attempt brute force, they will decrypt every possible string of that length with equal probability, yielding zero information.

#### Practical Stream Ciphers
Because distributing keys that are as long as the entire plaintext is logistically impossible, practical stream ciphers use a short, easily shared secret **seed** (the key) to generate a pseudo-random key stream that mimics the properties of a one-time pad [19].

Modern stream ciphers require a **nonce** (number used once) as an additional input to ensure that the key stream is never repeated, even if the same key is used to encrypt different messages [20].

*   **Examples**: **ChaCha20**, **RC4** (RC4 is thoroughly broken and is no longer secure) [20].

---

#### Counter (CTR) Mode
CTR mode effectively converts any block cipher (like AES) into a high-speed stream cipher [20].

##### CTR Encryption Formula
A counter value is combined with a nonce, encrypted using the block cipher, and the output block is XORed with the plaintext to produce ciphertext [20]:

$$C_i = P_i \oplus E_K(	ext{Nonce} \parallel 	ext{Counter}_i)$$

##### CTR Decryption Formula
Decryption is identical. We generate the exact same key stream by encrypting the nonce and counter, and XOR it with the ciphertext to recover the plaintext [20]:

$$P_i = C_i \oplus E_K(	ext{Nonce} \parallel 	ext{Counter}_i)$$

##### CTR Diagram Descriptions
*   **CTR Encryption**: The string "Nonce || Counter" (e.g., `0x59bcf35... || 00000001`) is passed into the block cipher encryption engine under key $K$. The output block is XORed with plaintext block $P_1$ to output ciphertext block $C_1$. The counter is then incremented, and the process is repeated.
*   **CTR Decryption**: Exactly like encryption, the string "Nonce || Counter" is passed to the block cipher *encryption* engine. The output is XORed with ciphertext block $C_1$ to recover plaintext block $P_1$. **Note: CTR decryption uses the block cipher's encryption function, not its decryption function.**

---

### Galois/Counter Mode (GCM)
Standard symmetric encryption modes like CBC or CTR only guarantee **confidentiality** (hiding the message), but they do not guarantee **integrity** (ensuring the message has not been altered). 

To solve this, **Galois/Counter Mode (GCM)** provides **Authenticated Encryption with Associated Data (AEAD)** [25].
*   It uses **CTR mode** to enforce confidentiality [20, 25].
*   It computes an authenticating tag over a Galois Finite Field (called a **Galois mode of authentication**) to enforce integrity [25].
*   This single, highly efficient construction ensures both **confidentiality** and **integrity** in parallel [25].

---

### Key Takeaways
*   **ECB mode** is insecure because it is deterministic; identical plaintext blocks yield identical ciphertext blocks, preserving structural patterns [17, 18].
*   **CBC mode** chains blocks together by XORing the previous ciphertext block, preventing pattern leakage [19].
*   **Stream ciphers** generate a pseudo-random keystream from a key and a **nonce** [19, 20].
*   **CTR mode** turns a block cipher into a stream cipher by encrypting a counter [20].
*   **GCM** is an AEAD mode providing both confidentiality and integrity [25].

---

### Quick Check
1.  **Question**: Why is key stream re-use (using the same key and nonce in CTR mode) catastrophic?
    *   *Answer*: If an attacker captures two ciphertexts $C_1 = P_1 \oplus S$ and $C_2 = P_2 \oplus S$ encrypted with the same key stream $S$, they can XOR them together: $C_1 \oplus C_2 = P_1 \oplus P_2$. This completely eliminates the cryptosystem's security, allowing the attacker to solve both plaintexts using linguistic context or known-plaintext attacks.
2.  **Question**: Why does GCM mode allow for "associated data" that is authenticated but not encrypted?
    *   *Answer*: Network packets require headers (like IP addresses) to be readable in transit by routers. GCM allows this metadata to remain unencrypted (so routers can read it) but includes it in the Galois authentication tag calculation to prevent attackers from altering it.

---

## 5. Cryptographic Hash Functions & Integrity

Confidentiality is useless if an attacker can silently modify your data. We use cryptographic hash functions and Message Authentication Codes (MACs) to guarantee data integrity.

### Foundational Hash Properties
A **hash function** maps an input of arbitrary length to an output of fixed length [20]. To be considered **cryptographic**, a hash function must be a "one-way" function (extremely hard to invert) [20].

Because a hash function maps infinite inputs to a finite set of outputs, **collisions** (where $H(x) = H(x')$ for $x 
eq x'$) are mathematically guaranteed to exist [20]. However, a secure cryptographic hash function must satisfy three foundational properties to prevent attacks [21]:

```
1. PREIMAGE RESISTANCE:      Hash(x) = y      <-- Given y, cannot find x [21]
2. 2ND PREIMAGE RESISTANCE:  Hash(x) = Hash(x') <-- Given x, cannot find different x' [21]
3. COLLISION RESISTANCE:     Hash(x) = Hash(x') <-- Cannot find any random pair x, x' [21]
```

1.  **Preimage Resistance (One-Wayness)**: Given a hash value $y$, it must be computationally infeasible to find any plaintext $x$ such that $H(x) = y$ [21].
2.  **Second Preimage Resistance**: Given a specific plaintext $x$, it must be computationally infeasible to find a different plaintext $x'$ ($x' 
eq x$) such that $H(x) = H(x')$ [21].
3.  **Collision Resistance**: It must be computationally infeasible to find *any* random pair of plaintexts $x$ and $x'$ ($x 
eq x'$) that hash to the same value ($H(x) = H(x')$) [21].

---

### Structural Constructions: Merkle-Damgård vs Sponge

#### 1. Merkle-Damgård Construction
Most classic hash functions divide the input into fixed-sized blocks and process them iteratively using a compression function $f$ [21]:

```
IV ---> [ f ] ---> [ f ] ---> [ f ] ---> H(M)
          ^          ^          ^
          |          |          |
         m_1        m_2        m_n
```
*Merkle-Damgård Pipeline: Iterative hashing of blocks $m_1, m_2, \dots$ through a compression function $f$ [21].*

*   **Examples**:
    *   **MD5**: 128-bit output (now completely broken; collisions found) [21].
    *   **SHA-1**: 160-bit output (now completely broken; collisions found) [21].
    *   **SHA-2**: Standardized family including **SHA-256** and **SHA-512** (highly secure; 256/512 bit outputs) [21].

#### 2. Sponge Construction
A modern alternative where a permutation function $f$ absorbs input blocks into a state variable at rate $r$ and capacity $c$, then squeezes out the hash block-by-byte [21].
*   **Examples**: **SHA-3** (based on the Keccak algorithm) [21].

---

### Collision Realities: The Tragic History of SHA-1
For years, SHA-1 was the global standard for file integrity. However, mathematically, the 160-bit key space yielded a maximum security of $2^{80}$ operations due to the **birthday paradox**. Over time, cryptographic attacks shattered this limit.

#### 1. The SHAttered Attack (23 February 2017)
Published by Google and CWI Amsterdam, this was the first real-world SHA-1 collision [22].
*   **Efficiency**: The attack was approximately **100,000 times faster** than a pure brute-force search [22].
*   **Computation**: It required $9,223,372,036,854,775,808$ ($2^{63}$) SHA-1 operations [22].
*   **Resource Equivalent**: This is equivalent to **6,500 years** of single-CPU computing, or **110 years** of single-GPU computing [22].
*   **Cost**: Cost between \$75,000 and \$120,000 on Amazon Web Services (EC2) instances at the time [22].

#### 2. The SHA-mbles Attack (07 January 2020)
Published by Gaëtan Leurent and Thomas Peyrin, this was the first **chosen-prefix collision** for SHA-1 [22].
*   In a chosen-prefix collision, the attacker can choose two arbitrary files with different headers (prefixes) and append specific data to force them to hash to the same value [22, 23]. This allows forgery of digital certificates or documents.
*   **Attack Metrics [22, 23]**:
    *   A chosen-prefix collision was computed in under **2 months** using a cluster of **900 Nvidia GTX 1060 GPUs** [22].
    *   The attack was **450,000 times faster** than a brute-force attack, requiring only $2^{61.2}$ operations [23]. This cost only **\$11,000** on commercial cloud systems [23].
    *   A standard collision was optimized to $2^{63.4}$ operations, costing **\$45,000** (equivalent to 107 years on a single GTX 1060 GPU) [23].

---

### Message Authentication Codes (MACs)
A hash function only guarantees that a file has not changed accidentally. If an attacker intercepts your transmission, they can modify the data, compute a fresh hash, and replace your hash.

To prevent this, we use a **Message Authentication Code (MAC)**, which is essentially a "hash function with a secret key" [23].
*   **Computation-Resistant**: Given multiple arbitrary pairs of messages $x$ and their corresponding codes $	ext{MAC}(x, k)$, it is computationally infeasible to forge a valid $	ext{MAC}(x', k)$ for a new message $x'$ without knowing the secret key $k$ [23].

#### The Three MAC Operations [23, 24]
1.  **KeyGen**: Generates the shared secret key [23].
2.  **Sign**: Inputs the secret key and a message, and outputs a MAC [23].
3.  **Verify**: Inputs the secret key, the message, and the MAC. It reconstructs the MAC and outputs "Accept" or "Reject" [24].

---

### Hash-Based MAC (HMAC)
One of the most common ways to construct a MAC is using a cryptographic hash function [24, 25].

#### What Can Go Wrong: Naive Chaining Pitfall
A common implementation mistake is to compute the MAC simply by hashing the key concatenated with the message:

$$	ext{MAC}_{	ext{naive}} = H(k \parallel M)$$ [24]

This is highly vulnerable to a **Length Extension Attack** on any Merkle-Damgård hash function (like SHA-256) [21, 24]. Because the final hash state is exposed, an attacker can append a block $M'$ to the message and calculate a valid hash $H(k \parallel M \parallel 	ext{padding} \parallel M')$ without ever knowing the key $k$ [24].

#### The Secure Solution: RFC 2104
To eliminate this vulnerability, **RFC 2104** defines the nested **HMAC** standard, which uses two nested passes of hashing with padded keys [24, 25]:

$$	ext{HMAC}(k, M) = H((k \oplus 	ext{opad}) \parallel H((k \oplus 	ext{ipad}) \parallel M))$$ [25]

Where:
*   $H$ is the underlying hash function (e.g., SHA-256) [24, 25].
*   $k$ is the secret key [24, 25].
*   $	ext{ipad}$ is the **inner padding** constant: repeating bytes of `0x36` [25].
*   $	ext{opad}$ is the **outer padding** constant: repeating bytes of `0x5c` [25].

---

### Key Takeaways
*   Cryptographic hashes map inputs to fixed outputs statelessly and one-way [20].
*   They must satisfy **preimage**, **second preimage**, and **collision resistance** [21].
*   **MD5** and **SHA-1** are entirely broken due to real-world collision attacks [21, 22].
*   A **MAC** secures integrity and authenticity using a key [23].
*   Naive hashing $H(k \parallel M)$ is vulnerable to **length extension attacks** [24]. Use standard **HMAC (RFC 2104)** instead [25].

---

### Quick Check
1.  **Question**: If you download a software package and the website displays a SHA-256 hash next to it, does checking the hash protect you if the website itself has been compromised by an attacker?
    *   *Answer*: No. If an attacker compromises the website, they can replace both the software package and the SHA-256 hash on the page. To ensure authenticity, you need a key-based signature or MAC.
2.  **Question**: How does the nested structure of HMAC prevent length extension attacks?
    *   *Answer*: By enclosing the inner hash output inside an outer hash pass ($H(k \oplus 	ext{opad} \parallel 	ext{inner\_hash})$), the final state of the inner hash (which contains the message) is hidden inside the outer hash, making it mathematically impossible to append blocks to the message and compute a valid signature.

---

## 6. Passwords & Key Derivation Protocols

Passwords are the weakest link in modern access control. Cryptographic engineers must handle them with extreme care, particularly during key generation and credential storage.

### Password Security & Key Derivation Functions (KDFs)
A cardinal rule of cryptography is:
> *Never use an ASCII password string directly as a cryptographic key! [26]*

Human passwords lack **entropy** (randomness). A key must be a uniformly distributed bit sequence. To bridge this gap, we use a **Key Derivation Function (KDF)** to stretch low-entropy passwords into high-entropy keys [26].

#### Credential Storage Rules [26]
*   Keys and ciphertexts should always be stored in separate locations [26].
*   Keys must never be stored in plaintext. They should be protected via:
    *   **Password-protected key stores** [26].
    *   **Hardware Security Modules (HSM)** [26].

---

### Password Storage Compliance (SAP SEC-266)
To securely encrypt private or secret keys in an enterprise environment, we use **PBKDF2** (Password-Based Key Derivation Function 2) [26].

#### Industry Standards [26]
*   **RFC 2898**: PKCS #5: Password-Based Cryptography Specification [26].
*   **SAP Product Standard Security SEC-266**: Mandates the strict use of PBKDF2 with high iteration counts and unique salts to derive storage keys [26].

These functions are intentionally designed to be computationally slow. By forcing the processor to loop thousands of times (iterations) to calculate a single key, we make it highly expensive for attackers to run offline dictionary or brute-force attacks against stolen key stores [26].

---

### Key Takeaways
*   Do not use plain ASCII strings as cryptographic keys; they lack entropy [26].
*   Use a **Key Derivation Function (KDF)** to stretch passwords [26].
*   Enterprise systems use **PBKDF2** (under RFC 2898 / SAP SEC-266) to safely secure master keys [26].
*   The final security of a derived key is fundamentally bounded by the strength of the user's password [27].

---

### Quick Check
1.  **Question**: What is the purpose of adding a random "salt" to a password before passing it to PBKDF2?
    *   *Answer*: A salt ensures that two users with the exact same password will have entirely different derived keys, preventing attackers from using precomputed lookup tables (rainbow tables) to break multiple accounts at once.

---

## 7. Asymmetric Cryptography: The RSA Cryptosystem

Symmetric cryptography is highly secure and fast, but it suffers from a major logistical flaw: **How do two parties share a symmetric key safely if they have never met?** This is solved by asymmetric cryptography.

### Motivation: Key Distribution over Untrusted Channels
If Bob wants to share a symmetric key with Alice over a public, untrusted channel, an eavesdropping attacker can intercept the key [28]. Once the key is intercepted, the attacker can decrypt all past and future communication [29].

```
              [ Public Registry ] (Contains Bob's Public Key)
                      ^
                      | (Retrieve Public Key)
                      |
Alice ---> Encrypts M using Bob's Public Key ---> Insecure Channel ---> Bob ---> Decrypts using Bob's Private Key [30]
```
*Asymmetric Encryption Concept: Anyone can encrypt using the public key, but only the holder of the mathematically paired private key can decrypt [29, 30].*

To solve this, each party has a **keypair** consisting of two mathematically dependent keys generated together [29]:
*   **Public Key**: Can be shared with anyone or uploaded to a public registry [29].
*   **Private Key**: Must be kept strictly secret [29]. If leaked, security is compromised.

---

### The RSA Trapdoor: Integer Factorization
Created by Ron Rivest, Adi Shamir, and Leonard Adleman, the **RSA Cryptosystem** is the most famous asymmetric standard [30]. It relies on a mathematical **trapdoor function**: a function that is easy to compute in one direction but extremely difficult to reverse unless you possess a special piece of information (the "trapdoor").

#### The Factorization Assumption
*   Given two massive prime numbers $p$ and $q$, it is trivial to multiply them to calculate $N = p \cdot q$ [30].
*   However, if you are only given $N$, it is computationally infeasible to find $p$ and $q$ [31, 33].
*   To remain secure today, $p$ and $q$ should be at least 1024 bits each, making $N$ a **2048-bit** or **3000-bit** number (having over 900 decimal digits) [31, 33].

```
p, q (Secret Primes) ---> EASY MULTIPLICATION ---> N = p * q (Public Modulus)
p, q <--- EXTREMELY HARD FACTORIZATION <--- N (Public Modulus) [31, 33]
```

> **Deep Dive: Shor's Algorithm & Quantum Threat**
> Cryptographers believe that factoring large numbers is a hard mathematical problem for classical computers [33]. The best-known classical algorithms (like the General Number Field Sieve) require exponential time.
> However, there is a known efficient algorithm called **Shor's Algorithm** that can solve both the integer factorization problem and the discrete logarithm problem in polynomial time [33, 49]. 
> Shor's algorithm requires an **ideal, fault-tolerant Quantum Computer** to operate [33, 49]. Since such machines are not yet available, RSA remains secure for now, but the industry is actively researching post-quantum alternatives.

---

### RSA Key Generation & Algorithms
To generate an RSA keypair, follow these mathematical steps [34, 35]:

1.  **Select Primes**: Pick two large, random prime numbers $p$ and $q$ (at least 1024 bits each) [34]. Keep them secret.
2.  **Calculate Modulus ($N$)**:
    
    $$N = p \cdot q$$ [34]
    
3.  **Calculate Euler's Totient ($\phi(N)$)**:
    
    $$\phi(N) = (p - 1) \cdot (q - 1)$$ [34]
    
    *Note: $\phi(N)$ is easy to compute if $p$ and $q$ are known, but extremely difficult to compute given only $N$ [33].*
4.  **Choose Public Exponent ($e$)**: Select $e$ such that:
    *   $1 < e < \phi(N)$ [34]
    *   $\gcd(e, \phi(N)) = 1$ (meaning $e$ and $\phi(N)$ are relatively prime) [34].
    *   *In modern systems, $e$ is almost always fixed to **65537** ($2^{16} + 1$) because it makes encryption calculations highly efficient [34].*
5.  **Calculate Private Exponent ($d$)**: Solve for $d$ such that:
    
    $$e \cdot d \equiv 1 \pmod{\phi(N)}$$ [34]
    
    This modular multiplicative inverse is computed using the Extended Euclidean Algorithm [34].

*   **Public Key**: $(e, N)$ [35]
*   **Private Key**: $(d, N)$ [35]

---

### RSA Encryption & Decryption
With the keypair generated, we can encrypt and decrypt messages ($M \in \mathbb{Z}_N$) [35, 36]:

#### Encryption Formula
Given public key $(e, N)$ and plaintext $M$, the ciphertext $C$ is [35]:

$$C = M^e \pmod N$$ [35]

#### Decryption Formula
Given private key $(d, N)$ and ciphertext $C$, the decrypted plaintext $M$ is [35]:

$$M = C^d \pmod N$$ [35]

#### Mathematical Proof of Correctness
Why does this work? Since $e \cdot d \equiv 1 \pmod{\phi(N)}$, we can write $e \cdot d = k \cdot \phi(N) + 1$ for some integer $k$ [34, 35]. By Euler's Theorem [35]:

$$C^d \pmod N \equiv (M^e)^d \equiv M^{e \cdot d} \equiv M^{k \cdot \phi(N) + 1} \equiv (M^{\phi(N)})^k \cdot M^1 \equiv (1)^k \cdot M \equiv M \pmod N$$ [35]

---

### Complete Step-by-Step Numerical Example
Let us run a complete, mathematically exact worked example using small primes for educational validation [36].

#### Step 1: Pick Primes
*   $P = 23$ [36]
*   $Q = 31$ [36]

#### Step 2: Compute Modulus $N$
*   $N = 23 \cdot 31 = \mathbf{713}$ [36]

#### Step 3: Compute Euler's Totient $\phi(N)$
*   $\phi(N) = (23 - 1) \cdot (31 - 1) = 22 \cdot 30 = \mathbf{660}$ [36]

#### Step 4: Pick Public Exponent $e$
*   We choose $e = \mathbf{127}$ [36]. 
    *   *Check: $\gcd(127, 660) = 1$ (127 is prime, and 660 is not divisible by 127, so they are relatively prime).*

#### Step 5: Compute Private Exponent $d$
We must solve for $d$ such that $127 \cdot d \equiv 1 \pmod{660}$ [34, 36].
Using the Extended Euclidean Algorithm:
1.  $660 = 5 \cdot 127 + 25$
2.  $127 = 5 \cdot 25 + 2$
3.  $25 = 12 \cdot 2 + 1$
Reversing the steps:
*   $1 = 25 - 12 \cdot 2$
*   $1 = 25 - 12 \cdot (127 - 5 \cdot 25) = 61 \cdot 25 - 12 \cdot 127$
*   $1 = 61 \cdot (660 - 5 \cdot 127) - 12 \cdot 127 = 61 \cdot 660 - 317 \cdot 127$
*   Therefore, $-317 \equiv 343 \pmod{660}$.
*   The private exponent is $d = \mathbf{343}$ [36].
*   *Verification: $127 \cdot 343 = 43561 	o 43561 \pmod{660} = 1$. Correct.*

#### Keypair Result
*   **Public Key**: $(e=127, N=713)$ [35, 36]
*   **Private Key**: $(d=343, N=713)$ [35, 36]

#### Step 6: Encryption of message $m = 41$
Let us encrypt plaintext message $m = 41$ [36]:

$$C = m^e \pmod N = 41^{127} \pmod{713}$$ [35, 36]

Using modular exponentiation:
*   $41^{127} \pmod{713} = \mathbf{330}$
*   **Ciphertext $C = 330$**

#### Step 7: Decryption of ciphertext $C = 330$
Let us recover the original plaintext using the private key [36]:

$$M = C^d \pmod N = 330^{343} \pmod{713}$$ [35, 36]

*   $330^{343} \pmod{713} = \mathbf{41}$
*   **Decrypted Plaintext $M = 41$**

The decrypted value matches the original message $m = 41$ exactly [36].

---

### Attacks against Plain RSA & Countermeasures
Plain RSA (without padding) suffers from several catastrophic mathematical weaknesses:

#### 1. Deterministic Encryption (No Semantic Security)
Because encryption is deterministic, encrypting the same message twice always yields the same ciphertext [37]. An attacker can guess possible plaintext messages, encrypt them using your public key, and compare them to the captured ciphertext [37].

#### 2. Short Message Attack (Size Constraint Failure)
If the plaintext $M$ is short and the exponent $e$ is small, the value $M^e$ may be smaller than the modulus $N$ [37].
*   **Example**: Let $M = 3$, $e = 13$, and $N = 3,000,009$ [37].
*   The encryption calculation is $3^{13} \pmod{3,000,009} = 1,594,323 \pmod{3,000,009} = 1,594,323$ [37].
*   Because the modulus had no effect ($M^e < N$), the attacker can easily decrypt the message by calculating the standard 13th root of the ciphertext over the integers: $\sqrt[13]{1,594,323} = 3$ [37, 38].
*   **Countermeasure**: Messages must be padded so that they are sufficiently long and the modulus always takes effect [38].

#### 3. Chinese Remainder Theorem Multi-Recipient Attack
If the same plaintext message $M$ is encrypted and sent to $e$ or more recipients who share the same public exponent $e$ (but have different moduli $N_i$), an attacker can intercept the ciphertexts and reconstruct the exact message $M$ using the **Chinese Remainder Theorem (CRT)** without factoring any of the moduli [38].

#### 4. Shared Modulus / Insider Attacks
If an organization generates a common modulus $N$ for all employees and only varies the key exponents $e_i$ and $d_i$ for each user, any employee can use their own key pair to factor the common modulus $N$, allowing them to decrypt the messages of every other employee [37].
*   **Countermeasure**: Never reuse a modulus $N$; always generate unique primes $p$ and $q$ for every keypair [37].

#### 5. Common Prime Factors
If prime generation is not truly random, different key pairs might accidentally share a prime factor. Lenstra et al. (2012) collected public keys from the web and discovered that "two out of every one thousand RSA moduli collected offer no security" because they shared prime factors with other keys, allowing them to be factored instantly using the Greatest Common Divisor ($\gcd$) algorithm [37].

#### 6. Totient Leakage
If the totient $\phi(N)$ is leaked, an attacker can use a simple quadratic equation (Vieta's formulas) to solve for the primes $p$ and $q$ [37]. Therefore, $\phi(N)$ must be kept strictly secret [37].

#### 7. Side-Channel Attacks
Attackers can analyze physical properties of the hardware executing the math (e.g., measuring the execution time of the **Square-and-Multiply** exponentiation algorithm) to extract private keys [36].
*   **Countermeasure**: Implementations must use constant-time algorithms and blinding. Never write your own RSA implementation—always use approved, vetted cryptographic libraries [36, 37].

---

### Optimal Asymmetric Encryption Padding (OAEP)
To eliminate all the vulnerabilities of plain RSA, we must apply an "all-or-nothing" randomized padding transformation to the plaintext before passing it to the RSA encryption engine [38]. The global industry standard is **OAEP** [38].

```
Plaintext Message (m) ---> [ Pad with k1 Zeros ] -------------------> XOR ---> Padded Block (X) ---> XOR ---> Final Block ---> RSA Encrypt
                                                                      ^                             ^
                                                                      |                             |
                       Random Seed (r) ---> [ Hash Function G ] -------                             |
                                                                                                    |
                                            [ Hash Function H ] ------------------------------------|
```
*OAEP Processing Pipeline: Combining a message, a random seed $r$, and hash functions $G$ and $H$ into a randomized padded block before RSA encryption [39, 40].*

#### Step-by-Step OAEP Algorithm [39, 40]
1.  **Padding**: Pad the message $m$ with $k_1$ zeros to format it to a fixed length ($m \parallel 00\dots0$) [39].
2.  **Generate Randomness**: Choose a cryptographically secure random seed $r$ of $k_0$ bits [39].
3.  **First Hash Pass**: Compute the hash $G$ of the random seed $r$ [39].
4.  **Mask Message**: Compute the masked message $X = (m \parallel 00\dots0) \oplus G(r)$ [39].
5.  **Second Hash Pass**: Compute the hash $H$ of $X$ [40].
6.  **Mask Seed**: Compute the masked seed $Y = r \oplus H(X)$ [40].
7.  The final result passed to the RSA encryption engine is the concatenated block $X \parallel Y$ [39].

This structure ensures that the input is always long, randomized, and highly secure against mathematical analysis.

---

### Key Takeaways
*   Asymmetric encryption solves the key distribution problem using a paired public key (unencrypted/public) and private key (strictly secret) [29, 30].
*   **RSA** relies on the computational difficulty of factoring the product of two massive primes ($N = p \cdot q$) [30, 31, 33].
*   **Plain RSA is highly vulnerable** to deterministic guessing, short message root attacks, and side-channel timing attacks [36, 37, 38].
*   **OAEP** is a randomized, two-round asymmetric padding scheme that must always be used with RSA to guarantee security [38, 39, 40].

---

### Quick Check
1.  **Question**: In your own words, why is knowing $\phi(N)$ equivalent to breaking RSA?
    *   *Answer*: Knowing $\phi(N)$ allows an attacker to compute $d \equiv e^{-1} \pmod{\phi(N)}$ instantly using the Extended Euclidean Algorithm, rendering the private key fully compromised [34].
2.  **Question**: Can you encrypt a file that is 5 Gigabytes in size directly using RSA?
    *   *Answer*: No. RSA can only encrypt inputs smaller than the modulus size $N$ (e.g., up to 2048 bits) [36]. To encrypt large files, we must use a **Hybrid Encryption** architecture.

---

## 8. Digital Signatures & Hybrid Systems

By combining symmetric and asymmetric cryptography, we can construct protocols that are both highly secure and performant.

### Mechanics of Digital Signatures
A **digital signature** acts as a cryptographically verifiable proof of authenticity and integrity [43]. It guarantees that a document was authored by the holder of the private key and has not been modified in transit [44, 45].

#### 1. Signature Generation (Sender Side) [42]
1.  The document (e.g., an email) can vary in size. Directly signing large documents with RSA is computationally slow and restricted by size limits [42].
2.  Therefore, the sender first hashes the document using a strong hash function like **SHA-512** to generate a fixed 512-bit digest [42].
3.  The sender encrypts this digest using their private key $(d, N)$ [42]:
    
    $$S \equiv 	ext{hash}^d \pmod N$$ [42]
    
4.  This signature $S$ is attached to the document [43].

#### 2. Signature Validation (Recipient Side) [43, 44]
1.  The recipient receives the document and the signature $S$ [43].
2.  The recipient computes a fresh hash of the received document using **SHA-512** [43].
3.  The recipient decrypts the signature $S$ using the sender's public key $(e, N)$ [44]:
    
    $$	ext{hash}' \equiv S^e \pmod N$$ [44]
    
4.  The recipient compares the fresh hash with the decrypted hash [45]. If they match:
    *   The document was signed with the private key paired with the sender's public key (proving **authenticity**) [44].
    *   The document has not been altered (proving **integrity**) [44, 45].

---

### The Logical Distinction: Signing vs Decryption
While the mathematical formula for signing ($X^d \pmod N$) is identical to decryption, they are **logically completely different operations** [45]:
*   Signing is applied to a public plaintext hash, not to a private ciphertext [45].
*   The output of signing is a public signature, not a private plaintext [45].
*   Confusing the two in software design can lead to catastrophic vulnerabilities where an attacker tricks a system into "signing" a piece of data that is actually a decrypted ciphertext, leaking secret keys.

---

### Hybrid Encryption Architecture
To protect massive payloads (like a 5GB database), modern networks use **Hybrid Encryption**, combining the speed of symmetric encryption with the key sharing ease of asymmetric encryption [40].

```
ALICE                                                                      BOB
  |                                                                         |
  | --- 1. Encrypt Symmetric Session Key K using Bob's Public Key --->     | [ Bob decrypts using Private Key ]
  |                                                                         |
  | <========== 2. Encrypt all Payload data using Symmetric Key K =========> | [ High-Speed Secure Session ]
```
*Hybrid Encryption Handshake: Solving key distribution with asymmetric keys and payload performance with symmetric keys [40].*

#### The Hybrid Process [40]
1.  Bob publishes his public key [29].
2.  Alice wants to send a large file to Bob. She generates a highly secure, temporary **symmetric session key** $K$ [40].
3.  Alice encrypts the large file using the symmetric key $K$ (highly efficient) [40].
4.  Alice encrypts the small symmetric key $K$ using Bob's asymmetric public key [40].
5.  Alice sends the encrypted file and the encrypted key to Bob [40].
6.  Bob uses his private key to decrypt the symmetric key $K$ [40].
7.  Bob uses the symmetric key $K$ to decrypt the large file [40].

---

### Key Takeaways
*   **Digital signatures** provide authenticity and integrity by hashing a document and encrypting the digest with a private key [42, 43, 44].
*   Signing and decryption use the same math but are logically distinct [45].
*   **Hybrid Encryption** uses asymmetric keys to securely share a symmetric session key, and then uses that symmetric key to encrypt the actual payload [40].

---

### Quick Check
1.  **Question**: If Alice's private key is stolen, what happens to the validity of her past digital signatures?
    *   *Answer*: They can no longer be trusted. An attacker possessing her private key can forge any signature they want. Alice must immediately revoke her public key.

---

## 9. Key Exchange & Perfect Forward Secrecy

Even with hybrid encryption, a critical vulnerability remains: **What happens if an organization's central master private key is compromised in the future?**

### Perfect Forward Secrecy (PFS)
Imagine an attacker tapping into a network backbone. They cannot decrypt the hybrid traffic, but they record and store all encrypted sessions [47, 48].
*   **The Trap**: If the attacker eventually steals or compromises the server's long-term private key years later, they can use it to decrypt the captured symmetric session keys, allowing them to retroactively decrypt **every past session** they recorded [48].
*   **The Solution**: **Perfect Forward Secrecy (PFS)** [47, 53]. PFS is a security property ensuring that even if a server's long-term private key is compromised in the future, all past session keys remain completely secure and cannot be decrypted [47, 48, 53].

---

### Diffie-Hellman Key Exchange (DH)
The primary mechanism to achieve PFS is the **Diffie-Hellman (DH) protocol**, the world's first public key agreement system [49]. It allows two parties to negotiate a strong shared symmetric key without ever transmitting the key itself [49].

#### The Discrete Logarithm Trapdoor
DH relies on the mathematical hardness of the **Discrete Logarithm Problem (DLP)** [48].
*   Given $g$, $x$, and prime modulus $p$, it is computationally easy to compute:
    
    $$a \equiv g^x \pmod p$$ [48, 51]
    
*   However, given only $a$, $g$, and $p$, it is computationally infeasible to solve for the exponent $x$ [48, 51]:
    
    $$x \equiv \log_g a \pmod p$$ [48]
    
*   To remain secure, the prime modulus $p$ must be at least **2048 bits** [49].

> **Deep Dive: Cyclic Groups & Generators**
> DH operates over a mathematical structure called a **Cyclic Group** under modular arithmetic [50]. 
> Think of modular arithmetic as a clock: on a 12-hour clock, $14$ is equivalent to $2$ o'clock, and $33 \pmod{12}$ is $9$ o'clock [50]. 
> For a prime modulus $p$, there exists an element $g$ (called a **generator**) whose sequential powers generate every single integer from $1$ to $p-1$ in a scrambled, pseudo-random order [50, 51]:
> 
> $$\{g^i \pmod p \mid 0 \le i \le p-1\} = \{1, 2, \dots, p-1\}$$ [51]
> 
> Plotting $g^i \pmod p$ reveals no predictable wave pattern; it behaves like chaotic mathematical noise, forming the foundation of the discrete logarithm hardness [51].

---

#### The Diffie-Hellman Handshake Protocol
Alice and Bob agree publicly on a prime $p$ and generator $g$ [51].

```
ALICE                                                              BOB
Secret: x                                                          Secret: y
Compute: A = g^x mod p                                             Compute: B = g^y mod p

  | ------------------------ Send A -----------------------------> |
  | <----------------------- Send B ------------------------------ |

Compute Session Key:                                               Compute Session Key:
S = B^x mod p = (g^y)^x = g^(xy)                                   S = A^y mod p = (g^x)^y = g^(xy) [51, 52]
```

1.  Alice selects a secret random integer $x \in [1, p-1]$ [51].
2.  Alice computes her public value:
    
    $$A \equiv g^x \pmod p$$ [51]
    
3.  Bob selects a secret random integer $y \in [1, p-1]$ [51].
4.  Bob computes his public value:
    
    $$B \equiv g^y \pmod p$$ [51]
    
5.  Alice and Bob exchange $A$ and $B$ over the public channel [51].
6.  Alice computes the shared secret:
    
    $$S \equiv B^x \pmod p \equiv (g^y)^x \equiv g^{xy} \pmod p$$ [51]
    
7.  Bob computes the shared secret:
    
    $$S \equiv A^y \pmod p \equiv (g^x)^y \equiv g^{xy} \pmod p$$ [51, 52]
    
Both derive the identical shared secret $g^{xy} \pmod p$ [51, 52]. An eavesdropper only intercepts $g$, $p$, $g^x$, and $g^y$, but cannot calculate $g^{xy}$ without solving the Discrete Logarithm Problem [48]. Once the session terminates, $x$, $y$, and the session key are permanently discarded, achieving PFS [49].

---

### DH Numerical Worked Example
Let us calculate a complete toy example using small numbers for educational validation [52].

#### Public Parameters
*   Modulus $p = 23$ [52]
*   Generator $g = 5$ [52]

#### Alice's Secret & Calculation
*   Alice picks secret exponent: $x = 12$ [52].
*   Alice computes public value:
    
    $$A = g^x \pmod p = 5^{12} \pmod{23}$$ [51, 52]
    
    *Calculation: $5^{12} \pmod{23} = \mathbf{18}$. Alice sends $18$ to Bob.*

#### Bob's Secret & Calculation
*   Bob picks secret exponent: $y = 19$ [52].
*   Bob computes public value:
    
    $$B = g^y \pmod p = 5^{19} \pmod{23}$$ [51, 52]
    
    *Calculation: $5^{19} \pmod{23} = \mathbf{7}$. Bob sends $7$ to Alice.*

#### Shared Secret Derivation
*   **Alice's computation**:
    
    $$S = B^x \pmod p = 7^{12} \pmod{23} = \mathbf{16}$$ [51, 52]
    
*   **Bob's computation**:
    
    $$S = A^y \pmod p = 18^{19} \pmod{23} = \mathbf{16}$$ [51, 52]
    
Both Alice and Bob successfully derive the identical shared secret: **16** [52].

---

### Man-in-the-Middle Attack & Signed DH
Standard Diffie-Hellman is completely **unauthenticated**. If Alice and Bob exchange keys, an attacker (Eve) sitting in the middle of the network can intercept their traffic and perform a **Man-in-the-Middle (MitM) attack** [52].

```
Alice (g^x) --------> Intercepted by Eve (g^z) --------> Bob (g^y)
Alice <------- Intercepted by Eve (g^z) <------- Bob
```

1.  Eve intercepts Alice's public value $g^x$ and sends Alice her own public value $g^z$ [52].
2.  Eve intercepts Bob's public value $g^y$ and sends Bob her public value $g^z$ [52].
3.  Alice and Eve negotiate shared secret $g^{xz}$ [52].
4.  Bob and Eve negotiate shared secret $g^{yz}$ [52].
5.  When Alice sends a message, Eve decrypts it using $g^{xz}$, reads or modifies it, encrypts it using $g^{yz}$, and forwards it to Bob [52]. Alice and Bob believe they are communicating securely, but Eve controls the session [52].

#### The Countermeasure: Signed Diffie-Hellman
To prevent MitM attacks, **digital signatures are crucial!** [52]. Alice and Bob must sign their public DH values ($g^x$ and $g^y$) using their long-term asymmetric private keys [53]. This allows them to verify each other's identities before negotiating the shared session key [53].

---

### Key Takeaways
*   **Perfect Forward Secrecy (PFS)** ensures past sessions remain secure even if long-term server keys are compromised in the future [47, 48, 53].
*   **Diffie-Hellman (DH)** relies on the hardness of the **Discrete Logarithm Problem** [48].
*   DH allows key agreement but does not provide authentication on its own, making it vulnerable to **Man-in-the-Middle attacks** [51, 52].
*   **Signed Diffie-Hellman** combines digital signatures with DH to enforce authentication and security [53].

---

### Quick Check
1.  **Question**: Why can't Eve calculate $g^{xy}$ simply by multiplying $g^x$ and $g^y$?
    *   *Answer*: Multiplying $g^x \cdot g^y$ yields $g^{x+y}$, which is mathematically completely different from the exponentiation $g^{xy}$. To find $g^{xy}$ from $g^x$ and $g^y$, Eve must solve for the exponents $x$ or $y$ using the discrete logarithm, which is computationally infeasible.

---

## 10. Modern Horizons: Elliptic Curve Cryptography (ECC) & Security Equivalences

As key sizes for RSA and traditional Diffie-Hellman expand to massive sizes (such as 15,360 bits) to maintain long-term security, computer systems require a more efficient algebraic framework. This is provided by Elliptic Curve Cryptography.

### Introduction to Elliptic Curves
**Elliptic Curve Cryptography (ECC)** is an approach to public-key cryptography based on the algebraic structure of elliptic curves over finite fields [53].

#### The Elliptic Curve Equation
The algebraic equation defining an elliptic curve is [53]:

$$y^2 = x^3 + ax + b$$

Where:
*   $a, b$ are coefficients defining the curve shape [54].
*   $x, y$ are coordinates on the curve [53].

```
                     y
                     |      * (P)
                     |     /
                     |    /  
                     |   /    
    -----------------+--* (Q)----------------- x
                     |                        |                         |                          |      * (R = P+Q, then reflected)
```
*Continuous Elliptic Curve Point Addition: A line passing through points $P$ and $Q$ intersects the symmetric curve at a third point, which is then reflected across the horizontal x-axis to define the point $P+Q$ [53].*

#### Point Addition & Group Law
To use elliptic curves for cryptography, we define a custom group operation called **Point Addition** ($P + Q = R$) [53]. 
*   **Continuous Field ($\mathbb{R}$)**: Geometrically, a line intersecting any two points $P$ and $Q$ on the curve will intersect the curve at a third point. We reflect this third point across the x-axis to find the sum point $R$ [53].
*   **Finite Field ($\mathbb{Z}_p$)**: In cryptography, we evaluate this equation modulo a prime $p$ [53, 54]. Geometrically, the curve is no longer a continuous line; it appears as a pseudo-random scattering of points on a grid [53]. However, the same algebraic laws for point addition hold perfectly.

---

### The Elliptic Curve Discrete Logarithm Problem (ECDLP)
The security of ECC relies on the hardness of the **Elliptic Curve Discrete Logarithm Problem (ECDLP)** [54].

#### Mathematical Formulation
Given an elliptic curve $E$, a public generator point $G$, and a public point $T$, find the integer $d$ such that [54]:

$$d \cdot G = T$$ [54]

Where:
*   $d \cdot G$ represents adding the point $G$ to itself $d$ times ($G + G + \dots + G = T$) [54].
*   $d$ is the private key (a randomly chosen integer) [54].
*   $T$ is the public key (the resulting point on the curve) [54].

While computing $d \cdot G$ (point multiplication) is extremely fast, reversing the operation to find $d$ from $T$ and $G$ is computationally infeasible [54].

#### Why ECC is Efficient
Because there is no known classical mathematical shortcut to solve the ECDLP (unlike integer factoring, which has advanced sieve methods), we can achieve equivalent security margins with significantly shorter key lengths [53, 54].
*   This makes ECC highly advantageous for resource-constrained hardware such as **RFID tags**, **Smart Cards**, and **Smart Meters** [54].

---

### Modern Keylength Security Equivalences
To assist systems architects in choosing secure parameters, ECRYPT-CSA publishes keylength equivalences mapping different cryptographic structures to their relative security strengths [55].

| Protection Level & Guidance | Symmetric Key Size (Bits) | Factoring Modulus RSA Size (Bits) | Discrete Logarithm Key Size (Bits) | Discrete Log Group Size (Bits) | Elliptic Curve Key Size (Bits) | Hash Output Size (Bits) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Legacy Standard Level**<br>*Should not be used in new systems* [55] | 80 | 1024 | 160 | 1024 | 160 | 160 [55] |
| **Near-Term Protection**<br>*Security for at least ten years (2018-2028)* [55] | 128 | 3072 | 256 | 3072 | 256 | 256 [55] |
| **Long-Term Protection**<br>*Security for thirty to fifty years (2018-2068)* [55] | 256 | 15360 | 512 | 15360 | 512 | 512 [55] |

Looking at the table, to achieve long-term security, a classical RSA key must be **15,360 bits** in size, which is computationally expensive to process [55]. In contrast, an Elliptic Curve key achieves the exact same security margin with only **512 bits**, demonstrating the massive efficiency advantages of ECC [55].

---

### Key Takeaways
*   **ECC** uses point addition and multiplication over elliptic curves defined modulo a prime $p$ [53, 54].
*   The security of ECC rests on the hardness of the **ECDLP** [54].
*   Because ECC is highly resistant to cryptanalysis, it achieves equivalent security margins with **dramatically shorter key sizes** than RSA [53, 54, 55].
*   ECC is ideal for constrained devices like Smart Cards, RFID tags, and IoT meters [54].

---

### Quick Check
1.  **Question**: Based on the ECRYPT-CSA table, if a system currently uses a 3072-bit RSA key for near-term protection, what size Elliptic Curve key would provide the same security strength?
    *   *Answer*: A **256-bit** Elliptic Curve key provides equivalent near-term security strength, but with a fraction of the computational overhead [55].
2.  **Question**: What is the private key in an ECC cryptosystem?
    *   *Answer*: The private key is a randomly chosen secret integer $d$ [54]. The corresponding public key is the curve point $T$ resulting from multiplying the generator point $G$ by that integer ($T = d \cdot G$) [54].
