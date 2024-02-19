import socket
import subprocess


def get_network_info():
    try:

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        cmd = "ipconfig"

        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        output, error = process.communicate()
                                   
        
        return {
            "Hostname": hostname,
            "IP Address": ip_address,
            "Network Information": output.decode('utf-8') if not error else f"Error: {error.decode('utf-8')}"  # Changed 'Network Information'
        } 
    except Exception as e:
        return f"An error occurred: {e}"
        

network_info = get_network_info()
for key, value in network_info.items():
    print(f"{key}: {value}")