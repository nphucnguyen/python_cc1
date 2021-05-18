from person1 import Operation
class AS3_Main(Operation):

    def menu(self):
        MENU ='''
        +-----------------Menu------------------+
        |   1.Load data from file               |
        |   2.Insert a new person               |
        |   3.Inorder traverse                  |
        |   4.Breath first traveral traverse    |
        |   5.Search by ID                      |
        |   6.Delete by ID                      |
        |   0.Exit                              |    
        '''
        print(MENU)
        x = input('Please enter the choice: ')
        if x == '1':
            self.load()
            print('Thanks!!!')
        elif x =='2':
            self.insert()
        elif x =='3':
            self.inorder_traverse()
        elif x =='4':
            self.breath_first_traverse()
        elif x =='5':
            self.searchByID()
        elif x =='6':
            self.deletebyID()
        # elif x =='7':
        #     self.sortByID()
        # elif x =='8':
        #     self.convertToBinary()
        # elif x =='9':
        #     self.loadToStackAndDisplay()
        # elif x =='10':
        #     self.loadToQueueAndDisplay()
        elif x =='0':
            return
        else:
            print('No option, please enter a choice again: ')
        return self.menu()
        # back to menu

main = AS3_Main()
main.menu()