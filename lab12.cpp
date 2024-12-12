#include <iostream>
#include <queue>
using namespace std;

// Function to perform BFS traversal
void bfs(int** graph, int s_index, int n) {
    bool* visited = new bool[n] {false};  // Array to track visited nodes
    queue<int> q1;  // Queue for BFS
    
    visited[s_index - 1] = true;  // Mark the starting node as visited
    q1.push(s_index - 1);  // Add the starting node to the queue
    
    while (!q1.empty()) {
        int node = q1.front();  // Get the front node of the queue
        q1.pop();  // Remove it from the queue
        
        // Print the current node
        cout << (node + 1) << " ";
        
        // Visit all unvisited neighbors of the current node
        for (int i = 0; i < n; ++i) {
            if (graph[node][i] == 1 && !visited[i]) {  // If there's an edge and the neighbor hasn't been visited
                visited[i] = true;  // Mark the neighbor as visited
                q1.push(i);  // Add the neighbor to the queue
            }
        }
    }
}


int** generateArray(int N, int E) 
{
    
    int** array = new int*[N];  // Allocate memory for n rows
    for (int i = 0; i < N; i++) 
    {
        array[i] = new int[N];
    }
    
    cout << "present Nodes: " << endl;
    for(int i = 0; i < N; ++i)
    {
        for(int j= 0; j < N; ++j)
        {
            array[i][j] = 0;//initialize all to 0 initially
        }
        cout << (i + 1) <<", ";
    }
    cout << endl <<endl;
    
    
    cout << "Please enter the following edges " <<endl;
    for (int i = 0; i < E; i++) 
    {
        int a = -1, b = -2;
    while(!((a > 0 && a <= N) && (b > 0 && b <= N) && (a != b)) )
        {
        cout << "For pair: " << (i + 1) << endl;//output pair number
        
        cout << "Enter a:  ";
        cin >>a;
        cout << "Enter b:  ";
        cin >>b;
        }
        array[a - 1][b - 1] = 1;
        array[b - 1][a - 1] = 1;
        cout << endl;
        
    }   
    return array;
}

int main() 
{
    const int n = 8;  // Number of nodes in the graph
    int starting_node = -2; // Starting vertex for BFS ( -2 by default)

    int N = 0, E = 0;

    while( !(N > 0 && E > 0 && (starting_node > 0 && starting_node <= N)) )
    {
    cout << endl << "Please enter size of matrix(number of nodes)"<<":";
    cin >> N;

    cout << "Please enter edge size (number of edges)"<<":";
    cin >> E;

    cout << "Enter starting node visited: ";
    cin >> starting_node;
    }
    
    int **matrix = generateArray(N, E);
    
    // Start BFS from vertex 2 (Node 2)
    cout << "BFS traversal starting from vertex 2: ";
    bfs(matrix, starting_node, n);



    // Clean up dynamic memory
    for (int i = 0; i < N; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;
    
    return 0;
}

