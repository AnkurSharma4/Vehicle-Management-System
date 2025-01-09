import tkinter as tk
from tkinter import ttk, messagebox

class VehicleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Management System")

        self.vehicle_type = tk.StringVar(value="Car")
        self.brand = tk.StringVar()
        self.model = tk.StringVar()
        self.extra_attr = tk.StringVar()
        self.vehicles = []

        self.create_widgets()

    def create_widgets(self):

        ttk.Label(self.root, text="Vehicle Type:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        ttk.Combobox(
            self.root, textvariable=self.vehicle_type, values=["Car", "Truck", "Motorcycle"], state="readonly"
        ).grid(row=0, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.root, text="Brand:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.brand).grid(row=1, column=1, padx=10, pady=5, sticky="w")


        ttk.Label(self.root, text="Model:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.model).grid(row=2, column=1, padx=10, pady=5, sticky="w")


        ttk.Label(self.root, text="Extra Attribute:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.extra_attr).grid(row=3, column=1, padx=10, pady=5, sticky="w")


        ttk.Button(self.root, text="Add Vehicle", command=self.add_vehicle).grid(row=4, column=0, padx=10, pady=10)
        ttk.Button(self.root, text="Show Details", command=self.show_details).grid(row=4, column=1, padx=10, pady=10)

    def add_vehicle(self):
        vehicle_type = self.vehicle_type.get()
        brand = self.brand.get()
        model = self.model.get()
        extra = self.extra_attr.get()

        if not (brand and model and extra):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if vehicle_type == "Car":
            try:
                vehicle = Car(brand, model, int(extra))
            except ValueError:
                messagebox.showerror("Error", "Number of doors must be an integer.")
                return
        elif vehicle_type == "Truck":
            try:
                vehicle = Truck(brand, model, float(extra))
            except ValueError:
                messagebox.showerror("Error", "Payload capacity must be a number.")
                return
        elif vehicle_type == "Motorcycle":
            if extra.lower() not in ["yes", "no"]:
                messagebox.showerror("Error", "Sidecar must be 'Yes' or 'No'.")
                return
            vehicle = Motorcycle(brand, model, extra.lower() == "yes")
        else:
            messagebox.showerror("Error", "Invalid vehicle type.")
            return

        self.vehicles.append(vehicle)
        messagebox.showinfo("Success", f"{vehicle_type} added successfully!")
        self.clear_fields()

    def clear_fields(self):
        self.brand.set("")
        self.model.set("")
        self.extra_attr.set("")

    def show_details(self):
        if not self.vehicles:
            messagebox.showinfo("Info", "No vehicles added yet.")
            return

        details = "\n\n".join([vehicle.get_details() for vehicle in self.vehicles])
        messagebox.showinfo("Vehicle Details", details)


if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleApp(root)
    root.mainloop()
