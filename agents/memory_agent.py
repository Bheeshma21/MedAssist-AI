class PatientMemory:

    def __init__(self):
        self.memory = {}

    def update(self, patient_data):

        for key, value in patient_data.items():

            if value is None:
                continue

            self.memory[key] = value

    def get_memory(self):
        return self.memory

    def clear(self):
        self.memory = {}


patient_memory = PatientMemory()