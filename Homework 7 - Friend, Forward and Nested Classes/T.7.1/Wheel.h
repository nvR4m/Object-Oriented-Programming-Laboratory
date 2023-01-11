#pragma once
class Wheel {
private:
	int size; 
	bool isForCarriage;
	double weareLevel; // if > 100, needs replacement
public:
	Wheel(int, bool, double);
	int getSize();
	bool getIsForCarriage();
	double getWeareLevel();
	void setWeareLevel(double);

};