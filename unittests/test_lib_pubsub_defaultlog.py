"""

:copyright: Copyright 2006-2009 by Oliver Schoenborn, all rights reserved.
:license: BSD, see LICENSE.txt for details.


"""

import imp_unittest, unittest
import wtc

from wx.lib.pubsub import pub
from wx.lib.pubsub.utils import notification
from StringIO import StringIO


#---------------------------------------------------------------------------


class lib_pubsub_DefaultLog(wtc.WidgetTestCase):
    
    
    def testNotifications(self):
        capture = StringIO()
        logger = notification.useNotifyByWriteFile(capture)
        def block():
            def listener(): pass
            pub.subscribe(listener, 'testNotifications')
        block()

    
#---------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
    
    