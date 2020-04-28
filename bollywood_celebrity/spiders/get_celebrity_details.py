import scrapy
from scrapy.loader.processors import TakeFirst
from scrapy.loader import ItemLoader
#from scrapy.spiders import Rule
from bollywood_celebrity.items import BollywoodCelebrityItem
#from scrapy.linkextractors import LinkExtractor


class getCelebrityDetails(scrapy.Spider):

	name = 'get_celebrity_details'

	start_urls=['https://www.bollywoodhungama.com/celebrities/top-100/']

	#rules = (Rule(LinkExtractor(),callback='parse_page'),)

	def parse(self,response):

		celebrity_list= response.css('.bh-top-100-celebs-slide > .bh-top-100-celebs-inner-slide > li')

		for celebrity in celebrity_list:

			#celebrity_detail = ItemLoader(item=BollywoodCelebrityItem(), selector=celebrity)

			#celebrity_detail.default_output_processor = TakeFirst()

			#celebrity_detail.add_css('name','figure > a::attr(title)')
			#celebrity_detail.add_css('image_urls','figure > a > noscript > img::attr(src)')
			#celebrity_detail.add_css('image',)
			#yield celebrity_detail.load_item()

			celebrity_detail= BollywoodCelebrityItem()

			celebrity_detail['image_urls']=celebrity.css('figure > a > noscript > img::attr(src)').extract()
			celebrity_detail['name']=celebrity.css('figure > a::attr(title)').extract_first()

			yield celebrity_detail


