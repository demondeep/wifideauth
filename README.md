# Wi-Fi Deauth: A Simple Tool for Wi-Fi Deauthentication Attacks ⚡️

![Wi-Fi Deauth](https://img.shields.io/badge/Wi-Fi%20Deauth-attack-orange)

Welcome to the **Wi-Fi Deauth** repository! This project provides a simple and effective tool for executing Wi-Fi deauthentication attacks. Whether you are a network security enthusiast or a professional, this tool can help you understand the vulnerabilities in Wi-Fi networks.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Wi-Fi networks are an integral part of our daily lives. However, they can also be vulnerable to attacks. A deauthentication attack forces a device to disconnect from a Wi-Fi network, making it a useful tool for testing network security. This repository aims to provide a straightforward way to perform such attacks.

For the latest releases, please visit [here](https://github.com/demondeep/wifideauth/releases). You can download the necessary files and execute them to get started.

## Features

- **Simple Interface**: Easy to use with minimal setup.
- **Cross-Platform**: Works on various operating systems.
- **Lightweight**: Small footprint for quick execution.
- **Real-Time Monitoring**: Observe network behavior during the attack.
- **Open Source**: Free to use and modify as per your needs.

## Installation

To get started with **Wi-Fi Deauth**, follow these simple steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/demondeep/wifideauth.git
   cd wifideauth
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. You can install the required libraries using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Executable**:
   For the latest version, check the [Releases section](https://github.com/demondeep/wifideauth/releases). Download the appropriate file and execute it.

## Usage

Once installed, you can use the tool with a simple command. Here’s a basic example:

```bash
python wifideauth.py --target <TARGET_MAC> --interface <YOUR_INTERFACE>
```

Replace `<TARGET_MAC>` with the MAC address of the device you want to disconnect, and `<YOUR_INTERFACE>` with your network interface name.

### Command Options

- `--target`: Specify the MAC address of the target device.
- `--interface`: Specify the network interface to use for the attack.
- `--help`: Display help information.

## Examples

### Example 1: Basic Deauth Attack

To disconnect a device with MAC address `00:11:22:33:44:55` using interface `wlan0`, run:

```bash
python wifideauth.py --target 00:11:22:33:44:55 --interface wlan0
```

### Example 2: Monitor Mode

Ensure your wireless card is in monitor mode for effective results. Use the following command:

```bash
sudo airmon-ng start wlan0
```

Then run the deauth command as shown above.

## Contributing

We welcome contributions! If you have suggestions or improvements, please fork the repository and submit a pull request. You can also open issues for any bugs or feature requests.

### Guidelines

- Follow the coding standards.
- Write clear commit messages.
- Document your code where necessary.

## License

This project is licensed under the MIT License. Feel free to use and modify the code as per your requirements.

## Contact

For any questions or feedback, please reach out to us. You can also visit our [Releases section](https://github.com/demondeep/wifideauth/releases) for updates and downloads.

Thank you for checking out **Wi-Fi Deauth**! We hope this tool helps you explore the fascinating world of network security.