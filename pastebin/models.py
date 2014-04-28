#-*- coding: utf-8 -*-
from django.db import models


class CodePaste(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=30)
    text = models.TextField()
    htmld_text = models.TextField()
    created_on = models.DateField(auto_now_add=1)

    @models.permalink
    def get_absolute_url(self):
        return 'pastebin.views.paste_details', [self.id]
    
    @models.permalink
    def get_plain_url(self):
        return 'pastebin.views.plain', [self.id]
    
    @models.permalink
    def get_html_url(self):
        return 'pastebin.views.html', [self.id]
    
    def save(self, *args, **kwargs):
        """Htmlize text and save to htmld_text. Use Pygments"""
        
        self.htmld_text = htmlize(self.text, self.language)
        super(CodePaste, self).save(*args, **kwargs)
        
    
def htmlize(text, language):
    from pygments import highlight
    from pygments.formatters.html import HtmlFormatter as Formatter
    if language == 'Python':   
        from pygments.lexers.parsers import PythonLexer as Lexer
    elif language == 'Perl':
        from pygments.lexers.parsers import PerlLexer as Lexer
    elif language == 'Ruby':
        from pygments.lexers.parsers import RubyLexer as Lexer
    elif language == 'PythonConsole':
        from pygments.lexers.agile import PythonConsoleLexer as Lexer
    elif language == 'PythonTraceback':
        from pygments.lexers.agile import PythonTracebackLexer as Lexer
    elif language == 'RubyConsole':
        from pygments.lexers.agile import RubyConsoleLexer as Lexer
    elif language == 'HtmlDjango':
        from pygments.lexers.templates import HtmlDjangoLexer as Lexer
    elif language == 'Html':
        from pygments.lexers.templates import HtmlLexer as Lexer
    else:
        from pygments.lexers.special import TextLexer as Lexer
    """
    Todo: I cant get this to work.
    lang_lexer = str(language + 'Lexer')
    Lexer = __import__('pygments.lexers', globals(), locals(), [lang_lexer, ])
    Or
    from pygments.lexers import get_lexer_by_name
    Lexer = get_lexer_by_name(language.lower())
    """
    htmld = highlight(text, Lexer(), Formatter(linenos='table'))
    return htmld
