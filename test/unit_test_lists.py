import unittest

#Test first function - create_bacteria_dict
from parse_usearch_output_lists import create_bacteria_dict

class TestCreateBacteriaDict(unittest.TestCase):

	def test_bacteriadict(self):
		self.input = open('test_list_input.txt','r')
		expected = {'Bug1': {'b0806;mcbA;': 2, 'b0836;bssR;': 1}, 'Bug2': {'b1021;pgaD;': 1}, 'Bug3': {'b1022;pgaC;': 1}, 'Bug4': {'b1023;pgaB;': 1}, 'Bug5': {'b1024;pgaA;': 2, 'b1023;pgaB;': 1, 'b1022;pgaC;': 1}} 
		actual = create_bacteria_dict(self.input)
		self.assertEqual(actual, expected)
		
#Test second function - get_gene_IDs		
from parse_usearch_output_lists import get_gene_IDs

class TestGetGenes(unittest.TestCase):

	def test_getgenes(self):
		self.genes_map = open('test_list_map.txt', 'r')
		expected = set(['b0806;mcbA;', 'b1060;bssS;', 'b1024;pgaA;', 'b1112;bhsA;', 'b1023;pgaB;', 'b1022;pgaC;', 'b1021;pgaD;', 'b0836;bssR;', 'b1127;pepT;'])
		actual = get_gene_IDs(self.genes_map)
		self.assertEqual(actual, expected)
		
#Test third function - write header
#from 

#class TestWriteHeader(unittest.TestCase):

#	def test_writeheader(self):
#		

#Test fourth function - write rows
#from 

#class TestWriteHeader(unittest.TestCase):

#	

if __name__ == '__main__':
    unittest.main()