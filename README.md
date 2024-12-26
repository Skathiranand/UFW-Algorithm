# UFW Management Tool
## UFW TOOL
The UFW Management Tool is a simple graphical user interface (GUI) application built using Python's Tkinter library. It allows users to manage the Uncomplicated Firewall (UFW) on Linux systems easily. Users can enable or disable UFW, allow or deny specific ports and IP addresses, and check the current status of the firewall.

## Technology used

[![My Skills](https://skillicons.dev/icons?i=py,linux,ubuntu&theme=dark)](https://skillicons.dev)
## Features
Check the current status of UFW.

Enable or disable UFW.

Allow or deny specific ports.

Allow or deny incoming and outgoing traffic from specific IP addresses.

Delete specific firewall rules.

User-friendly GUI for easy interaction.

## Requirements
Python 3.x

Tkinter (usually included with Python installations)

UFW (Uncomplicated Firewall) installed on your Linux system

Sudo privileges to execute UFW commands
## Install UFW
sudo apt install ufw

sudo ufw enable 

git clone https://github.com/yourusername/ufw-management-tool.git

python3 ufw_manager.py
## Usage
Launch the application.

Use the buttons to perform various actions:

Check UFW Status

Enable or Disable UFW

Allow or Deny Ports

Allow or Deny Incoming/Outgoing IPs

Delete Port Rules

Follow the prompts to enter the required information (e.g., port numbers or IP addresses).
