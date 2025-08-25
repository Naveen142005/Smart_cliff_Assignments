from game import conduct_game
from leaderboard import display, leaderboard
from questions import Questions
from user import User

def main():
    print ('Enter a user_name:')
    user_name = input()

    questions_dict_1 = {
        "Capital of France?": "Paris",
        "Largest planet in Solar System?": "Jupiter",
        "5 + 3 = ?": "8",
        "Python is a snake or a programming language?": "programming language"
    }

    question_obj_1 = Questions(questions_dict_1)
    user_1 = User(user_name, 0)
    conduct_game(question_obj_1, user_1)

    print(f"{user_1.get_name()} score : {user_1.get_mark()}/{question_obj_1.get_total_question()}")

    print('Enter a user_name:')
    user_name = input()

    questions_dict_2 = {
        "What is the capital of India?": "New Delhi",
        "Who developed the theory of relativity?": "Einstein",
        "Which data structure uses FIFO (First In First Out)?": "Queue",
        "The chemical symbol for water is?": "H2O",
        "What is 12 * 8?": "96"
    }

    question_obj_2 = Questions(questions_dict_2)
    user_2 = User(user_name, 0)
    conduct_game(question_obj_2, user_2)

    print(f" {user_2.get_name()} score : {user_2.get_mark()}/{question_obj_2.get_total_question()}")

    print('Leader Board...')
    curr_leaderboard = leaderboard([user_1, user_2])
    display(curr_leaderboard)


if __name__ == '__main__':
    main()