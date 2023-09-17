import redis
import time

# Redis connection
r = redis.Redis(host='192.168.20.71', port=6379, db=0)

# Power requirement for each system
power_req = {
    'life_support': 10,
    'environmental_systems': 5,
    'Comms': 15,
    'Defensive Systems': 15,
    'Maglev': 30,
    'psychic_diffuser': 25,
    'Access Control': 10,
    'spirit_containment_field': 40
}

def adjust_reactor_power(adjustment):
    current_power = int(r.get('Power'))
    current_power += adjustment
    r.set('Power', str(current_power))

class Reactor:
    @staticmethod
    def Nominal():
        r.set('Reactor', 'NOMINAL')
        adjust_reactor_power(1)

    @staticmethod
    def Cold():
        r.set('Reactor', 'COLD')

    @staticmethod
    def Scram():
        r.set('Reactor', 'SCRAM')
        adjust_reactor_power(-1)

    @staticmethod
    def Runaway():
        r.set('Reactor', 'RUNAWAY')
        adjust_reactor_power(2)

class EnvironmentalSystems:
    @staticmethod
    def On():
        r.set('environmental_systems', 'ON')
        adjust_reactor_power(power_req['environmental_systems'])

    @staticmethod
    def Off():
        r.set('environmental_systems', 'OFF')
        adjust_reactor_power(-power_req['environmental_systems'])

    @staticmethod
    def Fault():
        r.set('environmental_systems', 'FAULT')

class LifeSupport:
    @staticmethod
    def On():
        r.set('life_support', 'ON')
        adjust_reactor_power(power_req['life_support'])

    @staticmethod
    def Off():
        r.set('life_support', 'OFF')
        adjust_reactor_power(-power_req['life_support'])

    @staticmethod
    def Fault():
        r.set('life_support', 'FAULT')

class Comms:
    @staticmethod
    def On():
        r.set('Comms', 'ON')
        adjust_reactor_power(power_req['Comms'])

    @staticmethod
    def Off():
        r.set('Comms', 'OFF')
        adjust_reactor_power(-power_req['Comms'])

    @staticmethod
    def Fault():
        r.set('Comms', 'FAULT')

# ... Continuing for all the systems ...

class DefensiveSystems:
    @staticmethod
    def On():
        r.set('Defensive Systems', 'ON')
        adjust_reactor_power(power_req['Defensive Systems'])

    @staticmethod
    def Off():
        r.set('Defensive Systems', 'OFF')
        adjust_reactor_power(-power_req['Defensive Systems'])

    @staticmethod
    def Fault():
        r.set('Defensive Systems', 'FAULT')

class PsychicDiffuser:
    @staticmethod
    def On():
        r.set('psychic_diffuser', 'ON')
        adjust_reactor_power(power_req['psychic_diffuser'])

    @staticmethod
    def Off():
        r.set('psychic_diffuser', 'OFF')
        adjust_reactor_power(-power_req['psychic_diffuser'])

    @staticmethod
    def Fault():
        r.set('psychic_diffuser', 'FAULT')

class Maglev:
    @staticmethod
    def On():
        r.set('Maglev', 'ON')
        adjust_reactor_power(power_req['Maglev'])

    @staticmethod
    def Off():
        r.set('Maglev', 'OFF')
        adjust_reactor_power(-power_req['Maglev'])

    @staticmethod
    def Fault():
        r.set('Maglev', 'FAULT')

class AccessControl:
    @staticmethod
    def On():
        r.set('Access Control', 'ON')
        adjust_reactor_power(power_req['Access Control'])

    @staticmethod
    def Off():
        r.set('Access Control', 'OFF')
        adjust_reactor_power(-power_req['Access Control'])

    @staticmethod
    def Fault():
        r.set('Access Control', 'FAULT')

class SpiritContainmentField:
    @staticmethod
    def On():
        r.set('spirit_containment_field', 'ON')
        adjust_reactor_power(power_req['spirit_containment_field'])

    @staticmethod
    def Off():
        r.set('spirit_containment_field', 'OFF')
        adjust_reactor_power(-power_req['spirit_containment_field'])

    @staticmethod
    def Fault():
        r.set('spirit_containment_field', 'FAULT')

# The code map 
code_map = {
    1001: Reactor.Nominal,
    2001: Reactor.Cold,
    3001: Reactor.Scram,
    4001: Reactor.Runaway,
    1002: EnvironmentalSystems.On,
    2002: EnvironmentalSystems.Off,
    3002: EnvironmentalSystems.Fault,
    1003: LifeSupport.On,
    2003: LifeSupport.Off,
    3003: LifeSupport.Fault,
    1004: Comms.On,
    2004: Comms.Off,
    3004: Comms.Fault,
    1005: DefensiveSystems.On,
    2005: DefensiveSystems.Off,
    3005: DefensiveSystems.Fault,
    1006: PsychicDiffuser.On,
    2006: PsychicDiffuser.Off,
    3006: PsychicDiffuser.Fault,
    1007: Maglev.On,
    2007: Maglev.Off,
    3007: Maglev.Fault,
    1008: AccessControl.On,
    2008: AccessControl.Off,
    3008: AccessControl.Fault,
    1009: SpiritContainmentField.On,
    2009: SpiritContainmentField.Off,
    3009: SpiritContainmentField.Fault,
}

# A simple executor to activate the systems based on the entered code
def execute_system(code):
    if code in code_map:
        code_map[code]()
    else:
        print("Invalid code entered!")

# Test
if __name__ == "__main__":
    while True:
        try:
            code = int(input("Enter the code: "))
            execute_system(code)
        except ValueError:
            print("Please enter a valid integer code!")