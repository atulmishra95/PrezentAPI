from postApi import PostsApi


def main():
    api = PostsApi()

    # Task 1: GET /posts
    api.get_all_posts()

    # Task 2: GET /posts/1
    api.get_single_post(1)

    # Task 3: GET /posts/1/comments
    api.get_comments_for_post(1)

    # Task 4: GET /comments?postId=1
    api.get_comments_by_post_id(1)

    # Task 5: POST /posts
    api.create_post()

    # Task 6: PUT /posts/1
    api.update_post(1)

    # Task 7: PATCH /posts/1
    api.patch_post(1)

    # Task 8: DELETE /posts/1
    api.delete_post(1)

if __name__ == "__main__":
    main()
