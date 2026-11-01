def filter_comments_by_author(comments, author):
    return [x for x in comments if x.author_id == author.id]
