django-ckpages
==============
FlatPages with CKEditor support for content editing. This application substitute the Flatpages application, the
administration page will be using the excellent CKEditor for editing the content of the web pages.

Installation
------------
Install this application with pip, being still in development you can clone the repository and install the
application locally with this command:
```
pip install -e django-ckpages
```

Configuration
-------------
Set django-ckpages in the installed applications AFTER flatpages:
```python
INSTALLED_APP = (
    [...],
    'django.contrib.flatpages',
    'django_ckpages',
    [...]
)
```

If necessary to enhance the user experience for the editing, it is possible to configure CKEditor with
some specific options. To do this you need to set a parameter in the settings.py of your web application:
```python
CK_CONFIGURATION = "/static/js/ckconf.js"
```

The ckconf.js file can contains the CKEditor configuration, for example some styling for the editor to
resemble the styling of the final page:
```javascript
// Settings for CKEditor (refer to the CKEditor documentation)
CKEDITOR.config.bodyId = 'content'
CKEDITOR.config.contentsCss = [
	'/static/css/content.css',
	'/static/css/typo.css' 
]
```

Administration
--------------
Django-ckpages overrides the administration panel of the flatpage application, but in case of need
id possible to implement an admin class that inherits from the CKPageAdmin admin class, like this:
```python
class PageAdmin(CKPageAdmin):
    list_display = ('title', 'url',)
    fieldsets = (
        (None, { 'fields' : ('title', 'content',) }),
        ('Options', { 'fields' : ('sites', 'use_as_home',) }),
    )
```

At this point in the administration you should see the CKEditor used for text-area fields, in the
'content' field as it is configured in the ckconf.js file above.

Notes
-----
This application is distributed under the BSD-3 license.

The CKEditor application is distributed under the [GPL](http://www.gnu.org/licenses/gpl.html),
[LGPL](http://www.gnu.org/licenses/lgpl.html), [MPL](http://www.mozilla.org/MPL/) licenses.