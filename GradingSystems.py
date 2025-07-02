from itertools import count 
from logging import exception 
from math import trunc

def show_history() -> None:
    print("\n === Brief histor of python ===")
    print("\n === Created in the year 1991 ===")
    print("\n === py 3 in the year 2008 ===")
    print("\n === Program that computes the average score of students ===")

    #tuple is mutable while list is immutable
    
def get_names_score() -> tuple[list[str], list[float]]:
        while True:
            try:
                count = int(input("Number of students"))
                if count <= 0:
                    print("Enter number greater than zero")
                    continue
                break
            except ValueError:
                print("Invalid Input. Enter a valid number.")
                
        name_of_students = []
        scores = []
            
        print("\n Enter student names and their scores: ")
            
        for i in range (count):
            name = input(f'student {i + 1} name: ').strip()
            if not name:
                name = f'Student:{i+1}'
            name_of_students.append(name)
                     
            while True:
                try:
                    score = float(input(f"Enter the score for {name}: "))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("score must be between 0 and 100")
                        
                except ValueError:
                        print("Invalid Input. Enter a number")
                
        return name_of_students, scores
show_history()
names, scores = get_names_score()

average = sum(scores) / len(scores)
print(f"Average score of students: {average:.2f}")

# Optional:studet list with scores
