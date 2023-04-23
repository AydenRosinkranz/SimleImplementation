import random
class MCSTNode:
    def __init__(self, board, move=None, parent=None):
        self.board = board  # The current game state
        self.move = move  # The move that led to this state (None for the root node)
        self.parent = parent  # The parent node in the MCTS tree
        self.children = []  # List of child nodes in the MCTS tree
        self.wins = 0  # Number of wins from this node
        self.visits = 0  # Number of visits to this node

    def is_fully_expanded(self):
        unexplored_moves = [
            (i, j)
            for i in range(3)
            for j in range(3)
            if self.board.state[i][j] == ' '
        ]

        return len(unexplored_moves) == len(self.children)

    def is_terminal(self):
        return self.board.is_game_over()

    def best_child(self, c_param=1.4):
        best_score = -float("inf")
        best_child = None

        for child in self.children:
            exploitation = child.wins / child.visits
            exploration = c_param * ((self.visits)**0.5) / (1 + child.visits)
            score = exploitation + exploration

            if score > best_score:
                best_score = score
                best_child = child

        return best_child

    def expand(self, player):
        unexplored_moves = [
            (i, j)
            for i in range(3)
            for j in range(3)
            if self.board.state[i][j] == ' '
        ]

        if not unexplored_moves:
            return None

        move = random.choice(unexplored_moves)
        new_board = self.board.copy()
        new_board.make_move(move[0], move[1], player)

        child_node = MCSTNode(new_board, move, self)
        self.children.append(child_node)

        return child_node

    def backpropagate(self, result):
        self.visits += 1
        self.wins += result

        if self.parent:
            self.parent.backpropagate(1 - result)  # Invert the result for the parent node
# original: for logical comparison
# def get_move(self, game_status):
#     root = Node(game_status.board)
#     for i in range(self.num_simulations):
#         node = self.select(root)
#         if node:
#             self.expand(node)
#             child = random.choice(node.children)
#             reward = self.simulate(child.state)
#             self.backpropagate(child, reward)
#     best_child = self.select_best_child(root)
#     return self.get_move_from_states(game_status.board, best_child.state)
#
# def select(self, node):
#     while node.children:
#         selected_child = self.select_best_child(node)
#         if selected_child:
#             node = selected_child
#         else:
#             break
#     return node
#
# def select_best_child(self, node):
#     children = node.children
#     if not children:
#         return None
#     total_visits = sum(child.visits for child in children)
#     best_score = float('-inf')
#     best_child = None
#     for child in children:
#         exploitation_term = child.rewards[self.symbol] / child.visits
#         exploration_term = math.sqrt(math.log(total_visits) / child.visits)
#         score = exploitation_term + 1.4 * exploration_term
#         if score > best_score:
#             best_score = score
#             best_child = child
#     return best_child