import random


carrying_capacity = int(input("Enter the carrying capacity of the vehicle (from 100 to 600 kg): "))

if carrying_capacity < 100 or carrying_capacity > 600:
    print("The carrying capacity must be in the range from 100 to 600 kg.")
    exit()


loads = []
for i in range(20):

    weight = random.randint(int(carrying_capacity * 0.1), int(carrying_capacity * 0.25))
    print(weight)
    loads.append(weight)


shipments = []
total_weight = 0
for load in loads:
    if total_weight + load <= carrying_capacity:
        total_weight += load
    else:
        shipments.append(total_weight)
        total_weight = load

shipments.append(total_weight)


for i, shipment in enumerate(shipments):
    print(f"Shipment {i + 1}: {shipment} kg")

print(f"Minimum number of shipments: {len(shipments)}")

