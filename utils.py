from xhtml2pdf import pisa


def convert_html_to_pdf(source_html_path, output_filename, context=None):
    """
       :param source_html_path: path of the html file
       :param output_filename: name of the output file
       :param context: dictionary of data which need to be passed as context
       :return: file name
       """
    # open output file for writing (truncated binary)
    source_html = open(source_html_path,"r",encoding='utf-8').read()
    if context:
        context_keys = context.keys()
        for context_key in context_keys:
            source_html = source_html.replace(context_key, context.get(context_key))
    result_file = open(output_filename, "w+b")
    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(source_html.encode('utf-8'), dest=result_file,
                                encoding='utf-8')

    # close output file
    result_file.close()  # close output file

    return output_filename
