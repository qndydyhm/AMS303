# Chapter 1
 - 15. Since G is a simple graph, then for each vertex, it can have at most 1 edge with every other vetex, so the highest degree for a vertex in a simple graph is (n-1). Also, If there is a vertex with (n-1) degrees, then all the other vertices must have at least 1 degree, which means there are at most 1->(n-1) or 0->(n-2) with total of n-1 possible degrees. However, since there are n vertices, due to the pigeonhole principle, there must be at least two vetexes with the same degree.
 - 16. 5-gons, it is easy to find a circut with 5 nodes such as the star inside the left graph. There is also circuit with 6 nodes such as the outer loop of the right graph.
 - 29. There are n vertices and each vertex with degree r, then there is total of $n*r$ degrees. The number of edges is equal to half of the number of degrees, then there is exact $\frac{n*r}{2}$ edges for graph G.
 - 31. 1. k5,5
       2. cube
       3. w4
       4. impossible, according to q29, n*r must be division by 2, but it is no the case here.
       5. k7 with a circuit of length 7 removed
# Chapter 2
 - 3. 3, 4, 8, 3, skipped, 5, if regular, 5, if not, 3
 - 5. assuming a graph is disconnected, then it must be able to divided into two sets of vetices V1 and V2 where there is no edge between V1 and V2. Then its complement graph must contain a sub grapgh of edges with each vertex in V1 with each vetex in V2, which is $K_{(num\ of\ vertices\ in\ V_1),\ (num\ of\ vertices\ in\ V_2)}$ which is connected
 - 9. if $d(v, w) >= 2$, then there must be a vertex z on any path between v and w. $d(v, z)+d(z,w)$ is not greater than $d(v, w)$ because z can be chosen on the path of $d(v, w)$, also it is not smaller than $d(v, w)$ because if there exists a $d(v, z)+d(z,w)<=d(v, w)$, we can just chose that as the new $d(v, w)$
 - 33. 1. c5
       2. two self-complementary graph form a complete regular graph of n nodes and n-1 degrees on each vertex. According to 1.29, $\frac{n*r}{2} = \frac{n*(n-1)}{2}$. Also two self-complementary are isomorphic, then they have same number of edges $\frac{n*(n-1)}{4}$. Either n or n-1 must divisible by 4, n must be 4k or 4k+1.