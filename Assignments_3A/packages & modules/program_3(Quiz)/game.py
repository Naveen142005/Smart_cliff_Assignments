def conduct_game(question, user):
    question_dict = question.get_questions()

    for question, answer in question_dict.items():
        print(question)
        user_answer = input()
        if answer == user_answer:
            user.mark += 1

