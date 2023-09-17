import redis
import time

# Redis connection
r = redis.Redis(host='192.168.20.71', port=6379, db=0)

# Status indicators
status_indicators = {
    'Reactor': ['ON', 'COLD', 'SCRAM'],
    'environmental_systems': ['ON', 'OFF', 'FAULT'],
    'life_support': ['ON', 'OFF', 'FAULT'],
    'Comms': ['ON', 'OFF', 'FAULT'],
    'Defensive Systems': ['ON', 'OFF', 'FAULT'],
    'psychic_diffuser': ['ON', 'OFF', 'FAULT'],
    'Maglev': ['ON', 'OFF', 'FAULT'],
    'Access Control': ['ON', 'OFF', 'FAULT'],
    'spirit_containment_field': ['ON', 'OFF', 'FAULT'],
    'System Booted': ['YES', 'NO']
}

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

# Reset Redis with initial statuses
for status, states in status_indicators.items():
    r.set(status, states[1])  # sets all statuses to their 'OFF' equivalent

# Set initial power level
r.set('Power', '0')

def get_reactor_power():
    return int(r.get('Power'))

def set_reactor_power(power):
    r.set('Power', str(power))

class Reactor:
    system_name = "Reactor"

    @staticmethod
    def adjust_reactor_power(adjustment):
        current_power = get_reactor_power()
        current_power += adjustment
        set_reactor_power(current_power)

    class On:
        @staticmethod
        def execute():
            r.set(Reactor.system_name, 'ON')
            Reactor.adjust_reactor_power(1)

    class Off:
        @staticmethod
        def execute():
            r.set(Reactor.system_name, 'COLD')

    class Scram:
        @staticmethod
        def execute():
            r.set(Reactor.system_name, 'SCRAM')

class SystemWithPowerReq:
    @staticmethod
    def adjust_reactor_power(adjustment):
        current_power = get_reactor_power()
        current_power += adjustment
        set_reactor_power(current_power)

    class On:
        @staticmethod
        def execute():
            r.set(SystemWithPowerReq.system_name, 'ON')
            SystemWithPowerReq.adjust_reactor_power(power_req[SystemWithPowerReq.system_name])

    class Off:
        @staticmethod
        def execute():
            r.set(SystemWithPowerReq.system_name, 'OFF')
            SystemWithPowerReq.adjust_reactor_power(-power_req[SystemWithPowerReq.system_name])

    class Fault:
        @staticmethod
        def execute():
            r.set(SystemWithPowerReq.system_name, 'FAULT')

class EnvironmentalSystems(SystemWithPowerReq):
    system_name = "environmental_systems"

class LifeSupport(SystemWithPowerReq):
    system_name = "life_support"

class Comms(SystemWithPowerReq):
    system_name = "Comms"

class DefensiveSystems(SystemWithPowerReq):
    system_name = "Defensive Systems"

class PsychicDiffuser(SystemWithPowerReq):
    system_name = "psychic_diffuser"

class Maglev(SystemWithPowerReq):
    system_name = "Maglev"

class AccessControl(SystemWithPowerReq):
    system_name = "Access Control"

class SpiritContainmentField(SystemWithPowerReq):
    system_name = "spirit_containment_field"
            
# Mapping of code inputs to specific program executions
code_map = {
    1001: Reactor.On,
    2001: Reactor.Off,
    1002: EnvironmentalSystems.On,
    2002: EnvironmentalSystems.Off,
    1003: LifeSupport.On,
    2003: LifeSupport.Off,
    1004: Comms.On,
    2004: Comms.Off,
    1005: DefensiveSystems.On,
    2005: DefensiveSystems.Off,
    1006: PsychicDiffuser.On,
    2006: PsychicDiffuser.Off,
    1007: Maglev.On,
    2007: Maglev.Off,
    1008: AccessControl.On,
    2008: AccessControl.Off,
    1009: SpiritContainmentField.On,
    2009: SpiritContainmentField.Off
}

while True:
    input_code = int(input("Enter the code: "))  # Receive code input
    program_to_execute = code_map.get(input_code)
    if program_to_execute:
        program_to_execute.execute()
    else:
        print("Invalid Code")