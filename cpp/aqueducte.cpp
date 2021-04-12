#include <cmath>
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

class Point {        

  private:
    double x_cord;
    double y_cord;

  public:              

    Point(double x, double y){
        this->x_cord = x;
        this->y_cord = y;
    }

    double get_x() {  
        return x_cord;
    }

    double get_y() {  
        return y_cord;
    }

    static Point middle_with_y(Point first, Point second, double y) {  
        return Point((first.x_cord + second.x_cord) / 2, y);
    }

    double x_distance_to(Point point) {  
        return point.x_cord - this->x_cord;
    }

    double y_distance_to(Point point) {  
        return point.y_cord - this->y_cord;
    }

    double distance(Point point) {
        return sqrt(pow(x_distance_to(point), 2) + pow(y_distance_to(point), 2));
    }

};

class Land {        

  #define IMPOSSIBLE -1
  #define NON_CALCULATED 0

  private:

    int NUM_POINTS;
    int MAX_HEIGHT;
    int ALPHA;
    int BETA;
    vector<Point> points;
    vector<long long int> point_values_buffer;

    unsigned long long int pow_long_int(unsigned long long int number) {
        return number * number;
    }

    unsigned long long int cost_arch(Point first, Point second) {
        unsigned long long int distance = first.x_distance_to(second);
        return BETA * pow_long_int(distance);
    }

    unsigned long long int cost_support(Point point) {
        return ALPHA * (MAX_HEIGHT - point.get_y());
    }

    unsigned long long int total_cost(int first_point_index, int second_point_index) {
        long long int value = point_values_buffer[second_point_index];
        if (value == 0) 
            return cost_support(points[first_point_index]) + cost_support(points[second_point_index]) + cost_arch(points[first_point_index], points[second_point_index]);
        else if (value == IMPOSSIBLE) 
            return IMPOSSIBLE;
        else
            return cost_support(points[first_point_index]) + cost_arch(points[first_point_index], points[second_point_index]) + value;
    }

    bool valid_arch(int first_point_index, int second_point_index) {
        Point first_point = points[first_point_index];
        Point second_point = points[second_point_index];
        double radius_value = first_point.x_distance_to(second_point) / 2;
        double init_arch = MAX_HEIGHT - radius_value;
        Point radius_point = Point::middle_with_y(first_point, second_point, init_arch);
        if (init_arch < first_point.get_y() || init_arch < second_point.get_y()) {
            return false;
        } for (int i = first_point_index + 1; i < second_point_index; i++) {
            if ((points[i].get_y() >= init_arch) && pow(radius_point.distance(points[i]), 2) - pow(radius_value, 2) > 0)
                return false;
        }
        return true;
    }

    long long int get_minimum_cost_for_index(int index) {
        long long int minimum = IMPOSSIBLE;
        for (int i = index + 1; i < NUM_POINTS; i++) {
            if (valid_arch(index, i)) {
                long long int cost = total_cost(index, i);
                if (minimum == IMPOSSIBLE || (cost != IMPOSSIBLE && cost < minimum))
                    minimum = cost;
            }
        }
        return minimum;
    }

  public:

    Land(int num_points, int height, int alpha, int beta) {
        this->NUM_POINTS = num_points;
        this->MAX_HEIGHT = height;
        this->ALPHA = alpha;
        this->BETA = beta;
        this->point_values_buffer.resize(num_points, NON_CALCULATED);
    }

    void add_point_to_land(double x, double y) {
        points.push_back(Point(x, y));
    }

    long long int get_minimum_cost() {
        for (int i = NUM_POINTS - 2; i >= 0; i--) {
            long long int minimum = get_minimum_cost_for_index(i);
            point_values_buffer[i] = minimum;
        }
        return point_values_buffer[0];
    }

};

Land get_land_from_file(string file_name) {
    try {
        string line;
        ifstream myfile;
        myfile.open(file_name);
        getline(myfile, line);
        stringstream ss(line);
        string word;
        string constructor[4];
        for (int i = 0; ss >> word; i++)
            constructor[i] = word;
        Land land = Land(stoi(constructor[0]), stoi(constructor[1]), stoi(constructor[2]), stoi(constructor[3]));
        while(getline(myfile, line)) {
            stringstream ss2(line);
            string word2;
            string coord[2];
            for (int i = 0; ss2 >> word2; i++)
                coord[i] = word2;
            land.add_point_to_land(stod(coord[0]), stod(coord[1]));
        }
        myfile.close();
        return land;
    } catch (exception& e) {
        cout << "File " << file_name << " doesn't exist or has invalid syntax \n"; 
        exit(-1);
    }
}

string get_file_name(int argc, char **argv) {
    if (argc == 2)
        return argv[1];
    string file_name;
    cout << "Enter file name: ";
    cin >> file_name;
    return file_name;
}

int main(int argc, char **argv) {
    string file_name = get_file_name(argc, argv);
    Land land = get_land_from_file(file_name);
    long long int minimum = land.get_minimum_cost();
    string result = minimum == IMPOSSIBLE ? "impossible" : to_string(minimum);
    cout << result << "\n" ;
}
