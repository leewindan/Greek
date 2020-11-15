# -*- coding: utf-8 -*-
# Scrapy settings for Zeus project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Zeus'

SPIDER_MODULES = ['Zeus.spiders']
NEWSPIDER_MODULE = 'Zeus.spiders'

# 日志等级分为
# 1.DEBUG 调试信息
# 2.INFO 一般信息
# 3.WARNING 警告
# 4.ERROR 普通错误
# 5.CRITICAL 严重错误
# 如果设置,LOG_LEVEL="WARNING"，就只会WARNING等级之下的ERROR和CRITICAL,默认等级是1
# LOG_LEVEL = 'DEBUG'
# LOG_FILE = 'spider.log'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Zeus (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
DOWNLOAD_DELAY = 1

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'cache-control': 'max-age=0',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Zeus.middlewares.ZeusSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Zeus.middlewares.ZeusDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'Zeus.pipelines.ZeusPipeline': 300,
   'scrapy.pipelines.images.ImagesPipeline': 1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 处理中文json和txt乱码
# 保存json和txt文件，出现这种东西不是乱码，是unicode，例如：
# \u96a8\u6642\u66f4\u65b0> \u25a0\u25a0\u25a
# 在settings.py文件中加入下面一句code，之后就是中文了。
# FEED_EXPORT_ENCODING ='utf-8'

# 处理中文csv乱码
# 保存csv表格文件时，会出现中文乱码，这个确实是乱码，例如：
# 瀵掑啲瀹濈彔鎶勮鎴愬姛 鐖嗗彂浼ゅ 40涓?寮€蹇冧竴涓?
# 在settings.py文件中加入下面一句code，表格就是中文了
# FEED_EXPORT_ENCODING = 'gb18030'
# 所以，编程时，只要有中文，把上面两句直接先复制在settings文件里，生成文件时就不会错了

# 下载文件的设置
IMAGES_STORE = './Cute'
