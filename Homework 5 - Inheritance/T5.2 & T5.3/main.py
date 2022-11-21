'''
HOMEWORK 5
IRIMIA ANDREI - CEN2.2A

2. IMPLEMEMENT FORM AND RECTANGLE
3. IMPLEMENT COMPUTEAREA FUNCTION
'''
from Form import Form
from Rectangle import Rectange

fr1 = Form("Patrat")
rc1 = Rectange("Dreptunghi", 2, 3)
rc1.showMessage()
fr1.showMessage()
print(rc1.computeArea())
print(fr1.computeArea(2,4))