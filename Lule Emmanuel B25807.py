class Doctor:
    def __init__(self):
        self.questions = [
            "How are you feeling today? (Good/Bad): ",
            "Do you have any specific symptoms? (e.g., headache, fever): ",
            "On a scale of 1 to 10, how severe is your pain (1 = mild, 10 = severe)? ",
            "Have you been experiencing any unusual changes in your body? (Yes/No): ",
        ]

        self.responses = [
            "I see. It's important to take care of yourself.",
            "I'm sorry to hear that. Please tell me more about your symptoms.",
            "Thank you for sharing. Pain can be difficult to deal with.",
            "That's concerning. We should discuss this further.",
        ]


class Patient:
    def __init__(self):
        self.answers = []

    def answer_question(self, question):
        user_response = input(question).lower()
        return user_response

    def store_response(self, response):
        self.answers.append(response)


class VirtualDoctor:
    def __init__(self, doctor, patient):
        self.doctor = doctor
        self.patient = patient

    def talk_to_patient(self):
        print("Welcome to the Virtual Doctor!\n")
        for i, question in enumerate(self.doctor.questions):
            user_response = self.patient.answer_question(question)
            self.patient.store_response(self.doctor.responses[i])
            print(self.doctor.responses[i])

        print("\nThank you for using the Virtual Doctor!")


if __name__ == "__main__":
    doctor = Doctor()
    patient = Patient()
    virtual_doctor = VirtualDoctor(doctor, patient)
    virtual_doctor.talk_to_patient()
