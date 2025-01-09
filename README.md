# Vehicle Management System

A Python-based GUI application for managing different types of vehicles using the `tkinter` library. The application allows users to create vehicles (Car, Truck, Motorcycle), start and stop their engines, and view their details.

---

## Features

1. **Add Vehicles**:
   - Input vehicle details such as brand, model, and specific attributes (e.g., number of doors for cars).
   - Supports three types of vehicles:
     - **Car**: Requires the number of doors.
     - **Truck**: Requires the payload capacity (in tons).
     - **Motorcycle**: Requires whether it has a sidecar (Yes/No).

2. **View Vehicle Details**:
   - Displays the details of all added vehicles.

3. **Validation**:
   - Ensures that inputs are valid (e.g., numeric values for doors and payload).

---

## Prerequisites

- Python 3.x
- `tkinter` (comes pre-installed with most Python distributions)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/vehicle-management-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd vehicle-management-system
   ```

3. Run the application:

   ```bash
   python vehicle_management.py
   ```

---

## Usage

1. **Select Vehicle Type**:
   - Choose between Car, Truck, or Motorcycle from the dropdown.

2. **Enter Details**:
   - Provide the required details for the selected vehicle type.

3. **Add Vehicle**:
   - Click the `Add Vehicle` button to save the vehicle.

4. **Show Details**:
   - Click the `Show Details` button to view all added vehicles.

---

## File Structure

```
vehicle-management-system/
|-- vehicle_management.py  # Main application code
|-- README.md              # Project documentation
```

---

## Example Output

### Adding a Car:
- Brand: Toyota
- Model: Corolla
- Extra Attribute: 4 (Number of Doors)

### Adding a Truck:
- Brand: Ford
- Model: F-150
- Extra Attribute: 2.5 (Payload Capacity in Tons)

### Adding a Motorcycle:
- Brand: Harley-Davidson
- Model: Street 750
- Extra Attribute: Yes (Has Sidecar)

### Viewing Details:
```
Car: Toyota Corolla, Doors: 4
Truck: Ford F-150, Payload Capacity: 2.5 tons
Motorcycle: Harley-Davidson Street 750, Sidecar: Yes
```

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes and push to the branch:

   ```bash
   git commit -m "Add feature-name"
   git push origin feature-name
   ```

4. Open a pull request.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- Inspired by the power of object-oriented programming in Python.
- Developed using the `tkinter` library for GUI design.

