import psutil
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("850x500")

# Define a global variable to store the selected interface
selected_interface = None

def get_network_interfaces():
    # Get a list of network interfaces
    interfaces = psutil.net_if_addrs()
    return list(interfaces.keys())
    
def select_interface():
    global selected_interface
    selected_interface = interface_combobox.get()
    print("Selected Interface:", selected_interface)

# Create the main application window
root.title("Select Network Interface")

# Get available network interfaces
interfaces = get_network_interfaces()

# Create a label
label = customtkinter.CTkLabel(root, text="Select Network Interface:")
label.pack(pady=10)

# Create a combobox to select the network interface
interface_combobox = customtkinter.CTkComboBox(root, values=interfaces, state="readonly")
interface_combobox.pack()

# Create a button to select the interface
select_button = customtkinter.CTkButton(root, text="Select Interface", command=select_interface)
select_button.pack(pady=10)

# Run the application
root.mainloop()
