# Create a Business class
class Business():
  def __init__(self, name, franchises): # Constructor initializer method
    self.name = name
    self.franchises = franchises

#Create a Franchise class
class Franchise():
  def __init__(self, address, menus): # Constructor initializer method
    self.address = address
    self.menus = menus

  def __repr__(self): # Return a printable string representation of the address object
    return self.address
   
  def available_menus(self, time): # Available menus function
    available_menu = [] # Create empty list
    for menu in self.menus: # For loop
      if time >= menu.start_time and time <= menu.end_time: # If statement
        available_menu.append(menu)
    return available_menu

# Create a Menu class
class Menu():
  def __init__(self, name, items, start_time, end_time): # Constructor initializer method
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def __repr__(self): # Return a printable string representation of the name object
    return self.name + ' menu is available from ' + str(self.start_time) + ' until ' + str(self.end_time) + '.'
  
  def calculate_bill(self, purchased_items): # Calculate bill function
    bill = 0 # Create empty variable
    for purchased_item in purchased_items: # For loop
      if purchased_item in self.items: # If statement
        bill += self.items[purchased_item]
    return bill

# Create dictionary of brunch items for Menu class
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

# Create menu name, menu items, start time, and end time arguments for brunch menu in Menu class
brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)

# Create dictionary of early bird items for Menu class
early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}

# Create menu name, menu items, start time, and end time arguments for early bird menu in Menu class
early_bird_menu = Menu("Early Bird", early_bird_items, 1500, 1800)

# Create dictionary of dinner items for Menu class
dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}

# Create menu name, menu items, start time, and end time arguments for dinner menu in Menu class
dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)

# Create dictionary of kids items for Menu class
kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

# Create menu name, menu items, start time, and end time arguments for kids menu in Menu class
kids_menu = Menu("Kids", kids_items, 1100, 2100)

# Create available menus list for Franchise class
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

# Create address and menu arguments for flagship store in Franchise class
flagship_store = Franchise("1232 West End Road", menus)

# Create address and menu arguments for new installment franchise store in Franchise class
new_installment = Franchise("12 East Mulberry Street", menus)

# Create franchise name and franchise location arguments for new basta location in Business class
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Create dictionary of arepas menu items for Menu class
arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

# Create franchise name, menu items, start time, and end time arguments for arepas franchise in Menu class
arepas_menu = Menu("Take a' Arepa", arepas_items, 1000, 2000)

# Create address and menu arguments for new arepas place francise store in Franchise class
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# Create name and franchise location arguments for new arepa fanchise in Business class
arepa = Business("Take a' Arepa", [arepas_place])

# Print Brunch name
print(brunch_menu.name)
print('')
# Print when Brunch menu is available
print(brunch_menu)
print('')
# Print cost of an order from the Brunch menu
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
print('')
# Print cost of an order from the Early Bird menu
print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
print('')
# Print address of flagship store
print(flagship_store)
print('')
# Print which menus are available at the flagship store at 5:00 pm
print(flagship_store.available_menus(1700))
print('')
# Print the time when the arepa menu at the arepa franchise location is available
print(arepa.franchises[0].menus[0])

