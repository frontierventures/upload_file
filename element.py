#!/usr/bin/env python
from twisted.web.template import Element, renderer
from twisted.web.template import XMLString


class FileUpload(Element):
    loader = XMLString('''
                       <div xmlns:t="http://twistedmatrix.com/ns/twisted.web.template/0.1" t:render="form">
                       <form action="" method="POST" enctype="multipart/form-data">
                       <input type="file" name="upl_file"></input>
                       <input type="submit" value="submit"></input>
                       </form>
                       </div>
                        ''')

    @renderer
    def form(self, request, tag):
        return tag
