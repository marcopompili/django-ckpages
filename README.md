django-ckpages
==============
FlatPages with CKEditor support for content editing. This application substitute the Flatpages application, the
administration page will be using the excellent CKEditor for editing the content of the web pages.

Installation
------------
Install this application with pip, being still in development you can clone the repository and install locally
with this command:
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

CK_CONFIGURATION = "/static/js/ckconf.js"
```

The ckconf.js file can contains the CKEditor configuration, for example:

```javascript
// Settings for CKEditor (refer to the CKEditor documentation)
CKEDITOR.config.contentsCss = [
	'/static/css/content.css',
	'/static/css/typo.css' 
]
```

Administration
--------------
Now it's time to add the implement an admin class that inherits from the CKPageAdmin admin class, like this:
```python
class PageAdmin(CKPageAdmin):
    list_display = ('title', 'url')
    fieldsets = (
        (None, { 'fields' : ('title', 'content',) }),
        ('Options', { 'fields' : ('sites', 'use_as_home',) }),
    )
```

At this point in the administration you should see the CKEditor used for text-area fields.
