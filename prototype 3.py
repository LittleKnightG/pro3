import random
import json
from operator import attrgetter

class flashCard:
    def __init__(self, id, ques, ans):
        self.id = id
        self.ques = ques
        self.ans = ans

# Open the file for reading
with open('G:/My Drive/aarav/pc/A-Level/computer/a level project/main code/protoype_3/data/re.json', 'r') as f:

    # Load the JSON data from the file
    flashCard_data = json.load(f)

# Create a list to hold instances of the Student object
flashCards = []

# Iterate over the JSON array
for item in flashCard_data:

    # Create a new instance of Student for each item in the array
    flashCardItem = flashCard(item['id'], item['ques'], item['ans'])

    # Add the new instance to the list
    flashCards.append(flashCardItem)


# Alternatively, you can iterate over the students in the list like this:
for flashCard in flashCards:
    # Do something with each student
    print(flashCard.id)
    print(flashCard.ques)
    print(flashCard.ans)

newQuestionText= "question X"
newAnswerText= "answer x"
lastStoredFlashCard = max(flashCards, key=attrgetter('id'))
print(lastStoredFlashCard)
print(lastStoredFlashCard.id)
newId = int(lastStoredFlashCard.id) + 1
print(newId)
#newFlashCardItem = flashCard(newId, newQuestionText, newAnswerText)
#flashCards.append(newFlashCardItem)
json_object = json.dumps(flashCards)
with open("G:/My Drive/aarav/pc/A-Level/computer/a level project/main code/protoype_3/data/re.json", "w") as outfile:
    outfile.write(json_object)





def generate_math_questions(num_questions):
        operations = ["add", "subtract", "multiply", "divide"]
        questions = []
        answers = []
        for i in range(num_questions):
            operation = random.choice(operations)
            if operation == "add":
                a = random.randint(1, 100)
                b = random.randint(1, 100)
                question = f"What is {a} + {b}?"
                answer = str(a + b)
            elif operation == "subtract":
                a = random.randint(1, 100)
                b = random.randint(1, a)
                question = f"What is {a} - {b}?"
                answer = str(a - b)
            elif operation == "multiply":
                a = random.randint(1, 12)
                b = random.randint(1, 12)
                question = f"What is {a} x {b}?"
                answer = str(a * b)
            elif operation == "divide":
                a = random.randint(1, 144)
                b = random.randint(1, 12)
                question = f"What is {a} / {b}?"
                answer = str(int(a / b))
            questions.append(question)
            answers.append(answer)
        return questions, answers

def read_lines_from_file(filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        return [line.strip() for line in lines]

def get_subject():
        subjects = list(SUBJECT_FILES.keys())
        while True:
            subject = input(f"Choose a subject ({'/'.join(subjects)}): ")
            if subject in subjects:
                return subject
            else:
                print(f"Error: Invalid subject {subject}")

def get_num_questions():
        while True:
            try:
                num_questions = int(input("How many questions do you want to answer? "))
                if num_questions > 0:
                    return num_questions
                else:
                    print("Error: Number of questions must be greater than 0")
            except ValueError:
                print("Error: Please enter a valid integer")

def get_name():
        name = input("What is your name? ")
        return name

def get_score(name, subject):
        try:
            with open(f"{name}_{subject}_score.txt", "r") as f:
                score = int(f.read())
        except FileNotFoundError:
            score = 0
        return score

def update_score(name, subject, score):
        with open(f"{name}_{subject}_score.txt", "w") as f:
            f.write(str(score))
            print(15)

def play_game(name, subject, questions, answers, num_questions):
        num_questions = min(num_questions, len(questions))
        print(f"\n{' '.join(questions[0].split()[:2]).capitalize()} Questions:")
        score = 0
        for i in range(num_questions):
            index = random.randrange(len(questions))
            question = questions[index]
            answer = answers[index]
            response = input(f"\nQuestion {i+1}: {question}\n")
            if response.lower() == answer.lower():
                print("Correct!")
                score += 1
            else:
                print("Incorrect")
        print(f"\n{name}'s score for {subject}: {score}")
        update_score(name, subject, score)


def main():
        name = get_name()
        subject = get_subject()
        num_questions = get_num_questions()
        if subject == "math":
            questions, answers = generate_math_questions(num_questions)
        else:
            filename = SUBJECT_FILES[subject]
            questions = read_lines_from_file(filename)
            answers = read_lines_from_file(filename.replace("questions", "answers"))
        play_game(name, subject, questions, answers, num_questions)
        while True:
            play_again = input("Do you want to play again? (yes or no): ")
            if play_again.lower() == "yes":
                subject = get_subject()
                num_questions = get_num_questions()
                if subject == "math":
                    questions, answers = generate_math_questions(num_questions)
                else:
                    filename = SUBJECT_FILES[subject]
                    questions = read_lines_from_file(filename)
                    answers = read_lines_from_file(filename.replace("questions", "answers"))
                play_game(name, subject, questions, answers, num_questions)
            else:
                break


if __name__ == "__main__":
    main()
