from model.model import Model

myModel = Model()
print(myModel.buildGraph('QPL', 2))
print(myModel.getVicini())
print(myModel.getBestPath("35-51 81 STREET", "à"))