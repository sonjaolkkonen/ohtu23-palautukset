class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.points = [0,0]

    def won_point(self, player_name):
        if player_name == "player1":
            self.points[0] += 1
        else:
            self.points[1] += 1

    def get_score(self):

        def get_points_equal(points):
            points_dict = {0: "Love-All", 1:"Fifteen-All", 2:"Thirty-All", 3:"Deuce"}
            if points[0] == 0:
                return points_dict[0]
            if points[0] == 1:
                return points_dict[1]
            if points[0] == 2:
                return points_dict[2]
            else:
                return points_dict[3]
            
        def get_points_equal_or_over_four(points):
            points_dict = {0: "Advantage player1", 1:"Advantage player2", 2:"Win for player1", 3:"Win for player2"}
            minus_result = points[0] - points[1]

            if minus_result == 1:
                return points_dict[0]
            elif minus_result == -1:
                return points_dict[1]
            elif minus_result >= 2:
                return points_dict[2]
            else:
                return points_dict[3]
            

        def get_points_less_than_four(points):
            points_dict = {0: "Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}
            score = points_dict[points[0]] + "-" + points_dict[points[1]]
            return score
        
        if self.points[0] == self.points[1]:
            score = get_points_equal(self.points)
        elif self.points[0] >= 4 or self.points[1] >= 4:
            score = get_points_equal_or_over_four(self.points)
        else:   
            score = get_points_less_than_four(self.points)
        return score

