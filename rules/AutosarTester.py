#@Author: Dogukan GULYASAR
#Deadline of this file: 31.10.21
"""
-- Documentation --
1. Please add rules as a methods to the AutosarTester class.
2. If your rule contains any kind of non-token word (can't handle with the vera++ keywords) than please add your word to nonAllowed list.
3. Please do not add any additional constructor / destructor to the class.
4. Please do not add any functions to the outside of the class
5. Please use rule numbers with all lower cases for the method names. (ex: Rule A4-0-2 -> def a402():)
6. Please add comment line under the all method definition that explains the rule itself.
7. Please delete after calling your functions because of testing. We do not want to see any function calls in this file.
8. Please be careful about linenumber. It is data member so that if you change in function it will be stored as last value. If your function changes linenumber 
please reset linenumber to the 1 at the end of your function.
9. Please use vera.report functionality for the report test fails. We do not want to see any print() functions in this file.
10. Every Autosar rule means different function, please do not add two rules in one function even they are mostly same.
11. If your rule is only contains non allowed token or word than add your rule into the cantUseFeatures() function and add comment line of your rule number and 
definition as example.
"""

class AutosarTester:
    nonAllowed = []
    linenumber = 1
    def __init__(self):
        print("Constructed")

    def cantUseFeatures(self):
        print("You can not use this feature.")

    def a503(self):
    # The declaration of objects shall contain no more than two levels of pointer indirection
        for file in vera.getSourceFileNames():
            for line in vera.getAllLines(file):
                if "***" in line:
                    vera.report(file, self.linenumber, "No more than two levels of pointer indirection")
                self.linenumber+=1
        self.linenumber = 1
    
    def a513(self):
        # Paramter list (possibly empty) shall be included in every lambda expression. 
        
        for file in vera.getSourceFileNames():
            for token in vera.getTokens(file, 1, 0, -1, -1, ["leftbracket"]):
                print(token.value)
                print(token.line)
                print(token.name)
                self.linenumber = token.line
        print(vera.getLine(file, self.linenumber))

tester = AutosarTester() #Creating a instance of our class
tester.a513()
