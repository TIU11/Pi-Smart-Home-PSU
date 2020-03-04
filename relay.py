import gpiozero

# change this value based on which GPIO port the relay is connected to
RELAY_PIN = 18

# create a relay object.
# Triggered by the output pin going low: active_high=False.
# Initially off: initial_value=False
relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)

def toggle_relay():
    print("toggling relay")
    relay.toggle()

toggle_relay()