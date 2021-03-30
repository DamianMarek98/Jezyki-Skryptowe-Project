#include <iostream>
#include <fstream>
#include <string>
#include <ctime> // time_t
#include <chrono>

using namespace std;
using namespace std::chrono;

typedef high_resolution_clock Clock;
typedef Clock::time_point ClockTime;

static const string OUT_FILE = "C:\\Users\\zmddd\\Desktop\\Studia\\Mgr Sem I\\Jezyki-Skryptowe-Project\\Project_1\\results_c_impl_comb.txt";
static const string DATA_FILE = "C:\\Users\\zmddd\\Desktop\\Studia\\Mgr Sem I\\Jezyki-Skryptowe-Project\\Project_1\\test.txt";
static const string DELIMITER = ", ";
static const int NUMBER_OF_ELEMS = 252;

struct Data {
    int n;
    int k;
};


int64_t factorial(int n)
{
    int64_t result = 1;
    for (int i = 1; i <= n; i++) 
    {
        result *= i;
    }

    return result;
}

int64_t mathComb(int n, int k)
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
    int64_t n, k, res, counted_res;
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

        ClockTime start_time = Clock::now();
        for (int i = 0; i < 50000000; i++) {
            counted_res = mathComb(n, k);
        }
        ClockTime end_time = Clock::now();
        if (counted_res != res) 
        {
            cout << "Nieporpawny wnik dla n = " << n << " k = " << k << endl;
        }

        auto execution_time_sec = duration_cast<seconds>(end_time - start_time).count();
        auto execution_time_ms = duration_cast<milliseconds>(end_time - start_time).count();
        out_file << "n = " << n << " k = " << k << " res = " << counted_res << " time: " << execution_time_sec << "s, " << execution_time_ms << "ms" << endl;
    }
    out_file.close();
    data.close();
}

void measureTime() {
    ifstream data(DATA_FILE);
    string line;
    string val_n, val_k, val_res;
    Data dataRecords[NUMBER_OF_ELEMS];
    int iter = 0;
    while (getline(data, line))
    {
        val_n = line.substr(0, line.find(DELIMITER));
        line.erase(0, line.find(DELIMITER) + DELIMITER.length());
        val_k = line.substr(0, line.find(DELIMITER));
        line.erase(0, line.find(DELIMITER) + DELIMITER.length());
        dataRecords[iter].n = stoi(val_n);
        dataRecords[iter].k = stoi(val_k);
        iter++;
    }

    time_t begin, end;
    int n = 8000000;
    int64_t res;
    ClockTime start_time = Clock::now();
    time(&begin);
    for (int i = 0; i < n; i++) {
       for (int j = 0; j < NUMBER_OF_ELEMS; j++) {
          res = mathComb(dataRecords[j].n, dataRecords[j].k);
       }
    }
    time(&end);
    ClockTime end_time = Clock::now();

    double difference = difftime(end, begin);
    printf("Implementation test n = %d; time = %.2lf seconds.\n", n, difference);

    auto execution_time_sec = duration_cast<seconds>(end_time - start_time).count();
    auto execution_time_ms = duration_cast<milliseconds>(end_time - start_time).count();

    data.close();
}

int main()
{
    measureTime();
}

