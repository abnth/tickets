# -*- coding: utf-8 -*-
#
#  This file is part of django-taggit-autocomplete-modified.
#
#  django-taggit-autocomplete-modified provides autocomplete functionality
#  to the tags form field of django-taggit.
#
#  Development Web Site:
#    - http://www.codetrax.org/projects/django-taggit-autocomplete-modified
#  Public Source Code Repository:
#    - https://source.codetrax.org/hgroot/django-taggit-autocomplete-modified
#
#  Copyright 2011 George Notaras <gnot [at] g-loaded.eu>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#


from django.forms.widgets import Input
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

from taggit.utils import edit_string_for_tags
from taggit_autocomplete_modified import settings


class TagAutocomplete(Input):
    input_type = 'text'
    
    class Media:
        css = {
            'all': ('%sjquery.autocomplete.css' % settings.TAGGIT_AUTOCOMPLETE_MEDIA_URL,)
        }
        js = (
            '%sjquery.min.js' % settings.TAGGIT_AUTOCOMPLETE_MEDIA_URL,
            '%sjquery.autocomplete.js' % settings.TAGGIT_AUTOCOMPLETE_MEDIA_URL,
        )
    
    def render(self, name, value, attrs=None):
        if value is not None and not isinstance(value, basestring):
            # value contains a list a TaggedItem instances
            # Here we retrieve a comma-delimited list of tags suitable for editing by the user.
            value = edit_string_for_tags([o.tag for o in value.select_related('tag')])
        json_view = reverse('taggit_autocomplete_modified_tag_list')
        html = super(TagAutocomplete, self).render(name, value, attrs)
        js = u'<script type="text/javascript">jQuery().ready(function() { jQuery("#%s").autocomplete("%s", { multiple: true }); });</script>' % (attrs['id'], json_view)
        return mark_safe("\n".join([html, js]))
    
