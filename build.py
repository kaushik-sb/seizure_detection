
from glob import glob 

from jsmin import jsmin
import csscompressor

#-------------------------------------------------------------------------------
# File-level constants
#-------------------------------------------------------------------------------
CSS_INPUT_PATH = './webapp/**/*.js'
CSS_OUTPUT_PATH = './static/bundle.js'

JS_INPUT_PATH = './webapp/**/*.css'
JS_OUTPUT_PATH = './static/bundle.css'

def bundle_javascript():
    """
    Reads through .js files from the webapp folder and merges them into a single file, bundle.js.
    Minifies files in the process.

    Returns
    -------
    bool
    """
    input_path = CSS_INPUT_PATH
    output_path = CSS_OUTPUT_PATH
    output_js = ''

    for filename in glob(input_path, recursive=True):
        with open(filename, 'r', encoding='utf-8') as file:  # Specify encoding here
            output_js += jsmin(file.read(), quote_chars="'\"`") + '\n'

    with open(output_path, 'w', encoding='utf-8') as file:  # Specify encoding here
        file.write(output_js)

    return True


def bundle_css():
    """
    Reads through .css files from the webapp folder and merges them into a single file, bundle.js.
    Minifies files in the process.

    Returns
    -------
    bool
    """
    input_path = JS_INPUT_PATH
    output_path = JS_OUTPUT_PATH
    output_css = ''

    for filename in glob(input_path, recursive=True):
        with open(filename, 'r', encoding='utf-8') as file:  # Specify encoding here
            output_css += csscompressor.compress(file.read()) + '\n'

    with open(output_path, 'w', encoding='utf-8') as file:  # Specify encoding here
        file.write(output_css)

    return True


#-------------------------------------------------------------------------------
# Run if script called directly
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    bundle_javascript()
    bundle_css()
    print('App files built.')
