#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    
    vector<vector<int>> graph;
    graph.reserve(m);
    
    for (int i = 0; i < m; i++) {
        int u, v, weight;
        cin >> u >> v >> weight;
        graph.push_back({u, v, weight});
    }
    
    vector<int> distances(n + 1, 30000);
    distances[1] = 0;
    
    for (int i = 0; i < n - 1; i++) {
        for (const vector<int>& edge : graph) {
            int u = edge[0];
            int v = edge[1];
            int weight = edge[2];
            
            if (distances[u] != 30000 && distances[u] + weight < distances[v]) {
                distances[v] = distances[u] + weight;
            }
        }
    }
    
    distances.erase(distances.begin());
    for (int ele : distances) {
        cout << ele << ' ';
    }
    
    return 0;
}