# Stockholm Project

This project is a simulation of ransomware behavior for educational purposes only. It is designed to encrypt and decrypt files in a specific folder, mimicking the behavior of the WannaCry ransomware.

**WARNING: This program is for educational purposes only. Never use this or similar programs for malicious purposes.**

## Features

- Encrypts files in the `~/infection` folder
- Only affects files with extensions targeted by WannaCry
- Adds `.ft` extension to encrypted files
- Decrypts files when provided with the correct key
- Silent mode option

## Requirements

- Linux environment (tested on [your distribution])
- [Programming language used, e.g., Python 3.8+]
- [Any additional libraries, e.g., cryptography]

## Installation

1. Clone this repository:
   ```
   git clone [repository URL]
   cd stockholm
   ```

2. Install dependencies:
   ```
   [Command to install dependencies, e.g., pip install -r requirements.txt]
   ```

## Usage

Use the Makefile to compile and run the program:

```
make
./stockholm [options]
```

Options:
- `-h, --help`: Display help message
- `-v, --version`: Show program version
- `-r KEY, --reverse KEY`: Decrypt files using the provided key
- `-s, --silent`: Run in silent mode (no output)

## Examples

1. Encrypt files:
   ```
   ./stockholm
   ```

2. Decrypt files:
   ```
   ./stockholm -r YOUR_ENCRYPTION_KEY
   ```

3. Run in silent mode:
   ```
   ./stockholm -s
   ```

## Security Note

This program uses [encryption algorithm] for file encryption. The encryption key is [how the key is generated/stored].

## Disclaimer

This project is for educational purposes only. It is designed to demonstrate the mechanics of ransomware-like behavior in a controlled environment. Never use this or similar programs for malicious purposes or on systems you do not own or have explicit permission to test.