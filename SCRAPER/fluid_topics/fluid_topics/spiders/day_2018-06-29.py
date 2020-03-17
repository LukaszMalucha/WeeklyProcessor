# -*- coding: utf-8 -*-
import scrapy
from pathlib import Path
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from fluid_topics.items import FluidTopicsItem
from selenium.webdriver.common.keys import Keys
from time import sleep


# Helper function to create dates list:
def create_history_list():
	date_list = []
	date_list.append('2018-06-29_2018-06-29')


	return date_list

## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')


class ErraticFutureSpider(scrapy.Spider):
	name = 'day_2018-06-29'
	allowed_domains = ['johnsoncontrols.fluidtopics.net']
	start_urls = ['http://johnsoncontrols.fluidtopics.net/']

	history_list = (create_history_list())

	def parse(self, response):
		self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)

		self.driver.set_window_size(1920, 800)

		for date in self.history_list:
			self.driver.get(
				f'https://johnsoncontrols.fluidtopics.net/search/all?period=custom_{date}&sort=last_update&content-lang=en-US')
			sleep(6)
			page = Selector(text=self.driver.page_source)

			document_count = page.xpath('//*[@class="info-results-count"]/@data-results-count').extract_first()
			if document_count:
				page_loads = int(int(document_count) / 20) + 1
				for i in range(page_loads):
					body = self.driver.find_element_by_css_selector('body')
					body.send_keys(Keys.END)
					sleep(1.5)
					try:
						button = self.driver.find_element_by_xpath(
							'//button[contains(@class, "searchpager-load-more-button")]')
						button.click()
					except:
						pass
					sleep(1.5)

				sel = Selector(text=self.driver.page_source)
				document_cards = sel.xpath('//*[contains(@class, "searchresult-new-component")]')

				for card in document_cards:
					l = ItemLoader(item=FluidTopicsItem(), selector=card)
					title = card.xpath('.//*[@class="searchresult-title"]/a/span/text()').extract_first()
					created_at = date[11:]
					link = card.xpath('.//*[@class="searchresult-title"]/a/@href').extract_first()					
					breadcrumb_path = card.xpath('.//*[@class="searchresult-breadcrumb"]/span/text()').extract()
					breadcrumb = ""
					if breadcrumb_path:
						breadcrumb = '> '.join(breadcrumb_path)
					metadata = card.xpath('.//*[@class="metadata-list"]/li/@title').extract()
					metadata_list = []
					if metadata:
						for element in metadata:
							element = element.replace(",", " |")
							metadata_list.append(element)

					l.add_value('title', title)
					l.add_value('created_at', created_at)
					l.add_value('link', link)
					l.add_value('breadcrumb', breadcrumb)
					l.add_value('metadata', metadata_list)
					yield l.load_item()