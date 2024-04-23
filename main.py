class CarFinder:
  def __init__(self):
      self.allowed_vehicles_file = "allowed_vehicles.txt"
      self.load_allowed_vehicles()

  def load_allowed_vehicles(self):
      try:
          with open(self.allowed_vehicles_file, "r") as file:
              self.allowed_vehicles_list = file.read().splitlines()
      except FileNotFoundError:
          # If file doesn't exist, initialize with default list
          self.allowed_vehicles_list = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck',
                                        'Toyota Tundra', 'Rivian R1T', 'Ram 1500']
          self.save_allowed_vehicles()

  def save_allowed_vehicles(self):
      with open(self.allowed_vehicles_file, "w") as file:
          file.write("\n".join(self.allowed_vehicles_list))

  # Printing authorized vehicles
  def print_authorized_vehicles(self):
      print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
      for vehicle in self.allowed_vehicles_list:
          print(vehicle)

  # Searching a Vehicle
  def search_vehicle(self, search_query):
      if search_query in self.allowed_vehicles_list:
          print(f"{search_query} is an authorized vehicle.")
      else:
          print(f"{search_query} is not an authorized vehicle.")

  # Adding a Vehicle
  def add_vehicle(self, new_vehicle):
      self.allowed_vehicles_list.append(new_vehicle)
      self.save_allowed_vehicles()  # Update the file
      print(f"You have added \"{new_vehicle}\" as an authorized vehicle.")

  # Deleting a Vehicle
  def delete_vehicle(self, vehicle_to_delete):
      if vehicle_to_delete in self.allowed_vehicles_list:
          self.allowed_vehicles_list.remove(vehicle_to_delete)
          self.save_allowed_vehicles()  # Update the file
          print(f"You have deleted \"{vehicle_to_delete}\" from authorized vehicles.")
      else:
          print(f"\"{vehicle_to_delete}\" is not in the list of authorized vehicles.")

  # Running the Program
  def run(self):
      while True:
          print("********************************")
          print("AutoCountry Vehicle Finder v0.4")
          print("********************************")
          print("Please Enter the following number below from the following menu:")
          print("1. PRINT all Authorized Vehicles")
          print("2. SEARCH for Authorized Vehicle")
          print("3. ADD Authorized Vehicle")
          print("4. DELETE Authorized Vehicle")
          print("5. Exit")
          print("********************************")
          choice = input("Enter your choice: ")

          if choice == '1':
              self.print_authorized_vehicles()
          elif choice == '2':
              search_query = input("Enter the full Vehicle name you would like to search: ")
              self.search_vehicle(search_query)
          elif choice == '3':
              new_vehicle = input("Enter the full Vehicle name you would like to add: ")
              self.add_vehicle(new_vehicle)
          elif choice == '4':
              vehicle_to_delete = input("Enter the full Vehicle name you would like to delete: ")
              self.delete_vehicle(vehicle_to_delete)
          elif choice == '5':
              print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
              input("Press any key to exit...")
              break

# Unit Test #1
car_finder = CarFinder()
car_finder.run()

# Unit Test #2
car_finder = CarFinder()
car_finder.print_authorized_vehicles()

# Unit Test #3
car_finder = CarFinder()
car_finder.run()