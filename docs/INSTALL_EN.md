## Install and Use

---

### Without installing

```sh
# Repository cloning.
git clone https://github.com/stpatriarch/onekey.git && cd onekey

# Usage: This method allow you ran it without installig as a script.
python3 src/onekey/core/core.py 

```

### Installing

```sh
# Repository cloning.
git clone https://github.com/stpatriarch/onekey.git && cd onekey

# Virtula environment create a activation.
python3 -m venv venv && source venv/bin/activate

# installing.
pip install .
```

### Usage

```sh
# First method: It will require entering the key first, then the host.
# The generated password will be copied to the clipboard.
onekey

# Second method: You can enter both the key and the host at once.
# The generated password will be copied to the clipboard.
onekey -k your_key_here -h your_host_here

# New secure key generation if you don’t have one. Works in two modes.

# Simple random generation. Cannot be recovered.
onekey --keygen 

# Generation from your chosen phrase. Can be recovered.
onekey --keygen secret_word 

```
