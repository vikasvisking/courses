def ground_cost(weight):
  if weight <= 2:
    cost = weight * 1.50 +  20.00
  elif 2 < weight <= 6:
    cost = weight * 3.00 + 20.00
  elif 6 < weight <= 10:
    cost = weight* 4.00 + 20.00
  else:
    cost = weight*4.75 + 20.00
  return cost
  
print(ground_cost(4.8))

premium_ground_ship = ""

def drone(weight):
  if weight <= 2:
    cost = weight * 4.50
  elif 2< weight <=6 :
    cost = 9.00 * weight 
  elif 6 < weight <= 10:
    cost = weight * 12.00
  else:
    cost = weight * 14.25
  return cost
    
print(drone(1.5))

def shipping_method(weight):
  ground = ground_cost(weight)
  premium_ground_ship = 125.00
  droneShip = drone(weight)
  
  if ground < premium_ground_ship and ground < droneShip:
    print("ground is cheapest")
    print(ground)
  elif premium_ground_ship < ground and premium_ground_ship < droneShip:
    print("premium_ground_ship is cheapest")
    print(premium_ground_ship)
  elif droneShip < ground  and droneShip < premium_ground_ship:
    print("droneShip is cheapest")
    print(droneShip)
    
shipping_method(4.8)
shipping_method(41.5)


