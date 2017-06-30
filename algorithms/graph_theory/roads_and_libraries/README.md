# Roads and Libraries

Problem description:
[Roads and Libraries on HackerRank](https://www.hackerrank.com/challenges/torque-and-development)

## Initial Approach
1. Divide each query into connected components. Use BFS or DFS.
   Store graph in a form of adjacent list.
2. For each component:
   1. For each city:
      1. Assume we build library in this city.
      2. Build a graph with selected city as a root.
         When adding next city to the graph decide whether it is cheaper
         to build a separate library in next city or build a road from
         root city to the next city.
   2. Calculate the cost of selecting this city as a root with a library
      in it.

## Second Approach
1. Divide query into isolated components.
2. If c_lib < c_road:
   1. Build library in each city in this component.
3. Else c_lib >= c_road:
   1. Find minimal amount of roads required to connect all cities and
      build one library at random city.

## Third Approach
1. Divide query into isolated components.
2. If c_lib < c_road:
   1. Build library in each city in this component.
3. Else c_lib >= c_road:
   1. While we have cities connected to component with one road only:
      1. Remove these cities from queue
      2. Take into account the cost of the roads to these lonely cities.
   2. Find minimal amount of roads required to connect all remaining
      cities and build one library at random city.

## Fourth Approach
1. Divide query into isolated components by comparing input edges.
2. If c_lib < c_road:
   1. Build library in each city in this component.
3. Else c_lib >= c_road:
   1. cost = (n - 1) * c_road + c_lib