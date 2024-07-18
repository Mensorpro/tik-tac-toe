# Description: Implementation of the Minimax algorithm with alpha-beta pruning.
class Minimax:
    def __init__(self, game):
        self.game = game

    def minimax(self, state, depth, player, alpha, beta):
        if depth == 0 or self.game.is_over(state):
            return self.game.evaluate(state, self.game.max_player)

        is_maximizing_player = player == self.game.max_player
        if is_maximizing_player:
            best = -float('inf')
            for move in self.game.get_moves(state):
                new_state = self.game.apply_move(state, move, player)
                score = self.minimax(new_state, depth - 1, self.game.min_player, alpha, beta)
                best = max(best, score)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
            return best
        else:
            best = float('inf')
            for move in self.game.get_moves(state):
                new_state = self.game.apply_move(state, move, player)
                score = self.minimax(new_state, depth - 1, self.game.max_player, alpha, beta)
                best = min(best, score)
                beta = min(beta, best)
                if beta <= alpha:
                    break
            return best

    def get_best_move(self, state, depth, player):
        best_move = None
        alpha = -float('inf')
        beta = float('inf')

        is_maximizing_player = player == self.game.max_player
        best_score = -float('inf') if is_maximizing_player else float('inf')

        for move in self.game.get_moves(state):
            new_state = self.game.apply_move(state, move, player)
            score = self.minimax(new_state, depth - 1, self.game.min_player if is_maximizing_player else self.game.max_player, alpha, beta)

            if (is_maximizing_player and score > best_score) or (not is_maximizing_player and score < best_score):
                best_score = score
                best_move = move

            if is_maximizing_player:
                alpha = max(alpha, best_score)
            else:
                beta = min(beta, best_score)
                
            if beta <= alpha:
                break

        return best_move
