django-ckpages
==============

FlatPages with CKEditor support for content editing.


Installation
------------
Install this application with pip, being still in development you can clone the repository and install locally with this command:
```bash
pip install -e django-ckpages
```

Configuration
-------------
CK_CONFIGURATION must be set into the settings file to make this app work, an example:

```python
# in settings.py
CK_CONFIGURATION = "/static/js/ckconf.js"
```

and ckconf.js contains the CKEditor configuration, for example:

```javascript
// Settings for CKEditor (refer to the CKEditor documentation)
KEDITOR.config.bodyId = 'content'
CKEDITOR.config.contentsCss = [ 
	'/static/css/content.css',
	'/static/css/typo.css' 
]
```

At this point you should be set.


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

At this point in the administration you should see the CKEditor used for textarea fields.
