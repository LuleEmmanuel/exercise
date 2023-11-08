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

    def talk_to_patient(self):
        print("Welcome to the Virtual Doctor!\n")
        for i, question in enumerate(self.questions):
            user_response = input(question).lower()
            print(self.responses[i])
        print("\nThank you for using the Virtual Doctor!")

if __name__ == "__main__":
    doctor = Doctor()
    doctor.talk_to_patient()
