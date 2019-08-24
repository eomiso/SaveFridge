#-*- coding: utf-8 -*- 
import unittest #python test module
import image2text_imageai

class TddTest(unittest.TestCase): #unittest.TestCase를 상속받는 테스트 클래스를 생성
#    def testImage2text_meat(self): #meat 사진을 이용한 테스트
#        predictions = image2text_imageai.image2text("pictures/meat.jpg")
#        print('Input: meat')
#        print('============Test Result===========')
#        if 'meat' in predictions:
#            print('Success')
#        else:
#            print('Error')
#        print('')
    
    def testImage2text_strawberry(self): #딸기 사진을 이용한 테스트
        predictions = image2text_imageai.image2text("pictures/strawberry.jpg")
        print('Input: strawberry')
        print('============Test Result===========')
        if 'strawberry' in predictions:
            print('Success')
        else:
            print('Error')
        print('')
            
#    def testImage2text_onions(self): #양파사진을 이용한 테스트
#        predictions = image2text_imageai.image2text("pictures/onions.jpeg")
#        print('Input: onions')
#        print('============Test Result===========')
#        if 'onion' in predictions:
#            print('Success')
#        else:
#            print('Error')
#        print('')
        
    def testImage2text_car(self): #자동차 사진을 이용한 테스트
        predictions = image2text_imageai.image2text("pictures/car.jpeg")
        print('Input: car')
        print('============Test Result===========')
        if 'car' in predictions:
            print('Success')
        else:
            print('Error')
        print('')
    
    def testImage2text_eggs(self):
        predictions = image2text_imageai.image2text("pictures/eggs_white.jpg")
        print('Input: eggs')
        print('============Test Result===========')
        if 'eggs' in predictions:
            print('Success')
        else:
            print('Error')
        print('')

    def testImage2text_pizza(self):
        predictions = image2text_imageai.image2text("pictures/pizza_real.jpeg")
        print('Input: pizza')
        print('============Test Result===========')
        if 'pizza' in predictions:
            print('Success')
        else:
            print('Error')
        print('')
    

if __name__ == '__main__':
    unittest.main()
