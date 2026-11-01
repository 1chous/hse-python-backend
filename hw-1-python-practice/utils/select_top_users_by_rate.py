def select_top_users_by_rate(users, top_size):
    a = sorted(users, key=lambda user: user.rate, reverse=True)
    return a[:top_size]
