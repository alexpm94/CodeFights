# CodeFights
This repository contains my solution to certain problems form Code Fights
# Path trajectory and mapping
This section is about the algorithms that have  been used to obtain the desired path
to follow. Also, here is shown our methodology to achieve a correct mapping in few steps.
## BFS
Breadth-first search is an algorithm for traversing or searching tree or graph data structures.
It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key) and explores the neighbor nodes first, before moving to the next level neighbours.
```
Wkikipedia https://en.wikipedia.org/wiki/Breadth-first_search
```
We have used BFS to simple determinate the shortest path from a point to a goal. We have used BFS in the next order:

```
Start to Red box
Red box to Green box
Green box to Blue box
Blue box to Yellow box
Yellow box to the End (opposite corner)
```
## Mapping simulation

## Path following simulation
Firstly we must create a grid with all its nodes interconnected, this step we call it the graph creation.
In the code "car_movements.py", we can change the size of the grid in te section "number of tiles".
Then we have to update the graph with all the founded boxes so that we can delete the forbidden connections. This step should be done by the mappig.
Forbbiden connection are the ones which the car cannot traverse. As in the image bellow.
![con2](https://user-images.githubusercontent.com/33235648/38569088-048f8862-3cb0-11e8-96df-dea6e9e9acfc.png)

Once the graph has been updated, the next step is to determine the shortest path in the order we described above.
Then we determine the angles that the car should turn in every node.
The output is the next:
```
[90, 0, 0, 0, -90, 0, 0, 0, 0, 180, 0, 0, 0, -90, 0, -90, 0, -90, 0, 0, 0, 0, 90, 0, 180, 0, 0, -90, 0, 0, 0, 0, -90, 0, 0, 0]
```
In the next image we see the simulation of the car taversing all the boxes in the specific order. Strating
at the left-down corner  and finishing at the right-uppper corner.

![final_path](https://user-images.githubusercontent.com/33235648/38567638-5db27426-3cac-11e8-99fb-dd45342dc3fb.png)

