# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest, Request
from selenium import webdriver
import time


class ImgurSpider(scrapy.Spider):
	name = 'imgur'
	allowed_domains = ['ebay.com']
	start_urls = ['http://www.ebay.com/sch/i.html?_odkw=books&_osacat=0&_trksid=p2045573.m570.l1313.TR0.TRC0.Xpython&_nkw=python&_sacat=0&_from=R40']

	def __init__(self):
		self.driver = webdriver.Firefox()

	def parse(self, response):
		self.driver.get(response.url)

		while True:
			next = self.driver.find_element_by_xpath('//td[@class="pagn-next"]/a')

			try:
				print(next)
				next.click()

				# get the data and write it to scrapy items
			except:
				break

		self.driver.close()