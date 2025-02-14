from baseApi import BaseApi


class PostsApi(BaseApi):
    def get_all_posts(self):
        print("Fetching all posts...")
        response = self.get("posts")
        self.print_response(response)

    def get_single_post(self, post_id):
        print(f"Fetching post with ID {post_id}...")
        response = self.get(f"posts/{post_id}")
        self.print_response(response)

    def get_comments_for_post(self, post_id):
        print(f"Fetching comments for post with ID {post_id}...")
        response = self.get(f"posts/{post_id}/comments")
        self.print_response(response)

    def get_comments_by_post_id(self, post_id):
        print(f"Fetching comments for post with ID {post_id} using query parameter...")
        response = self.get("comments", params={"postId": post_id})
        self.print_response(response)

    def create_post(self):
        print("Creating a new post...")
        new_post = {
            "title": "New Post Title",
            "body": "This is the body of the new post.",
            "userId": 1
        }
        response = self.post("posts", new_post)
        self.print_response(response)

    def update_post(self, post_id):
        print(f"Updating post with ID {post_id}...")
        updated_post = {
            "id": post_id,
            "title": "Updated Post Title",
            "body": "This is the updated body of the post.",
            "userId": 1
        }
        response = self.put(f"posts/{post_id}", updated_post)
        self.print_response(response)

    def patch_post(self, post_id):
        print(f"Patching post with ID {post_id}...")
        patch_data = {
            "title": "Patched Post Title"
        }
        response = self.patch(f"posts/{post_id}", patch_data)
        self.print_response(response)

    def delete_post(self, post_id):
        print(f"Deleting post with ID {post_id}...")
        response = self.delete(f"posts/{post_id}")
        self.print_response(response)
