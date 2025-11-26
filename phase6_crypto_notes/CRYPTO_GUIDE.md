# Phase 6 Guide - Basic Cryptography

## What This Phase Is About

Understanding the cryptographic primitives behind Bitcoin and Lightning Network well enough to speak accurately about them in policy contexts.

**This is NOT a math-heavy phase.** You need conceptual understanding, not cryptographic proofs.

---

## 🎓 Prerequisites & Learning Resources

### Python Skills Needed: **Minimal**
- Optional: Basic Python to run hash/signature demos
- Most of this phase is conceptual reading and note-taking

### Math Background: **None Required**
You don't need to understand the math behind elliptic curves. You need to understand:
- What a hash does
- What a signature proves
- How these enable Bitcoin's security model

---

## 📚 Core Learning Resources

### Bitcoin Cryptography Basics:

**Best Starting Points:**
- **[Bitcoin Wiki: Technical Background](https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses)** - How addresses work
- **[Bitcoin Wiki: Hash Functions](https://en.bitcoin.it/wiki/Hash)** - What hashing does in Bitcoin
- **[Mastering Bitcoin Chapter 4](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch04.asciidoc)** - Keys, addresses, wallets (free)

📺 **YouTube:**
- **[3Blue1Brown: 256-bit Security](https://www.youtube.com/watch?v=S9JGmA5_unY)** - Beautiful visual explanation
- **Anders Brownworth: Blockchain Demo** - Search for his hash visualization tool
- **Andreas Antonopoulos: Keys & Addresses** - Search his channel

### Hashing:
- **[SHA-256 Visualizer](https://andersbrownworth.com/blockchain/hash)** - Play with hashing interactively
- **Concept:** One-way function, collision resistance, deterministic

### Digital Signatures (ECDSA):
- **[Bitcoin Wiki: ECDSA](https://en.bitcoin.it/wiki/Elliptic_Curve_Digital_Signature_Algorithm)** - Overview
- **Key Concepts:**
  - Private key = secret number
  - Public key = derived from private key (one-way)
  - Signature = proves you have private key without revealing it
  - Verification = anyone can check signature is valid

### Taproot & Schnorr:
- **[Bitcoin Optech: Taproot](https://bitcoinops.org/en/topics/taproot/)** - Policy-relevant explainer
- **[BIP 340/341/342](https://github.com/bitcoin/bips)** - Technical specs (skim only)
- **Focus for policy work:**
  - Privacy improvements (makes complex scripts look like simple payments)
  - Signature aggregation (multiple signatures → one signature)
  - Why this matters for Lightning Network and multisig

📺 **YouTube:**
- **[Bitcoin Optech: Taproot Workshop](https://bitcoinops.org/en/schorr-taproot-workshop/)** - Videos available
- Search: "Taproot explained" - multiple good explainers

---

## 🎯 What "Good Enough" Looks Like

You don't need to be a cryptographer. You need to be able to:

✅ **Explain to a staffer:**
- "What's the difference between hashing and encryption?"
- "How do Bitcoin signatures work?"
- "What did Taproot improve?"

✅ **Write accurately:**
- No confusing "encrypted" with "hashed"
- No claiming Bitcoin uses "blockchain encryption" (it doesn't)
- Understand what "cryptographic security" actually means

✅ **Understand policy implications:**
- Why Bitcoin addresses are pseudonymous, not anonymous
- How privacy tech (Taproot, CoinJoin) works conceptually
- Why "banning encryption" wouldn't break Bitcoin

---

## 📝 Suggested Workflow

This phase runs **all year** in parallel with others:

1. **Week 1-2:** Read about hashing (play with SHA-256 visualizer)
2. **Week 3-4:** Read about public/private keys and ECDSA
3. **Week 5-6:** Taproot and Schnorr (focus on "why it matters")
4. **Ongoing:** Take notes in the `.md` files in this folder
5. **Optional:** Write a simple Python script that hashes text and verifies signatures

### Time Commitment:
- **~30-60 minutes per week** throughout the year
- Reading + note-taking, not coding
- Sprinkle it in during downtime

---

## 🔗 Optional: Hands-On Python Demo

If you want to actually run cryptographic functions (optional but fun):

```python
import hashlib

# Hash example
text = "Hello Bitcoin"
hash_result = hashlib.sha256(text.encode()).hexdigest()
print(f"SHA-256: {hash_result}")

# For signatures, use a library like 'ecdsa' or 'bitcoin' package
```

**Resources:**
- **[Python hashlib docs](https://docs.python.org/3/library/hashlib.html)**
- **[python-bitcoinlib](https://github.com/petertodd/python-bitcoinlib)** - For Bitcoin-specific crypto

---

## 📁 Note on Repository Structure

**All work stays in this folder** (`/phase6_crypto_notes/`).

This phase doesn't require a "personal project" - just complete notes in the three `.md` files:
- `hashing_vs_encryption.md`
- `ecdsa_basics.md`
- `taproot_notes.md`

Fill these in as you learn throughout the year.

