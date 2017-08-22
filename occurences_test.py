"""
	Filename: occurences_test.py
	Author: David Docteur
	Date: 22/08/2017
	Description: This class is a unit test in order to make
	  sure that the script is behaving correctly.
	Version: Python v3.6.0
"""

import random
import unittest
from occurences import LinkedList, process_lists


class TestStringsList(unittest.TestCase):

	def test_scenario1(self):
		"""
			Test the example given in the job requirement.
		"""
		linked_list = LinkedList()
		self.assertTrue(linked_list.isEmpty())
		list  = ['g','gh','ghj','g']
		list2 = ['j','ju','gh','gk','gn']
		linked_list.addNode(list)
		linked_list.addNode(list2)
		self.assertEqual(linked_list.countNodes(), 2)
		
		(occurences, uniques, total) = process_lists(linked_list)
		self.assertEqual(occurences.replace(" ", ""), 'gh')
		self.assertEqual(uniques, 7)
		self.assertEqual(total, 9)
		
		
	def test_scenario2(self):
		"""
			Test with empty lists.
		"""
		linked_list = LinkedList()
		self.assertTrue(linked_list.isEmpty())
		list  = []
		list2 = []
		linked_list.addNode(list)
		linked_list.addNode(list2)
		self.assertEqual(linked_list.countNodes(), 2)
		
		(occurences, uniques, total) = process_lists(linked_list)
		self.assertEqual(occurences, '')
		self.assertEqual(uniques, 0)
		self.assertEqual(total, 0)
	
	
	def test_scenario3(self):
		"""
			Test with no lists/nodes at all.
		"""
		linked_list = LinkedList()
		self.assertTrue(linked_list.isEmpty())
		self.assertEqual(linked_list.countNodes(), 0)
		
		(occurences, uniques, total) = process_lists(linked_list)
		self.assertEqual(occurences, '')
		self.assertEqual(uniques, 0)
		self.assertEqual(total, 0)
		
		
	def test_scenario4(self):
		"""
			Let's see how it behaves with much more lists.
			That could be a good CPU stress test by the way!
		"""
	
		max_lists = 500
		count = 0
		linked_list = LinkedList()
		
		while count < max_lists:
			random_list = random.sample(range(500), max_lists)
			linked_list.addNode(random_list)
			count += 1
		self.assertEqual(linked_list.countNodes(), max_lists)
		
		(occurences, uniques, total) = process_lists(linked_list)
		self.assertTrue(occurences != '')
		self.assertTrue(uniques > -1)
		self.assertTrue(total > 0)
		
		
	def test_scenario5(self):
		"""
			Test with only one list, just to make sure
			that it does not loop on it.
		"""
		linked_list = LinkedList()
		self.assertTrue(linked_list.isEmpty())
		list  = ['g','gh','ghj','g']
		linked_list.addNode(list)
		self.assertEqual(linked_list.countNodes(), 1)
		
		(occurences, uniques, total) = process_lists(linked_list)
		self.assertEqual(occurences.replace(" ", ""), '')
		self.assertEqual(uniques, 4)
		self.assertEqual(total, 4)
		
		
if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestStringsList)
	unittest.TextTestRunner(verbosity=1).run(suite)