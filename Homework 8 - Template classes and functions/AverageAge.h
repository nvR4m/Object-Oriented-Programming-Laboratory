#include <list>
using namespace std;

template <class T>
class AverageAge {
private:
    list<T> items;
public:
    AverageAge(list<T> items) {
        this->items = items;
    }
    float average() {
        float sum = 0;
        for (T item : this->items) {
            sum += item.getAge();
        }
        return sum / this->items.size();
    }
};

