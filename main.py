from DynamicModel import DynamicModel

filename="source.dat"

try:
    with open(filename) as sourceFile:
        dataLines = sourceFile.readlines()
        print(dataLines)
    model = DynamicModel()
    model.initModel(dataLines)
    model.optimization()
    model.showResult()
    model.drawGraph()

except IOError:
    print("出错了...")
print("计算结束，再见...")