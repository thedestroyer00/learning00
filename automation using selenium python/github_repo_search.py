# GiHub search list automation : 

from time import sleep 
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options

class RepoAutomation():

	def __init__(self):
		
		self.opt = Options()
		self.opt.set_headless()
		self.driver = webdriver.Firefox(options = self.opt)
		self.driver.get('https://github.com')

	def searchbar(self, tag):
		
		search = self.driver.find_element_by_css_selector('input.input-sm')
		search.clear()
		search.send_keys(tag)
		search.submit()
		sleep(5)
		print(self.driver.find_element_by_css_selector('div.flex-column > h3:nth-child(1)').text + '\n')
		
	def print_repolist(self):

		print('Topic: ' + self.driver.find_element_by_css_selector('h3.mb-1').text)
		
		repo_elements = self.driver.find_elements_by_css_selector('a.v-align-middle')
		repo_notes = self.driver.find_elements_by_css_selector('p.mb-1')
		
		print('\nRepositories : \t\t\t\t\t' + 'Sort: ' +self.driver.find_element_by_css_selector('summary.btn > span:nth-child(2)').text)
		for i in range(len(repo_elements)):
			repo_link = str(repo_elements[i].get_attribute('href'))

			print('\nrepo name : ' + repo_link[19:])
			print('repo link : ' + repo_link )
			print('repo note : ' + repo_notes[i].text + '\n')


repo = RepoAutomation()
search_tag = repo.searchbar('selenium python')
repo.print_repolist()
