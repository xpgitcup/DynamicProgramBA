import networkx as nx
import matplotlib.pyplot as plot

class DynamicModel:
    # 基础属性 --- 从前向后顺序递推算法
    nodes = []
    distance = []
    strategyVector = []
    nodePos = {}

    # 初始化模型
    def initModel(self, dataLines):
        # 识别阶段数，确定各个元素的字母
        m = len(dataLines) + 1
        zimu = []
        for i in range(0, m):
            zimu.append(chr(ord('A') + i))
        print("字母：", zimu)

        # 识别节点、边
        self.nodes.append(['A'])  # 现增加起点
        for i in range(len(dataLines)):
            vtemp = dataLines[i].split(";")
            vvtemp = vtemp[0].split()
            nv = len(vvtemp)  # 每一行的元素数
            v = []  # 每一行的节点
            for j in range(0, nv):
                if nv > 1:
                    v.append("%c%d" % (zimu[i + 1], j + 1))
                else:
                    v.append(zimu[i + 1])
            self.nodes.append(v)  # 节点识别结束

            # 开始识别边的数据
            ne = len(vtemp)
            ev = []
            for j in range(0, ne):
                vvtemp = vtemp[j].split()
                nne = len(vvtemp)
                eev = []
                for k in range(0, nne):
                    eev.append(int(vvtemp[k]))
                ev.append(eev)
            self.distance.append(ev)
        print(self.nodes)
        print(self.distance)
        print()
        return

    # 优化运算
    def optimization(self):
        print("动态规划分析：")
        m = len(self.nodes) - 1
        print("可以划分成%d个阶段。\n" % m)

        # 对每个阶段进行循环
        for i in range(m):
            print("阶段分析：")
            print(self.nodes[i], "--->", self.nodes[i + 1])
            statusNumber = len(self.nodes[i])  # 状态数
            selectNumber = len(self.nodes[i + 1])  # 决策数
            ss = []
            # 决策循环在外面
            for j in range(selectNumber):
                # 对每个状态进行循环，找到对应该决策的最佳状态
                tempd = []
                for k in range(statusNumber):
                    # 路径选择
                    d = {}
                    d["i"] = self.nodes[i][k]  # 起点
                    d["j"] = self.nodes[i + 1][j]  # 终点
                    elen = self.distance[i][k][j]  # 上一阶段的决策
                    if (i == 0):
                        d["value"] = elen
                    else:
                        d["value"] = self.strategyVector[i - 1][k]["value"] + elen
                    tempd.append(d)  # 所有的决策汇集到一起
                print("当前选择下寻优:", tempd)
                opt = min(tempd, key=lambda e: e["value"])
                # 记录当前决策
                opt["index"] = self.nodes[i].index(opt["i"])
                print(opt)
                ss.append(opt)
            # 阶段循环完成后，登记决策
            self.strategyVector.append(ss)

        # 最终的优化结果
        print("最终的优化结果：")
        for v in self.strategyVector:
            print(v)
        print()
        return

    # 显示结果
    def showResult(self):
        path = []
        m = len(self.strategyVector)
        i = m - 1
        while i >= 0:
            if i == m - 1:
                path.append(self.strategyVector[i][0]["j"])
                k = self.strategyVector[i][0]["index"]
            else:
                path.append(self.strategyVector[i][k]["j"])
                k = self.strategyVector[i][k]["index"]
            i -= 1
        path.append(self.strategyVector[0][k]["i"])
        path.reverse()
        print(path)
        print()
        return

    # 绘图
    def drawGraph(self):
        graph = self.setupGraphNodes()
        # 边
        for i in range(len(self.nodes)):
            if i > 0:
                nstart = len(self.nodes[i - 1])
                nstop = len(self.nodes[i])
                for j in range(nstart):
                    for k in range(nstop):
                        print(self.distance[i - 1][j][k])
                        if (self.distance[i - 1][j][k] < 100):
                            q = self.distance[i - 1][j][k]
                            start = self.nodes[i - 1][j]
                            stop = self.nodes[i][k]
                            graph.add_edge(start, stop, d=q)
        pos = self.setupNodePos()
        print(pos)
        plot.xlim(-1, 33)
        plot.ylim(-10, 8)
        nx.draw_networkx(graph, pos)
        nx.draw_networkx_edge_labels(graph, pos, rotate=True, label_pos=0.8)
        plot.title("DynamicPrograming")
        plot.savefig("graph.png")
        plot.show()
        return

    def setupGraphNodes(self):
        graph = nx.Graph()
        # 添加节点
        for e in self.nodes:
            for ee in e:
                graph.add_node(ee)
        return graph

    def setupNodePos(self):
        # 坐标
        pos = {}
        x = 0
        y = 0
        index = 0
        for i in range(len(self.nodes)):
            x = i * (4 + 0.2 * i)
            for j in range(len(self.nodes[i])):
                nn = len(self.nodes[i])
                dy = 4
                sty = (nn - 1) / 4 * (-8)
                y = sty + j * dy
                p = {self.nodes[i][j]: [x, y]}
                pos.update(p)
                index += 1
        self.nodePos = pos
        return pos

    def drawResult(self):
        grapha = self.setupGraphNodes()
        # 边
        m = len(self.strategyVector)
        i = m - 1
        while i >= 0:
            if i == m - 1:
                start = self.strategyVector[i][0]["i"]
                stop = self.strategyVector[i][0]["j"]
                d = self.strategyVector[i][0]["value"]
                k = self.strategyVector[i][0]["index"]
            else:
                start = self.strategyVector[i][k]["i"]
                stop = self.strategyVector[i][k]["j"]
                d = self.strategyVector[i][k]["value"]
                k = self.strategyVector[i][k]["index"]
            grapha.add_edge(start, stop, d=d)
            i -= 1
        plot.xlim(-1, 33)
        plot.ylim(-10, 8)
        nx.draw_networkx(grapha, self.nodePos)
        nx.draw_networkx_edge_labels(grapha, self.nodePos, rotate=True, label_pos=0.8)
        plot.title("DynamicProgramingResult")
        plot.savefig("graphResult.png")
        plot.show()
        return
