import unittest
import demographic_data_analyzer

class TestDemographicDataAnalyzer(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.data = demographic_data_analyzer.calculate_demographic_data_analyzer(print_test=False)
    
    def test_race_count(self):
        actual = self.data['race_count'].to_list()
        expected = [27816, 3124, 1039, 311, 271]
        self.assertCountEqual(actual, expected, msg="Expexted equal to be [27816, 3124, 1039, 311, 271]")
    
    def test_average_age_men(self):
        actual = self.data['average_age_men']
        expected = 39.0
        self.assertAlmostEqual(actual, expected,msg="Expected equal to be 39.0")
    
    def test_percentage_bachelors(self):
        actual = self.data['percentage_bachelors']
        expected = 16.4
        self.assertAlmostEqual(actual, expected,msg="Expected equal to be 16.4")
        
    def test_higher_education_rich(self):
        actual = self.data['higher_education_rich']
        expected = 46.5
        self.assertAlmostEqual(actual, expected,msg="Expected equal to be 46.5")
        
    def test_lower_education_rich(self):
        actual = self.data['lower_education_rich']
        expected = 17.4
        self.assertAlmostEqual(actual, expected,msg="Expected equal to be 17.4")
        
    def test_min_work_hours(self):
        actual = self.data['min_work_hours']
        expected = 1
        self.assertAlmostEqual(actual, expected,msg="Expected equal to be 1")
    
    def test_rich_percentage(self):
        actual = self.data['rich_percentage']
        expected = 10
        self.assertAlmostEqual(actual, expected,msg="Expected equal to be 10")
        
    def test_highest_earning_country(self):
        actual = self.data['highest_earning_country']
        expected = "Iran"
        self.assertEqual(actual, expected,msg="Expected equal to be Iran")
    
    def test_highest_earning_country_percentage(self):
        actual = self.data['highest_earning_country_percentage']
        expected = 41.9
        self.assertAlmostEqual(actual, expected,msg="Expected equal to be 41.9")
        
    def test_popular_job_in_India(self):
        actual = self.data['popular_job_in_India']
        expected = "Prof-specialty"
        self.assertEqual(actual, expected,msg="Expected equal to be Prof-specialty")

if __name__ == '__main__':
    unittest.main()

