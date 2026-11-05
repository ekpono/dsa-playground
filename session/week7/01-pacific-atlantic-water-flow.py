directions = [ (0, 1), (-1, 0), (1, 0), (0, -1) ]

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        width = len(heights[0])
        height = len(heights)
        result = []

        goodPacific = []

        def dfs(row, column, visited):
            if visited[row][column]:
                return

            visited[row][column] = True

            island = heights[row][column]

            for x, y in directions:
                if row + x < 0 or column + y < 0 or row + x >= height or column + y >= width:
                    continue
                goodNeighbor = heights[row + x][column + y]
                if goodNeighbor >= island:
                    dfs(row + x, column + y, visited)



        pacificVisited = [ [ 0 ] * len(heights[0]) for _ in range(len(heights)) ]
        atlanticVisited = [ [ 0 ] * len(heights[0]) for _ in range(len(heights)) ]

        for i in range(len(heights[0])):
            dfs(0, i, pacificVisited)

        for i in range(len(heights)):
            dfs(i, 0, pacificVisited)

        for i in range(len(heights[0])):
            dfs((height - 1), i, atlanticVisited)

        for i in range(len(heights)):
            dfs(i, (width - 1), atlanticVisited)

        for i in range(height):
            for j in range(width):
                if pacificVisited[i][j] == True and atlanticVisited[i][j] == True:
                    result.append([i, j])


        return result


# THIS SOLUTION WORKED BUT IT HAS TIMEOUT BECAUSE OF UNNECESSARY visited RECURSION in the second for loop pacificVisited  and atlanticVisited
# directions = [ (0, 1), (-1, 0), (1, 0), (0, -1) ]
#
# class Solution(object):
#     def pacificAtlantic(self, heights):
#         """
#         :type heights: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         width = len(heights[0])
#         height = len(heights)
#         result = []
#
#
#
#         def dfs(row, column, visited, name):
#             print(row, column, visited, name)
#             if name == "pacific" and (column <= 0 or row <= 0):
#                 return True
#
#             if name == "atlantic" and (column >= (width - 1) or row >= (height - 1)):
#                 return True
#
#             if visited[row][column]:
#                 return False
#
#             visited[row][column] = True
#             island = heights[row][column]
#             goodIsland = [False, False, False, False]
#
#             index = 0
#             for x, y in directions:
#                 if row + x < 0 or column + y < 0 or row + x >= height or column + y >= width:
#                     continue
#
#                 goodNeighbor = heights[row + x][column + y]
#                 if goodNeighbor <= island:
#                     goodIsland[index] = dfs(row + x, column + y, visited, name)
#
#                 index+=1
#
#
#             return True in goodIsland
#
#
#
#         for i in range(height):
#             isIsland = []
#             for j in range(width):
#                 pacificVisited = [ [ 0 ] * len(heights[0]) for _ in range(len(heights)) ]
#                 atlanticVisited = [ [ 0 ] * len(heights[0]) for _ in range(len(heights)) ]
#                 pacific = dfs(i, j, pacificVisited, "pacific")
#                 atlantic = dfs(i, j, atlanticVisited, "atlantic")
#
#                 if pacific and atlantic:
#                     result.append([i, j])
#
#         return result