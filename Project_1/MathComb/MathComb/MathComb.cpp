#include <iostream>
#include <fstream>
#include <string>
#include <chrono>

using namespace std;
using namespace std::chrono;

typedef high_resolution_clock Clock;
typedef Clock::time_point ClockTime;

static const string OUT_FILE = "C:\\Users\\zmddd\\Desktop\\Studia\\Mgr Sem I\\Jezyki-Skryptowe-Project\\Project_1\\results_c_impl_comb.txt";
static const string DATA_FILE = "C:\\Users\\zmddd\\Desktop\\Studia\\Mgr Sem I\\Jezyki-Skryptowe-Project\\Project_1\\test.txt";
static const string DELIMITER = ", ";


int factorial(int n) 
{
    int result = 1;
    for (int i = 1; i <= n; i++) 
    {
        result *= i;
    }

    return result;
}

int mathComb(int n, int k)
{
    if (k > n) 
    {
        return 0;
    }
    else 
    {
        return factorial(n) / (factorial(k) * factorial(n - k));
    }
}

void test() {
    ifstream data(DATA_FILE);
    ofstream out_file(OUT_FILE);

    string line;
    string val_n, val_k, val_res;
    int n, k, res, counted_res;
    size_t pos = 0;
    while (getline(data, line)) 
    {
        val_n = line.substr(0, line.find(DELIMITER));
        line.erase(0, line.find(DELIMITER) + DELIMITER.length());
        val_k = line.substr(0, line.find(DELIMITER));
        line.erase(0, line.find(DELIMITER) + DELIMITER.length());
        val_res = line;
        n = stoi(val_n);
        k = stoi(val_k);
        res = stoi(val_res);

        clock_t start, end;
        ClockTime start_time = Clock::now();
        for (int i = 0; i < 10000000; i++) {
            counted_res = mathComb(n, k);
        }
        ClockTime end_time = Clock::now();
        if (counted_res != res) 
        {
            cout << "Nieporpawny wnik dla n = " << n << " k = " << k << endl;
        }

        auto execution_time_sec = duration_cast<seconds>(end_time - start_time).count();
        auto execution_time_ms = duration_cast<milliseconds>(end_time - start_time).count();
        out_file << "n = " << n << " k = " << k << " res = " << counted_res << " time: " << execution_time_sec << "," << execution_time_ms << endl;
    }
    out_file.close();
    data.close();
}

int main()
{
    test();
}

//max: 12 silnia
