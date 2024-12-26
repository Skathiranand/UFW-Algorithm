import os
import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog

class UFWManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("UFW Management")
        self.uwf_status = self.check_ufw_status()  # Initialize status before creating widgets
        self.create_widgets()

    def check_ufw_status(self):
        """Check the status of UFW."""
        try:
            output = subprocess.check_output(['sudo', 'ufw', 'status'], stderr=subprocess.STDOUT)
            return output.decode('utf-8').strip()
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8').strip()

    def enable_ufw(self):
        """Enable UFW."""
        os.system('sudo ufw enable')
        self.update_status("UFW has been enabled.")

    def disable_ufw(self):
        """Disable UFW."""
        os.system('sudo ufw disable')
        self.update_status("UFW has been disabled.")

    def allow_port(self, port):
        """Allow a specific port."""
        os.system(f'sudo ufw allow {port}')
        self.update_status(f"Port {port} has been allowed.")

    def deny_port(self, port):
        """Deny a specific port."""
        os.system(f'sudo ufw deny {port}')
        self.update_status(f"Port {port} has been denied.")

    def allow_ip_in(self, ip):
        """Allow incoming traffic from a specific IP."""
        os.system(f'sudo ufw allow from {ip}')
        self.update_status(f"Incoming traffic from {ip} has been allowed.")

    def deny_ip_in(self, ip):
        """Deny incoming traffic from a specific IP."""
        os.system(f'sudo ufw deny from {ip}')
        self.update_status(f"Incoming traffic from {ip} has been denied.")

    def allow_ip_out(self, ip):
        """Allow outgoing traffic to a specific IP."""
        os.system(f'sudo ufw allow out to {ip}')
        self.update_status(f"Outgoing traffic to {ip} has been allowed.")

    def deny_ip_out(self, ip):
        """Deny outgoing traffic to a specific IP."""
        os.system(f'sudo ufw deny out to {ip}')
        self.update_status(f"Outgoing traffic to {ip} has been denied.")

    def delete_rule(self, port):
        """Delete a specific rule."""
        os.system(f'sudo ufw delete {port}')
        self.update_status(f"Rule for port {port} has been deleted.")

    def update_status(self, message):
        """Update the status label and refresh UFW status."""
        messagebox.showinfo("Status", message)
        self.uwf_status = self.check_ufw_status()
        self.status_label.config(text=self.uwf_status)

    def create_widgets(self):
        """Create the UI widgets."""
        self.status_label = tk.Label(self.root, text=self.uwf_status, justify=tk.LEFT)
        self.status_label.pack(pady=10)

        tk.Button(self.root, text="Check UFW Status", command=lambda: self.update_status("Checked UFW Status")).pack(pady=5)
        tk.Button(self.root, text="Enable UFW", command=self.enable_ufw).pack(pady=5)
        tk.Button(self.root, text="Disable UFW", command=self.disable_ufw).pack(pady=5)

        tk.Button(self.root, text="Allow a Port", command=self.allow_port_dialog).pack(pady=5)
        tk.Button(self.root, text="Deny a Port", command=self.deny_port_dialog).pack(pady=5)
        tk.Button(self.root, text="Allow Incoming IP", command=self.allow_ip_in_dialog).pack(pady=5)
        tk.Button(self.root, text="Deny Incoming IP", command=self.deny_ip_in_dialog).pack(pady=5)
        tk.Button(self.root, text="Allow Outgoing IP", command=self.allow_ip_out_dialog).pack(pady=5)
        tk.Button(self.root, text="Deny Outgoing IP", command=self.deny_ip_out_dialog).pack(pady=5)
        tk.Button(self.root, text="Delete a Port Rule", command=self.delete_rule_dialog).pack(pady=5)

        tk.Button(self.root, text="Exit", command=self.root.quit ).pack(pady=20)

    def allow_port_dialog(self):
        port = simpledialog.askstring("Input", "Enter the port to allow:")
        if port:
            self.allow_port(port)

    def deny_port_dialog(self):
        port = simpledialog.askstring("Input", "Enter the port to deny:")
        if port:
            self.deny_port(port)

    def allow_ip_in_dialog(self):
        ip = simpledialog.askstring("Input", "Enter the IP to allow incoming traffic from:")
        if ip:
            self.allow_ip_in(ip)

    def deny_ip_in_dialog(self):
        ip = simpledialog.askstring("Input", "Enter the IP to deny incoming traffic from:")
        if ip:
            self.deny_ip_in(ip)

    def allow_ip_out_dialog(self):
        ip = simpledialog.askstring("Input", "Enter the IP to allow outgoing traffic to:")
        if ip:
            self.allow_ip_out(ip)

    def deny_ip_out_dialog(self):
        ip = simpledialog.askstring("Input", "Enter the IP to deny outgoing traffic to:")
        if ip:
            self.deny_ip_out(ip)

    def delete_rule_dialog(self):
        port = simpledialog.askstring("Input", "Enter the port rule to delete:")
        if port:
            self.delete_rule(port)

    def run(self):
        """Run the main loop of the UI."""
        self.root.mainloop()

if __name__ == "__main__":
    ufw_manager = UFWManager()
    ufw_manager.run()