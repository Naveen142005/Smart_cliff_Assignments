def leaderboard(user_list):
    result = []
    for user  in user_list:
        result.append([user.mark, user.user_name])

    result.sort(reverse=True)
    return result

def display(result):
    for user in result:
        print(f"{user[1]} -> {user[0]}")


