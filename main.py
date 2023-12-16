import demographic_data_analyzer
import test_module
from unittest import TestProgram

# check and test mofules
print(demographic_data_analyzer.calculate_demographic_data_analyzer(print_test=False))
#line for unit testing
TestProgram(module='test_module',exit=False)