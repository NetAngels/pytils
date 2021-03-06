# -*- coding: utf-8 -*-
# pytils - russian-specific string utils
# Copyright (C) 2006-2009  Yury Yurevich
#
# http://pyobject.ru/projects/pytils/
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, version 2
# of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
"""
Unit-tests for pytils.dt
"""

import datetime
import time
import unittest

import pytils

class DistanceOfTimeInWordsTestCase(unittest.TestCase):
    """
    Test case for pytils.dt.distance_of_time_in_words
    """

    def setUp(self):
        """
        Setting up environment for tests
        """
        self.time = 1156862275.7711999
        self.dtime = {}
        self.updateTime(self.time)

    def updateTime(self, _time):
        """Update all time-related values for current time """
        self.dtime['10sec_ago'] = _time - 10
        self.dtime['1min_ago'] = _time - 60
        self.dtime['10min_ago'] = _time - 600
        self.dtime['1hr_ago'] = _time - 3720
        self.dtime['10hr_ago'] = _time - 36600
        self.dtime['1day_ago'] = _time - 87600
        self.dtime['1day1hr_ago'] = _time - 90600
        self.dtime['2day_ago'] = _time - 87600*2

        self.dtime['in_10sec'] = _time + 10
        self.dtime['in_1min'] = _time + 61
        self.dtime['in_10min'] = _time + 601
        self.dtime['in_1hr'] = _time + 3721
        self.dtime['in_10hr'] = _time + 36601
        self.dtime['in_1day'] = _time + 87601
        self.dtime['in_1day1hr'] = _time + 90601
        self.dtime['in_2day'] = _time + 87600*2 + 1

    def ckDefaultAccuracy(self, typ, estimated):
        """
        Checks with default value for accuracy
        """
        t0 = time.time()
        # --- change state !!! attention
        self.updateTime(t0)
        # ---
        t1 = self.dtime[typ]
        res = pytils.dt.distance_of_time_in_words(from_time=t1, to_time=t0)
        # --- revert state to original value
        self.updateTime(self.time)
        # ---
        self.assertEquals(res, estimated)

    def ckDefaultToTime(self, typ, accuracy, estimated):
        """
        Checks with default value of time
        """
        t0 = time.time()
        # --- change state !!! attention
        self.updateTime(t0)
        # ---
        t1 = self.dtime[typ]
        res = pytils.dt.distance_of_time_in_words(t1, accuracy)
        # --- revert state to original value
        self.updateTime(self.time)
        # ---
        self.assertEquals(res, estimated)

    def testDOTIWDefaultAccuracy(self):
        """
        Unit-test for distance_of_time_in_words with default accuracy
        """
        self.ckDefaultAccuracy("10sec_ago", u"менее минуты назад")
        self.ckDefaultAccuracy("1min_ago", u"1 минуту назад")
        self.ckDefaultAccuracy("10min_ago", u"10 минут назад")
        self.ckDefaultAccuracy("1hr_ago", u"1 час назад")
        self.ckDefaultAccuracy("10hr_ago", u"10 часов назад")
        self.ckDefaultAccuracy("1day_ago", u"1 день назад")
        self.ckDefaultAccuracy("1day1hr_ago", u"1 день назад")
        self.ckDefaultAccuracy("2day_ago", u"2 дня назад")

        self.ckDefaultAccuracy("in_10sec", u"менее чем через минуту")
        self.ckDefaultAccuracy("in_1min", u"через 1 минуту")
        self.ckDefaultAccuracy("in_10min", u"через 10 минут")
        self.ckDefaultAccuracy("in_1hr", u"через 1 час")
        self.ckDefaultAccuracy("in_10hr", u"через 10 часов")
        self.ckDefaultAccuracy("in_1day", u"через 1 день")
        self.ckDefaultAccuracy("in_1day1hr", u"через 1 день")
        self.ckDefaultAccuracy("in_2day", u"через 2 дня")

    def testDOTIWDefaultToTimeAcc1(self):
        """
        Unit-tests for distance_of_time_in_words with default to_time and accuracy=1
        """
        # accuracy = 1
        self.ckDefaultToTime("10sec_ago", 1, u"менее минуты назад")
        self.ckDefaultToTime("1min_ago", 1, u"минуту назад")
        self.ckDefaultToTime("10min_ago", 1,  u"10 минут назад")
        self.ckDefaultToTime("1hr_ago", 1, u"час назад")
        self.ckDefaultToTime("10hr_ago", 1, u"10 часов назад")
        self.ckDefaultToTime("1day_ago", 1, u"вчера")
        self.ckDefaultToTime("1day1hr_ago", 1, u"вчера")
        self.ckDefaultToTime("2day_ago", 1, u"позавчера")

        self.ckDefaultToTime("in_10sec", 1, u"менее чем через минуту")
        self.ckDefaultToTime("in_1min", 1, u"через минуту")
        self.ckDefaultToTime("in_10min", 1, u"через 10 минут")
        self.ckDefaultToTime("in_1hr", 1, u"через час")
        self.ckDefaultToTime("in_10hr", 1, u"через 10 часов")
        self.ckDefaultToTime("in_1day", 1, u"завтра")
        self.ckDefaultToTime("in_1day1hr", 1, u"завтра")
        self.ckDefaultToTime("in_2day", 1, u"послезавтра")

    def testDOTIWDefaultToTimeAcc2(self):
        """
        Unit-tests for distance_of_time_in_words with default to_time and accuracy=2
        """
        # accuracy = 2
        self.ckDefaultToTime("10sec_ago", 2, u"менее минуты назад")
        self.ckDefaultToTime("1min_ago", 2, u"минуту назад")
        self.ckDefaultToTime("10min_ago", 2,  u"10 минут назад")
        self.ckDefaultToTime("1hr_ago", 2, u"1 час 2 минуты назад")
        self.ckDefaultToTime("10hr_ago", 2, u"10 часов 10 минут назад")
        self.ckDefaultToTime("1day_ago", 2, u"вчера")
        self.ckDefaultToTime("1day1hr_ago", 2, u"1 день 1 час назад")
        self.ckDefaultToTime("2day_ago", 2, u"позавчера")

        self.ckDefaultToTime("in_10sec", 2, u"менее чем через минуту")
        self.ckDefaultToTime("in_1min", 2, u"через минуту")
        self.ckDefaultToTime("in_10min", 2, u"через 10 минут")
        self.ckDefaultToTime("in_1hr", 2, u"через 1 час 2 минуты")
        self.ckDefaultToTime("in_10hr", 2, u"через 10 часов 10 минут")
        self.ckDefaultToTime("in_1day", 2, u"завтра")
        self.ckDefaultToTime("in_1day1hr", 2, u"через 1 день 1 час")
        self.ckDefaultToTime("in_2day", 2, u"послезавтра")

    def testDOTIWDefaultToTimeAcc3(self):
        """
        Unit-tests for distance_of_time_in_words with default to_time and accuracy=3
        """
        # accuracy = 3
        self.ckDefaultToTime("10sec_ago", 3, u"менее минуты назад")
        self.ckDefaultToTime("1min_ago", 3, u"минуту назад")
        self.ckDefaultToTime("10min_ago", 3,  u"10 минут назад")
        self.ckDefaultToTime("1hr_ago", 3, u"1 час 2 минуты назад")
        self.ckDefaultToTime("10hr_ago", 3, u"10 часов 10 минут назад")
        self.ckDefaultToTime("1day_ago", 3,
                                u"1 день 0 часов 20 минут назад")
        self.ckDefaultToTime("1day1hr_ago", 3,
                                u"1 день 1 час 10 минут назад")
        self.ckDefaultToTime("2day_ago", 3,
                                u"2 дня 0 часов 40 минут назад")

        self.ckDefaultToTime("in_10sec", 3, u"менее чем через минуту")
        self.ckDefaultToTime("in_1min", 3, u"через минуту")
        self.ckDefaultToTime("in_10min", 3, u"через 10 минут")
        self.ckDefaultToTime("in_1hr", 3, u"через 1 час 2 минуты")
        self.ckDefaultToTime("in_10hr", 3, u"через 10 часов 10 минут")
        self.ckDefaultToTime("in_1day", 3,
                                u"через 1 день 0 часов 20 минут")
        self.ckDefaultToTime("in_1day1hr", 3,
                                u"через 1 день 1 час 10 минут")
        self.ckDefaultToTime("in_2day", 3,
                                u"через 2 дня 0 часов 40 минут")

    def testDOTWDatetimeType(self):
        """
        Unit-tests for testing datetime.datetime as input values
        """
        first_time = datetime.datetime.now()
        second_time = first_time + datetime.timedelta(0, 1000)
        self.assertEquals(pytils.dt.distance_of_time_in_words(
            from_time=first_time,
            accuracy=1,
            to_time=second_time),
                          u"16 минут назад")

    def testDOTIWExceptions(self):
        """
        Unit-tests for testings distance_of_time_in_words' exceptions
        """
        self.assertRaises(TypeError, pytils.dt.distance_of_time_in_words, "test")
        self.assertRaises(TypeError, pytils.dt.distance_of_time_in_words, time.time(), "test")
        self.assertRaises(TypeError, pytils.dt.distance_of_time_in_words, time.time(), 2, "test")
        self.assertRaises(pytils.err.InputParameterError, pytils.dt.distance_of_time_in_words, "test")
        self.assertRaises(pytils.err.InputParameterError, pytils.dt.distance_of_time_in_words, time.time(), "test")
        self.assertRaises(pytils.err.InputParameterError, pytils.dt.distance_of_time_in_words, time.time(), 2, "test")
        self.assertRaises(ValueError, pytils.dt.distance_of_time_in_words, time.time(), 0)

    def testIssue25DaysFixed(self):
        """
        Unit-test for testing that Issue#25 is fixed (err when accuracy==1, days<>0, hours==1)
        """
        d_days = datetime.datetime.now() - datetime.timedelta(13, 3620)
        self.assertEquals(pytils.dt.distance_of_time_in_words(d_days),
                          u"13 дней назад")

    def testIssue25HoursFixed(self):
        """
        Unit-test for testing that Issue#25 is fixed (err when accuracy==1, hours<>0, minutes==1)
        """
        d_hours = datetime.datetime.now() - datetime.timedelta(0, 46865)
        self.assertEquals(pytils.dt.distance_of_time_in_words(d_hours),
                          u"13 часов назад")

    def testFormatResultStr(self):
        """
        Unit-test for testing format result str
        """
        from_time = datetime.datetime.now() - datetime.timedelta(seconds=1200)
        standard_format = pytils.dt.DistanceCounter()
        class CustomCounter(pytils.dt.DistanceCounter):
            def format_result_str(self, in_future, result_str):
                suffix = in_future and u'раньше' or u'позже'
                return u'на %s %s' % (result_str, suffix)
        custom_format = CustomCounter()
        self.assertEqual(
            standard_format.distance_of_time_in_words(from_time),
            u'20 минут назад'
        )
        self.assertEqual(
            custom_format.distance_of_time_in_words(from_time),
            u'на 20 минут позже'
        )
        from_time = datetime.datetime.now() + datetime.timedelta(seconds=1210)
        self.assertEqual(
            standard_format.distance_of_time_in_words(from_time),
            u'через 20 минут'
        )
        self.assertEqual(
            custom_format.distance_of_time_in_words(from_time),
            u'на 20 минут раньше'
        )


class RuStrftimeTestCase(unittest.TestCase):
    """
    Test case for pytils.dt.ru_strftime
    """

    def setUp(self):
        """
        Setting up environment for tests
        """
        self.date = datetime.date(2006, 8, 25)

    def ck(self, format, estimates, date=None):
        """
        Checks w/o inflected
        """
        if date is None:
            date = self.date
        res = pytils.dt.ru_strftime(format, date)
        self.assertEquals(res, estimates)

    def ckInflected(self, format, estimates, date=None):
        """
        Checks with inflected
        """
        if date is None:
            date = self.date
        res = pytils.dt.ru_strftime(format, date, True)
        self.assertEquals(res, estimates)

    def ckInflectedDay(self, format, estimates, date=None):
        """
        Checks with inflected day
        """
        if date is None:
            date = self.date
        res = pytils.dt.ru_strftime(format, date, inflected_day=True)
        self.assertEquals(res, estimates)

    def ckPreposition(self, format, estimates, date=None):
        """
        Checks with inflected day
        """
        if date is None:
            date = self.date
        res = pytils.dt.ru_strftime(format, date, preposition=True)
        self.assertEquals(res, estimates)

    def testRuStrftime(self):
        """
        Unit-tests for pytils.dt.ru_strftime
        """
        self.ck(u"тест %a", u"тест пт")
        self.ck(u"тест %A", u"тест пятница")
        self.ck(u"тест %b", u"тест авг")
        self.ck(u"тест %B", u"тест август")
        self.ckInflected(u"тест %B", u"тест августа")
        self.ckInflected(u"тест выполнен %d %B %Y года",
                          u"тест выполнен 25 августа 2006 года")
        self.ckInflectedDay(u"тест выполнен в %A", u"тест выполнен в пятницу")

    def testRuStrftimeWithPreposition(self):
        """
        Unit-tests for pytils.dt.ru_strftime with preposition option
        """
        self.ckPreposition(u"тест %a", u"тест в\xa0пт")
        self.ckPreposition(u"тест %A", u"тест в\xa0пятницу")
        self.ckPreposition(u"тест %A", u"тест во\xa0вторник", datetime.date(2007, 6, 5))

    def testRuStrftimeZeros(self):
        """
        Unit-test for testing that Issue#24 is correctly implemented

        It means, 1 April 2007, but 01.04.2007
        """
        self.ck(u"%d.%m.%Y", u"01.04.2007", datetime.date(2007, 4, 1))
        self.ckInflected(u"%d %B %Y", u"1 апреля 2007", datetime.date(2007, 4, 1))

    def testRuStrftimeExceptions(self):
        """
        Unit-tests for testing pytils.dt.ru_strftime's exceptions
        """
        self.assertRaises(TypeError, pytils.dt.ru_strftime, time.time())
        self.assertRaises(TypeError, pytils.dt.ru_strftime, u"%Y.%m.%d%", time.time())
        self.assertRaises(pytils.err.InputParameterError, pytils.dt.ru_strftime, time.time())
        self.assertRaises(pytils.err.InputParameterError, pytils.dt.ru_strftime, u"%Y.%m.%d%", time.time())

    def testIssue20Fixed(self):
        """
        Unit-test for testing that Issue#20 is fixed (typo)
        """
        self.assertEquals(u"воскресенье",
                          pytils.dt.ru_strftime(
                              u"%A",
                              datetime.date(2007,3,18),
                              inflected_day=True)
                         )


if __name__ == '__main__':
    unittest.main()
