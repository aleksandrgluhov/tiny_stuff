import random
import time
try:
   import androidhelper as android
except ImportError:
   import android
random.seed()
c=['TNJk10t','1NkEc22','o2e9gOY','AsJ6oQ1','OyUBx1I','u0Pp8Um','AnPzCMH','UXKcnYO','Fm6GzZe','R3jLUm1',
     'NepiwJ6','bs9b4wX','1tbun9T','HL40vK6','kDtymqn','rhw43rh','EH8scqF','BhpMQbl','2dp3LGD','dipoQ0u',
     'QFUPSGr','nsv0Bog','27zWcFq','gFHtI3n','fwa4iXk','h0mY0sP','LnnZoIc','ZSCzRkX','FziVDyt','QSxMd1O',
     'PqKOSCH','sQo3fsJ','8yQdP7K','EpemC03','pzYQg97','YWXLFrA','QvhrXV2','uFHjYhq','d7b7Jq','Ad52U0u',
     'TNRAHyX','GtvjwUg','BtodxVS','4CIJmAD','SZioVdc','lpuDdpN','TWD2et2','Q0eKEOy']
u='http://i.imgur.com/%s.png' % random.choice(c)
d=android.Android()
d.webViewShow(u)
time.sleep(4)