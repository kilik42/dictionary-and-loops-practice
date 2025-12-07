# ---------------------------------------------------------
# Project Prompt: FoodDash – Restaurant Order Lookup System
# (An Uber Eats–style food delivery application)
# ---------------------------------------------------------

# You have been hired to help build a simple version of an
# Uber Eats–style app called "FoodDash".
#
# Your program will manage CUSTOMER ORDERS for delivery.
# Each order will be stored as a DICTIONARY.
# All orders will be stored together in a LIST.

# The FoodDash support worker must be able to:

# 1. Enter a customer's name OR order ID
# 2. Instantly see the order details:
#    - Order ID
#    - Customer Name
#    - Restaurant Name
#    - List of Items Ordered
#    - Total Price
#    - Delivery Address
#    - Order Status (Placed, Preparing, Out for Delivery, Delivered, Canceled)
#    - Driver Name (if assigned)

# ---------------------------------------------------------
# Students must:
# ---------------------------------------------------------

# - Describe the search process in plain English
# - Explain what key(s) can be searched (customer name, order ID)
# - Explain what values are returned (full order info)
# - Explain what happens if no order is found

# ---------------------------------------------------------
# be able to add new data (new orders)
# ---------------------------------------------------------

# Your program must allow the FoodDash worker to ADD a brand
# new order into the system while the program is running.

# The program should:
# 1. Ask the user for the following information:
#    - Order ID (must be unique)
#    - Customer Name
#    - Restaurant Name
#    - Delivery Address
#    - Driver Name (or "None" if not assigned yet)
#    - Order Status (start as "Placed" or "Preparing")
#
# 2. Ask the user how many items are in the order.
#    Then, for each item, ask:
#       - Item name
#       - Item price
#
# 3. Store ALL items for that order in a LIST called "items".
#
# 4. Calculate the TOTAL PRICE of the order
#    by adding up all the item prices.

# 5. Create ONE dictionary for the new order with keys:
#    - "order_id"
#    - "customer"
#    - "restaurant"
#    - "address"
#    - "driver"
#    - "status"
#    - "items"       (list of item names)
#    - "total_price" (number)

# 6. Append (add) this dictionary to the main orders list.

# 7. After adding the order, the program must:
#    - Print a confirmation message
#    - Print the new total number of orders
#    - Print the full details of the new order

# 8. If the Order ID is already being used by another order:
#    - Do NOT add the new order
#    - Display an error message that the Order ID is taken

# ---------------------------------------------------------
# be able to update existing orders
# ---------------------------------------------------------

# The FoodDash worker must be able to UPDATE parts of an order.

# The program should allow these updates:
# - Change the Order Status
#   (Placed → Preparing → Out for Delivery → Delivered or Canceled)
# - Assign or change the Driver Name
# - Update the Delivery Address (if the customer calls in a change)

# The worker must:
# 1. Enter the Order ID
# 2. Choose what they want to update:
#       - 1: Status
#       - 2: Driver
#       - 3: Address
# 3. Enter the new value
# 4. See the updated order printed on the screen

# If the Order ID does NOT exist:
# - Print a clear error message
# - Do not crash the program

# ---------------------------------------------------------
# be able to view filtered lists of orders
# ---------------------------------------------------------

# The system should support helpful views for the worker:

# 1. Show ALL orders from a specific restaurant.
# 2. Show ALL orders with a specific status
#    (for example, all "Out for Delivery" orders).
# 3. Show ALL orders assigned to a specific driver.

# For each of these views:
# - Ask the user for a filter (restaurant name, status, or driver).
# - Loop through the list of orders.
# - Print only the orders that match the filter.

# ---------------------------------------------------------
# (optional challenge) be able to cancel orders
# ---------------------------------------------------------

# The FoodDash worker must be able to cancel an order.

# - Ask for the Order ID.
# - If it exists, change its status to "Canceled".
# - Print a confirmation message and the updated order.
# - If it does not exist, show an error message.

# ---------------------------------------------------------
# data rules & integrity
# ---------------------------------------------------------

# - Every order MUST have:
#   - An Order ID
#   - A Customer Name
#   - A Restaurant Name
#   - A Delivery Address
#   - A Status
#   - A Total Price
#
# - No two orders may share the same Order ID.
# - The program should not crash if the user searches
#   for an Order ID or name that does not exist.
#   It must show a clear message instead.
#
# - Items and prices should stay together logically:
#   if items or prices change, the total_price should be updated.

