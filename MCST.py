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