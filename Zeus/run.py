# -*- coding: utf-8 -*-

from scrapy import cmdline
import datetime

if __name__ == '__main__':
    today = datetime.datetime.now()
    output_file_path = 'xp1024_{}{}{}_{}{}.csv'.format('%02d' % today.year,
                                                       '%02d' % today.month,
                                                       '%02d' % today.day,
                                                       '%02d' % today.hour,
                                                       '%02d' % today.minute)

    cmd = 'scrapy crawl xp1024 -o ' + output_file_path
    cmdline.execute(cmd.split())
