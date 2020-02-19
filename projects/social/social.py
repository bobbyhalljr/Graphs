import random

class User:
    def __init__(self, name):
        self.name = name
        
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"USER {i+1}")

        # Create friendships
        # create a list with all possible friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
                
        # shuffle the list 
        random.shuffle(possible_friendships)
        print("-----")
        print(possible_friendships)
        print("-----")
        
        # grab the first N pairs from the list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        
        * Hint 1: What kind of graph search guarantees you a shortest path?
        * Hint 2: Instead of using a `set` to mark users as visited, you could use a `dictionary`. Similar to sets, checking if something is in a dictionary runs in O(1) time. 
        If the visited user is the key, what would the value be?
        """
        # BFS / Queue
        
        # create an empty queue
        q = Queue()
        # add a path to the user_id
        q.enqueue( [user_id] ) 
        # create an empty dict
        visited = {}  # Note that this is a dictionary, not a set
        # while the queue is not empty 
        counter = 0
        while q.size() > 0:
            counter += 1
            print(counter)
            # dequeue the first path
            path = q.dequeue()
            # grab the last friend key / value from the path
            v = path[-1]
            # check if it's the target
            if v == user_id:
                # if so return the path
                return path
            # check if its been visited
            # if it has not been visited...
            if v not in visited:
                # mark it as visited
                visited.add(v)
                # then add a path to all the neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    # make a copy of the path before adding
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)
        
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(2)
    print(connections)
