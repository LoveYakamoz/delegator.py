import delegator
import unittest
class WidgetTestCase(unittest.TestCase):
    '''
    让所有执行测试的类都继承于TestCase类，
    可以将TestCase看成是对特定类进行测试的方法的集合 
    '''
  
    def setUp(self):
        '''在setUp()方法中进行测试前的初始化工作'''
        pass

    def tearDown(self):
        '''
        并在tearDown()方法中执行测试后的清除工作，
        setUp()和tearDown()都是TestCase类中定义的方法
        '''
        pass
    '''
    def test_delegator_run(self):     
        c = delegator.run(['sleep', '3'], block=False)
        c.out
    '''
    def test_delegator_dir_run(self):
        c = delegator.run(['dir'], block=False)
        print (c.out)

    def test_ls_run(self):
        c = delegator.run(['ls', '-lrt'], block=False)
        print (c.out)

    def test_cowsay_run(self):
        c = delegator.run(['cowsay'], block=True)
        print (c.out)

if __name__ == "__main__": 
    unittest.main()