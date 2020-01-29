def manhattanHeuristic(position, problem, info={}):
    "The Manhattan Distance heuristic for a PositionSearchProblem"
    "Exraído do arquivo 'searchAgents.py'"

    xy1 = position
    xy2 = problem.goal
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

def euclideanHeuristic(position, problem, info{}):
    "The Euclidean distance heuristic for a PositionSearchProblem"
    "Exraído do arquivo 'searchAgents.py'"

    xy1 = position
    xy2 = problem.goal

    return ( (xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2 ) ** 0.5

def maxXYHeuristic(position, problem, info={}):
    "Retorna o valor máximo entre a distância em termos de eixo X e a "
    "distância em termos de eixo Y entre position e o problem.goal"
    "Para esse problema em particular, a posição do pacman sempre está em coordenada maior que a da comida"
    "Então não é necessário valor absoluto das subtrações medidas. Idem para as heurísticas max_X e max_Y abaixo"
    xy1 = position
    xy2 = problem.goal

    return max( (xy1[0] - xy2[0]) , (xy1[1] - xy2[1]) )

def maxXHeuristic(position, problem, info={}):
    "Retorna a distância entre o pacman e o problem.goal em termos de coordenada x"
    xy1 = position
    xy2 = problem.goal
    return xy1[0] - xy2[0]

def maxYHeuristic(position, problem, info={}):
    "Retorna a distância entre o pacman e o problem.goal em termos de coordenada y"
    xy1 = position
    xy2 = problem.goal
    return xy1[1] - xy2[1]

def euclideanSquareHeuristic(position, problem, info={}):
    "Quadrado da distância euclidiana entre o pacman e a comida"
    xy1 = position
    xy2 = problem.goal
    return ( (xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2 )