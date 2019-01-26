import codecs

TPL_JS_SCRIPT = '''{fn_name}={fn}'''

JS_FN = '''function (e) {
    return e.replace(
        /[a-zA-Z]/g,
        function(e) {
            return String.fromCharCode((e<="Z"?90:122)>=(e=e.charCodeAt(0)+13)?e:e-26)});
        }
    );
}'''

JS_INLINE = '''replace(/[a-zA-Z]/g,function(e){return String.fromCharCode((e<="Z"?90:122)>=(e=e.charCodeAt(0)+13)?e:e-26)})'''

TPL_NOSCRIPT = '<noscript>{preface}<span class="obfuscated-email-noscript"><strong><u>{split}</u></strong></span></noscript>'

TPL_MAILTO = '<a href=\\"mailto:{email}\\" rel=\\"nofollow\\">{text}</a>'


def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]


def obfuscate(email, text=None, noscript_preface='', inline_js=True,
              js_fn_name='obfuscateEmail', escape_quotes_in_text=True):

    display_none = '<span style="display:none;">null</span>'

    text = text or email
    if escape_quotes_in_text:
        text = text.replace("'", "\\'")
        text = text.replace('"', '\\"')

    noscript_split = display_none.join(split_len(email, len(email)//3))

    rot13_mailto = codecs.encode(TPL_MAILTO.format(email=email, text=text), 'rot_13')
    noscript = TPL_NOSCRIPT.format(preface=noscript_preface, split=noscript_split)

    if inline_js:
        return '<script type="text/javascript">document.write("{rot13}".{js_inline});</script>{noscript}'.format(
            noscript=noscript,
            js_inline=JS_INLINE,
            rot13=rot13_mailto
        )

    return (
        '<script type="text/javascript">document.write({fn_name}("{rot13}"));</script>{noscript}'.format(
            noscript=noscript,
            rot13=rot13_mailto,
            fn_name=js_fn_name
        ), TPL_JS_SCRIPT.format(fn_name=js_fn_name,fn=JS_FN)
    )
