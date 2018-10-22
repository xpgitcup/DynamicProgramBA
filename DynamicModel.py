class DynamicModel:
    # 基础属性 --- 从前向后顺序递推算法
    nodes = []
    distance = []
    strategyVector = []

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
        return

    # 优化运算
    def optimization(self):
        print("\n动态规划分析：")
        m = len(self.nodes) - 1
        print("可以划分成%d个阶段。\n" % m)

        # 对每个阶段进行循环
        for i in range(m):
            print("阶段分析：")
            print(self.nodes[i], "--->", self.nodes[i + 1])
            statusNumber = len(self.nodes[i]) #状态数
            selectNumber = len(self.nodes[i + 1]) #决策数
            ss = []
            # 决策循环在外面
            for j in range(selectNumber):
                for k in range(statusNumber):
                    #

        return

    # 显示结果
    def showResult(self):
        return

    # 绘图
    def drawGraph(self):
        return
