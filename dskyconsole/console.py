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
    return int(r.get('Power') or 0)

def set_reactor_power(value):
    r.set('Power', str(value))

class BaseProgram:
    def __init__(self, system_name):
        self.system_name = system_name

    def set_status(self, status):
        r.set(self.system_name, status)

    def adjust_reactor_power(self, adjustment):
    current_power = get_reactor_power()
    current_power += adjustment
    set_reactor_power(current_power)

    def execute(self):
        pass  # Placeholder to be overridden

class Reactor(BaseProgram):
    def __init__(self):
        super().__init__("Reactor")

    class On(BaseProgram):
        def execute(self):
            self.set_status('ON')
            self.adjust_reactor_power(1)

    class Off(BaseProgram):
        def execute(self):
            self.set_status('COLD')

    class Scram(BaseProgram):
        def execute(self):
            self.set_status('SCRAM')

class EnvironmentalSystems(BaseProgram):
    def __init__(self):
        super().__init__("environmental_systems")

    class On(BaseProgram):
        def execute(self):
            self.set_status('ON')
            self.adjust_reactor_power(power_req[self.system_name])

    class Off(BaseProgram):
        def execute(self):
            self.set_status('OFF')
            self.adjust_reactor_power(-power_req[self.system_name])

    class Fault(BaseProgram):
        def execute(self):
            self.set_status('FAULT')

class LifeSupport(BaseProgram):
    def __init__(self):
        super().__init__("life_support")

    class On(BaseProgram):
        def execute(self):
            self.set_status('ON')
            self.adjust_reactor_power(power_req[self.system_name])

    class Off(BaseProgram):
        def execute(self):
            self.set_status('OFF')
            self.adjust_reactor_power(-power_req[self.system_name])

    class Fault(BaseProgram):
        def execute(self):
            self.set_status('FAULT')

class Comms(BaseProgram):
    def __init__(self):
        super().__init__("Comms")

    class On(BaseProgram):
        def execute(self):
            self.set_status('ON')
            self.adjust_reactor_power(power_req[self.system_name])

    class Off(BaseProgram):
        def execute(self):
            self.set_status('OFF')
            self.adjust_reactor_power(-power_req[self.system_name])

    class Fault(BaseProgram):
        def execute(self):
            self.set_status('FAULT')

class DefensiveSystems(BaseProgram):
    def __init__(self):
        super().__init__("Defensive Systems")

    class On(BaseProgram):
        def execute(self):
            self.set_status('ON')
            self.adjust_reactor_power(power_req[self.system_name])

    class Off(BaseProgram):
        def execute(self):
            self.set_status('OFF')
            self.adjust_reactor_power(-power_req[self.system_name])

    class Fault(BaseProgram):
        def execute(self):
            self.set_status('FAULT')

class PsychicDiffuser(BaseProgram):
    def __init__(self):
        super().__init__("psychic_diffuser")

    class On(BaseProgram):
        def execute(self):
            self.set_status('ON')
            self.adjust_reactor_power(power_req[self.system_name])

    class Off(BaseProgram):
        def execute(self):
            self.set_status('OFF')
            self.adjust_reactor_power(-power_req[self.system_name])

    class Fault(BaseProgram):
        def execute(self):
            self.set_status('FAULT')

class Maglev(BaseProgram):
    def __init__(self):
        super().__init__("Maglev")

    class On(BaseProgram):
        def execute(self):
            self.set_status('ON')
            self.adjust_reactor_power(power_req[self.system_name])

    class Off(BaseProgram):
        def execute(self):
            self.set_status('OFF')
            self.adjust_reactor_power(-power_req[self.system_name])

    class Fault(BaseProgram):
        def execute(self):
            self.set_status('FAULT')

class AccessControl(BaseProgram):
    def __init__(self):
        super().__init__("Access Control")

    class On(BaseProgram):
        def execute(self):
            self.set_status('ON')
            self.adjust_reactor_power(power_req[self.system_name])

    class Off(BaseProgram):
        def execute(self):
            self.set_status('OFF')
            self.adjust_reactor_power(-power_req[self.system_name])

    class Fault(BaseProgram):
        def execute(self):
            self.set_status('FAULT')

class SpiritContainmentField(BaseProgram):
    def __init__(self):
        super().__init__("spirit_containment_field")

    class On(BaseProgram):
        def execute(self):
            self.set_status('ON')
            self.adjust_reactor_power(power_req[self.system_name])

    class Off(BaseProgram):
        def execute(self):
            self.set_status('OFF')
            self.adjust_reactor_power(-power_req[self.system_name])

    class Fault(BaseProgram):
        def execute(self):
            self.set_status('FAULT')
            
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
    program_class = code_map.get(input_code)
    if program_class:
        program_instance = program_class()
        program_instance.execute()
    else:
        print("Invalid Code")