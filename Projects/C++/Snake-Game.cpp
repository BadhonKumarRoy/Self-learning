#include <iostream>
#include <deque>
using namespace std;

const int ROW = 30;
const int COL = 50;

enum Direction { UP, DOWN, LEFT, RIGHT };
struct Point{
    int row;
    int col;
};
struct Snake{
    deque<Point> body;
    Direction dir = RIGHT;
    char headChar = 'O';
    char bodyChar = 'o';
};

void display(char matrix[ROW][COL]){
    for(int i = 0; i < ROW; i++){
        for(int j = 0; j < COL; j++){
            cout << matrix[i][j];

                if(j == COL-1){
                    cout << endl;
                }
        }
    }
}

void grid(char matrix[ROW][COL]){
    for(int i = 0; i < ROW; i++){
        for(int j = 0; j < COL; j++){

            if(i == 0 || i == ROW-1){
                matrix[i][j] = '#';
            }
            else if(j == 0 || j == COL-1){
                matrix[i][j] = '#';
            }
            else{
                matrix[i][j] = ' ';
            }
        }
    }
    display(matrix);
}

void snake_movement(){

}

int main()
{
    char matrix[ROW][COL];
    grid(matrix);
    snake_movement();
}
